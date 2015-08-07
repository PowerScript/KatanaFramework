# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : Client POP3    #
# Script by : RedToor        #
# Date      : 22/05/2015     #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Katana Core                #
from core.design import *    #
from core import help        #
from core import ping        #
d=DESIGN()                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Libraries                  #
import poplib                #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaulthost="127.0.0.1"
defaultport="110"
defaultuser="admin"
defaultpass="admin"
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(para,parb,parc,pard):
	global defaulthost,defaultport,defaultuser,defaultpass
	defaulthost=para
	defaultport=parb
	defaultuser=parc
	defaultpass=pard
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
			print ""
			cpop3(0)
		elif actions[0:10] == "set target":
			defaulthost = actions[11:]
			defaulthost = defaulthost.replace("http://", "")
			d.change("target",defaulthost)
			cpop3(0)
		elif actions[0:8] == "set port":
			defaultport = actions[9:]
			d.change("port",defaultport)
			cpop3(0)
		elif actions[0:8] == "set user":
			defaultuser = actions[9:]
			d.change("user",defaultuser)
			cpop3(0)
		elif actions[0:8] == "set pass":
			defaultpass = actions[9:]
			d.change("pass",defaultpass)
			cpop3(0)
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
										cmd = raw_input(colors[1]+" CLT~"+colors[3]+"pop3/> "+colors[0])
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
					d.nomatch()
			except:
				d.off()
		else:
			d.nocommand()
	except:
		d.kbi()
		exit()
	cpop3(0)