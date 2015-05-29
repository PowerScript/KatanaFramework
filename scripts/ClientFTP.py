# KATANA
# client FTP 
# Script by RedToor
# 03/03/2015

from core import help
from lib.ftplib.ftplib import FTP
import subprocess
import os
W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'
defaulthost="127.0.0.1"
defaultport="21"
defaultdat1="anonymous"
defaultdat2="pass"
def cftp():
	try:
		global defaulthost,defaultport,defaultdat1,defaultdat2
		actions = raw_input(O+"     ktn/clt/ftp > "+W)
		if actions == "show options":
			print ""
			print "     ["+R+"+"+W+"] options"
			print "     |host           : yes"
			print "     |port           : no/yes"
			print "     |username       : yes"
			print "     |password       : yes\n"
			print ""
			print "     ["+G+"+"+W+"] options current"
			print "     |host           : ",defaulthost
			print "     |port           : ",defaultport
			print "     |username       : ",defaultdat1
			print "     |password       : ",defaultdat2
			print ""
			cftp()
		elif actions[0:8] == "set host":
			defaulthost = actions[9:]
			print "     host           : "+defaulthost+" "+O+"     Saved!!!"+W
			cftp()
		elif actions[0:8] == "set port":
			defaultport= actions[9:]
			print "     port           : "+defaultport+" "+O+"     Saved!!!"+W
			cftp()
		elif actions[0:12] == "set username":
			defaultdat1 = actions[13:]
			print "     username       : "+defaultdat1+" "+O+"     Saved!!!"+W
			cftp()
		elif actions[0:12] == "set password":
			defaultdat2= actions[13:]
			print "     password       : "+defaultdat2+" "+O+"     Saved!!!"+W
			cftp()
		elif actions=="back":
			return 
		elif actions=="exit":
			print C+"     GooD"+W+" bye."
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
			print ""
			try:
				ftp = FTP(defaulthost) 
				if True:
					try:
						print("     ["+G+"+"+W+"] host LIVE")
						print("     ["+G+"+"+W+"] Running")
						ftp.login(defaultdat1,defaultdat2)									
						if True:
							try:
								cmd="nop"
								patch=""
								print "\n     ["+B+"*"+W+"] FTP Client help\n"
								print "           ls	: list files  ex: ls" 
								print "           cd	: change dir  ex: cd web/site"
								print "           mk	: create dir  ex: mk images"
								print "           rm	: remove file ex: remove config.js"
								print "           rmd  : remove dir  ex: remove sex"
								print "           get  : get file    ex: get index.php"
								print "           put  : up file     ex: put login.php"
								while(cmd!="exit"):
									cmd = raw_input(O+" ftp/"+patch+"> "+W)
									if cmd == "ls":
										ftp.retrlines("LIST")
									if cmd[0:2] == "cd":
										try:
											ftp.cwd(cmd[3:])
											if True:
												patch=cmd[3:]
												if patch == "..":
													patch=""
										except:
											print "     ["+O+"!"+W+"] Error: diretory wrong"
									if cmd[0:3] == "get":
										lfile=cmd[4:].replace("\n","")
										try:
											ftp.retrbinary('RETR '+lfile,open(lfile,'wb').write)
											if True:
												subprocess.Popen("cp "+lfile+" /root/Desktop/;rm "+lfile+"", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
												print "      ["+O+"!"+W+"] Saved, /root/Desktop/"+lfile
										except:
											print "     ["+O+"!"+W+"] Error: file wrong"
									if cmd[0:3] == "put":
										lfile=cmd[4:].replace("\n","")
										w = open(lfile, 'rb')
										try:
											ftp.storbinary("STOR r.r",w)
										except:
											print "     ["+O+"!"+W+"] Error: file wrong"
									if cmd[0:2] == "rm":
										try:
											ftp.delete(cmd[3:])
										except:
											print "     ["+O+"!"+W+"] Error: file wrong"
									if cmd[0:3] == "rmd":
										pat=cmd[4:].replace("\n","")
										ftp.rmd(pat)
									if cmd[0:2] == "mk":
										try:
											ftp.mkd(cmd[3:])
										except:
											print "     ["+O+"!"+W+"] Error: diretory wrong"

							except(KeyboardInterrupt):
								print("\n     ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
							except Exception,e:
								print("     ["+R+"-"+W+"] Timeout", e)
					except:
						print("     ["+R+"-"+W+"] username or password Wrong")
			except:
				print("     ["+R+"-"+W+"] target off")
		else:
			print "     ["+O+"!"+W+"] command No Accept"+W
	except(KeyboardInterrupt):
		print("\n     ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
	cftp()