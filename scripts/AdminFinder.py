# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Module    : Admin finder   #
# Script by : RedToor        #
# Date      : 28/02/2015     #
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
import httplib               #
import socket                #
import time                  #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaulthost=LOCAL_IP
defaultport=HTTP_PORT
defaultdicc=TABLE_FOLDER_ADMIN
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(target,port,dictionary):
	global defaulthost,defaultport,defaultdicc
	defaulthost=target
	defaultport=port
	defaultdicc=dictionary
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
			d.descrip("table","no","Dictionary",defaultdicc)
			d.space()
		elif actions[0:10] == "set target":
			defaulthost=defaulthost.replace("http://", "")
			defaulthost=ping.update(defaulthost,actions,"target")
			d.change("target",defaulthost)
		elif actions[0:8] == "set port":
			defaultport=ping.update(defaultport,actions,"port")
			d.change("port",defaultport)
		elif actions[0:9] == "set table":
			defaultdicc=ping.update(defaultport,actions,"table")
			d.change("table",defaultdicc)
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
						d.loading_file()
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
									print " "+Suf+" Response "+patch
									results="-"+Suf+" "+patch+"\n"+results
									resultn=patch+","+resultn
								else:
									print " "+Alr+" Checking..."+colors[0]+patch
						if results != "":
							print "\n"+results
							ping.savefive("Admin Finder",defaulthost,defaultport,results)
						else:
							print "\n "+Nrs+" Not Results :(.\n"

					except:
						Errors.Errors(event=sys.exc_info()[0], info=defaultdicc)
			except:
				Errors.Errors(event=sys.exc_info()[0], info=defaulthost+":"+defaultport)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info()[0], info=False)
	adminfinder(0)
