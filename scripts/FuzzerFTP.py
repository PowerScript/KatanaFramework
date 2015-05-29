# KATANA
# Fuzzer FTP 
# Script by RedToor
# 23/05/2015

from core import help
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
defaultport="21"
defaultdat1="anonymous"
defaultdat2="pass"
defaultlent="5000"
defaultstri="A"
def fftp():
	try:
		global defaulthost,defaultport,defaultdat1,defaultdat2,defaultstri,defaultlent
		actions = raw_input(O+"     ktn/clt/ftp > "+W)
		if actions == "show options":
			print ""
			print "     ["+R+"+"+W+"] options"
			print "     |host           : yes"
			print "     |port           : no/yes"
			print "     |username       : yes"
			print "     |password       : yes"
			print "     |length         : yes"
			print "     |buffer         : yes"
			print ""
			print "     ["+G+"+"+W+"] options current"
			print "     |host           : ",defaulthost
			print "     |port           : ",defaultport
			print "     |username       : ",defaultdat1
			print "     |password       : ",defaultdat2
			print "     |length         : ",defaultlent
			print "     |buffer         : ",defaultstri
			print ""
			fftp()
		elif actions[0:8] == "set host":
			defaulthost = actions[9:]
			print "     host           : "+defaulthost+" "+O+"     Saved!!!"+W
			fftp()
		elif actions[0:8] == "set port":
			defaultport= actions[9:]
			print "     port           : "+defaultport+" "+O+"     Saved!!!"+W
			fftp()
		elif actions[0:12] == "set username":
			defaultdat1 = actions[13:]
			print "     username       : "+defaultdat1+" "+O+"     Saved!!!"+W
			fftp()
		elif actions[0:12] == "set password":
			defaultdat2= actions[13:]
			print "     password       : "+defaultdat2+" "+O+"     Saved!!!"+W
			fftp()
		elif actions[0:10] == "set buffer":
			defaultstri= actions[11:]
			print "     buffer         : "+defaultstri+" "+O+"     Saved!!!"+W
			fftp()
		elif actions[0:10] == "set length":
			defaultlent= actions[11:]
			print "     length         : "+defaultlent+" "+O+"     Saved!!!"+W
			fftp()
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
			print "     length         : ",defaultlent
			print "     buffer         : ",defaultstri
			print ""
			try:
				red=socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
				red.connect((defaulthost, int(defaultport))) 
				red.recv(4000)
				if True:
					try:
						print("     ["+G+"+"+W+"] host LIVE")
						print("     ["+G+"+"+W+"] Running")
						print("     ["+O+"!"+W+"] Logging...")								
						red.send("USER "+defaultdat1+"\r\n")								
						red.send("PASS "+defaultdat2+"\r\n")								
						red.recv(1020)											
						last=red.recv(4000)										
						succefull="230"	
						if last.find(succefull) == 0:
							print("     ["+G+"+"+W+"] Logged")
							print("     ["+O+"+"+W+"] Fuzzing...")
							red.send("PASV\r\n")								
							red.recv(1020)	
							string=defaultstri*defaultlent
							red.send("DELE "+string+"\r\n")
							b=red.recv(2000000)
							print b
							red.close()
						else:
							print("     ["+R+"-"+W+"] No Logged")
					except(KeyboardInterrupt):
						print("\n   ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
						exit()
			except:
				print("     ["+R+"-"+W+"] target off")	
		else:
			print "     ["+O+"!"+W+"] command No Accept"+W
	except(KeyboardInterrupt):
		print("\n   ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
		exit()
	fftp()