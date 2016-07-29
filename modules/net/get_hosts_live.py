# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from core.Function import get_gateway,get_local_ip,KTFVAR
from xml.dom import minidom
import xml.etree.ElementTree as ET
import commands
import re
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="2.1"
	init.Description        ="Host's live scanner in LAN"
	init.CodeName           ="net/sc.hosts"
	init.DateCreation       ="22/08/2015"      
	init.LastModification   ="16/05/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE     RQ     DESCRIPTION
		'range':[get_local_ip()+"/24" ,True ,'Range Scan'],
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	commands.getoutput(NMAP_PATH+' -sn '+str(init.var['range'])+' -oX tmp/KTFVAR.xml > null')
	GateWay=get_gateway()
	tree = ET.parse('tmp/KTFVAR.xml')
	root = tree.getroot()
	IPf=0
	counter=0
	for host in root.findall('host'):
		for hosted in host.findall('address'):
			if hosted.get('addrtype') == "ipv4":
				IPf=hosted.get('addr')
			else:
				if GateWay == IPf :
					IPf=colors[8]+colors[4]+"{GW:"+IPf+"}"+colors[0]
				KTFVAR.append(" "+IPf+"\t"+str(hosted.get('addr'))+"\t"+str(hosted.get('vendor')))
	Space()
	print " "+colors[10]+colors[7]+" # \t IP \t\t     MAC    \t\t      VENDOR          "+colors[0]
	for HOST in KTFVAR:
		counter+=1				
		print " ["+str(counter)+"]"+HOST
	Space()
	commands.getoutput('rm tmp/KTFVAR.xml > null')

# END CODE MODULE ############################################################################################
