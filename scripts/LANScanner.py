# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                       #
# Modules   : Host live LAN     #
# Script by : RedToor           #
# Date      : 22/08/2015        #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                   #
from core.design import *       #
from core import help           #
from core import ping           #
d=DESIGN()                      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                     #
import subprocess               #        
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
defaultnet="192.168.1.0"
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

def run(para):
	global defaultnet
	defaultnet=para
	hostl(1)


def hostl(run):
	global defaultnet
	try:
		if run!=1:
			actions=raw_input(d.prompt("net/lanlive"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("nets","yes","Local area net",defaultnet)
			print ""
			hostl(0)
		elif actions[0:8] == "set nets":
			defaultnet = actions[9:]
			d.change("nets",defaultnet)
			hostl(0)
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
				subprocess.call('nmap -sP '+defaultnet+'/24', shell=True)
				print ""
			except(KeyboardInterrupt, SystemExit):
				d.kbi()
		else:
			d.nocommand()
	except:
		d.kbi()
		exit()
	hostl(0)