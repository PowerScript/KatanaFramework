# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from datetime import datetime
from time import gmtime, strftime
from subprocess import  PIPE, Popen
import re,curses,time                   
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="cl3ar"
	init.Version            ="1.1"
	init.Description        ="Arp Attack monitor."
	init.CodeName           ="net/sf.mon"
	init.DateCreation       ="28/02/2015"      
	init.LastModification   ="23/12/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	cmd=Popen(['arp', '-a', '-n'], stdout=PIPE, stderr=PIPE)
	try:
		starting=cmd.stdout.read()
		cmd.stdout.close()
	except:
		cmd.stdout.close()
		printk.err("No network found")
	pattern = r"((([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])[ (\[]?(\.|dot)[ )\]]?){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]))"
	printk.inf("Monitoring ARP's tables")
	printk.inf("if you want to stop server (PRESS [Ctrol + C])")

	while(True):
		cmd=Popen(['arp', '-a', '-n'], stdout=PIPE, stderr=PIPE)
		try:
			look=cmd.stdout.read()
			cmd.stdout.close()
		except:
			printk.err("No network found")
		if(str(starting))==(str(look)):
			printk.inf("all right, the ARP/s tables have not changed... at: "+datetime.now().strftime('%H:%M:%S'))
		else:
			printk.war(" ARP Table Changed at: "+datetime.now().strftime('%H:%M:%S'))
			printk.war(" Data: ---------------------------------------------")
			print " "+look
			printk.war(" Data: ---------------------------------------------")
		time.sleep(14)

# END CODE MODULE ############################################################################################