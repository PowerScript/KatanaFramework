# KATANA
# WPA Brute Force
# Script by RedToor
# 11/06/2015

from core import help
import subprocess
W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'
defaultcap="core/test/wpa.cap-01.cap"
defaultdic="core/db/pass.dicc"
defaultmac="E8:40:F2:32:37:FD"
def wpabtf():
	global defaultdic,defaultcap,defaultmac
	actions = raw_input(O+"     ktn/wifi/wpabtf > "+W)
	if actions == "show options":
		print ""
		print "     ["+R+"+"+W+"] options"
		print "     |File Capture    : yes"
		print "     |Mac Target      : yes"
		print "     |Dictionary      : yes/no\n"
		print ""
		print "     ["+G+"+"+W+"] options current"
		print "     |cap             : ",defaultcap
		print "     |mac             : ",defaultmac
		print "     |dictionary      : ",defaultdic
		print ""
	elif actions=="back":
		pass 
	elif actions=="exit":
		print C+"     GooD"+W+" bye."
		exit()
	elif actions[0:7] == "set cap":
			defaultcap = actions[8:]
			print "     Capture      : "+defaultcap+" "+O+"     Saved!!!"+W
			wpabtf()
	elif actions[0:14] == "set dictionary":
			defaultdic = actions[15:]
			print "     Dictionary   : "+defaultdic+" "+O+"     Saved!!!"+W
			wpabtf()
	elif actions[0:7] == "set mac":
			defaultmac = actions[8:]
			print "     Mac Target   : "+defaultmac+" "+O+"     Saved!!!"+W
			wpabtf()
	elif actions == "help":
			help.help()
	elif actions == "run":
		try:
			print ""
			print "     ["+G+"+"+W+"] options current"
			print "     Capture      : ",defaultcap
			print "     Mac Target   : ",defaultmac
			print "     Dictionary   : ",defaultdic
			print ""
			try:
				Arch=open(defaultdic,'r')
				if True:
					try:
						Arch=open(defaultcap,'r')
						if True:
							try:
								subprocess.call('aircrack-ng -w '+defaultdic+' -b '+defaultmac+' '+defaultcap+'', shell=True)
								print""
							except(KeyboardInterrupt, SystemExit):
								print("\n     ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
					except:
						print "     ["+O+"!"+W+"] Error to open Capture"
			except:
				print "     ["+O+"!"+W+"] Error to open Dictionary"
				
		except(KeyboardInterrupt, SystemExit):
			print("\n     ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
	else:
		print "     ["+O+"!"+W+"] command No Accept"+W
	wpabtf()
