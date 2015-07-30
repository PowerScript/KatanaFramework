# :-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                 #
# Modules   : Whois       #
# Script by : RedToor     #
# Date      : 09/07/2015  #
# :-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core             #
from core.design import * #
from core import help     #
from core import ping     #
d=DESIGN()                #
# :-:-:-:-:-:-:-:-:-:-:-: #
# Libraries               #
from lib import whois     #
# :-:-:-:-:-:-:-:-:-:-:-: #
# Default                 #
# :-:-:-:-:-:-:-:-:-:-:-: #
defaulthost="127.0.0.1"
defaultport="80"
# :-:-:-:-:-:-:-:-:-:-:-: #

def run(para,parb):
	global defaulthost,defaultport
	defaulthost=para
	defaultport=parb
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
			print ""
		elif actions[0:10] == "set target":
			defaulthost = actions[11:]
			d.change("target",defaulthost)
			wuis(0)
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
					except(KeyboardInterrupt):
						d.kbi()
						exit()
			except:
				d.off()
		else:
			d.nocommand()
	except:
		d.kbi()
		exit()
	wuis(0)