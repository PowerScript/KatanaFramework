# KATANA
# Whois
# Script by RedToor
# 09/07/2015

from core import help
from lib import whois
import socket

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
def wuis():
	try:
		global defaulthost,defaultport
		actions = raw_input(O+"     ktn/web/whois > "+W)
		if actions == "show options":
			print ""
			print "     ["+R+"+"+W+"] options"
			print "     |host           : yes\n"
			print ""
			print "     ["+G+"+"+W+"] options current"
			print "     |host           : ",defaulthost
			print ""
			wuis()
		elif actions[0:8] == "set host":
			defaulthost = actions[9:]
			print "     host           : "+defaulthost+" "+O+"     Saved!!!"+W
			wuis()
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
				red=socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
				red.connect((defaulthost, int(defaultport))) 
				if True:
					print("     ["+G+"+"+W+"] target LIVE")
					print("     ["+G+"+"+W+"] Running")
					print ""
					try:
						w = whois.whois(defaulthost)
						if w:
							wd = w.__dict__
							for k, v in wd.items():
								print('%20s\t"%s"' % (k, v))
							print ""
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
		exit()
	wuis()
