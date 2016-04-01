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
from lib.ftplib.ftplib import FTP
from core import help         #
from pexpect import pxssh     #
import poplib                 #
import socket                 #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="RedToor"
	initialize.Version            ="1.1"
	initialize.Despcription       ="Test Credentials protocols."
	initialize.CodeName           ="mcs/ts.login"
	initialize.DateCreation       ="03/05/2015"      
	initialize.LastModification   ="27/03/2016"

	# DEFAULT VARIABLES             VALUE                NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[[LOCAL_IP          , "target" , "yes" , "IP or DNS"]]  #[0][0]
	initialize.DEFAULT_VARIABLE  +=[[USERNAME          , "user"   , "yes" , "Username"]]   #[1][0]
	initialize.DEFAULT_VARIABLE  +=[["anonymous"       , "pass"   , "yes" , "Password"]]   #[2][0]
initialize()
# END INFORMATION MODULE

# MAIN FUNCTION
def main(run):
	try:
		# HEAD MODULE
		if run:	actions=raw_input(Message.prompt(initialize.CodeName))
		else  : actions="run"
		if   getFunction.KatanaCheckActionShowOptions(actions):getFunction.ShowOptions(initialize.DEFAULT_VARIABLE)
		elif getFunction.KatanaCheckActionSetValue(actions)   :initialize.DEFAULT_VARIABLE=getFunction.UpdateValue(actions,initialize.DEFAULT_VARIABLE)
		elif getFunction.KatanaCheckActionisBack(actions)     :return
		# END HEAD MODULE
		elif getFunction.runModule(actions):
			Message.run()
			# CODE MODULE    ############################################################################################
			try:
				Message.testing("Mysql","3306")
				MySQLdb.connect(initialize.DEFAULT_VARIABLE[0][0],initialize.DEFAULT_VARIABLE[1][0],initialize.DEFAULT_VARIABLE[2][0],'')
				Message.live_protocol()
				if True:
					print(" "+Suf+" Logged with "+initialize.DEFAULT_VARIABLE[1][0]+"/"+initialize.DEFAULT_VARIABLE[2][0]+" in Mysql")
			except:
				print " "+Bad+" Service Off or No Logged."

			try:
				Message.testing("SSH",SSH_PORT)
				connect = pxssh.pxssh()
				connect.login(initialize.DEFAULT_VARIABLE[0][0],initialize.DEFAULT_VARIABLE[1][0],initialize.DEFAULT_VARIABLE[2][0])
				d.live_protocol()
				if True:
					print(" "+Suf+" Logged with "+initialize.DEFAULT_VARIABLE[1][0]+"/"+initialize.DEFAULT_VARIABLE[2][0]+" in SSH")
			except:
				print " "+Bad+" Service Off or No Logged."
			try:
				Message.testing("FTP",FTP_PORT)
				ftp.login(initialize.DEFAULT_VARIABLE[1][0],initialize.DEFAULT_VARIABLE[2][0])
				if True:
					print(" "+Suf+" Logged with "+initialize.DEFAULT_VARIABLE[1][0]+"/"+initialize.DEFAULT_VARIABLE[2][0]+" in FTP")
			except:
				print " "+Bad+" Service Off or No Logged."
			try:
				Message.testing("POP3",POP_PORT)
				red=poplib.POP3(initialize.DEFAULT_VARIABLE[0][0], 110)
				red.user(initialize.DEFAULT_VARIABLE[1][0]+"@"+initialize.DEFAULT_VARIABLE[0][0])
				red.pass_(initialize.DEFAULT_VARIABLE[2][0])
				if True:
					print(" "+Suf+" Logged with "+initialize.DEFAULT_VARIABLE[1][0]+"/"+initialize.DEFAULT_VARIABLE[2][0]+" in POP3")
			except:
				print " "+Bad+" Service Off or No Logged."
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
def run(target,username,password):
	initialize.DEFAULT_VARIABLE [0][0] = target
	initialize.DEFAULT_VARIABLE [1][0] = username
	initialize.DEFAULT_VARIABLE [2][0] = password
	main(False)
# END LINKER FUNCTION
