# KATANA
# Joomscan runer 
# Script by RedToor
# 26/05/2015

import subprocess
from core import help
W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'
defaulthost="127.0.0.1"
defaultport="80"
def xjoomla():
	try:
		global defaulthost,defaultport
		actions = raw_input(O+"     ktn/web/joomscan > "+W)
		if actions == "show options":
			print ""
			print "     ["+R+"+"+W+"] options"
			print "     |host           : yes\n"
			print ""
			print "     ["+G+"+"+W+"] options current"
			print "     |host           : ",defaulthost
			print ""
			xjoomla()
		elif actions[0:8] == "set host":
			defaulthost = actions[9:]
			print "     host           : "+defaulthost+" "+O+"     Saved!!!"+W
			xjoomla()
		elif actions=="exit":
			print C+"     GooD"+W+" bye."
			return
			return
		elif actions == "run":
			print("\n     ["+O+"!"+W+"] Checking target")
			print "     ["+G+"+"+W+"] options current"
			print "     host           : ",defaulthost
			print ""
			try:
				if True:
					print("     ["+G+"+"+W+"] target LIVE")
					print("     ["+G+"+"+W+"] Running")
					try:
						subprocess.call('cd /usr/share/joomscan/;./joomscan.pl -u '+defaulthost, shell=True)
					except(KeyboardInterrupt):
						print("\n     ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
			except:
				print("     ["+R+"-"+W+"] target off")
		elif actions=="back":
			return
		else:
			print "     ["+O+"!"+W+"] command No Accept"+W
	except(KeyboardInterrupt):
		print("\n   ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
	xjoomla()