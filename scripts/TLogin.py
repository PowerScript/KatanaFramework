# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : Test Login     #
# Script by : RedToor        #
# Date      : 23/05/2015     #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Katana Core                #
from core.design import *    #
from core.Setting import *   #
from core import Errors      #
from core import help        #
from core import ping        #
import sys                   #
d=DESIGN()                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Libraries                  #
#from lib import MySQLdb     #
from lib.ftplib.ftplib import FTP
from core import help        #
from pexpect import pxssh    #
import poplib                #
import socket                #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaulthost=LOCAL_IP
defaultport=POP_PORT
defaultuser=USERNAME
defaultpass=PASSWORD
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(target,port,username,password):
	global defaulthost,defaultport,defaultuser,defaultpass
	defaulthost=target
	defaultport=port
	defaultuser=username
	defaultpass=password
	tlogin(1)

def tlogin(run):
	try:
		global defaulthost,defaultport,defaultuser,defaultpass
		if run!=1:
			actions=raw_input(d.prompt("mc/tlogin"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("target","yes","IP or DNS",defaulthost)
			d.descrip("port","no","Port of target",defaultport)
 			d.descrip("user","yes","Username",defaultuser)
 			d.descrip("pass","yes","Password",defaultpass)
			d.space()
			tlogin(0)
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
		elif actions[0:8] == "set pass":
			defaultpass=ping.update(defaultpass,actions,"pass")
			d.change("pass",defaultpass)
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
				d.testing("Mysql",SQL_PORT)
				MySQLdb.connect(defaulthost,defaultuser,defaultpass,'')
				d.live_protocol()
				if True:
					print(" "+Suf+" Logged with "+defaultuser+"/"+defaultpass+" in Mysql")
			except:
				Errors.Errors(event=sys.exc_info()[0], info=False)

			try:
				d.testing("SSH",SSH_PORT)
				connect = pxssh.pxssh()
				connect.login(defaulthost,defaultuser,defaultpass)
				d.live_protocol()
				if True:
					print(" "+Suf+" Logged with "+defaultuser+"/"+defaultpass+" in SSH")
			except:
				Errors.Errors(event=sys.exc_info()[0], info=False)
			try:
				d.testing("FTP",FTP_PORT)
				ftp.login(defaultuser,defaultpass)
				if True:
					print(" "+Suf+" Logged with "+defaultuser+"/"+defaultpass+" in FTP")
			except:
				print " "+Bad+" Service Off or No Logged."
			try:
				d.testing("POP3",POP_PORT)
				red=poplib.POP3(defaulthost, 110)
				red.user(defaultuser+"@"+defaulthost)
				red.pass_(defaultpass)
				if True:
					print(" "+Suf+" Logged with "+defaultuser+"/"+defaultpass+" in POP3")
			except:
				print " "+Bad+" Service Off or No Logged."
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info()[0], info=False)
	tlogin(0)
