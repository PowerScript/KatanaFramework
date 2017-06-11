# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from bs4 import BeautifulSoup
import httplib,re,socket
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.0"
	init.Description        ="Subdomain Brute Force"
	init.CodeName           ="web/sub.dns"
	init.DateCreation       ="25/04/2017"      
	init.LastModification   ="10/05/2017"
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
	Totalresults = []

	printk.step("[1] Step : Starting Brute Force...")
	with open(init.var['file'],'r') as list_path:
		for path in list_path:
			path=path.replace("\n","")
			try:
				IP = socket.gethostbyname(path+"."+init.var['target'])
				printk.suff(" | Response "+path+"."+init.var['target']+" IP["+IP+"]")
				Totalresults.append({'DNS':path+"."+init.var['target'],'IP':IP})
			except:
				printk.inf(" | Checking `"+colors[0]+path+"."+init.var['target']+"`")

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
		connection.request("GET", "/search?q=site:"+str(init.var['target']))
		connection.addheaders=[('User-agent', WEB.RamdonAgent())]
		response = connection.getresponse()

	if response.status == 200:
		soup = BeautifulSoup(response.read(), "lxml")
		divList = soup.findAll('cite')
		for ids in divList:
			host_name = re.findall('(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}',ids.text)
			printk.suff(" | Found  "+host_name[0])
			IP = socket.gethostbyname(host_name[0])
			Totalresults.append({'DNS':str(host_name[0]),'IP':str(IP)})	

	printk.step("[*] Results")
	for item in Totalresults:
		print "\t  | + "+item['DNS']+"\t\tIP["+item['IP']+"]"
	print "\t,--"

# END CODE MODULE ############################################################################################
