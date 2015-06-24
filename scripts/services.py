# KATANA
# Services
# Script by RedToor
# 11/06/2015

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
def services(process):
	try:
		actions = raw_input(O+"     ktn/server/"+process+" > "+W)
		if actions == "show options":
			print ""
			print ""
			print "     ["+G+"!"+W+"] Not Options enables."
			print ""
			print ""
			services(process)
		elif actions=="exit":
			print C+"     GooD"+W+" bye."
			return
			return
		elif actions == "help":
			help.help()
		elif actions == "run":
			print ""
			try:
				if True:
					print("     ["+G+"+"+W+"] Running")
					try:
						print("     ["+O+"!"+W+"] Starting Service "+process)
						subprocess.call('service '+process+' start > nul', shell=True)
						print("     ["+G+"+"+W+"] Service started")
						print ""
						raw_input("     ["+O+"!"+W+"] Press any key for Stop Service")
						print("     ["+O+"!"+W+"] Stopping Service "+process)
						subprocess.call('service '+process+' stop > nul ', shell=True)
						print("     ["+G+"+"+W+"] Service Stoped")
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
		print("\n     ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
		exit()
	services(process)
