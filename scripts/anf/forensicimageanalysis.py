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
	initialize.Despcription       ="Forensic Image Analysis with exiftool."
	initialize.CodeName           ="anf/af.imagen"
	initialize.DateCreation       ="28/09/2015"      
	initialize.LastModification   ="31/03/2016"

	# DEFAULT VARIABLES             VALUE                   NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[["core/test/test.jpg", "target" , "yes" , "Path file"]]  #[0][0]
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
				Message.loading_file()
				with open(initialize.DEFAULT_VARIABLE [0][0],'r') as comprossed:
					if True:
						print "\n "+Hlp+" Forensic Imagen Client help"
						print " --------------------------------------------"
						print " |extract_all | extract all MD  | ...       |" 
						print " |comment     | comment some    | comment :)|" 
						print " --------------------------------------------\n"	  												
						cmd="nop"
						parameter="ROO"
						while(cmd!="exit"):
							cmd = raw_input(Message.Client_prompt('forence{IMAGEN}'))
							if(cmd=="extract_all"):
								subprocess.call("perl files/exiftool/exiftool "+initialize.DEFAULT_VARIABLE [0][0], shell=True)
							elif(cmd=="comment"):
								subprocess.call("perl files/exiftool/exiftool -comment="+parameter+" "+initialize.DEFAULT_VARIABLE [0][0], shell=True)
			except:
				Errors.Errors(event=sys.exc_info()[0], info=initialize.DEFAULT_VARIABLE [0][0])
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
def run(target):
	initialize.DEFAULT_VARIABLE [0][0] = target
	main(False)
# END LINKER FUNCTION