# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from xml.dom import minidom
import xml.etree.ElementTree as ET
import re
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="3.0"
	init.Description        ="Host's live scanner in LAN"
	init.CodeName           ="net/sc.hosts"
	init.DateCreation       ="22/08/2015"      
	init.LastModification   ="12/25/2016"
	init.Collaborators      =None
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE           RQ     DESCRIPTION
		'range':[LOCAL_IP+"/24" ,True ,'Range Scan']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	printk.wait("Scanning range of Targets: "+str(init.var['range'])+" wait it may take a few minutes.")
	SYSTEM.Command_exe("Scanning with Nmap                                ","nmap -sn "+str(init.var['range'])+" -oX tmp/resultnmap.xml", std=False)
	GateWay_d=NET.GetGateway()
	MY_IP    =NET.GetLocalIp()
	C  = 0
	IP = ""
	MAC= ""
	VENDOR=""
	for host in ET.parse('tmp/resultnmap.xml').getroot().findall('host'):
		for hosted in host.findall('address'):
			if hosted.get('addrtype') == "ipv4":
				IP = hosted.get('addr')
			
				if GateWay_d == IP :IP=colors[4]+"{G:"+IP+"}"+colors[0]
				if MY_IP == IP     :IP=colors[3]+"{I:"+IP+"}"+colors[0]	

				C += 1

			if hosted.get('addrtype') == "mac":
				MAC = hosted.get('addr')
				VENDOR = hosted.get('vendor')

		print "  | #" + str(C) + " --> IP: " + IP + " \t< MAC: " + str(MAC) + " " + str(VENDOR)
		G_KTFVAR.append(str(IP)+":"+str(MAC))
	SYSTEM.Command_exe("Clearning Temp files                              ","rm tmp/resultnmap.xml", std=False)

# END CODE MODULE ############################################################################################
