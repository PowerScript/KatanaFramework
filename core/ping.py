#
# Katana framework 
# @Katana Ping functions
#

from xml.dom import minidom
from scapy.all import *

import xml.etree.ElementTree as ET
import fcntl, socket, struct
import readline, rlcompleter
import subprocess
import threading
import StringIO
import commands  
import Setting
import logging
import urllib
import colors
import socket
import time 
import sys                   
import re

ap_list = []
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
VARIABLESIP=[]
VARIABLESMAC=[]

### PING ###
def live(defaulthost, defaultport):
	red=socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
	red.connect((defaulthost, int(defaultport))) 
	red.close()

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
	
### NO USED ###
def PacketHandler(pkt):
  if pkt.haslayer(Dot11) :
		if pkt.type == 0 and pkt.subtype == 8 :
			if pkt.addr2 not in ap_list :
				ap_list.append(pkt.addr2)
				print " BSSID: %s \t ESSID: %s " %(pkt.addr2, pkt.info)
				#sniff(iface="mon0", prn = PacketHandler)
### RUN TASK ###
def Rtask(process):   
        commands.getoutput(process)

### SUBPROCESS THREAD ###
def Subprocess(process):
	Hire=threading.Thread(target=Rtask, args=(process,))  
	Hire.start()

### AP's SCAN ###
def scanwifi(mon):
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
	commands.getoutput('rm /usr/share/katana/tmp/*.netxml')
		
### MY LOCAL IP ### 
def myip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try: 
		s.connect(("google.com",80))
		if True:
			ip=s.getsockname()[0]
			s.close()
			return ip
	except:
		s.close()
		return False

### GET EXTANAL IP ###
def get_external_ip():
	try:	
	    site = urllib.urlopen("http://checkip.dyndns.org/").read()
	    grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', site)
	    address = grab[0]
	    if True:
	    	print(" You Public IP: "+address+"\n")
	except:
		print " ["+colors.R+"-"+colors.W+"] Not Connect to nothing Network.\n"

### INTERFACES SCANNING ###
def interfaces(output):
	Interfaces=commands.getoutput(" netstat -i | grep 'wlan' | awk '{print $1}'")
	Interfaces=Interfaces.replace("\n",",")
	if output==1:
		if Interfaces=="":
			Interfaces="Interfaces  : No network cards was found."
		else:
			print " Interfaces : ",Interfaces

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
	test=conneted()
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
	status_1=subprocess.call(cmd+' > null', shell=True)
	if status_1==0:
		return tabulations+"[\033[1m"+colors.G+"OK"+colors.W+"]"+colors.W
	else:
		return tabulations+"["+colors.R+"\033[1mERROR"+colors.W+"]"+colors.W+"["+colors.B+"\033[1mWARNING"+colors.W+"]"


### GET GATEWAY ###
def get_gateway(output):
	test=conneted()
	if test!=False:
		ip_r_l=subprocess.Popen("ip r l",shell=True,stdout=subprocess.PIPE).communicate()[0]
		s = StringIO.StringIO(ip_r_l)
		for line in s:
			if "default" in line:
				gateway = re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',line).group(0)

	if output==1 and test!=False:
		print " Gateway    :  "+gateway
	if output==2 and test!=False:
		return gateway

### am I Connected? ###
def conneted():
	test=myip()
	if test!=False:
		return test
	else:
		return False

### GET MY MAC ADRRESS ###
def my_mac_address(output):
	if conneted()!=False:
	    my_macs = [get_if_hwaddr(i) for i in get_if_list()]
	    for maca in my_macs:
	        if(maca != "00:00:00:00:00:00") and output==1:
	            print " Mac Address:  "+maca
	            return


### VARIABLES TEMP ###
def SaveVariable(secuence,matrix):
	if secuence[5:8]=="IP:":
		IPss=int(secuence[8:])-1
		IPsaved=matrix[IPss]
		grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', IPsaved)
		address = grab[0]
		N=len(VARIABLESIP)
		print " -->Saved variable {\033[40m::IP"+str(N)+colors.W+"} "+address
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
		print " -->Saved variable {\033[40m::MAC"+str(N)+colors.W+"} "+str(address)
		MakeVarTmpMAC(Value=address)

def MakeVarTmpIP(Value):
	VARIABLESIP.append(Value)
def MakeVarTmpMAC(Value):
	VARIABLESMAC.append(Value)

### UPDATE PARAMATERS ###
def update(variable,value,name):
	var=len(name)+5
	value=value[var:]
	if value[0:4] == "::IP":
		N=int(value[4:])-1
		return VARIABLESIP[N]
	elif value[0:5] == "::MAC":
		N=int(value[5:])-1
		return VARIABLESMAC[N]
	else:
		return value
