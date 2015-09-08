# :-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                 #
# Modules   : Whois       #
# Script by : RedToor     #
# Date      : 09/07/2015  #
# :-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core             #
from core.design import * #
from core.Setting import *#
from core import Errors   #
from core import help     #
from core import ping     #
import sys                #
d=DESIGN()                #
# :-:-:-:-:-:-:-:-:-:-:-: #
# Libraries               #
from lib import whois     #
# :-:-:-:-:-:-:-:-:-:-:-: #
# Default                 #
# :-:-:-:-:-:-:-:-:-:-:-: #
defaulthost=LOCAL_IP
defaultport=HTTP_PORT
# :-:-:-:-:-:-:-:-:-:-:-: #

def run(target,port):
	global defaulthost,defaultport
	defaulthost=target
	defaultport=port
	wuis(1)

def wuis(run):
	try:
		global defaulthost,defaultport
		if run!=1:
			actions=raw_input(d.prompt("web/whois"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("target","yes","IP or DNS",defaulthost)
			d.descrip("port","no","Port of target",defaultport)
			d.space()
		elif actions[0:10] == "set target":
			defaulthost=defaulthost.replace("http://", "")
			defaulthost=ping.update(defaulthost,actions,"target")
			d.change("target",defaulthost)
		elif actions[0:8] == "set port":
			defaultport=ping.update(defaultport,actions,"port")
			d.change("port",defaultport)
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
						w = whois.whois(defaulthost)
						if w:
							wd = w.__dict__
							for k, v in wd.items():
								print('%20s\t"%s"' % (k, v))
							print ""
					except:
						Errors.Errors(event=sys.exc_info(), info=False)
			except:
				Errors.Errors(event=sys.exc_info()[0], info=defaulthost+":"+defaultport)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info()[0], info=False)
	wuis(0)