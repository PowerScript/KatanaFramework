# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
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
	init.LastModification   ="23/12/2016"
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
	printk.suff("Computer")
	print "       | IP Local   : ",NET.GetLocalIp()
	print "       | Ip Externa : ",NET.GetPublicIp()
	print "       | Interfaces : ",NET.GetInterfacesOnSystem()
	print "       | Gateway    : ",NET.GetGateway()
	print "       | Machaddress: ",NET.GetMacAddress()	
	print "       | Username   : ",commands.getoutput('whoami')
	print "       | OS         : ",commands.getoutput('uname')
	print "       | Version    : ",commands.getoutput('uname -r')
	printk.suff("Katana")
	print "       | Core       : ",Information.version
	print "       | Build      : ",Information.build

# END CODE MODULE ############################################################################################
