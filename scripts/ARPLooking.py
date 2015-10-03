# :-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                 #
# Modules   : ARPLooking  #
# Script by : cl34r       #
# Date      : 28/02/2015  #
# :-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core             #
from core.design import * #
from core.Setting import *#
from core import Errors   #
from core import help     #
from core import ping     #
import sys
d=DESIGN()                #
# :-:-:-:-:-:-:-:-:-:-:-: #
# Libraries               #
from datetime import datetime
from time import gmtime, strftime
from subprocess import  PIPE, Popen
import re
import curses
import time
# :-:-:-:-:-:-:-:-:-:-:-: #
# Default                 #
# :-:-:-:-:-:-:-:-:-:-:-: #
defautlany="if i believed in god, i'll be his slave."
# :-:-:-:-:-:-:-:-:-:-:-: #

def run():
        arplook(1)

def arplook(run):
        try:
                while True:   
                        if run!=1:
                                actions=raw_input(d.prompt("net/arplook"))
                        else:
                                actions="run"
                        if actions == "show options" or actions == "sop":
                                d.option()
                                d.noptions()
                        elif actions=="exit" or actions=="x":
                                d.goodbye()
                                exit()
                        elif actions=="help" or actions=="h":
                                help.help()
                        elif actions=="back" or actions=="b":
                                pass
                        elif actions=="run"  or actions=="r":
                                d.run()
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
                                if True:
					print " "+Alr+" Monitoring ARP's tables"
					while(True):
		                                try:
		                                        cmd=Popen(['arp', '-a', '-n'], stdout=PIPE, stderr=PIPE)
		                                        try:
		        					look=cmd.stdout.read()
		        			                cmd.stdout.close()
		                                        except:
		        				        error=cmd.stderr.read()
		        				        #print error
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
		                                except:                                              
		                                        Errors.Errors(event=sys.exc_info()[0], info=True)
                        else:
				d.No_actions()
        except:
                Errors.Errors(event=sys.exc_info(), info=False)
        arplook(0)
