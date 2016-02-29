# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Module    : Client MYSQL   #
# Script by : RedToor        #
# Date      : 15/05/2015     #
# Version   : 1.1            #
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
import socket                #
#from lib import MySQLdb     #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaulthost=LOCAL_IP
defaultport=SQL_PORT
defaultuser=USERNAME
defaultpass=PASSWORD
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(target,port,username,password):
	global defaulthost,defaultport,defaultuser,defaultpass
	defaulthost=target
	defaultport=port
	defaultuser=username
	defaultpass=password
	cmysql(1)


def cmysql(run):
	global defaulthost,defaultport,defaultuser,defaultpass
	try:
		if run!=1:
			actions=raw_input(d.prompt("clt/sql"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("target","yes","IP or DNS",defaulthost)
			d.descrip("port","no","Port of target",defaultport)
 			d.descrip("user","yes","Username",defaultuser)
 			d.descrip("pass","yes","Password",defaultpass)
			d.space()
			cmysql(0)
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
				ping.live(defaulthost,defaultport)
				if True:
					try:
						con=MySQLdb.connect(defaulthost, defaultuser, defaultpass,"")
						if True:
							try:
								cmd="nop"
								print "\n "+Hlp+" SQL Client help\n"
								print "  -------------------------------------------------------------------------------------------------------"
								print "  |"+colors[6]+"Commd"+colors[0]+"            | "+colors[6]+"Description"+colors[0]+"     | "+colors[6]+"Examples"+colors[0]+"                                                        |"
								print "  -------------------------------------------------------------------------------------------------------"
								print "  |show databases   | list databases  | show databases                                                  |" 
								print "  |use	            | select database | use user_table                                                  |"
								print "  |show tables	    | list tables     | show tables                                                     |"
								print "  |create database  | create databases| create database USERS                                           | "
								print "  |create table	    | create tables   | create table EMAILS (id INT PRIMARY KEY, name VARCHAR(20))      | "
								print "  |drop database    | drop databases  | drop database USERS                                             | "
								print "  |drop table       | drop tables     | drop table EMAIL                                                | "
								print "  |insert	    | insert data     | insert into EMAILS values ( '2', 'Dean@mail.ru' )               | "
								print "  |update           | update data     | update EMAILS set name='Willy' where id=1                       | "
								print "  |select           | select data     | select id, name from EMAILS                                     | "
								print "  -------------------------------------------------------------------------------------------------------"
								print ""
								while(cmd!="exit"):
									cmd = raw_input(d.Client_prompt('sql'))
									cur=con.cursor() 
									try:
										tor=cur.execute(cmd)
										if True:
											for x in range(tor):
	   											print cur.fetchone()
	   								except:
	   									print " "+Bad+" No command '"+cmd+"' found"
							except:
								Errors.Errors(event=sys.exc_info()[0], info=False)
					except:
						Errors.Errors(event=sys.exc_info(), info=defaulthost+":"+defaultport)
			except:
				Errors.Errors(event=sys.exc_info()[0], info=defaulthost+":"+defaultport)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info()[0], info=False)
	cmysql(0)
