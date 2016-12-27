# This module requires katana framework 
# https://github.com/RedToor/Katana

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES 
from email import parser                 
import poplib
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.1"
	init.Description        ="Console Client for POP3 Protocol."
	init.CodeName           ="clt/cl.pop"
	init.DateCreation       ="22/05/2015"      
	init.LastModification   ="25/12/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE                RQ     DESCRIPTION
		'target':["pop.gmail.com"     ,True ,'Host Target'],
		'port'  :[POP_PORT            ,False,'Port Target'],
		'user'  :["my_em@hotmail.com" ,True ,'Username'],
		'pass'  :["password"          ,True ,'Password']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):

	con=poplib.POP3_SSL("pop.gmail.com")
	con.user(init.var['user'])
	con.pass_(init.var['pass'])
	cmd="nop"

	printk.inf("POP3 Console")
	HelpBanner  = [["Commands","Description","Example"]]
	HelpBanner += [["list","list mails","list"]]
	HelpBanner += [["read","show mail","retr 2"]]
	HelpBanner += [["dele","remove mail","dele 2"]]
	GRAPHICAL.CreateTable(HelpBanner)

	while(cmd!="exit"):
		cmd = raw_input(ClientPrompt(init.CodeName,"pop"))
		if cmd == "list":
			messages = [con.retr(i) for i in range(1, len(con.list()[1]) + 1)]
			messages = ["\n".join(mssg[1]) for mssg in messages]
			messages = [parser.Parser().parsestr(mssg) for mssg in messages]
			for message in messages:
			    print message['subject']
		elif cmd[0:4] == "read":
			for j in con.retr(int(cmd[5:])+1)[1]:
				print j
		elif cmd[0:4] == "dele":
			con.dele(int(cmd[5:])+1)[1]
			printk.inf("email marked for delete ('quit' for exit and delete all email marked)")
		elif cmd == "help":GRAPHICAL.CreateTable(HelpBanner)
		elif cmd == "quit":
			con.quit()
			break

# END CODE MODULE ############################################################################################
