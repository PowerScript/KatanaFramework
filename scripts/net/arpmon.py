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
from datetime import datetime
from time import gmtime, strftime
from subprocess import  PIPE, Popen
import re                     #
import curses                 #
import time                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="cl3ar"
	initialize.Version            ="1.1"
	initialize.Despcription       ="Arp Attack monitor"
	initialize.CodeName           ="net/arpmon"
	initialize.DateCreation       ="28/02/2015"      
	initialize.LastModification   ="24/03/2016"

	# DEFAULT VARIABLES
initialize()
# END INFORMATION MODULE

# MAIN FUNCTION
def main(run):
	try:
		if run:	actions=raw_input(Message.prompt(initialize.CodeName))
		else  : actions="run"
		if getFunction.KatanaCheckActionisBack(actions)     :return
		if True:
			Message.run()
			# CODE MODULE    ############################################################################################
			cmd=Popen(['arp', '-a', '-n'], stdout=PIPE, stderr=PIPE)
			try:
				starting=cmd.stdout.read()
				cmd.stdout.close()
			except:
				error=cmd.stderr.read()
				print error
				cmd.stdout.close()
				print "[+] No network found"
			pattern = r"((([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])[ (\[]?(\.|dot)[ )\]]?){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]))"
			print " "+Alr+" Monitoring ARP's tables"
			while(True):
				cmd=Popen(['arp', '-a', '-n'], stdout=PIPE, stderr=PIPE)
				try:
					look=cmd.stdout.read()
					cmd.stdout.close()
				except:
					error=cmd.stderr.read()
					cmd.stdout.close()
					print(" "+Bad+" No network found")
				if(str(starting))==(str(look)):
					print " "+Alr+" all right, the ARP/s tables have not changed... ", " at: ", datetime.now().strftime('%H:%M:%S')
				else:
					print " "+War+" ARP Table Changed ", " at: ", datetime.now().strftime('%H:%M:%S')
					print " "+War+" Data: ---------------------------------------------"
					print " "+look
					print "  ----------------------------------------------------------"
				time.sleep(14)            		
            # END CODE MODULE ############################################################################################
		else:
			getFunction.KatanaCheckActionGlobalCommands(actions)
	except:
		Errors.Errors(event=sys.exc_info(), info=sys.exc_traceback.tb_lineno)
	main(True)
# END MAIN FUNCTION

# LINKER FUNCTION
def run():
	main(False)
# END LINKER FUNCTION