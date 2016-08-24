# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES 
from core.Function import ListDevicesConnectADB,MakeTable
from lib.adb.adb import adb_commands,common_cli
import stat,os
# END LIBRARIES

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.0"
	init.Description        ="Forensic Android Analysis."
	init.CodeName           ="anf/af.imagen"
	init.DateCreation       ="23/08/2016"      
	init.LastModification   ="23/08/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE               RQ     DESCRIPTION
		'device':["16xxxxxxxxxxxxxx" ,True ,'Device Target']
	}

	init.aux = """
 List Device Connected:\n"""+str(ListDevicesConnectADB())+"\n"

	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	print " Comming soon..."


# END CODE MODULE ############################################################################################
