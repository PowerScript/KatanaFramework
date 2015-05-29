# KATANA
# Brute Force Form Base HTTP
# Script by cl34r
# 28/02/2015

import re
import curses
import time
from datetime import datetime
from time import gmtime, strftime
from core import help
from subprocess import  PIPE, Popen
cmd=Popen(['arp', '-a', '-n'], stdout=PIPE, stderr=PIPE)
W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'
try:
        starting=cmd.stdout.read()
        cmd.stdout.close()
except:
        error=cmd.stderr.read()
        print error
        cmd.stdout.close()
	print "["+R+"-"+W+"] No network found"
pattern = r"((([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])[ (\[]?(\.|dot)[ )\]]?){3}([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5]))"
defaulthost="127.0.0.1"
def arplook():
        global defaulthost
        while True:   
                actions = raw_input(O+"     ktn/web/arplook > "+W)
                if actions == "help":
                        help.help()
                elif actions == "exit":
                        print C+"   GooD"+W+" bye."
                        exit()
                elif actions == "back":
                        return
                elif actions == "show options":
                        print ""
                        print "     ["+R+"+"+W+"] options"
                        print "     |target         : no\n"
                        print ""
                        print "     ["+G+"+"+W+"] options current"
                        print "     |target         : ",defaulthost
                        print ""
                        arplook()
                elif actions[0:10] == "set target":
                        print "     ["+O+"!"+W+"] You can't do changes"
                        arplook()
                elif actions == "run":
                        print("\n     ["+G+"+"+W+"] Running")
                        while 1:
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
                                except(KeyboardInterrupt, SystemExit):
                                        print("     ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
                                        return
                                        return
                                        exit()
        arplook()
