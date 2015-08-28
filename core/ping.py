#
# Katana framework 
# @Katana Ping functions
#


from scapy.all import *
import urllib
import re
import colors
import socket
import time 
import commands   
import subprocess
ap_list = []

def live(defaulthost, defaultport):
	red=socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
	red.connect((defaulthost, int(defaultport))) 
	red.close()
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
def PacketHandler(pkt):
  if pkt.haslayer(Dot11) :
		if pkt.type == 0 and pkt.subtype == 8 :
			if pkt.addr2 not in ap_list :
				ap_list.append(pkt.addr2)
				print " BSSID: %s \t ESSID: %s " %(pkt.addr2, pkt.info)
def scanwifi():
	print " Scanning APs - "+colors.O+"Ctrl+C"+colors.W+" for Stop.\n"
	sniff(iface="mon0", prn = PacketHandler)
def myip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try: 
		s.connect(("google.com",80))
		if True:
			print(" You Local IP: "+s.getsockname()[0]+"\n")
	except:
		print " ["+colors.R+"-"+colors.W+"] Not Connect to nothing Network.\n"
	s.close()
def get_external_ip():
	try:	
	    site = urllib.urlopen("http://checkip.dyndns.org/").read()
	    grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', site)
	    address = grab[0]
	    if True:
	    	print(" You Public IP: "+address+"\n")
	except:
		print " ["+colors.R+"-"+colors.W+"] Not Connect to nothing Network.\n"
def interfaces():
	Interfaces=commands.getoutput("airmon-ng | grep 'wlan' | awk '{print $1}'")
	Interfaces=Interfaces.replace("\n",",")
	if Interfaces=="":
		Interfaces="No network cards was found."
	print " Interfaces      : ",Interfaces
def monitor():
	Monitor=commands.getoutput("airmon-ng | grep 'mon' | awk '{print $1}'")
	Monitor=Monitor.replace("\n",",")
	if Monitor=="":
		Monitor="No monitor mode enabled, use 'start {Interface}' right here."
	print " Int... Monitor  : ",Monitor
	if Monitor!="No monitor mode enabled, use 'start {Interface}' right here.":
		scanwifi()
		print ""