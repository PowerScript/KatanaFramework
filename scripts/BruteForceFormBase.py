# KATANA
# Brute Force Form Base HTTP
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
defoulthost="127.0.0.1"
defoultport="80"
defoultpach="/admin/login.php"
defoultdic1="core/db/user.dicc"
defoultdic2="core/db/pass.dicc"
def httpformbasebruteforce():
	try:
		global defoulthost,defoultport,defoultpach,defoultdic1,defoultdic2
		actions = raw_input(B+"   web/formbt > "+W)
		if actions == "show options":
			print "     ["+R+"+"+W+"] options"
			print "     target         : yes"
			print "     port           : no/yes"
			print "     patch          : yes"
			print "     dictionaries   : no/yes\n"
			print "     ["+G+"+"+W+"] options current"
			print "     target         : ",defoulthost
			print "     port           : ",defoultport
			print "     patch          : ",defoultpach
			print "     dictionary_1   : ",defoultdic1
			print "     dictionary_2   : ",defoultdic2
			httpformbasebruteforce()
		elif actions=="back":
			pass
		elif actions=="exit":
			print C+"   GooD"+W+" bye."
			return
		elif actions[0:10] == "set target":
				defoulthost = actions[11:]
				defoulthost = defoulthost.replace("http://", "")
				print "     target         : "+defoulthost+" "+O+"     Saved!!!"+W
				httpformbasebruteforce()
		elif actions[0:8] == "set port":
				defoultport = actions[9:]
				print "     port           : "+defoultport+" "+O+"     Saved!!!"+W
				httpformbasebruteforce()
		elif actions[0:9] == "set patch":
				defoultpach = actions[10:]
				print "     patch          : "+defoultpach+" "+O+"     Saved!!!"+W
				httpformbasebruteforce()
		elif actions[0:16] == "set dictionary_1":
				defoultdic1 = actions[17:]
				print "     dictionary_1   : "+defoultdic1+" "+O+"     Saved!!!"+W
				httpformbasebruteforce()
		elif actions[0:16] == "set dictionary_2":
				defoultdic2 = actions[17:]
				print "     dictionary_2   : "+defoultdic2+" "+O+"     Saved!!!"+W
				httpformbasebruteforce()
		elif actions == "help":
			help.help()

	except(KeyboardInterrupt, SystemExit):
		print("   ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
	httpformbasebruteforce()