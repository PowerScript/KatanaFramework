# This module requires katana framework 
# https://github.com/RedToor/Katana
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                 #
from core.design import *     #
from core.Setting import *    #
from core import Errors       #
from core import getFunction  #
import sys                    #
Message=DESIGN()              #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                   #
from xml.dom import minidom   #
import xml.etree.ElementTree as ET
import commands               #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="RedToor"
	initialize.Version            ="2.0"
	initialize.Despcription       ="Ports, OS, Etc Scan to host."
	initialize.CodeName           ="net/sc.scan"
	initialize.DateCreation       ="28/11/2015"      
	initialize.LastModification   ="25/03/2016"

	# DEFAULT VARIABLES             VALUE                            NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[[getFunction.Myip()           , "target"  , "yes" , "Target or DNS"]]      #[0][0]
	initialize.DEFAULT_VARIABLE  +=[["profile-0"                  , "type "   , "no"  , "Profile scan"]]       #[1][0]
initialize()
# END INFORMATION MODULE

# MAIN FUNCTION
def main(run):
	try:
		# HEAD MODULE
		if run:	actions=raw_input(Message.prompt(initialize.CodeName))
		else  : actions="run"
		if getFunction.KatanaCheckActionShowOptions(actions):
			getFunction.ShowOptions(initialize.DEFAULT_VARIABLE)
			Message.helpAUX()
			print " "+colors[7]+"Type         Description                      Speed"+colors[0]
			print " [profile-0] Intense scan                       slow"	
			print " [profile-1] Intense scan plus UDP              slow"
			print " [profile-2] Intense scan, all TCP ports        very slow"	
			print " [profile-3] Intense scan, no ping              slow"
			print " [profile-4] Ping scan                          fast"	
			print " [profile-5] Quick scan                         fast"
			print " [profile-6] Quick scan plus                    fast"                        	
			print " [profile-7] Quick traceroute                   fast"
			print " [profile-8] Regular scan                       slow"	
			print " [profile-9] Slow comprehensive scan            fast"
			Message.space()
		elif getFunction.KatanaCheckActionSetValue(actions)   :initialize.DEFAULT_VARIABLE=getFunction.UpdateValue(actions,initialize.DEFAULT_VARIABLE)
		elif getFunction.KatanaCheckActionisBack(actions)     :return
		# END HEAD MODULE
		elif getFunction.runModule(actions):
			Message.run()
			# CODE MODULE    ############################################################################################
			try:
				if getFunction.isConect():
					parameter="-T4 -A -v"
					if initialize.DEFAULT_VARIABLE[1][0]  =="profile-0":
						parameter="-T4 -A -v"
					elif initialize.DEFAULT_VARIABLE[1][0]=="profile-1":
						parameter="-sS -sU -T4 -A -v"
					elif initialize.DEFAULT_VARIABLE[1][0]=="profile-2":
						parameter="-p 1-65535 -T4 -A -v"
					elif initialize.DEFAULT_VARIABLE[1][0]=="profile-3":
						parameter="-T4 -A -v -Pn"
					elif initialize.DEFAULT_VARIABLE[1][0]=="profile-4":
						parameter="-sn"
					elif initialize.DEFAULT_VARIABLE[1][0]=="profile-5":
						parameter="-T4 -F"
					elif initialize.DEFAULT_VARIABLE[1][0]=="profile-6":
						parameter="-sV -T4 -O -F --version-light"
					elif initialize.DEFAULT_VARIABLE[1][0]=="profile-7":
						parameter="-sn --traceroute"
					elif initialize.DEFAULT_VARIABLE[1][0]=="profile-8":
						parameter=""
					elif initialize.DEFAULT_VARIABLE[1][0]=="profile-9":
						parameter="-sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script 'default or (discovery and safe)'"
					else:
						print " "+Bad+" Type not allow, use show options or sop and see Auxiliar help."
						initialize.DEFAULT_VARIABLE[1][0]="profile-0"
						main(True)
					print " "+Alr+" Scanning Target: "+initialize.DEFAULT_VARIABLE[0][0]+" wait it may take a few minutes."
					OSMATCHs=[]
					SERVICEs=[]
					INFORMEs=[]
					MAC="Unknow"
					VENDOR="Unknow"
					Message.space()
					commands.getoutput(NMAP_PATH+" "+parameter+" "+initialize.DEFAULT_VARIABLE[0][0]+" -oX tmp/portScanner-tmp.xml > null")
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
					print " Ip address: "+initialize.DEFAULT_VARIABLE[0][0]
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
					Message.space()
				else:
					Message.Noconnect()
			except:
				Errors.Errors(event=sys.exc_info(), info=False)
			# END CODE MODULE ############################################################################################
		else:
			getFunction.KatanaCheckActionGlobalCommands(actions)
	# ERROR GENERAL
	except:
		Errors.Errors(event=sys.exc_info(), info=sys.exc_traceback.tb_lineno)
	# END ERROR GENERAL
	main(True)
# END MAIN FUNCTION

# LINKER FUNCTION
def run(target,profile):
	initialize.DEFAULT_VARIABLE [0][0] = target
	initialize.DEFAULT_VARIABLE [1][0] = profile
	main(False)
# END LINKER FUNCTION
