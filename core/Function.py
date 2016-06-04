#!/usr/bin/env python
#HEAD#########################################################
#
# Katana Framework | Function                           
# Main library
#
# 
# Last Modified: 01/06/2016
#
#########################################################HEAD#

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from GeneralCommands import *
from Default import *
from Design import *
from Update import update
import xml.etree.ElementTree as ET
from xml.dom import minidom
from scapy.all import *
from Information import version,build,date
import fcntl        ,struct   ,readline,rlcompleter,subprocess
import threading    ,StringIO ,httplib ,commands   ,random ,re
import logging      ,urllib   ,Help    ,socket     ,time   ,sys, readline


ap_list = []
VARIABLESIP=[]
VARIABLESMAC=[]
AGENT_ARRAY=[]
File_Agent_Open=False
NUMBER_AGENTS=0
Desing=DESIGN()
KTFVAR=[]

### GENERAL ###
def KatanaCheckActionShowModules(action):
	if action == SHOW_MODULES or action == SHOW_MODULES_SHORT: return True

### UPDATE VARIABLES MODULE
def UpdateValue(action,matriz):
	for Namevalue in matriz.options:
		if action[len(SETET)+1:len(SETET)+1+len(Namevalue)] == Namevalue:
			checkValue=action[len(SETET)+2+len(Namevalue):]
			if checkValue[0:4] == "::IP" : checkValue = VARIABLESIP[int(checkValue[4:])-1]
			if checkValue[0:5] == "::MAC": checkValue = VARIABLESMAC[int(checkValue[5:])-1]
			ChangeValue(Namevalue,checkValue)
			matriz.options[Namevalue] = [checkValue,matriz.options[Namevalue][1],matriz.options[Namevalue][2]]
			return matriz
	try:
		for Namevalue in matriz.extra:
			if action[len(SETET)+1:len(SETET)+1+len(Namevalue)] == Namevalue:
				checkValue=action[len(SETET)+2+len(Namevalue):]
				if checkValue[0:4] == "::IP" : checkValue = VARIABLESIP[int(checkValue[4:])-1]
				if checkValue[0:5] == "::MAC": checkValue = VARIABLESMAC[int(checkValue[5:])-1]
				ChangeValue(Namevalue,checkValue)
				matriz.extra[Namevalue] = [checkValue,matriz.extra[Namevalue][1],matriz.extra[Namevalue][2]]
				return matriz
	except:Nothing=False
	NoExistsparameter()
	return matriz

def KatanaCheckActionSetValue(action):
	if action[:len(SETET)]==SETET            : return True
def KatanaCheckActionUseModule(action):
	if action[:len(SELECT)]==SELECT          : return True
def KatanaCheckActionGetInfo(action):
	if action[:len(GETINFO)]==GETINFO        : return True
def KatanaCheckActionShowOptions(action):
	if action == SHOW or action == SHOW_SHORT: return True
def KatanaCheckActionShowMOptions(action):
	if action == SHOW_MORE or action == SHOWM_SHORT: return True
def KatanaCheckActionExefunction(action):
	if action[:len("f::")] == "f::"          : return True
def KatanaCheckActionSaveValue(action):
	if action[:4] == SAVEV                   : return True
def KatanaCheckActionisBack(action):
	if action==BACKING                       : return True
def runModule(action):
	if action=="run"                         : 
		RunModule()
		return True

### SHOW INFORMATION MODULE ###
def ShowInformationModule(init):
	print "\n |->Author  : "+str(init.Author)            
	print " |->Version : "+str(init.Version)           
	print " |->Description : "+str(init.Description)       
	print " |->CodeName : "+str(init.CodeName)          
	print " |->DateCreation : "+str(init.DateCreation)        
	print " |->LastModification : "+str(init.LastModification)
	print " |->References : "+str(init.References)         
	print " |->License : "+str(init.License)+"\n"

### GLOBAL COMMANDS ###
def KatanaCheckActionGlobalCommands(action):
	if     action[:len(EXIT)]        == EXIT   or action[:len(EXIT)]        == EXIT_SHORT  : exit()
	elif   action[:len(HELP)]        == HELP   or action[:len(HELP_SHORT)]  == HELP_SHORT  : Help.help()
	elif   action[:len("version")]   == "version"        :printAlert(3,"V:["+version+"] B:["+build+"] D:["+date+"]")
	elif   action[:len(UPDATE)]      == UPDATE or action[:len(UPDATE_SHORT)]== UPDATE_SHORT: update("functions")
	elif action[:len(EXECUTECOMMAND)]==EXECUTECOMMAND    :subprocess.call(action[len(EXECUTECOMMAND):], shell=True)
	elif   action[:len(CLEAR)]       == CLEAR  or action[:len(CLEAR_SHORT)] == CLEAR_SHORT : subprocess.call('clear', shell=True)
	elif   action[:len(SAVEV)]       == SAVEV            :SaveValue(action)
	elif   action                    == ""               :return
	else                                                 :CommandNotFound()

### EXECUTE FUNCTION ###
def Executefunction(query):
	try:

		if query[len("f::"):len("get_aps")+len("f::")] == "get_aps": 
			query = query[len("f::")+len("get_aps"):].replace("(","").replace(")","").split(",")
			get_aps(str(query[0]),int(query[1]))

		elif query[len("f::"):len("start_monitor")+len("f::")]== "start_monitor":
			query = query[len("f::")+len("start_monitor"):].replace("(","").replace(")","").split(",")
		    
			if start_monitor(query[0]):printAlert(3,query[0]+" now is in monitor mode.")
			else:NoDeviceFound(query[0]) 

		elif query[len("f::"):len("get_interfaces")+len("f::")]    == "get_interfaces":    print " ",get_interfaces()
		elif query[len("f::"):len("get_monitors_mode")+len("f::")] == "get_monitors_mode": print " ",get_monitors_mode()
		elif query[len("f::"):len("get_local_ip")+len("f::")]      == "get_local_ip":      print " ",get_local_ip()
		elif query[len("f::"):len("get_external_ip")+len("f::")]   == "get_external_ip":   print " ",get_external_ip()
		elif query[len("f::"):len("get_gateway")+len("f::")]       == "get_gateway":       print " ",get_gateway()

		else:functionNotFound()                                                                                 
	except:printAlert(6,"Check Again your Functions command.")

### SHOW OPTIONS ###
def ShowOptions(Options):
	Desing.option()
	for VAR in Options.options:
	 	Desing.description(str(VAR),Options.options[VAR][1],str(Options.options[VAR][2]),str(Options.options[VAR][0]))
	Space()
	try:
		if Options.aux:
			helpAUX()
			print Options.aux
	except:b=0

### SHOW FULL OPTIONS ###
def ShowFullOptions(Options):
	Desing.option()
	for VAR in Options.options:
	 	Desing.description(str(VAR),Options.options[VAR][1],str(Options.options[VAR][2]),str(Options.options[VAR][0]))
	Space()

	try:
		for VAR in Options.extra:
		 	Desing.description(str(VAR),Options.extra[VAR][1],str(Options.extra[VAR][2]),str(Options.extra[VAR][0]))
		Space()
	except:b=0
		
	try:
		if Options.aux:
			helpAUX()
			print Options.aux
	except:b=0

### VARIABLES TEMP ###
def SaveValue(secuence):
	try:
		if secuence[len(SAVEV):len(SAVEV)+2]=="ip":
			nID  = int(secuence[len(SAVEV)+3:])-1
		 	grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', KTFVAR[nID])
		 	address = grab[0]
			VARIABLESIP.append(address)
		 	N=len(VARIABLESIP)
			print " ---> variable Saved {"+colors[8]+"::IP"+str(N)+colors[0]+"} "+address

		if secuence[len(SAVEV):len(SAVEV)+3]=="mac":
		 	nID  = int(secuence[len(SAVEV)+4:])-1
		 	p = re.compile(ur'([0-9a-f]{2}(?::[0-9a-f]{2}){5})', re.IGNORECASE)
		 	address=re.findall(p, KTFVAR[nID])
		 	address=str(address)
		 	address=address.replace("'","")
		 	address=address.replace("[","")
		 	address=address.replace("]","")
		 	VARIABLESMAC.append(address)
		 	N=len(VARIABLESMAC)
			printAlert(3,"---> variable Saved {"+colors[8]+"::MAC"+str(N)+colors[0]+"} "+address)
	except:printAlert(6,"Check Again your Command for TEMP variables.")

### PING ###
def isLive(defaulthost, defaultport):
	if True:
		redTEST=socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
		redTEST.connect((defaulthost, int(defaultport))) 
		redTEST.close()
		return True
	return False

### START MONITOR INTERFACE ###
def start_monitor(interface):
	commands.getoutput("airmon-ng check kill")
	if checkDevice(interface):
		state=commands.getoutput("airmon-ng start "+interface)
		if state:return True
	return False

### MAQUETAR ###
def Maquetar(matriz):
	MMM = len(matriz[0])
	NNN = len(matriz)
	MAY = []
	VAR = 0
	MAYC = 0 
	VARB = 0
	while VAR != MMM:
		while VARB != NNN:
			if MAYC < len(matriz[VARB][VAR]):MAYC=len(matriz[VARB][VAR])
			VARB+=1
		MAY+=[MAYC]
		MAYC=0
		VAR+=1 
		VARB=0

	SUM = 0
	VAR = 0
	while VAR != len(MAY):
		SUM=SUM+MAY[VAR]
		VAR+=1


	VAR = 0
	LINE = " "
	while VAR != MMM:
		VARC=0
		ADDS=" "
		DIF = MAY[VAR] - len(matriz[0][VAR])
		if DIF != 0:
			while VARC != DIF:
				ADDS+=" "
				VARC+=1
		LINE += colors[13]+colors[10]+matriz[0][VAR]+ADDS+colors[0]
		VAR+=1
	print LINE

	VAR = 1
	VARB = 0
	LINE = " "
	while VAR != NNN:
		while VARB != MMM:
			ADDS =" "
			VARC=0
			DIF  = MAY[VARB] - len(matriz[VAR][VARB])
			if DIF != 0:
				while VARC != DIF:
					ADDS+=" "
					VARC+=1
			LINE += matriz[VAR][VARB]+ADDS
			VARB+=1
		LINE+="\n "
		VARB=0
		VAR+=1

	print LINE+"\n"

### AP's SCAN ###
def get_aps(mon,timeout):
	commands.getoutput('rm '+FOLDER_KATANA+'tmp/*.netxml')
	printAlert(0,"Scanning Access Points in Interface '"+mon+"', Please wait "+str(timeout)+"seg")
	Subprocess("airodump-ng "+mon+" -w '"+FOLDER_KATANA+"tmp/ktf.wifi' --wps --output-format netxml --write-interval "+str(timeout))
	time.sleep(timeout+1)
	APCOUNTER    = 0
	CLCOUNTER    = 0
	ESSIDs       = []
	BSSIDs       = []
	MANUs        = []
	CHANNELs     = []
	ENCRYPTAIONs = []
	PWRs         = []
	CLIENTMACs   = []
	CLIENTMANs   = []
	CLIENTESSs   = []
	tree = ET.parse(FOLDER_KATANA+'tmp/ktf.wifi-01.kismet.netxml')
	root = tree.getroot()
	try:
		Space()
		b =  [["#","MAC","CH","PWR","ENCRYPTION","VENDOR","ESSID"]]

		for network in root.findall('wireless-network'):
			if network.get('type')=="infrastructure":
				for essid in network.findall('SSID'):

					APCOUNTER += 1

					if essid.find('essid') is not None:
						ESSIDs.append(essid.find('essid').text)
					else:
						ESSIDs.append("NULL")

					if essid.find('encryption') is not None:
						ENCRYPTAIONs.append(essid.find('encryption').text)
					else:
						ENCRYPTAIONs.append("NULL")

		for network in root.findall('wireless-network'):
			if network.get('type')=="infrastructure":	
				BSSIDs.append(network.find('BSSID').text)
				MANUs.append(network.find('manuf').text)
				CHANNELs.append(network.find('channel').text)

		for network in root.findall('wireless-network'):
			if network.get('type')=="infrastructure":
				for essid in network.findall('snr-info'):
					PWRs.append(essid.find('last_signal_rssi').text)

		for network in root.findall('wireless-network'):
			if network.get('type')=="probe":
				for probe in network.findall('wireless-client'):
					CLCOUNTER+=1
					CLIENTMACs.append(probe.find('client-mac').text)
					CLIENTMANs.append(probe.find('client-manuf').text)

					for essid in probe.findall('SSID'):
						if essid.find('ssid') is not None:
							CLIENTESSs.append(essid.find('ssid').text)
						else:
							CLIENTESSs.append("NULL")
		LIST=0
		while LIST < APCOUNTER:
			b += [[str(LIST),str(BSSIDs[LIST]),str(CHANNELs[LIST]),str(PWRs[LIST]),str(ENCRYPTAIONs[LIST]),str(MANUs[LIST]),str(ESSIDs[LIST])]]
			LIST+=1

		b +=  [["","","","","","",""]]
		b +=  [["#","MAC","","","","VENDOR","PROBE"]]
		b +=  [["","","","","","",""]]


		LIST=0
		while LIST < CLCOUNTER:
			b += [[str(LIST),str(CLIENTMACs[LIST]),"","","",str(CLIENTMANs[LIST]),str(CLIENTESSs[LIST])]]
			LIST+=1

		Maquetar(b)
		commands.getoutput('killall airodump-ng')
	except:FAIL=1292

### LOG's ###
def saveRegister(init, data):  
	SET = ""
	for VAR in init.options:
		SET += "["+VAR+"|"+init.options[VAR][0]+"]"
	log=open('core/logs/register.log','a')
	log.write('\n ===================================== ')
	log.write('\n Module  : '+init.CodeName)
	log.write('\n Date    : '+time.strftime('%c'))
	log.write('\n Attack  : '+SET)
	log.write('\n Data    : '+data)
	log.close()

def SaveErrorLog(event):
	log=open('core/logs/Errors.log','a')
	log.write('\n Date    : '+time.strftime('%c'))
	log.write('\n info    : '+str(event))
	log.close()

### RUN TASK ###
def Rtask(process):
	xtem="" 
	if XTERM_OPTION:xtem="xterm -e "
	commands.getoutput(xtem+process)

### SUBPROCESS THREAD ###
def Subprocess(process):
	Hire=threading.Thread(target=Rtask, args=(process,))  
	Hire.start()

### MY LOCAL IP ### 
def get_local_ip():
	SocCKet = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try: 
		SocCKet.connect(("google.com",80))
		if True:
			IP_Address=SocCKet.getsockname()[0]
			SocCKet.close()
			return IP_Address
	except:
		SocCKet.close()
		return "NULL"

### GET EXTANAL IP ###
def get_external_ip():
	try:	
	    site = urllib.urlopen("http://checkip.dyndns.org/").read()
	    grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', site)
	    address = grab[0]
	    return address
	except:
		return "NULL"

### INTERFACES SCANNING ###
def get_interfaces():
	Interfaces=commands.getoutput("netstat -i | awk '{print $1}'")
	Interfaces=Interfaces.replace("\n",",")
	Interfaces=Interfaces.replace("Kernel,Iface,","")
	Interfaces=Interfaces.split(",")
	if len(Interfaces) >= 0:
		return Interfaces
	return "NULL"

### CHECK DEVICE ###
def checkDevice(device):
	devices=commands.getoutput("netstat -i | awk '{print $1}'")
	devices=devices.split("\n")
	for interface in devices:
		if device == interface : return True
	NoDeviceFound(device)
	return False

### GET MONITORS INTERFACE ###
def get_monitors_mode():
	Monitor=commands.getoutput("airmon-ng | grep 'mon' | awk '{print $2}'")
	Monitor=Monitor.split("\n")
	if len(Monitor) >= 0:
		return Monitor
	return "NULL"


### VALIDATE MAC ###
def checkMAC(mac):
	if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()): return True
	printAlert(1,"is not MAC address")

### IP's SCANNING LAN ###
def get_lan_ips(output):
	test=isConect()
	count=0
	if test!=False:
		array_ip=[]
		commands.getoutput('nmap -sn '+test+'/24 -oX tmp/ips.xml > null')
		xmldoc = minidom.parse('tmp/ips.xml')
		itemlist = xmldoc.getElementsByTagName('address')
		for s in itemlist:
		    ip=s.attributes['addr'].value
		    if ip!=test:
		    	array_ip.append(ip)

	if output==1 and test!=False:
		for ip in array_ip:
			
			if ip.find(":") <= 0 :
				mac=ip
				if get_gateway(2)==mac:
					mac+="]["+colors.B+"GATEWAY"+colors.W
			else:
				count=count+1
				print " [ "+str(count),"] Host's up  : ["+mac+"]["+ip+"]"
		commands.getoutput('rm tmp/ips.xml > null')
	else:
		return False

### STATUS CMD ###
def status_cmd(cmd):
	status_1=subprocess.call(cmd+' >/dev/null 2>&1', shell=True)
	if status_1==0:
		return "[\033[1m"+colors[2]+"OK"+colors[0]+"]"+colors[0]
	else:
		return "["+colors[1]+"\033[1mERROR"+colors[0]+"]"+colors[0]+"["+colors[3]+"\033[1mWARNING"+colors[0]+"]"


### GET GATEWAY ###
def get_gateway():
	ip_r_l=subprocess.Popen("ip r l",shell=True,stdout=subprocess.PIPE).communicate()[0]
	s = StringIO.StringIO(ip_r_l)
	for line in s:
		if "default" in line:
			gateway = re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',line).group(0)
			return gateway
	return "NULL"

### am I Connected? ###
def isConect():
	ip_r_l=subprocess.Popen("ip r l",shell=True,stdout=subprocess.PIPE).communicate()[0]
	s = StringIO.StringIO(ip_r_l)
	for line in s:
		if "default" in line:
			return True
	printAlert(1,"you not is connected to a network.\n")
	return False


### GET MY MAC ADRRESS ###
def get_my_mac_address():
	if isConect()!=False:
	    my_macs = [get_if_hwaddr(i) for i in get_if_list()]
	    for maca in my_macs:
	        if(maca != "00:00:00:00:00:00"):
	            return maca
	return "NULL"

### STATUS HTTP ###
def checkStatusHTTP(host, port, filerequest):
	connection = httplib.HTTPConnection(host,port)
	connection.request("GET", "/"+filerequest)
	response = connection.getresponse()
	code = response.status
	description = ["unknowk","unknowk"]
	if code == 200 : description = [ "OK"                                       , "Suf" ]
	if code == 201 : description = [ "Created"                                  , "Suf" ]
	if code == 202 : description = [ "Accepted"                                 , "Suf" ]
	if code == 203 : description = [ "Non/Authoritative Information (HTTP/1.1)" , "Suf" ]
	if code == 204 : description = [ "No Content"                               , "Suf" ]
	if code == 205 : description = [ "Reset Content"                            , "Suf" ]
	if code == 206 : description = [ "Partial Content"                          , "Suf" ]
	if code == 207 : description = [ "Multi/Status (Multi/Status, WebDAV)"      , "Suf" ]
	if code == 208 : description = [ "Already Reported (WebDAV)"                , "Suf" ]
	if code == 300 : description = [ "Multiple Choices"                         , "Inf:Redirection" ]
	if code == 301 : description = [ "Moved Permanently"                        , "Inf:Redirection" ]
	if code == 302 : description = [ "Found"                                    , "Inf:Redirection" ]
	if code == 303 : description = [ "See Other (from HTTP/1.1)"                , "Inf:Redirection" ]
	if code == 304 : description = [ "Not Modified"                             , "Inf:Redirection" ]
	if code == 305 : description = [ "Use Proxy (desde HTTP/1.1)"               , "Inf:Redirection" ]
	if code == 306 : description = [ "Switch Proxy"                             , "Inf:Redirection" ]
	if code == 307 : description = [ "Temporary Redirect (desde HTTP/1.1)"      , "Inf:Redirection" ]
	if code == 308 : description = [ "Permanent Redirect"                       , "Inf:Redirection" ]                
	if code == 400 : description = [ "Bad Request"                              , "Inf:Redirection" ]
	if code == 401 : description = [ "Unauthorized"                             , "Err:Client" ]
	if code == 402 : description = [ "Payment Required"                         , "Err:Client" ]
	if code == 403 : description = [ "Forbidden"                                , "Err:Client" ]
	if code == 404 : description = [ "Not Found"                                , "Err:Client" ]
	if code == 405 : description = [ "Method Not Allowed"                       , "Err:Client" ]
	if code == 406 : description = [ "Not Acceptable"                           , "Err:Client" ]
	if code == 407 : description = [ "Proxy Authentication Required"            , "Err:Client" ]
	if code == 408 : description = [ "Request Timeout"                          , "Err:Client" ]
	if code == 409 : description = [ "Conflict"                                 , "Err:Client" ]
	if code == 410 : description = [ "Gone"                                     , "Err:Client" ]
	if code == 411 : description = [ "Length Required"                          , "Err:Client" ]
	if code == 412 : description = [ "Precondition Failed"                      , "Err:Client" ]
	if code == 413 : description = [ "Request Entity Too Large"                 , "Err:Client" ]
	if code == 414 : description = [ "Request/URI Too Long"                     , "Err:Client" ]
	if code == 415 : description = [ "Unsupported Media Type"                   , "Err:Client" ]
	if code == 416 : description = [ "Requested Range Not Satisfiable"          , "Err:Client" ]
	if code == 417 : description = [ "Expectation Failed"                       , "Err:Client" ]
	if code == 418 : description = [ "I'm a teapot"                             , "Err:Client" ]
	if code == 422 : description = [ "Unprocessable Entity (WebDAV / RFC 4918)" , "Err:Client" ]
	if code == 423 : description = [ "Locked (WebDAV / RFC 4918)"               , "Err:Client" ]
	if code == 424 : description = [ "Failed Dependency (WebDAV) (RFC 4918)"    , "Err:Client" ]
	if code == 425 : description = [ "Unassigned"                               , "Err:Client" ]
	if code == 426 : description = [ "Upgrade Required (RFC 7231)"              , "Err:Client" ]
	if code == 428 : description = [ "Precondition Required"                    , "Err:Client" ]
	if code == 429 : description = [ "Too Many Requests"                        , "Err:Client" ]
	if code == 431 : description = [ "Request Header Fileds Too Large)"         , "Err:Client" ]
	if code == 451 : description = [ "Unavailable for Legal Reasons"            , "Err:Client" ]
	if code == 500 : description = [ "Internal Server Error"                    , "Err:Server" ]
	if code == 501 : description = [ "Not Implemented"                          , "Err:Server" ]
	if code == 502 : description = [ "Bad Gateway"                              , "Err:Server" ]
	if code == 503 : description = [ "Service Unavailable"                      , "Err:Server" ]
	if code == 504 : description = [ "Gateway Timeout"                          , "Err:Server" ]
	if code == 505 : description = [ "HTTP Version Not Supported"               , "Err:Server" ]
	if code == 506 : description = [ "Variant Also Negotiates (RFC 2295)"       , "Err:Server" ]
	if code == 507 : description = [ "Insufficient Storage (WebDAV / RFC 4918)" , "Err:Server" ]
	if code == 508 : description = [ "Loop Detected (WebDAV)"                   , "Err:Server" ]
	if code == 510 : description = [ "Not Extended (RFC 2774)"                  , "Err:Server" ]
	if code == 511 : description = [ "Network Authentication Required"          , "Err:Server" ]
	if (description[1]=="Err:Server"):
		printAlert(1,"Connection : "+description[0])
		return False
	if (description[1]=="Err:Client"):
		printAlert(6,"Connection : "+description[0])
		return False
	if (description[1]=="Suf")       :
		printAlert(3,"Connection : "+description[0])
		return True

### USER-AGENT GENERATOR ###
def RamdonAgent():
	global NUMBER_AGENTS,File_Agent_Open
	NUMBER_AGENTS=0
	if File_Agent_Open==False:
		with open(AGENTS_BROWSER,'r') as AGENT_LIST:
			for AGENT in AGENT_LIST:
				NUMBER_AGENTS=1+NUMBER_AGENTS
				AGENT_ARRAY.append(AGENT.replace("\n",""))
	File_Agent_Open=True
	Generate = 0
	Generate = random.randint(0, NUMBER_AGENTS)
	return AGENT_ARRAY[Generate]

### MAKE TABLES ###
def MakeTable(matriz):
	MMM = len(matriz[0])
	NNN = len(matriz)
	MAY = []
	VAR = 0
	MAYC = 0 
	VARB = 0
	while VAR != MMM:
		while VARB != NNN:
			if MAYC < len(matriz[VARB][VAR]):MAYC=len(matriz[VARB][VAR])
			VARB+=1
		MAY+=[MAYC]
		MAYC=0
		VAR+=1 
		VARB=0

	SUM = 0
	VAR = 0
	while VAR != len(MAY):
		SUM=SUM+MAY[VAR]
		VAR+=1

	VAR = 0
	R=" ----"
	while VAR != SUM:
		R+="-"
		VAR+=1
	print R

	VAR = 0
	LINE = " |"
	while VAR != MMM:
		VARC=0
		ADDS=""
		DIF = MAY[VAR] - len(matriz[0][VAR])
		if DIF != 0:
			while VARC != DIF:
				ADDS+=" "
				VARC+=1
		LINE += colors[13]+colors[8]+colors[11]+matriz[0][VAR]+ADDS+colors[0]+"|"
		VAR+=1
	print LINE
	print R

	VAR = 1
	VARB = 0
	LINE = " |"
	while VAR != NNN:
		while VARB != MMM:
			ADDS =""
			VARC=0
			DIF  = MAY[VARB] - len(matriz[VAR][VARB])
			if DIF != 0:
				while VARC != DIF:
					ADDS+=" "
					VARC+=1
			LINE += matriz[VAR][VARB]+ADDS+"|"
			VARB+=1
		LINE+="\n |"
		VARB=0
		VAR+=1

	print LINE+R[:-2].replace(" ","")+"|\n"

### GET NUMBER MODULES INSTALLED ###
def get_number_modules():
	tree = ET.parse('core/modules.xml')
	root = tree.getroot()
	Number=0
	for modules in root.findall('module'):
		Number+=1
	return Number

### GET NUMBER MODULES INSTALLED ###
def get_number_tools():
	tree = ET.parse('core/tools.xml')
	root = tree.getroot()
	Number=0
	for modules in root.findall('tool'):
		Number+=1
	return Number

class MyCompleter(object):  
    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  
            if text:  
                self.matches = [s for s in self.options 
                                    if s and s.startswith(text)]
            else:  
                self.matches = self.options[:]
        try: 
            return self.matches[state]
        except IndexError:
            return None

### LOAD BUFFER ###
def LoadBuffer():
	completer = MyCompleter([SETET, GETINFO, EXECUTECOMMAND, CLEAR, SHOW_MODULES, "target", "port", "version", "f::",RUN, UPDATE, SHOW_MORE])
	readline.set_completer(completer.complete)
	readline.parse_and_bind('tab: complete')

### CHECK IF INTERFACE SUPPORT AP MODE ###
def CheckAPmode():
	output = commands.getoutput('iw list | grep "* AP"')
	if len(output) > 0 : return True
	printAlert(1,"You device not support AP mode.")
	return False
