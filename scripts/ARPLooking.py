# :-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                 #
# Modules   : ARPLooking  #
# Script by : cl34r       #
# Date      : 28/02/2015  #
# :-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core             #
from core.design import * #
from core import help     #
from core import ping     #
d=DESIGN()                #
# :-:-:-:-:-:-:-:-:-:-:-: #
# Libraries               #
import re
import curses
import time
from datetime import datetime
from time import gmtime, strftime
from subprocess import  PIPE, Popen
# :-:-:-:-:-:-:-:-:-:-:-: #
# Default                 #
# :-:-:-:-:-:-:-:-:-:-:-: #
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
                                        try:
                                                cmd=Popen(['arp', '-a', '-n'], stdout=PIPE, stderr=PIPE)
                                                try:
                					look=cmd.stdout.read()
                			                cmd.stdout.close()
                                                except:
                				        error=cmd.stderr.read()
                				        print error
                        				cmd.stdout.close()
                					print("     ["+R+"-"+W+"] No network found")
                                                if(str(starting))==(str(look)): 
                                                        print "     ["+O+"!"+W+"] Good...           ", " at: ", datetime.now().strftime('%H:%M:%S')
                                                else: 
                                                        print "     ["+O+"!"+W+"] ARP Table Changed ", " at: ", datetime.now().strftime('%H:%M:%S')
                                                        print "     ["+G+"+"+W+"] Data:\n", look
                                                time.sleep(15)
                                        except:
                                                d.kbi()                                                
                                                arplook(0)
                        else:
                                d.nocommand()
        except:
                d.kbi()
                exit()
        arplook(0)
