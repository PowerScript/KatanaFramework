# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                       #
# Modules   : Port Scanner      #
# Script by : RedToor           #
# Date      : 28/11/2015        #
# Version   : 1.1               #
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
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
defaultnet="192.168.1.215"
defaulttyp="p-0"
parameter="-T4 -A -v"
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

def run(target, types):
	global defaultnet,defaulttyp
	defaultnet=target
	defaulttyp=types
	PortScanner(1)


def PortScanner(run):
	global defaultnet,defaulttyp,parameter
	try:
		if run!=1:
			actions=raw_input(d.prompt("net/portscan"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("target","yes","IP or DNS",defaultnet)
			d.descrip("type","no","Type of scan",defaulttyp)
			d.space()
			d.helpAUX()
			print " "+colors[7]+"Type  Description                       Speed"+colors[0]
			print " [p-0] Intense scan                       slow"	
			print " [p-1] Intense scan plus UDP              slow"
			print " [p-2] Intense scan, all TCP ports        very slow"	
			print " [p-3] Intense scan, no ping              slow"
			print " [p-4] Ping scan                          fast"	
			print " [p-5] Quick scan                         fast"
			print " [p-6] Quick scan plus                    fast"                        	
			print " [p-7] Quick traceroute                   fast"
			print " [p-8] Regular scan                       slow"	
			print " [p-9] Slow comprehensive scan            fast"
			d.space()
			PortScanner(0)
		elif actions[0:10] == "set target":
			defaultnet=ping.update(defaultnet,actions,"target")
			d.change("target",defaultnet)
		elif actions[0:8] == "set type":
			defaulttyp=ping.update(defaultnet,actions,"type")
			if defaulttyp=="p-0":
				parameter="-T4 -A -v"
			elif defaulttyp=="p-1":
				parameter="-sS -sU -T4 -A -v"
			elif defaulttyp=="p-2":
				parameter="-p 1-65535 -T4 -A -v"
			elif defaulttyp=="p-3":
				parameter="-T4 -A -v -Pn"
			elif defaulttyp=="p-4":
				parameter="-sn"
			elif defaulttyp=="p-5":
				parameter="-T4 -F"
			elif defaulttyp=="p-6":
				parameter="-sV -T4 -O -F --version-light"
			elif defaulttyp=="p-7":
				parameter="-sn --traceroute"
			elif defaulttyp=="p-8":
				parameter=""
			elif defaulttyp=="p-9":
				parameter="-sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script 'default or (discovery and safe)'"
			else:
				defaulttyp="p-0"
 				print " "+Bad+" Type not allow, use show options or sop and see Auxiliar help."
				PortScanner(0)
			defaulttyp=ping.update(defaulttyp,actions,"type")
			d.change("type",defaulttyp)
		elif actions=="exit" or actions=="x":
			d.goodbye()
			exit()
		elif actions=="help" or actions=="h":
			help.help()
		elif actions=="back" or actions=="b":
			return
		elif actions=="run"  or actions=="r":
			d.run()
			try:
				print " "+Alr+" Scanning Target: "+defaultnet+" wait it may take a few minutes."
				OSMATCHs=[]
				SERVICEs=[]
				INFORMEs=[]
				MAC="Unknow"
				VENDOR="Unknow"
				d.space()
				commands.getoutput(NMAP_PATH+" "+parameter+" "+defaultnet+" -oX tmp/portScanner-tmp.xml > null")
				tree = ET.parse('tmp/portScanner-tmp.xml')
				root = tree.getroot()
				for host in root.findall('host'):
					for address in host.findall('address'):
						p=address.get('addr')
						if not address.get('vendor'):
							VENDOR=VENDOR 
						else:
							VENDOR=address.get('vendor')
						if p.find(":") <= 0 :
							IP=address.get('addr')
						else: 
							MAC=address.get('addr')

					for ports in host.findall('ports'):
						for port in ports.findall('port'):
							PROTOCOL=port.get('protocol')
							PORT=port.get('portid')
							for service in port.findall('service'):
								if not service.get('product'):
									product="{NULL}"
									version="{NULL}"
									info="{NULL}"	
								else:
									product=service.get('product')
									version=service.get('version')
									info=service.get('extrainfo')
								product=str("{NULL}" if product is None else product)
								version=str("{NULL}" if version is None else version)
								info=str("{NULL}" if info is None else info)
								SERVICEs.append(colors[7]+service.get('name')+colors[0]+" ["+product+"] "+version+info+" "+colors[10]+colors[3]+PROTOCOL+"-Port: "+PORT+colors[0])

					for hostscript in host.findall('hostscript'):
						for script in hostscript.findall('script'):
							if script.get('id') == 'smb-os-discovery':
								INFORMEs.append(script.get('output'))

					for os in host.findall('os'):
						for osmatch in os.findall('osmatch'):
							OSMATCHs.append(osmatch.get('name'))


				print " Ip address: "+defaultnet
				print " Mac       : "+MAC
				print " Vendor    : "+VENDOR
				print " OS Matchs : "
				for os in OSMATCHs:
					print "             "+os
				print " Services  : " 				
				for services in SERVICEs:
					print "             "+str(services) 
				print " Report    :"
				for informer in INFORMEs:
					informer=str("{NULL}" if informer is "" else informer)
					print str(informer) 
				commands.getoutput('rm tmp/portScanner-tmp.xml > null')
				d.space()
			except:
				Errors.Errors(event=sys.exc_info(), info=sys.exc_traceback.tb_lineno)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info(), info=False)
	PortScanner(0)

