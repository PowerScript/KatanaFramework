#!/usr/bin/env python
# Copyright (C) 2013-2016  Vincent Pelletier <plr.vincent@gmail.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
"""
Advanced hotplug examples.
Presents ways of integrating hotplug into your userland USB driver.
"""
from __future__ import print_function
import select
import sys
import usb1

# A few helpers for demonstration...
mode_dict = {}

class NoHotplugSupport(Exception):
    pass

def onAwesomeDeviceLeft(awesome_device):
    print('Device left:', str(awesome_device))

def onAwesomeDeviceArrived(awesome_device):
    awesome_device.onClose = onAwesomeDeviceLeft
    print('Device arrived:', str(awesome_device))

class SelectPoller(object):
    """
    Dummy poller based on select, because it exists on all platforms.
    WARNING: this class is just for a trivial demonstration, and
    inherits select() limitations. The most important limitation is
    that regitering descriptors does not wake/affect a running poll.
    """
    def __init__(self):
        self._fd_dict = {}

    def register(self, fd, events):
        self._fd_dict[fd] = events

    def unregister(self, fd):
        self._fd_dict.pop(fd)

    def poll(self, timeout=None):
        flag_list = (select.POLLIN, select.POLLOUT, select.POLLPRI)
        result = {}
        for fd_list, happened_flag in zip(
                select.select(*([[
                    fd
                    for fd, events in self._fd_dict.iteritems() if events & flag
                ] for flag in flag_list] + [timeout])),
                flag_list,
            ):
            result[fd] = result.get(fd, 0) | happened_flag
        return result.items()
# (end of demonstration helpers)

class AwesomeDevice(object):
    # Application can set this property to do cleanup when device gets closed,
    # for example when device has left.
    onClose = lambda device: None

    def __init__(self, handle):
        self._handle = handle

    def __str__(self):
        # For demonstration purposes only.
        return 'Awesome Device at ' + str(self._handle.getDevice())

    def close(self):
        # Note: device may have already left when this method is called,
        # so catch USBErrorNoDevice around cleanup steps involving the device.
        try:
            self.onClose(self)
            # Put device in low-power mode, release claimed interfaces...
            pass
        except usb1.USBErrorNoDevice:
            pass
        self._handle.close()

class AwesomeDeviceHoarderBase(object):
    """
    Manages the horde of connected devices.
    """

    def __init__(
            self,
            onDeviceArrived=(lambda awesome_device: False),
        ):
        """
        onDeviceArrived (callable)
            Allows further actions by the application when a relevant device
            arrives, so that it integrates with other devices (ex: send
            different key events when the same button is pressed on different
            devices).
            Returns whether this device should be ignored.
        """
        self.context = usb1.USBContext()
        if not self.context.hasCapability(usb1.CAP_HAS_HOTPLUG):
            raise NoHotplugSupport(
                'Hotplug support is missing. Please update your libusb version.'
            )
        self._device_dict = {}
        self._onDeviceArrived = onDeviceArrived

    def _registerCallback(self):
        self.context.hotplugRegisterCallback(
            self._onHotplugEvent,
            # Just in case more events are added in the future.
            events=usb1.HOTPLUG_EVENT_DEVICE_ARRIVED | usb1.HOTPLUG_EVENT_DEVICE_LEFT,
            # Edit these if you handle devices from a single vendor, of a
            # single product type or of a single device class; and simplify
            # device filtering accordingly in _onHotplugEvent.
            #vendor_id=,
            #product_id=,
            #dev_class=,
        )

    @staticmethod
    def isDeviceSupported(vendor_id, device_id):
        """
        Check if we should drive the device which arrived.
        Simplify this if libusb hotplug API filter is enough (ex: handling a
        single device type).
        """
        # This example handles all devices.
        return True

    def _onHotplugEvent(self, context, device, event):
        if event == usb1.HOTPLUG_EVENT_DEVICE_LEFT:
            awesome_device = self._device_dict.pop(device, None)
            if awesome_device is not None:
                awesome_device.close()
            return
        # Remove next branch if libusb hotplug API filtering is enough (ex:
        # handling a single device type).
        if not self.isDeviceSupported(
                device.getVendorID(),
                device.getProductID(),
            ):
            return
        try:
            handle = device.open()
        except usb1.USBError:
            return
        awesome_device = AwesomeDevice(handle)
        if self._onDeviceArrived(awesome_device):
            awesome_device.close()
            return
        self._device_dict[device] = awesome_device

# Below are alternative APIs. Choose the one most suitable to your needs,
# and ignore the others. This is of course not an exhaustive list.

class AwesomeDeviceHoarderSimple(AwesomeDeviceHoarderBase):
    """
    API 1: USB-event-centric application.
    Simplest API, for userland drivers which only react to USB events.
    """
    def run(self):
        with self.context:
            print('Registering hotplug callback...')
            self._registerCallback()
            print('Callback registered. Monitoring events, ^C to exit')
            while True:
                self.context.handleEvents()

def simple():
    AwesomeDeviceHoarderSimple(onAwesomeDeviceArrived).run()
mode_dict['simple'] = simple

class AwesomeDeviceHoarderEventLoop(AwesomeDeviceHoarderBase):
    """
    API 2:
    More complex, for userland drivers which need to react to other events
    (sockets, user input, ...). Application must then integrate libusb
    polling in its event loop (see usb1.USBPollerThread and usb1.USBPoller).
    """
    def __enter__(self):
        self.context.open()
        print('Registering hotplug callback...')
        self._registerCallback()
        print('Callback registered.')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.context.close()

def eventloop():
    with AwesomeDeviceHoarderEventLoop(onAwesomeDeviceArrived) as awesome_device_hoarder:
        base_poller = SelectPoller()
        # In real code, file descriptor would be independently registered
        # to base_poller.
        # The event loop would be something like:
        poller = usb1.USBPoller(awesome_device_hoarder.context, base_poller)
        print('Monitoring events, ^C to exit')
        while True:
            poller.poll()
mode_dict['eventloop'] = eventloop

def main():
    try:
        mode = mode_dict[sys.argv[1]]
    except (KeyError, IndexError):
        print('Usage: %s [%s]' % (
            sys.argv[0],
            '|'.join(mode_dict),
        ))
        sys.exit(1)
    print(
        'NOTE: this example needs sufficient permissions to be able to '
        'open USB devices to produce any interesting output. If you see '
        'nothing below, check you have USB devices plugged *and* that you '
        'have sufficient permissions to open them.'
    )
    try:
        mode()
    except NoHotplugSupport, exc:
        print(exc.value)
        sys.exit(1)
    except (KeyboardInterrupt, SystemExit):
        print('Exiting')

if __name__ == '__main__':
    main()
