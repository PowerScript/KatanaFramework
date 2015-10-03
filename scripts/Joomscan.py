# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : Joomscan runer #
# Script by : RedToor        #
# Date      : 26/05/2015     #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Katana Core                #
from core.design import *    #
from core.Setting import *   #
from core import Errors      #
from core import help        #
from core import ping        #
import sys                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Libraries                  #
import subprocess            #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaulthost="127.0.0.1"
defaultport="80"
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(target,port):
	global defaulthost,defaultport
	defaulthost=target
	defaultport=port
	xjoomla(1)

def xjoomla(run):
	try:
		global defaulthost,defaultport
		if run!=1:
			actions=raw_input(d.prompt("web/joomscan"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("target","yes","IP or DNS",defaulthost)
			d.descrip("port","no","Port of target",defaultport)
			print ""
		elif actions[0:10] == "set target":
			defaulthost = actions[11:]
			d.change("target",defaulthost)
			xjoomla(0)
		elif actions=="exit" or actions=="x":
			d.goodbye()
			exit()
		elif actions=="help" or actions=="h":
			help.help()
		elif actions=="back" or actions=="b":
			return
			return
		elif actions=="run"  or actions=="r":
			d.run()
			try:
				ping.live(defaulthost,defaultport)
				if True:
					try:
						subprocess.call('cd /pentest/web/joomscan/;./joomscan.pl -u '+defaulthost+":"+defaultport, shell=True)
					except(KeyboardInterrupt):
						d.kbi()
			except:
				d.off()
		else:
			d.nocommand()
	except:
		d.kbi()
		exit()
	xjoomla(0)
