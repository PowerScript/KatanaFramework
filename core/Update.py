#!/usr/bin/env python2
#HEAD#########################################################
#
# Katana Framework | Update File                             
# Last Modified: 25/11/2016
#
#########################################################HEAD#

from Design import *
from core import Information
import httplib,urllib,subprocess,socket,json,os,sys 

printk = printk()

if os.getuid() != 0:
	Space()
	printk.inf("Katana Framework.")
	printk.err("this must be run as "+colors[7]+"root"+colors[0]+".")
	printk.inf("login as root ("+colors[1]+"sudo"+colors[0]+") or try "+colors[0]+"sudo python ktf.update"+colors[0]+"\n")
	exit(1)


def update(fromCall,force):
	print ""
	printk.inf("Update - Katana framework - Connecting with server")
	printk.inf("Version Current : Core:"+Information.version+" Build:"+Information.build+" Date "+Information.date)
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
		printk.inf("Last Version    : Core:%s Build:%s Date %s" % (core, build, dateupdate))

		if (build==Information.build) and force!=False:
			printk.suff("katana already updated.\n")
		else:
			if fromCall == "installer":
				printk.war("Exists a New Version, you can download for update.")
				return
			printk.inf("Downloading Last Version")
			subprocess.Popen("git clone https://github.com/PowerScript/KatanaFramework.git /tmp/katana",  stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
			subprocess.Popen("cp -R /tmp/katana/* /usr/share/KatanaFramework/ && rm -rf /tmp/katana", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
			printk.suff("Katana framework was Updated.\n")
		return True

	except:printk.err("Error, No connneted to Internet or server is down.\n")
