# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                       #
# Modules   : Host live LAN     #
# Script by : RedToor           #
# Date      : 22/08/2015        #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                   #
from core.design import *       #
from core.Setting import *      #
from core import Errors         #
from core import help           #
from core import ping           #
import sys                      #
d=DESIGN()                      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                     #
import subprocess               #        
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
defaultnet=MY_IP
defaulttyp="fast"
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

def run(nets, types):
	global defaultnet,defaulttyp
	defaultnet=nets
	defaulttyp=types
	hostl(1)


def hostl(run):
	global defaultnet,defaulttyp
	try:
		if run!=1:
			actions=raw_input(d.prompt("net/lanlive"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("nets","yes","Local area net",defaultnet)
			#d.descrip("type","no","type scan",defaulttyp)
			d.helpAUX()
			if ping.conneted()!=False:
				print " You IP     : ",ping.myip()
			else:
				print d.noconnect()
			#print " Type       :  {fast}{intense}"
			d.space()
			hostl(0)
		elif actions[0:8] == "set nets":
			defaultnet=ping.update(defaultnet,actions,"nets")
			d.change("nets",defaultnet)
		elif actions[0:8] == "set type":
			defaulttyp=ping.update(defaulttyp,actions,"type")
			d.change("type",defaulttyp)
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
				d.space()
				ping.lan_ips(1)
				d.space()
			except:
				Errors.Errors(event=sys.exc_info(), info=False)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info()[0], info=False)
	hostl(0)
