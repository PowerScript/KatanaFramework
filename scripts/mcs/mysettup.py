# This module requires katana framework 
# https://github.com/RedToor/Katana
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                 #
from core.design import *     #
from core.Setting import *    #
from core import Errors       #
from core import getFunction  #
import sys                    #
Message=DESIGN()              #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                   #
import commands               #
from core import info         #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="RedToor"
	initialize.Version            ="2.0"
	initialize.Despcription       ="Setting computer"
	initialize.CodeName           ="mcs/i.settup"
	initialize.DateCreation       ="30/08/2015"      
	initialize.LastModification   ="25/03/2016"

	# DEFAULT VARIABLES
initialize()
# END INFORMATION MODULE

# MAIN FUNCTION
def main(run):
	try:
		if True:
			Message.run()
			# CODE MODULE    ############################################################################################
			print " "+colors[12]+"Computer"+colors[0]
			print "       IP Local   : ",getFunction.Myip()
			print "       Ip Externa : ",getFunction.get_external_ip()
			print "       Interfaces : ",getFunction.get_interfaces()
			print "       Gateway    : ",getFunction.get_gateway()
			print "       Machaddress: ",getFunction.my_mac_address()	
			print "       Username   : ",commands.getoutput('whoami')
			print "       OS         : ",commands.getoutput('uname')
			print "       Version    : ",commands.getoutput('uname -r')
			print " "+colors[13]+"Katana"+colors[0]
			print "       Core       : ",info.version
			print "       Build      : ",info.build
			return
            # END CODE MODULE ############################################################################################
	except:
		Errors.Errors(event=sys.exc_info(), info=sys.exc_traceback.tb_lineno)
	main(True)
# END MAIN FUNCTION

# LINKER FUNCTION
def run():
	main(False)
# END LINKER FUNCTION