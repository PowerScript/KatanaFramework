# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from lib.pysock import socks
import urllib2,socket,urllib
# END LIBRARIES

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.0"
	init.Description        ="Proxy list checker."
	init.CodeName           ="mcs/px.checker"
	init.DateCreation       ="26/07/2015"      
	init.LastModification   ="23/12/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME      VALUE                    RQ     DESCRIPTION
		'file'     :["files/test/Proxys.txt",True ,'List Proxy List'],
		'separator':[":"                    ,True ,'Separator IP[:]PORT']
	}

	# EXTRA OPTIONS MODULE
	init.extra = {
		# NAME    VALUE   RQ    DESCRIPTION
		'timeout1':["4"  ,True,'Timeout HTTP'],
		'timeout2':["180",True,'Timeout SOCK']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):

	socket.setdefaulttimeout(int(init.var['timeout2']))
	socks.socket.setdefaulttimeout(7)
	Loadingfile(init.var['file'])
	ProxyList = [["IP","PORT","HTTP","SOCK4","SOCK5"]]
	
	with open(init.var['file'],'r') as proxys:
		for proxy in proxys:
			HTTP=False
			SOCK4=False
			SOCK5=False
			proxy=proxy.replace("\n","").split(init.var['separator'])
			printk.inf("Testing  IP:"+proxy[0]+" PORT:"+proxy[1])
			try:
				printk.inf(" |-> Checking HTTP tunnel.")
				proxy_handler = urllib2.ProxyHandler({'http': proxy[0]+init.var['separator']+proxy[1]})        
				opener = urllib2.build_opener(proxy_handler)
				opener.addheaders = [('User-agent', 'Mozilla/5.0')]
				urllib2.install_opener(opener)        
				req=urllib2.Request('http://www.google.com')
				sock=urllib2.urlopen(req,timeout = int(init.var['timeout1']))
				printk.suff(" |-> HTTP tunnel Working")
				HTTP=True
			except:printk.inf(" |-> HTTP tunnel Not Working")
			try:
				printk.inf(" |-> Checking SOCK4 tunnel.")
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, proxy[0],int(proxy[1]))
				socket.socket = socks.socksocket
				urllib.urlopen("http://www.google.com/")
				printk.suff(" |-> SOCK4 tunnel Working")
				SOCK4=True
			except:printk.inf(" |-> SOCK4 tunnel Not Working")
			try:
				printk.inf(" |-> Checking SOCK5 tunnel.")
				socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, proxy[0],int(proxy[1]))
				socket.socket = socks.socksocket
				urllib.urlopen("http://www.google.com/")
				printk.suff(" |-> SOCK5 tunnel Working")
				SOCK5=True
			except:printk.inf(" |-> SOCK5 tunnel Not Working")
			if HTTP == True or SOCK4 == True or SOCK5 == True:ProxyList+=[[proxy[0],proxy[1],str(HTTP),str(SOCK4),str(SOCK5)]]
	printk.inf("Proxys Lives.")
	GRAPHICAL.CreateTable(ProxyList)
	Space()

# END CODE MODULE ############################################################################################