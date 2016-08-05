# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES 
from core.Function import get_interfaces,checkDevice,get_monitors_mode
from scapy.all import *       
# END LIBRARIES 

# END LIBRARIES 
def init():
	init.Author             ="RedToor"
	init.Version            ="1.0"
	init.Description        ="Network Sniffer"
	init.CodeName           ="net/sc.sniff"
	init.DateCreation       ="22/03/2016"      
	init.LastModification   ="18/05/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME       VALUE               RQ     DESCRIPTION
		'interface' :[INTERFACE_ETHERNET,True ,'Monitor Interface'],
		'filter'    :["ALL"             ,False,'Filter sniff']
	}
	
	init.aux = """
 (filter) options
 -> [ALL] Whatever
 -> [DNS] Domains Name Service
 -> [FTP] File Transfer Protocol
 -> [POP] Post Office Protocol

 Devices Founds: """+str(get_interfaces())+"""
 Monitors Inter: """+str(get_monitors_mode())+"""
 Functions     : For Start Monitor Mode, type 'f::start_monitor(Interface)' 
"""
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	if  init.var['filter'] == "DNS" : FILTER = "udp or port 53"
	elif init.var['filter']  == "FTP" : FILTER = "port 21"
	elif init.var['filter']  == "ALL" : FILTER = "udp or tcp"
	elif init.var['filter']  == "POP" : FILTER = "port 110"
	else:
		printAlert(1,"Type not allow, use show options or sop and see Auxiliar help.")
		FILTER = "udp or tcp"
		return
	
	if checkDevice(init.var['interface']):
		print " "+colors[10]+" #\t"+colors[4]+"PROTOCOL    SOURCE\t\tDESTINE\t\tDATA          "+colors[0]
		while True:sniff(filter=FILTER, prn=callback, store=0, iface=init.var['interface'])

# END CODE MODULE ############################################################################################

def callback(pkt):
	try:
		if pkt.dport == 53 and pkt[DNS].opcode == 0L and pkt[IP].proto == 17:return " "+str(pkt[IP].id)+"\t"+colors[13]+"  DNS   "+colors[0]+" "+str(pkt[IP].src)+"->\t\t"+pkt[DNS].qd.qname+colors[0]
		if pkt.dport == 21:return " "+str(pkt[IP].id)+"\t"+colors[12]+"  FTP   "+colors[0]+" "+str(pkt[IP].src)+"->\t\t"+str(pkt[IP].dst)+"\t"+pkt[Raw].load.replace("\n", ".")+colors[0]
		if pkt.dport == 110:return " "+str(pkt[IP].id)+"\t"+colors[11]+"  POP   "+colors[0]+" "+str(pkt[IP].src)+"->\t\t"+colors[0]
		if init.var['filter'] == "ALL":return " "+colors[9]+str(pkt[IP].id)+"\t"+"  Other "+" "+str(pkt[IP].src)+"->\t\t"+colors[0]
	except:n=None
