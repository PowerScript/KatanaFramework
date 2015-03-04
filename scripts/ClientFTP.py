# KATANA
# client FTP 
# Script by RedToor
# 03/03/2015
from core import help
from lib.ftplib.ftplib import FTP
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
defaultdat1="anonymous"
defaultdat2="password"
def cftp():
	global defaulthost,defaultport,defaultdat1,defaultdat2
	actions = raw_input(B+"   clt/ftp > "+W)
	if actions=="back":
		return 
	elif actions=="exit":
		print C+"   GooD"+W+" bye."
		exit()
	elif actions == "help":
		help.help()
	elif actions == "run":
		print("\n     ["+O+"!"+W+"] Checking target")
		print "     ["+G+"+"+W+"] options current"
		print "     host           : ",defaulthost
		print "     port           : ",defaultport
		print "     username       : ",defaultdat1
		print "     password       : ",defaultdat2
		try:
			ftp = FTP('ftp.debian.org')   
			if True:
				try:
					print("     ["+G+"+"+W+"] host LIVE")
					print("     ["+G+"+"+W+"] Running")
					ftp.login()        
					if True:
						try:
							cmd="nop"
							while(cmd!="exit"):
								cmd = raw_input(O+"  CmD/ > "+W)
								#FTP.transfercmd(cmd)        
								#ftp.cwd('debian')               
								ftp.retrlines(cmd)           
								#ftp.retrbinary('RETR README', open('README', 'wb').write)
							#ftp.quit()
						except(KeyboardInterrupt):
							print("   ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
						except:
							print("     ["+R+"-"+W+"] Timeout")
				except:
					print("     ["+R+"-"+W+"] username or password Wrong")
		except:
			print("     ["+R+"-"+W+"] target DEAD")
	cftp()
