# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from core.Function import get_external_ip,get_local_ip,get_interfaces,get_gateway,get_my_mac_address
from core import Information
import commands
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="2.0"
	init.Description        ="Setting computer"
	init.CodeName           ="mcs/i.settup"
	init.DateCreation       ="30/08/2015"      
	init.LastModification   ="25/03/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}
	
	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE     RQ     DESCRIPTION
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	printAlert(3,"Computer")
	print "       | IP Local   : ",get_local_ip()
	print "       | Ip Externa : ",get_external_ip()
	print "       | Interfaces : ",get_interfaces()
	print "       | Gateway    : ",get_gateway()
	print "       | Machaddress: ",get_my_mac_address()	
	print "       | Username   : ",commands.getoutput('whoami')
	print "       | OS         : ",commands.getoutput('uname')
	print "       | Version    : ",commands.getoutput('uname -r')
	printAlert(3,"Katana")
	print "       | Core       : ",Information.version
	print "       | Build      : ",Information.build
	Space()
# END CODE MODULE ############################################################################################
