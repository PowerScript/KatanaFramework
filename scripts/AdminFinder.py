# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : Admin finder   #
# Script by : RedToor        #
# Date      : 28/02/2015     #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Katana Core                #
from core.design import *    #
from core import help        #
from core import ping        #
d=DESIGN()                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Libraries                  #
import httplib               #
import socket                #
import sys                   #
import time                  #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaulthost="127.0.0.1"
defaultport="80"
defaultdicc="core/db/commons-dir-admin.tbl"
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(para,parb,parc):
	global defaulthost,defaultport,defaultdicc
	defaulthost=para
	defaultport=parb
	defaultdicc=parc
	adminfinder(1)


def adminfinder(run):
	try:
		global defaulthost,defaultport,defaultdicc
		if run!=1:
			actions=raw_input(d.prompt("web/cpfinder"))
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
			adminfinder(0)
		elif actions[0:8] == "set port":
			defaultport = actions[9:]
			d.change("port",defaultport)
			adminfinder(0)
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
						with open(defaultdicc,'r') as dirt:
							results=""
							resultn=""
							for patch in dirt: 
								patch=patch.replace("\n","")
								patch = "/" + patch
								connection = httplib.HTTPConnection(defaulthost,defaultport)
								connection.request("GET",patch)
								response = connection.getresponse()
								if response.status == 200 or response.status == 301:
									print " ["+colors[2]+"+"+colors[0]+"] Response "+patch
									results="-["+colors[2]+"*"+colors[0]+"]"+patch+"\n"+results
									resultn=patch+","+resultn
								else:
									print " ["+colors[4]+"!"+colors[0]+"] Checking..."+colors[0]+patch
						if results != "":
							print "\n"+results
							log=open('core/logs/logsAdminFinder.log','a')
							log.write('\n ===================================== ')
							log.write('\n Module  : Admin Finder')
							log.write('\n Data    : '+time.strftime('%c'))
							log.write('\n target  : '+defaulthost)
							log.write('\n port    : '+defaultport)
							log.write('\n found   : '+resultn)
							log.close()
						else:
							print "\n ["+colors[1]+"-"+colors[0]+"] Not Found CP\n"
					except:
						d.kbi()
			except:
				d.off()
		else:
			d.nocommand()
	except:
		d.kbi()
		exit()
	adminfinder(0)