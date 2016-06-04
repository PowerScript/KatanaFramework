#!/usr/bin/env python
#HEAD#########################################################
#
# Katana Framework | Update File                             
# this file reviews the file (core/version.json) on server
# the latest version of the framework and compares 
# with the current version (core/Information.py) on the host
# and proceeds to download and install.
#
# 
# Last Modified: 03/06/2016
#
#########################################################HEAD#

from Design import *
from core import Information
import httplib,urllib,subprocess,socket,json,os,sys 

if os.getuid() != 0:
	Space()
	printAlert(5,"Katana Framework.")
	printAlert(1,"this must be run as "+colors[7]+"root"+colors[0]+".")
	printAlert(0,"login as root ("+colors[1]+"sudo"+colors[0]+") or try "+colors[0]+"sudo python ktf.file.py"+colors[0]+"\n")
	exit(1)


def update(fromCall):
	print ""
	printAlert(0,"Update - Katana framework - Connecting with server")
	printAlert(0,"Version Current : Core:"+Information.version+" Build:"+Information.build+" Date "+Information.date)
	try:
		red=socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
		red.connect(("raw.githubusercontent.com", 443)) 

		conn = httplib.HTTPSConnection("raw.githubusercontent.com")
		conn.request("GET", "/PowerScript/KatanaFramework/master/core/version.json")
		response = conn.getresponse()
		getjson= response.read()
		data_string = json.loads(getjson)

		core=data_string["Katana"]["Update"]["Core"]
		build=data_string["Katana"]["Update"]["Build"]
		dateupdate=data_string["Katana"]["Update"]["Date"]
		printAlert(0,"Last Version    : Core:%s Build:%s Date %s" % (core, build, dateupdate))

		if (build<=Information.build):
			printAlert(3,"katana already updated.\n")
		else:
			if fromCall == "installer":
				printAlert(6,"Exists a New Version, you can download for update.")
				return
			printAlert(0,"Downloading Last Version")
			subprocess.Popen("cd /tmp;git clone https://github.com/PowerScript/KatanaFramework.git;cp -R /tmp/KatanaFramework/* /usr/share/KatanaFramework/;rm -rf /tmp/KatanaFramework/*", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
			subprocess.Popen("cd /usr/share/KatanaFramework/core;sudo python Upgrade.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
			printAlert(0,"Upgrading.")
			printAlert(3,"Katana framework was Updated.\n")
		return

	except:printAlert(1,"Error, No connneted to Internet or server is down.\n")
