# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : Client POP3    #
# Script by : RedToor        #
# Date      : 22/05/2015     #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Katana Core                #
from core.design import *    #
from core.Setting import *   #
from core import Errors      #
from core import help        #
from core import ping        #
import sys                   #
d=DESIGN()                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Libraries                  #
import poplib                #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaulthost=LOCAL_IP
defaultport=POP_PORT
defaultuser=USERNAME
defaultpass=PASSWORD
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(target,port,username,password):
	global defaulthost,defaultport,defaultuser,defaultpass
	defaulthost=target
	defaultport=port
	defaultuser=username
	defaultpass=password
	cpop3(1)

def cpop3(run):
	try:
		global defaulthost,defaultport,defaultuser,defaultpass
		if run!=1:
			actions=raw_input(d.prompt("clt/pop3"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("target","yes","IP or DNS",defaulthost)
			d.descrip("port","no","Port of target",defaultport)
 			d.descrip("user","yes","Username",defaultuser)
 			d.descrip("pass","yes","Password",defaultpass)
			d.space()
			cpop3(0)
		elif actions[0:10] == "set target":
			defaulthost=defaulthost.replace("http://", "")
			defaulthost=ping.update(defaulthost,actions,"target")
			d.change("target",defaulthost)
		elif actions[0:8] == "set port":
			defaultport=ping.update(defaultport,actions,"port")
			d.change("port",defaultport)
		elif actions[0:8] == "set user":
			defaultuser=ping.update(defaultuser,actions,"user")
			d.change("user",defaultuser)
		elif actions[0:8] == "set pass":
			defaultpass=ping.update(defaultpass,actions,"pass")
			d.change("pass",defaultpass)
		elif actions=="exit" or actions=="x":
			d.goodbye()
			exit()
		elif actions=="help" or actions=="h":
			help.help()
		elif actions=="back" or actions=="b":
			return
		elif actions=="run"  or actions=="r":
			d.run()
			try:
				red=poplib.POP3(defaulthost, defaultport)
				try:
					red.user(defaultuser)
					red.pass_(defaultpass)	
					if True:
						cmd="nop"
						print "\n "+Hlp+" POP3 Client help\n"
						print "  ----------------------------------------"
						print "  |"+colors[6]+"Commd"+colors[0]+"| "+colors[6]+"Description"+colors[0]+" | "+colors[6]+"Examples"+colors[0]+"         |"
						print "  ----------------------------------------"
						print "  |list	| list mails  | list             |" 
						print "  |retr	| show mail   | retr 2           |"
						print "  |dele	| remove mail | dele 2           |"
						print "  |quit	|exit d remove| quit             | "
						print "  ----------------------------------------"
						print ""
						if True:
							if True:
								if True:
									while(cmd!="exit"):
										cmd = raw_input(d.Client_prompt('pop3'))
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
											    	print " "+Alr+" email marked for delete ('quit' for exit and delete all email marked)"
											except Exception,e:
												 print(" "+Bad+" Error", e)
										if cmd == "quit":
											red.quit()
											print " "+Alr+" Exit, bye."
											break
				except:
					d.No_match()
			except:
				Errors.Errors(event=sys.exc_info()[0], info=defaulthost+":"+defaultport)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info()[0], info=False)
	cpop3(0)