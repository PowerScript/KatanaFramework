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
import httplib                #
import socket                 #
import time                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="RedToor"
	initialize.Version            ="1.1"
	initialize.Despcription       ="Administrator Panel finder, Search for Brute force possibles Cpanels."
	initialize.CodeName           ="web/cp.finder"
	initialize.DateCreation       ="28/09/2015"      
	initialize.LastModification   ="31/03/2016"

	# DEFAULT VARIABLES             VALUE                NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[[LOCAL_IP          , "target" , "yes" , "IP or DNS"]]      #[0][0]
	initialize.DEFAULT_VARIABLE  +=[[HTTP_PORT         , "port"   , "no"  , "Service port"]]   #[1][0]
	initialize.DEFAULT_VARIABLE  +=[[TABLE_FOLDER_ADMIN, "table"  , "no"  , "Tables commons"]] #[2][0]
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
						with open(initialize.DEFAULT_VARIABLE[2][0],'r') as dirt:
							results=""
							resultn=""
							for patch in dirt: 
								patch=patch.replace("\n","")
								patch = "/" + patch
								connection = httplib.HTTPConnection(initialize.DEFAULT_VARIABLE[0][0],initialize.DEFAULT_VARIABLE[1][0])
								connection.request("GET",patch)
								response = connection.getresponse()
								if response.status == 200 or response.status == 301:
									print " "+Suf+" Response "+patch
									results="-"+Suf+" "+patch+"\n"+results
									resultn=patch+","+resultn
								else:
									print " "+Alr+" Checking `"+colors[0]+patch+"` Response:"+str(response.status)
						if results != "":
							print "\n"+results
							getFunction.savefive("Admin Finder",initialize.DEFAULT_VARIABLE[0][0],initialize.DEFAULT_VARIABLE[1][0],results)
						else:
							print "\n "+Nrs+" Not Results :(.\n"

					except:
						Errors.Errors(event=sys.exc_info(), info=initialize.DEFAULT_VARIABLE[2][0])
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
def run(target,port,dictionary):
	initialize.DEFAULT_VARIABLE [0][0] = target
	initialize.DEFAULT_VARIABLE [1][0] = port
	initialize.DEFAULT_VARIABLE [2][0] = dictionary
	main(False)
# END LINKER FUNCTION
