# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : Client MYSQL   #
# Script by : RedToor        #
# Date      : 15/05/2015     #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Katana Core                #
from core.design import *    #
from core import help        #
from core import ping        #
d=DESIGN()                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Libraries                  #
import socket                #
#from lib import MySQLdb     #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaulthost="127.0.0.1"
defaultport="3306"
defaultuser="root"
defaultpass="toor"
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(para,parb,parc,pard):
	global defaulthost,defaultport,defaultuser,defaultpass
	defaulthost=para
	defaultport=parb
	defaultuser=parc
	defaultpass=pard
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
			print ""
			cmysql(0)
		elif actions[0:10] == "set target":
			defaulthost = actions[11:]
			defaulthost = defaulthost.replace("http://", "")
			d.change("target",defaulthost)
			cmysql(0)
		elif actions[0:8] == "set port":
			defaultport = actions[9:]
			d.change("port",defaultport)
			cmysql(0)
		elif actions[0:8] == "set user":
			defaultuser = actions[9:]
			d.change("user",defaultuser)
			cmysql(0)
		elif actions[0:8] == "set pass":
			defaultpass = actions[9:]
			d.change("pass",defaultpass)
			cmysql(0)
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
									cmd = raw_input(colors[1]+" CLT~"+colors[3]+"sql/> "+colors[0])
									cur=con.cursor() 
									try:
										tor=cur.execute(cmd)
										if True:
											for x in range(tor):
	   											print cur.fetchone()
	   								except:
	   									print " ["+colors[1]+"-"+colors[0]+"] Error: command"				
							except(KeyboardInterrupt):
								d.kbi()
							except Exception,e:
								print(" ["+colors[1]+"-"+colors[0]+"] Timeout.", e)
					except:
						d.nomatch()
			except:
				d.off()
		else:
			d.nocommand()
	except:
		d.kbi()
		exit()
	cmysql(0)