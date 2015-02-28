# KATANA
# Admin finder
# Script by RedToor
# 28/02/2015
import httplib
import socket
import sys
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
defaultdicc="core/db/commons-dir-admin.tbl"
def adminfinder():
	try:
		global defaulthost,defaultport,defaultdicc
		actions = raw_input(B+"   web/cpfinder > "+W)
		if actions == "show options":
			print "     ["+R+"+"+W+"] options"
			print "     target         : yes"
			print "     port           : yes/no"
			print ""
			print "     ["+G+"+"+W+"] options current"
			print "     target         : ",defaulthost
			print "     port           : ",defaultport
			adminfinder()
		elif actions=="back":
			pass
		elif actions=="exit":
			print C+"   GooD"+W+" bye."
			return
		elif actions == "help":
			help.help()
		elif actions[0:10] == "set target":
				defaulthost = actions[11:]
				defaulthost = defaulthost.replace("http://", "")
				print "     target         : "+defaulthost+" "+O+"     Saved!!!"+W
				adminfinder()
		elif actions[0:8] == "set port":
				defaultport = actions[9:]
				defaultport = defaultport.replace("http://", "")
				print "     port           : "+defaultport+" "+O+"     Saved!!!"+W
				adminfinder()
		elif actions=="run":
			print("\n     ["+O+"!"+W+"] Checking target")
			print "     ["+G+"+"+W+"] options current"
			print "     target         : "+defaulthost
			print "     port           : "+defaultport
			print
			try:
				red=socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
				red.connect((defaulthost, int(defaultport))) 
				if True:
					print("     ["+G+"+"+W+"] target LIVE")
					print("     ["+G+"+"+W+"] Running")
					try:
						with open(defaultdicc,'r') as dirt:
							for patch in dirt: 
								patch=patch.replace("\n","")
								patch = "/" + patch
								connection = httplib.HTTPConnection(defaulthost,defaultport)
								connection.request("GET",patch)
								response = connection.getresponse()
								if response.status == 200:
									print "     ["+G+"+"+W+"] SUCCESSFUL Possible +- CPANEL in "+patch
									red.close
									adminfinder()
								else:
									print "     ["+O+"!"+W+"] Checking with "+patch
					except(KeyboardInterrupt, SystemExit):
						print("   ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
			except:
				print("     ["+R+"-"+W+"] target DEAD")
	except(KeyboardInterrupt, SystemExit):
		print("   ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
	adminfinder()