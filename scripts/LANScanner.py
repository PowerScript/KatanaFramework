# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                       #
# Modules   : Host live LAN     #
# Script by : RedToor           #
# Date      : 22/08/2015        #
# Version   : 2.0               #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                   #
from core.design import *       #
from core.Setting import *      #
from core import Errors         #
from core import help           #
from core import ping           #
import sys                      #
d=DESIGN()                      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                     #
from xml.dom import minidom
import xml.etree.ElementTree as ET
import commands         
import re
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
defaultnet=MY_IP
defaulttyp="fast"
IPs=[]
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

def run(nets, types):
	global defaultnet,defaulttyp
	defaultnet=nets
	defaulttyp=types
	hostl(1)


def hostl(run):
	global defaultnet,defaulttyp
	try:
		if run!=1:
			actions=raw_input(d.prompt("net/lanlive"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("nets","yes","Local area net",defaultnet)
			#d.descrip("type","no","type scan",defaulttyp)
			d.helpAUX()
			if ping.conneted()!=False:
				print " You IP     : ",ping.myip()
			else:
				print d.noconnect()
			#print " Type       :  {fast}{intense}"
			d.space()
			hostl(0)
		elif actions[0:8] == "set nets":
			defaultnet=ping.update(defaultnet,actions,"nets")
			d.change("nets",defaultnet)
		elif actions[0:8] == "set type":
			defaulttyp=ping.update(defaulttyp,actions,"type")
			d.change("type",defaulttyp)
		elif actions=="exit" or actions=="x":
			d.goodbye()
			exit()
		elif actions=="help" or actions=="h":
			help.help()
		elif actions=="back" or actions=="b":
			return
		elif actions[0:5]=="save:":
			ping.SaveVariable(secuence=actions, matrix=IPs)
		elif actions=="run"  or actions=="r":
			d.run()
			try:
				d.space()
				commands.getoutput(NMAP_PATH+' -sn '+str(defaultnet)+'/24 -oX tmp/ips.xml > null')
				GateWay=ping.get_gateway(2)
				tree = ET.parse('tmp/ips.xml')
				root = tree.getroot()
				IPf=0
				counter=0
				IP=""
				for host in root.findall('host'):
					for hosted in host.findall('address'):
						if hosted.get('addrtype') == "ipv4":
							IPf=hosted.get('addr')
						else:
							if GateWay == IPf :
								IPf=colors[8]+colors[4]+"{GW:"+IPf+"}"+colors[0]
							IPs.append(" "+IPf+" "+str(hosted.get('addr'))+" "+str(hosted.get('vendor')))
				print " "+colors[10]+colors[7]+" # \t IP \t\t MAC \t\t VENDOR         "+colors[0]

				for HOST in IPs:
					counter=counter+1				
					print " ["+str(counter)+"]"+HOST
				d.space()
				commands.getoutput('rm tmp/ips.xml > null')
			except:
				Errors.Errors(event=sys.exc_info(), info=False)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info(), info=False)
	hostl(0)
