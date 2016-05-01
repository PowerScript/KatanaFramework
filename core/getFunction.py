#!/usr/bin/env python
#HEADER#######################
# Katana framework           #
# Functions File             #
# Last Modified: 30/04/2016  #
# Review: 1                  #
#######################HEADER#

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from GeneralCommands import *
from xml.dom import minidom
from scapy.all import *
from design import *
import xml.etree.ElementTree as ET
import fcntl, socket, struct
import readline, rlcompleter
import updatekatana
import subprocess
import threading
import StringIO
import commands  
import Setting
import logging
import urllib
import colors
import help
import socket
import time 
import sys                   
import re

ap_list = []
VARIABLESIP=[]
VARIABLESMAC=[]
Desing=DESIGN()

### GENERAL ###
def KatanaCheckActionShowModules(action):
	if action == SHOW_MODULES or action == SHOW_MODULES_SHORT: return True
def UpdateValue(action,matriz):
	if action[:len(SETET)]==SETET:
		var=0
		for Namevalue in matriz:
			if action[len(SETET)+1:len(SETET)+1+len(Namevalue[[1][0]])]==Namevalue[[1][0]]: 
				checkValue=action[len(SETET)+2+len(Namevalue[[1][0]]):]
				if checkValue[0:4] == "::IP" : checkValue = VARIABLESIP[int(checkValue[4:])-1]
				if checkValue[0:5] == "::MAC": checkValue = VARIABLESIP[int(checkValue[5:])-1]
				Desing.change(Namevalue[[1][0]],checkValue)
				matriz[var][0]=checkValue
				return matriz
			var+=1
	return matriz
def KatanaCheckActionSetValue(action):
	if action[:len(SETET)]==SETET            : return True
def KatanaCheckActionUseModule(action):
	if action[:len(SELECT)]==SELECT          : return True
def KatanaCheckActionShowOptions(action):
	if action == SHOW or action == SHOW_SHORT: return True
def KatanaCheckActionSaveValue(action):
	if action[:4] == "save"                  : return True
def KatanaCheckActionisBack(action):
	if action==BACKING                       : return True
def runModule(action):
	if action=="run"                         : return True
def KatanaCheckActionGlobalCommands(action):
	if     action[:len(EXIT)]        == EXIT   or action[:len(EXIT)]        == EXIT_SHORT  : exit()
	elif   action[:len(HELP)]        == HELP   or action[:len(HELP_SHORT)]  == HELP_SHORT  : help.help()
	elif   action[:len(UPDATE)]      == UPDATE or action[:len(UPDATE_SHORT)]== UPDATE_SHORT: updatekatana.update()
	elif   action[:len(CLEAR)]       == CLEAR  or action[:len(CLEAR_SHORT)] == CLEAR_SHORT : subprocess.call('clear', shell=True)
	else: Desing.Helper()
def ShowOptions(Options):
	Desing.option()
	var = 0
	for Option in Options:
		Desing.descrip(str(Options[var][1]),str(Options[var][2]),str(Options[var][3]),str(Options[var][0]))
		var+=1
 	Desing.space()

### VARIABLES TEMP ###
def SaveValue(secuence,matrix):
	if secuence[5:8]=="IP:":
		IPss=int(secuence[8:])-1
		IPsaved=matrix[IPss]
		grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', IPsaved)
		address = grab[0]
		N=len(VARIABLESIP)
		print "----> variable Saved {\033[40m::IP"+str(N)+colors.W+"} "+address
		MakeVarTmpIP(Value=address)

	if secuence[5:9]=="MAC:":
		IPss=int(secuence[9:])-1
		IPsaved=matrix[IPss]
		p = re.compile(ur'([0-9a-f]{2}(?::[0-9a-f]{2}){5})', re.IGNORECASE)
		address=re.findall(p, IPsaved)
		address=str(address)
		address=address.replace("'","")
		address=address.replace("[","")
		address=address.replace("]","")
		N=len(VARIABLESMAC)
		print "----> variable Saved {\033[40m::MAC"+str(N)+colors.W+"} "+str(address)
		MakeVarTmpMAC(Value=address)
def MakeVarTmpIP(Value):
	VARIABLESIP.append(Value)
def MakeVarTmpMAC(Value):
	VARIABLESMAC.append(Value)

### PING ###
def live(defaulthost, defaultport):
	red=socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
	red.connect((defaulthost, int(defaultport))) 
	red.close()

### AP's SCAN ###
def scanwifi(mon):
	commands.getoutput('rm /usr/share/katana/tmp/*')
	print " "+colors.GR+"Scanning Access Points in Interface '"+mon+"', Please wait 10s"+colors.W
	Subprocess('airodump-ng '+mon+' -w /usr/share/katana/tmp/ktf.wifi --output-format netxml --write-interval 10')
	time.sleep(10)
	commands.getoutput('killall airodump-ng')
	numberID=0
	ESSIDs       = []
	BSSIDs       = []
	MANUs        = []
	CHANNELs     = []
	ENCRYPTAIONs = []
	LISTAPs      = []
	tree = ET.parse('/usr/share/katana/tmp/ktf.wifi-01.kismet.netxml')
	root = tree.getroot()
	print " "+colors.GR+" #\t"+colors.O+"ESSID"+colors.W+colors.GR+"\tMAC\t"+colors.P+"VENDOR"+colors.W+colors.GR+"\tCHANNEL\t"+colors.B+"ENCRYPTION"+colors.W+colors.GR+"              "+colors.W
	for network in root.findall('wireless-network'):
		for essid in network.findall('SSID'):
			ESSIDs.append(essid.find('essid').text)
			ENCRYPTAIONs.append(essid.find('encryption').text)
		BSSIDs.append(network.find('BSSID').text)
		MANUs.append(network.find('manuf').text)
		CHANNELs.append(network.find('channel').text)
	numberID=0
	for ESSID in ESSIDs:
		print colors.W+" ["+str(numberID)+"] "+colors.O+ESSIDs[numberID]+colors.W+" "+BSSIDs[numberID]+" "+colors.P+MANUs[numberID]+colors.W+" "+CHANNELs[numberID]+" "+colors.B+ENCRYPTAIONs[numberID]+colors.W
		numberID=numberID+1
		
### LOG's ###
def save(module, target, port, dat1, dat2):
	log=open('core/logs/logsBruteForce.log','a')
	log.write('\n ===================================== ')
	log.write('\n Module  : '+module)
	log.write('\n Data    : '+time.strftime('%c'))
	log.write('\n target  : '+target)
	log.write('\n port    : '+port)
	log.write('\n Cracked : username : '+dat1+' , password : '+dat2)
	log.close()
def savetwo(module, files, password):
	log=open('core/logs/logsBruteForce.log','a')
	log.write('\n ===================================== ')
	log.write('\n Module  : '+module)
	log.write('\n Data    : '+time.strftime('%c'))
	log.write('\n file    : '+files)
	log.write('\n Cracked : password : '+password)
	log.close()
def savethree(module,target,port,patch,username,password):
	log=open('core/logs/logsBruteForce.log','a')
	log.write('\n ===================================== ')
	log.write('\n Module  : '+module)
	log.write('\n Data    : '+time.strftime('%c'))
	log.write('\n target  : '+target)
	log.write('\n port    : '+port)
	log.write('\n Patch   : '+patch)
	log.write('\n Cracked : username: '+username+', password : '+password)
	log.close()
def savefour(module,target,port,patch,method,dat1,dat2,username,password):
	log=open('core/logs/logsBruteForce.log','a')
	log.write('\n ===================================== ')
	log.write('\n Module  : '+module)
	log.write('\n Data    : '+time.strftime('%c'))
	log.write('\n target  : '+target)
	log.write('\n port    : '+port)
	log.write('\n Patch   : '+patch)
	log.write('\n Cracked : '+dat1+':'+username+', '+dat2+':'+password)
	log.close()
def savefive(module,target,port,results):
	log=open('core/logs/logsAdminFinder.log','a')
	log.write('\n ===================================== ')
	log.write('\n Module  : '+module)
	log.write('\n Data    : '+time.strftime('%c'))
	log.write('\n target  : '+target)
	log.write('\n port    : '+port)
	log.write('\n Found   : '+results)
	log.close()
	
### RUN TASK ###
def Rtask(process):   
        commands.getoutput(process)

### SUBPROCESS THREAD ###
def Subprocess(process):
	Hire=threading.Thread(target=Rtask, args=(process,))  
	Hire.start()

### MY LOCAL IP ### 
def Myip():
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
	if Interfaces=="":
		return "NULL"
	else:
		return Interfaces

### CHECK DEVICE ###
def checkDevice(device):
	devices=commands.getoutput("netstat -i")
	if devices.find(device) >= 0:
		return True
	else:
		return False

### GET MONITORS ###
def monitor():
	Monitor=commands.getoutput("airmon-ng | grep 'mon' | awk '{print $2}'")
	Monitor=Monitor.replace("\n",",")
	if Monitor=="":
		Monitor="No monitor mode enabled, use 'start {Interface}' right here."
	print " Int... Monitor  : ",Monitor
	if Monitor!="No monitor mode enabled, use 'start {Interface}' right here.":
		scanwifi(Monitor)
		print ""

### IP's SCANNING LAN ###
def lan_ips(output):
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
def status_cmd(cmd,tabulations):
	status_1=subprocess.call(cmd+' >/dev/null 2>&1', shell=True)
	if status_1==0:
		return tabulations+"[\033[1m"+colors.G+"OK"+colors.W+"]"+colors.W
	else:
		return tabulations+"["+colors.R+"\033[1mERROR"+colors.W+"]"+colors.W+"["+colors.B+"\033[1mWARNING"+colors.W+"]"


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
	return False


### GET MY MAC ADRRESS ###
def my_mac_address():
	if isConect()!=False:
	    my_macs = [get_if_hwaddr(i) for i in get_if_list()]
	    for maca in my_macs:
	        if(maca != "00:00:00:00:00:00"):
	            return maca
	return "NULL"

### STATUS HTTP ###
def checkStatus(code):
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
	return description
