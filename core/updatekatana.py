#
# Katana framework 
# @Katana Update
#

from core import colors
from core import Errors
from core import info
import httplib,urllib 
import subprocess
import socket
import json
import os
import sys 

if os.getuid() != 0:
	print "\n ["+colors.R+"-"+colors.W+"] ERROR:"+colors.B+" Katana"+colors.B+" must be run as "+colors.R+"root"+colors.W+"."
	print " ["+colors.R+"-"+colors.W+"] login as root ("+colors.R+"sudo"+colors.W+") or try "+colors.W+"sudo python ktf.file.py"+colors.W+"\n"
	exit(1)

def update():
	print ""
	print "     ["+colors.O+"!"+colors.W+"] Update - Katana framework"
	print "     ["+colors.O+"!"+colors.W+"] Version Current : Core:"+info.version+" Build:"+info.build+" Date "+info.date
	try:
		red=socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
		red.connect(("raw.githubusercontent.com", int(443))) 
		if True:
			conn = httplib.HTTPSConnection("raw.githubusercontent.com")
			conn.request("GET", "/RedToor/Katana/master/core/version.json")
			response = conn.getresponse()
			getjson= response.read()
			data_string = json.loads(getjson)
			core=data_string["Katana"]["Update"]["Core"]
			build=data_string["Katana"]["Update"]["Build"]
			dateupdate=data_string["Katana"]["Update"]["Date"]
			print "     ["+colors.O+"!"+colors.W+"] Last Version    : Core:%s Build:%s Date %s" % (core, build, dateupdate)
			if (build==info.build):
				print "     ["+colors.O+"!"+colors.W+"] katana already updated.\n"
			else:
				print  "     ["+colors.O+"!"+colors.W+"] Downloading Last Version"
				subprocess.Popen("cd /tmp;git clone https://github.com/RedToor/katana.git;cp -R /tmp/katana/* /usr/share/katana/;rm -rf /tmp/katana/*", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
				subprocess.Popen("cd /usr/share/katana/core;sudo python upgrade.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
				print "     ["+colors.O+"!"+colors.W+"] Upgrading."
				print "     ["+colors.G+"+"+colors.W+"] Katana framework was Updated.\n"
			return
	except:
		#print "     Event: "+str(sys.exc_info())
		print "     ["+colors.R+"-"+colors.W+"] Error, No connneted to Internet. \n"
