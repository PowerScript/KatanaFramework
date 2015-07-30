# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                     #
# Modules   : GetDataReport   #
# Script by : RedToor         #
# Date      : 02/03/2015      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                 #
from core.design import *     #
from core import help         #
from core import ping         #
d=DESIGN()                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                   #
import socket                 #
import subprocess             #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                     #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
defaultred="www.google.com"
defaultjav="true"
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

def run(para,parb):
	global defaultred,defaultjav
	defaultred=para
	defaultjav=parb
	getdatareport(1)

def getdatareport(run):
	try:
		global defaultred,defaultjav
		if run!=1:
			actions=raw_input(d.prompt("seng/gdreport"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("link","yes","redirectly",defaultred)
			d.descrip("javas","no","JS for Geo",defaultjav)
 			print ""
		elif actions[0:8] == "set link":
				defaultred = actions[9:]
				d.change("link",defaultred)
				getdatareport(0)
		elif actions[0:9] == "set javas":
				defaultjav = actions[10:]
				if defaultjav == "true" or defaultjav == "false":
					d.change("javas",defaultjav)
				else:
					d.nodataallow()
				getdatareport(0)
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
				subprocess.call('echo "<?php \$url=\'http://'+defaultred+'\';\$javascript=\''+defaultjav+'\';?>" > /var/www/appconfig.php', shell=True)
				print("\n ["+colors[4]+"!"+colors[0]+"] Running Apache Server")
				subprocess.call('cp files/getdatareport/* /var/www/', shell=True)
				subprocess.call('chmod -c 777 /var/www/', shell=True)
				subprocess.call('service apache2 start', shell=True)
				if True:
					try:
						print(" ["+colors[2]+"+"+colors[0]+"] Apache Started")
						print(" ["+colors[2]+"+"+colors[0]+"] Script Running in http://127.0.0.1/redirect.php?id=1337")
						print(" ["+colors[4]+"!"+colors[0]+"] The Report will be save in /var/www/")
						print""
						print(" ["+colors[2]+"+"+colors[0]+"] Running GetDataReport Script...")
						raw_input(" ["+colors[3]+"-"+colors[0]+"] Press any key for Stop GetDataReport")
						print(" ["+colors[4]+"!"+colors[0]+"] Stoping Process")
						subprocess.call('rm /var/www/redirect.php', shell=True)
						subprocess.call('rm /var/www/appconfig.php', shell=True)
						subprocess.call('rm /var/www/jquery.js', shell=True)
						subprocess.call('apache2ctl stop', shell=True)
						print(" ["+colors[4]+"!"+colors[0]+"] Stoping Apache and GetDataReport Script")
						print(" ["+colors[2]+"+"+colors[0]+"] Scritp Stoped and Apache")
					except:
						print(" ["+colors[4]+"!"+colors[0]+"] Stoping Process")
						subprocess.call('service apache2 stop', shell=True)
						subprocess.call('rm /var/www/redirect.php', shell=True)
						subprocess.call('rm /var/www/appconfig.php', shell=True)
						subprocess.call('rm /var/www/jquery.js', shell=True)
						print(" ["+colors[2]+"+"+colors[0]+"] Stoped")
						getdatareport(0)
			except:
				d.kbi()
				exit()
		else:
			d.nocommand()
	except:
		d.kib()
		exit()
	getdatareport(0)