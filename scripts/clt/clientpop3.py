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
	initialize.Despcription       ="Console Client for POP3 Protocol."
	initialize.CodeName           ="clt/cl.pop"
	initialize.DateCreation       ="22/05/2015"      
	initialize.LastModification   ="03/06/2016"

	# DEFAULT VARIABLES             VALUE                  NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[[LOCAL_IP            , "target" , "yes" , "IP or DNS"]]         #[0][0]
	initialize.DEFAULT_VARIABLE  +=[[POP_PORT            , "port"   , "no"  , "Service port"]]      #[1][0]
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
						con=poplib.POP3(initialize.DEFAULT_VARIABLE[0][0], initialize.DEFAULT_VARIABLE[1][0])
						if True:
							try:
								con.user(initialize.DEFAULT_VARIABLE[2][0])
								con.pass_(initialize.DEFAULT_VARIABLE[3][0])	
								cmd="nop"
								print "\n "+Hlp+" POP3 Client help"
								print " -------------------------------------------------------------------------------------------------------"
								print " |"+colors[6]+"Command"+colors[0]+"|"+colors[6]+"Description"+colors[0]+"|"+colors[6]+"Examples"+colors[0]+"|"
								print " -------------------------------------------------------------------------------------------------------"
								print " |list	| list mails  | list             |" 
								print " |retr	| show mail   | retr 2           |"
								print " |dele	| remove mail | dele 2           |"
								print " ---------------------------------------\n"
								while(cmd!="exit"):
									cmd = raw_input(d.Client_prompt('pop3'))
									if cmd == "list":
										numMessages = len(red.list()[1])
										for i in range(numMessages):
										    print "	mail "+str(i)
									if cmd[0:4] == "retr":
										for j in red.retr(int(cmd[5:])+1)[1]:
											print j
									if cmd[0:4] == "dele":
										try:
										    red.dele(int(cmd[5:])+1)[1]
										    if True:
										    	print " "+War+" email marked for delete ('quit' for exit and delete all email marked)"
										except Exception,e:
											 print(" "+Bad+" Error", e)
									if cmd == "quit":
										red.quit()
										print " "+Alr+" Exit, bye."
										break
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
