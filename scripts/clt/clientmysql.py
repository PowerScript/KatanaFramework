# This module requires katana framework 
# https://github.com/RedToor/Katana
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                 #
from core.design import *     #
from core.Setting import *    #
from core import Errors       #
from core import getFunction  #
import sys                    #
Message=DESIGN()              #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                   #
import MySQLdb                #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="RedToor"
	initialize.Version            ="1.1"
	initialize.Despcription       ="Console Client for Mysql Protocol."
	initialize.CodeName           ="clt/cl.sql"
	initialize.DateCreation       ="15/05/2015"      
	initialize.LastModification   ="31/03/2016"

	# DEFAULT VARIABLES             VALUE                  NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[[LOCAL_IP            , "target" , "yes" , "IP or DNS"]]         #[0][0]
	initialize.DEFAULT_VARIABLE  +=[[SQL_PORT            , "port"   , "no"  , "Service port"]]      #[1][0]
	initialize.DEFAULT_VARIABLE  +=[[USERNAME            , "user"   , "yes" , "Username target"]]   #[2][0]
	initialize.DEFAULT_VARIABLE  +=[[PASSWORD            , "pass"   , "yes" , "Password target"]]   #[3][0]
initialize()
# END INFORMATION MODULE

# MAIN FUNCTION
def main(run):
	try:
		# HEAD MODULE
		if run:	actions=raw_input(Message.prompt(initialize.CodeName))
		else  : actions="run"
		if getFunction.KatanaCheckActionShowOptions(actions)  :getFunction.ShowOptions(initialize.DEFAULT_VARIABLE)
		elif getFunction.KatanaCheckActionSetValue(actions)   :initialize.DEFAULT_VARIABLE=getFunction.UpdateValue(actions,initialize.DEFAULT_VARIABLE)
		elif getFunction.KatanaCheckActionisBack(actions)     :return
		# END HEAD MODULE
		elif getFunction.runModule(actions):
			Message.run()
			# CODE MODULE    ############################################################################################
			try:
				getFunction.live(initialize.DEFAULT_VARIABLE[0][0],initialize.DEFAULT_VARIABLE[1][0])
				if True:
					try:
						con=MySQLdb.connect(initialize.DEFAULT_VARIABLE[0][0], initialize.DEFAULT_VARIABLE[2][0], initialize.DEFAULT_VARIABLE[3][0],"")
						if True:
							try:
								cmd="nop"
								print "\n "+Hlp+" SQL Client help"
								print " -------------------------------------------------------------------------------------------------------"
								print " |"+colors[6]+"Command"+colors[0]+"          | "+colors[6]+"Description"+colors[0]+"     | "+colors[6]+"Examples"+colors[0]+"                                                        |"
								print " -------------------------------------------------------------------------------------------------------"
								print " |show databases   | list databases  | show databases                                                  |" 
								print " |use	           | select database | use user_table                                                  |"
								print " |show tables	   | list tables     | show tables                                                     |"
								print " |create database  | create databases| create database USERS                                           | "
								print " |create table	   | create tables   | create table EMAILS (id INT PRIMARY KEY, name VARCHAR(20))      |   "
								print " |drop database    | drop databases  | drop database USERS                                             | "
								print " |drop table       | drop tables     | drop table EMAIL                                                | "
								print " |insert	   | insert data     | insert into EMAILS values ( '2', 'Dean@mail.ru' )               | "
								print " |update           | update data     | update EMAILS set name='Willy' where id=1                       | "
								print " |select           | select data     | select id, name from EMAILS                                     | "
								print " -------------------------------------------------------------------------------------------------------\n"
								current = "sql"
								while(cmd!="exit"):
									cmd = raw_input(Message.Client_prompt(current))
									cur = con.cursor() 
									try:
										tor=cur.execute(cmd)
										if True:
											for x in range(tor):
	   											print (" -%s") % cur.fetchone()
	   										print " "+Suf+" ------- > OK."
	   										if cmd[:3] == "use": current = "sql:"+cmd[4:]
	   								except:
	   									print " "+Bad+" No command '"+cmd+"' found"
							except:
								Errors.Errors(event=sys.exc_info(), info=False)
					except:
						Errors.Errors(event=sys.exc_info(), info=initialize.DEFAULT_VARIABLE[2][0]+":"+initialize.DEFAULT_VARIABLE[3][0])
			except:
				Errors.Errors(event=sys.exc_info(), info=initialize.DEFAULT_VARIABLE[0][0]+":"+initialize.DEFAULT_VARIABLE[1][0])			# END CODE MODULE ############################################################################################
			# END CODE MODULE ############################################################################################
		else:
			getFunction.KatanaCheckActionGlobalCommands(actions)
	# ERROR GENERAL
	except:
		Errors.Errors(event=sys.exc_info(), info=sys.exc_traceback.tb_lineno)
	# END ERROR GENERAL
	main(True)
# END MAIN FUNCTION

# LINKER FUNCTION
def run(target,port,username,password):
	initialize.DEFAULT_VARIABLE[0][0] = target
	initialize.DEFAULT_VARIABLE[1][0] = port
	initialize.DEFAULT_VARIABLE[2][0] = username
	initialize.DEFAULT_VARIABLE[3][0] = password
	main(False)
# END LINKER FUNCTION