# This Tool requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from os import system as sysc
# END LIBRARIES 

class init:
	
	Author      = "0xicl33n"
	Description = "Update Debian based system"
	var         = {}
	Arguments   = {'y'[True,'Assume yes and proceed with update']}

def Main():
	sysc('sudo apt-get update && sudo apt-get %s upgrade && sudo apt-get clean && sudo apt-get dist-upgrade %s') % init.var['y']