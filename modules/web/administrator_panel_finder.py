# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from core.Function import isLive,RamdonAgent,saveRegister
from bs4 import BeautifulSoup
import httplib                
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="2.0"
	init.Description        ="Administrator Panel finder, Brute Force + Google Dork + Port Scan."
	init.CodeName           ="web/cp.finder"
	init.DateCreation       ="28/09/2015"      
	init.LastModification   ="14/05/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE     RQ     DESCRIPTION
		'target':[LOCAL_IP ,True ,'Host Target'],
		'port'  :[HTTP_PORT,False,'Port Target'],
		'file'  :[TABLE_FOLDER_ADMIN ,False,'Tables URL'],
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	isLive(init.var['target'],init.var['port'])
	Loadingfile(init.var['file'])
	Totalresults=""

	printAlert(5,"[1] Step : Starting Brute Force...")
	with open(init.var['file'],'r') as list_path:
		for path in list_path:
			path="/"+path.replace("\n","")
			connection = httplib.HTTPConnection(init.var['target'],init.var['port'])
			connection.addheaders=[('User-agent', RamdonAgent())]
			connection.request("GET",path)
			response = connection.getresponse()
			if response.status == 200 or response.status == 301:
				printAlert(3," | Response "+init.var['target']+path)
				Totalresults+="\t|"+init.var['target']+path+"\n"
			else:printAlert(0," | Checking `"+colors[0]+path+"` Response:"+str(response.status))
			
	printAlert(5,"[2] Step : Starting Google Dorking...")
	connection = httplib.HTTPConnection("www.google.com",80)
	connection.request("GET", "/search?q=inurl:admin+site:"+str(init.var['target']))
	connection.addheaders=[('User-agent', RamdonAgent())]
	response = connection.getresponse()
	soup = BeautifulSoup(response.read(), "lxml")
	divList = soup.findAll('cite')
	for ids in divList:
		printAlert(3,"| Result  "+ids.text)
		Totalresults+="\t | "+ids.text+"\n"

	printAlert(5,"[3] Step : Scanning Port commons...")
	commonports = [2082,2083,2095,2096]
	for port in commonports:
		printAlert(0," | Testing Port "+str(port))
		if isLive(init.var['target'],port):
			printAlert(3," | "+str(port)+" Port Open!")
			Totalresults+="\t|"+str(port)+" Open! \n"

	printAlert(0,"[*] Total Result")
	print Totalresults
	saveRegister(init,Totalresults)

# END CODE MODULE ############################################################################################