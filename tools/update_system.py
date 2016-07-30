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
	Arguments   = {
	
	'y':[False,'No Assume "yes" and proceed with update']}

def Main():
	Assume="--yes"
	if init.var['y'] == "enable":Assume=""
	sysc('sudo apt-get update && sudo apt-get '+Assume+' upgrade && sudo apt-get clean && sudo apt-get dist-upgrade '+Assume)
