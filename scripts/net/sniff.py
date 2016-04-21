# This module requires katana framework 
# https://github.com/RedToor/Katana
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                 #
from core.design import *     #
from core.Setting import *    #
from core import Errors       #
from core import getFunction  #
import sys                    #
Messages=DESIGN()             #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                   #
from scapy.all import *       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="RedToor"
	initialize.Version            ="1.0"
	initialize.Despcription       ="Network Sniffer"
	initialize.CodeName           ="net/sc.sniff"
	initialize.DateCreation       ="22/03/2015"      
	initialize.LastModification   ="27/03/2016"

	# DEFAULT VARIABLES             VALUE                       NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[["eth0"                   , "inter"  , "yes" , "Device to sniff"]] #[0][0]
	initialize.DEFAULT_VARIABLE  +=[["ALL"                    , "filter" , "no"  , "filter sniff"]]    #[1][0]
initialize()
# END INFORMATION MODULE

# MAIN FUNCTION
def main(run):
	try:
		# HEAD MODULE
		if run:	actions=raw_input(Messages.prompt(initialize.CodeName))
		else  : actions="run"
		if   getFunction.KatanaCheckActionShowOptions(actions):
			getFunction.ShowOptions(initialize.DEFAULT_VARIABLE)
			Messages.helpAUX()
			print " Current Interfaces : ", getFunction.get_interfaces()
			Messages.space()
			print " "+colors[7]+"Type         Description"+colors[0]
			print " [ALL]        Whatever"	 
			print " [DNS]        Domains Name Service"	
			print " [FTP]        File Transfer Protocol"
			print " [POP]        Post Office Protocol"
			Messages.space()
		elif getFunction.KatanaCheckActionSetValue(actions)   :initialize.DEFAULT_VARIABLE=getFunction.UpdateValue(actions,initialize.DEFAULT_VARIABLE)
		elif getFunction.KatanaCheckActionisBack(actions)     :return
		# END HEAD MODULE
		elif getFunction.runModule(actions):
			Messages.run()
			# CODE MODULE    ############################################################################################
			if  initialize.DEFAULT_VARIABLE[1][0] == "DNS" : FILTER = "udp or port 53"
			if initialize.DEFAULT_VARIABLE[1][0]  == "FTP" : FILTER = "port 21"
			if initialize.DEFAULT_VARIABLE[1][0]  == "ALL" : FILTER = "udp or tcp"
			if initialize.DEFAULT_VARIABLE[1][0]  == "POP" : FILTER = "port 110"
			if getFunction.checkDevice(initialize.DEFAULT_VARIABLE[0][0]):
				print " "+colors[10]+" #\t"+colors[4]+"PROTOCOL\tSOURCE\t\tDESTINE\t\tDATA          "+colors[0]
				while True:
    					sniff(filter=FILTER, prn=callback, store=0, iface=initialize.DEFAULT_VARIABLE[0][0])
			else:
				Messages.NoDeviceFound(initialize.DEFAULT_VARIABLE[0][0])
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
def run(device, filters):
	initialize.DEFAULT_VARIABLE [0][0] = device
	initialize.DEFAULT_VARIABLE [1][0] = filters
	main(False)
# END LINKER FUNCTION

def callback(pkt):
	try:
		if pkt.dport == 53:
			return " "+colors[13]+str(pkt[IP].id)+"\t"+str(pkt[IP].proto)+"\t\t"+str(pkt[IP].src)+"\t"+pkt[DNS].qd.qname+colors[0]
		if pkt.dport == 21:
			return " "+colors[12]+str(pkt[IP].id)+"\t"+str(pkt[IP].proto)+"\t\t"+str(pkt[IP].src)+"\t"+str(pkt[IP].dst)+"\t"+pkt[Raw].load.replace("\n", ".")+colors[0]
		if pkt.dport == 3306:
			return " "+colors[11]+str(pkt[IP].id)+"\t"+str(pkt[IP].proto)+"\t\t"+str(pkt[IP].src)+"\t"+colors[0]
		else:
			return " "+colors[9]+str(pkt[IP].id)+"\t"+str(pkt[IP].proto)+"\t\t"+str(pkt[IP].src)+"\t"+colors[0]
	except:
		f=1

