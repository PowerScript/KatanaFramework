# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from bs4 import BeautifulSoup
import httplib,re        
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.0"
	init.Description        ="Subdomain Brute Force"
	init.CodeName           ="web/sub.dns"
	init.DateCreation       ="25/04/2017"      
	init.LastModification   ="25/04/2017"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE                RQ     DESCRIPTION
		'target':[LOCAL_IP           ,True , 'Host Target'],
		'port'  :[HTTP_PORT          ,False, 'Port Target'],
		'file'  :[TABLE_SUBDOMAIN    ,False, 'Subdomain List']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	NET.CheckConnectionHost(init.var['target'],init.var['port'],5)
	Loadingfile(init.var['file'])
	Totalresults=""

	printk.step("[1] Step : Starting Brute Force...")
	with open(init.var['file'],'r') as list_path:
		for path in list_path:
			path=path.replace("\n","")
			if init.var['port'] == "443" : 
				connection = httplib.HTTPSConnection(path+"."+init.var['target'])
			else : connection = httplib.HTTPConnection(path+"."+init.var['target'],int(init.var['port']))
			connection.addheaders=[('User-agent', WEB.RamdonAgent())]
			connection.request("GET","/")
			response = connection.getresponse()

			if response.status == 200 or response.status == 301:
				printk.suff(" | Response "+path+"."+init.var['target'])
				Totalresults+="\t  |"+path+"."+init.var['target']+"\n"
			else:printk.inf(" | Checking `"+colors[0]+path+"` Response:"+str(response.status))
			connection.close()
	printk.step("[2] Step : Starting Google Dorking...")
	connection = httplib.HTTPSConnection("www.google.com")
	connection.request("GET", "/search?q=inurl:."+str(init.var['target']))
	connection.addheaders=[('User-agent', WEB.RamdonAgent())]
	response = connection.getresponse()

	if response.status == 302:
		html_response = response.read()
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html_response)
		host_name = re.findall('(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}',urls[0])
		connection = httplib.HTTPSConnection(host_name[0])
		connection.request("GET", "/search?q=inurl:admin+site:"+str(init.var['target']))
		connection.addheaders=[('User-agent', WEB.RamdonAgent())]
		response = connection.getresponse()

	if response.status == 200:
		soup = BeautifulSoup(response.read(), "lxml")
		divList = soup.findAll('cite')
		for ids in divList:
			printk.suff(" | Result  "+ids.text)
			Totalresults+="\t  | "+ids.text+"\n"

	UTIL.sRegister(init,Totalresults)

# END CODE MODULE ############################################################################################
