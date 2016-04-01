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
import subprocess             #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="RedToor"
	initialize.Version            ="1.1"
	initialize.Despcription       ="Joomla Scan Vulnerability - External Script"
	initialize.CodeName           ="web/sc.joomla"
	initialize.DateCreation       ="26/05/2015"      
	initialize.LastModification   ="24/03/2016"

	# DEFAULT VARIABLES             VALUE                NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[[LOCAL_IP          , "target" , "yes" , "IP or DNS"]]      #[0][0]
	initialize.DEFAULT_VARIABLE  +=[[HTTP_PORT         , "port"   , "no"  , "Service port"]]   #[1][0]
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
					subprocess.call('cd files/joomlavs/;ruby joomlavs.rb -a -u '+initialize.DEFAULT_VARIABLE[0][0]+":"+initialize.DEFAULT_VARIABLE[1][0], shell=True)
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
	main(False)
# END LINKER FUNCTION