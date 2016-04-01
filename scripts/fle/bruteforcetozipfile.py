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
import zipfile                #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="LeSZO ZerO"
	initialize.Version            ="2.0"
	initialize.Despcription       ="Brute Force to ZIP file."
	initialize.CodeName           ="fle/bt.zip"
	initialize.DateCreation       ="28/02/2015"      
	initialize.LastModification   ="31/03/2016"

	# DEFAULT VARIABLES             VALUE                  NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[["core/test/test.zip", "target" , "yes" , "Zip with pass"]]     #[0][0]
	initialize.DEFAULT_VARIABLE  +=[[DITIONARY_PASSWORDS , "dict"   , "no"  , "Wordlist"]]          #[1][0]
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
				Message.loading_file()
				Arch = open(initialize.DEFAULT_VARIABLE[1][0],"r")
				if True:
					leeArchivo = Arch.readlines()
					try:
						ZIParch = zipfile.ZipFile(initialize.DEFAULT_VARIABLE[0][0])
						if True:
							for palabra in leeArchivo:
								palabraLlegada = palabra.split("\n")
								try:
									ZIParch.extractall(pwd=str(palabraLlegada[0]))
									if True:
										getFunction.savetwo("BruteForceZIP",initialize.DEFAULT_VARIABLE[0][0],palabraLlegada[0])
										print "\n-"+Suf+" file Cracked with =",str(palabraLlegada[0])+"\n"
										break
								except:
									print " "+Alr+" Checking with ",str(palabraLlegada[0])
					except:
						Errors.Errors(event=sys.exc_info(), info=initialize.DEFAULT_VARIABLE[0][0])
			except:
				Errors.Errors(event=sys.exc_info(), info=initialize.DEFAULT_VARIABLE[1][0])
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
def run(target,dictionary):
	initialize.DEFAULT_VARIABLE[0][0] = target
	initialize.DEFAULT_VARIABLE[1][0] = dictionary
	main(False)
# END LINKER FUNCTION