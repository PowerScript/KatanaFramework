# KATANA
# client POP3 
# Script by RedToor
# 22/05/2015
from core import help
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
defaultdat1="webmaster@localhost.com"
defaultdat2="password"
def cpop3():
	try:
		global defaulthost,defaultport,defaultdat1,defaultdat2
		actions = raw_input(B+"   clt/pop3 > "+W)
		if actions == "show options":
			print "     ["+R+"+"+W+"] options"
			print "     host           : yes"
			print "     port           : no/yes"
			print "     username       : yes"
			print "     password       : yes\n"
			print "     ["+G+"+"+W+"] options current"
			print "     host           : ",defaulthost
			print "     port           : ",defaultport
			print "     username       : ",defaultdat1
			print "     password       : ",defaultdat2
			cpop3()
		elif actions[0:8] == "set host":
			defaulthost = actions[9:]
			print "     host           : "+defaulthost+" "+O+"     Saved!!!"+W
			cpop3()
		elif actions[0:8] == "set port":
			defaultport= actions[9:]
			print "     port           : "+defaultport+" "+O+"     Saved!!!"+W
			cpop3()
		elif actions[0:12] == "set username":
			defaultdat1 = actions[13:]
			print "     username       : "+defaultdat1+" "+O+"     Saved!!!"+W
			cpop3()
		elif actions[0:12] == "set password":
			defaultdat2= actions[13:]
			print "     password       : "+defaultdat2+" "+O+"     Saved!!!"+W
			cpop3()
		elif actions=="back":
			pass 
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
				red=poplib.POP3(defaulthost, defaultport)
				if True:
					try:
						print("     ["+G+"+"+W+"] host LIVE")
						print("     ["+G+"+"+W+"] Running")
						red.user(defaultdat1)
						red.pass_(defaultdat2)								
						if True:
							try:
								cmd="nop"
								print "\n     ["+B+"*"+W+"] POP3 Client help\n"
								print "           list	: list mails     ex: list"
								print "           retr	: show mail      ex: retr 2"
								print "           dele	: remove mail    ex: remove 2"
								print "           quit	: exit d remove  ex: quit"
								while(cmd!="exit"):
									cmd = raw_input(O+" pop3> "+W)
									if cmd == "list":
										numMessages = len(red.list()[1])
										for i in range(numMessages):
										    print "	mail "+str(i)
									if cmd[0:4] == "retr":
										for j in red.retr(int(cmd[5:])+1)[1]:
											print j
									if cmd[0:4] == "dele":
										try:
										    red.dele(int(cmd[5:])+1)[1]
										    if True:
										    	print "      ["+O+"!"+W+"] email marked for delete ('quit' for exit and delete all email marked)"
										except Exception,e:
											 print("     ["+R+"-"+W+"] Error", e)
									if cmd == "quit":
										red.quit()
										print "      ["+O+"!"+W+"] Exit, bye."
										break
							except(KeyboardInterrupt):
								print("\n   ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
							except Exception,e:
								print("     ["+R+"-"+W+"] Timeout", e)
					except:
						print("     ["+R+"-"+W+"] username or password Wrong")
			except:
				print("     ["+R+"-"+W+"] target DEAD")
	except(KeyboardInterrupt):
		print("\n   ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
	cpop3()