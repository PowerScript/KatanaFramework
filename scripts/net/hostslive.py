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
import re                     #
IPs=[]                        #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="RedToor"
	initialize.Version            ="2.0"
	initialize.Despcription       ="Host's live scanner in LAN"
	initialize.CodeName           ="net/cs.hosts"
	initialize.DateCreation       ="22/08/2015"      
	initialize.LastModification   ="24/03/2016"

	# DEFAULT VARIABLES             VALUE                       NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[[getFunction.Myip()+"/24", "range"  , "yes" , "Range Scan"]] #[0][0]
initialize()
# END INFORMATION MODULE

# MAIN FUNCTION
def main(run):
	try:
		# HEAD MODULE
		if run:	actions=raw_input(Message.prompt(initialize.CodeName))
		else  : actions="run"
		if   getFunction.KatanaCheckActionShowOptions(actions):getFunction.ShowOptions(initialize.DEFAULT_VARIABLE)
		elif getFunction.KatanaCheckActionSetValue(actions)   :initialize.DEFAULT_VARIABLE=getFunction.UpdateValue(actions,initialize.DEFAULT_VARIABLE)
		elif getFunction.KatanaCheckActionSaveValue(actions)  :getFunction.SaveValue(actions,IPs)
		elif getFunction.KatanaCheckActionisBack(actions)     :return
		# END HEAD MODULE
		elif getFunction.runModule(actions):
			Message.run()
			# CODE MODULE    ############################################################################################
			try:
				if getFunction.isConect():
					Message.space()
					commands.getoutput(NMAP_PATH+' -sn '+str(initialize.DEFAULT_VARIABLE[0][0])+' -oX tmp/ips.xml > null')
					GateWay=getFunction.get_gateway()
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
					Message.space()
					commands.getoutput('rm tmp/ips.xml > null')
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
def run(ranges):
	initialize.DEFAULT_VARIABLE [0][0] = ranges
	main(False)
# END LINKER FUNCTION