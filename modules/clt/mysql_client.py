# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
import MySQLdb                
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.1"
	init.Description        ="Console Client for Mysql Protocol."
	init.CodeName           ="clt/cl.sql"
	init.DateCreation       ="15/05/2015"      
	init.LastModification   ="21/05/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE     RQ     DESCRIPTION
		'target':[LOCAL_IP ,True ,'Host Target'],
		'port'  :[SQL_PORT ,False,'Port Target'],
		'user'  :[USERNAME ,True ,'Username'],
		'pass'  :[PASSWORD ,True ,'Password']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):

	con=MySQLdb.connect(init.var['target'], init.var['user'], init.var['pass'],"",int(init.var['port']))
	cmd="nop"
	current = "sql"
	printk.inf("SQL Console")
	HelpBanner  = [["Commands","Description","Example"]]
	HelpBanner += [["show databases","show databases","show databases"]]
	HelpBanner += [["use","select database","use USERS"]]
	HelpBanner += [["show tables","list tables","show tables"]]
	HelpBanner += [["create database","create databases","create database USERS "]]
	HelpBanner += [["create table","create tables","create table EMAILS (name VARCHAR(20))"]]
	HelpBanner += [["drop database","drop databases","drop database USERS"]]
	HelpBanner += [["drop table","drop tables","drop table EMAIL"]]
	HelpBanner += [["insert","insert data","insert into EMAILS values ( '2', 'Dean@m.ru')"]]
	HelpBanner += [["update","update data","update EMAILS set name='Willy' where id=1"]]
	HelpBanner += [["select","select data","select id, name from EMAILS"]]
	GRAPHICAL.CreateTable(HelpBanner)

	while(cmd!="exit"):
		cmd = raw_input(ClientPrompt(init.CodeName,current))
		if cmd == "help":GRAPHICAL.CreateTable(HelpBanner)
		else:
			try:
				cur = con.cursor() 
				tor=cur.execute(cmd)
				for x in range(tor):
					print (" -%s") % cur.fetchone()
					if cmd[:3] == "use": current = "sql:"+cmd[4:]
				if True:printAlert(3,"------- > OK.")
			except Exception , e:printk.err(e)

# END CODE MODULE ############################################################################################
