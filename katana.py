# KATANA 
# Autor : RedToor
# Tool  : Python  
# Coders: RedToor, LeSZO ZerO, cl34r.
# 
# Made in Colombia, for KALI Distro ;) 
#
# KATANA Framework, Make for Kali Linux (Distribution) 
# it's Projects can be share 'd edicted, No Commerce

from scripts import Whois
from scripts import GenDic
from scripts import Wifi_DDOS
from scripts import WpaBTF
from scripts import services
from scripts import Joomscan
from scripts import TLogin
from scripts import FuzzerFTP
from scripts import BruteForcePOP3
from scripts import BruteForceSQL
from scripts import BruteForceSSH
from scripts import BruteForceFTP
from scripts import BruteRAR
from scripts import BruteZIP
from scripts import BruteForceFormBase
from scripts import BruteForceHTTP
from scripts import ClientMYSQL
from scripts import ClientFTP
from scripts import ClientPOP3
from scripts import GetDataReport
from scripts import ARPLooking
from scripts import AdminFinder
from core import info
from core import help
from core import colors
from core import updatekatana

print """
	   
                  __                         __
         ___  ___/  \_______________   ___  /  \---
         | .|/ ./ __ \__   ___/.....\  | | / __ \----
         | .  ./ /__\ \/../ _ \. /\..\ | |/ /__\ \-----
         | .| .\.\  /./../ /_\.\.\ \..\| |\.\  /./---
         |_.|\_.\.\/./._/./   \_\.\ \..__| \.\/./--
	    _______?___________________________________
	   {_| | | | I################################/
	      ^ ^ ^ ^THE FRAMEWORK, Build ("""+info.version+""")
	   by """+colors.W+"""Red"""+colors.GR+"""Toor"""+colors.W+"""

	   """+colors.R+"""Command"""+colors.W+"""\t"""+colors.C+"""  Description"""+colors.W+"""
	   help		: help about command
	   show modules	: modules
	   show options : options mudule
	   use		: use module
	   set          : set up 
	   update       : update Katana

	  """

def katana():
	try:
		action = raw_input(colors.O+" ktn/ "+colors.W)
		if action == "show modules":
			print "\n 	_____________________"
			print "	|web's application|"+colors.G+"5"+colors.W+"|"
			print "	-------------------------------------------------------"
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"web/httpbt"+colors.W+"\t | "+colors.C+"brute force to HTTP 401"+colors.W+"         |"+colors.R+"<--"+colors.W
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"web/formbt"+colors.W+"\t | "+colors.C+"brute force to form POST/GET"+colors.W+"    |"+colors.R+"<--"+colors.W
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"web/cpfinder"+colors.W+" | "+colors.C+"admin panel finder"+colors.W+"              |"+colors.R+"<--"+colors.W
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"web/joomscan"+colors.W+" | "+colors.C+"Scanner Vul's CMS Jommla"+colors.W+"        |"+colors.R+"<--"+colors.W
			#print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"web/ddos"+colors.W+"     | "+colors.C+"denial of service web"+colors.W+"           |"+colors.R+"<--"+colors.W
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"web/whois"+colors.W+"    | "+colors.C+"who-is web"+colors.W+"                      |"+colors.R+"<--"+colors.W
			print "	-------------------------------------------------------\n 	____________________"
			print "	|sniffing network|"+colors.G+"1"+colors.W+"|"
			print "	-------------------------------------------------------"
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"net/arplook"+colors.W+"\t | "+colors.C+"ARP attack detector"+colors.W+"             |"+colors.R+"<--"+colors.W
			print "	-------------------------------------------------------\n 	______________________"
			print "	|social engineering|"+colors.G+"1"+colors.W+"|"
			print "	-------------------------------------------------------"
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"seng/gdreport"+colors.W+"| "+colors.C+"getting information with web"+colors.W+"    |"+colors.R+"<--"+colors.W
			print "	-------------------------------------------------------\n 	_________"
			print "	|files|"+colors.G+"2"+colors.W+"|"
			print "	-------------------------------------------------------"
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"file/brutezip"+colors.W+"| "+colors.C+"brute force to zip files"+colors.W+"        |"+colors.R+"<--"+colors.W
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"file/bruterar"+colors.W+"| "+colors.C+"brute force to rar files"+colors.W+"        |"+colors.R+"<--"+colors.W
			print "	-------------------------------------------------------\n 	___________"
			print "	|Clients|"+colors.G+"3"+colors.W+"|"
			print "	-------------------------------------------------------"
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"clt/ftp"+colors.W+"\t | "+colors.C+"ftp client"+colors.W+"                      |"+colors.R+"<--"+colors.W
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"clt/sql"+colors.W+"\t | "+colors.C+"sql client"+colors.W+"                      |"+colors.R+"<--"+colors.W
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"clt/pop3"+colors.W+"\t | "+colors.C+"pop3 client"+colors.W+"                     |"+colors.R+"<--"+colors.W
			print "	-------------------------------------------------------\n 	____________"
			print "	|Services|"+colors.G+"3"+colors.W+"|"
			print "	-------------------------------------------------------"
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"server/sql"+colors.W+"\t | "+colors.C+"sql Server"+colors.W+"                      |"+colors.R+"<--"+colors.W
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"server/apache"+colors.W+"| "+colors.C+"http Server"+colors.W+"                     |"+colors.R+"<--"+colors.W
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"server/ssh"+colors.W+"\t | "+colors.C+"ssh Server"+colors.W+"                      |"+colors.R+"<--"+colors.W
			print "	-------------------------------------------------------\n 	_________________________"
			print "	|Brute Force Protocols|"+colors.G+"4"+colors.W+"|"
			print "	-------------------------------------------------------"
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"bt/ftp"+colors.W+"\t | "+colors.C+"brute force to ftp"+colors.W+"              |"+colors.R+"<--"+colors.W
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"bt/sql"+colors.W+"\t | "+colors.C+"brute force to sql"+colors.W+"              |"+colors.R+"<--"+colors.W
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"bt/ssh"+colors.W+"\t | "+colors.C+"brute force to ssh"+colors.W+"              |"+colors.R+"<--"+colors.W
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"bt/pop3"+colors.W+"\t | "+colors.C+"brute force to pop3"+colors.W+"             |"+colors.R+"<--"+colors.W
			print "	-------------------------------------------------------\n 	___________"
			print "	|Fuzzers|"+colors.G+"1"+colors.W+"|"
			print "	-------------------------------------------------------"
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"fz/ftp"+colors.W+"\t | "+colors.C+"fuzzer to ftp"+colors.W+"                   |"+colors.R+"<--"+colors.W
			print "	-------------------------------------------------------\n 	________"
			print "	|Wifi|"+colors.G+"2"+colors.W+"|"
			print "	-------------------------------------------------------"
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"wifi/wpabtf"+colors.W+"\t | "+colors.C+"brute force to wpa encriptation"+colors.W+" |"+colors.R+"<--"+colors.W
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"wifi/ddos"+colors.W+"\t | "+colors.C+"denial of service wifi"+colors.W+"          |"+colors.R+"<--"+colors.W
			print "	-------------------------------------------------------\n 	_________________"
			print "	|Miscellaneous|"+colors.G+"2"+colors.W+"|"
			print "	-------------------------------------------------------"
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"mc/tlogin"+colors.W+"\t | "+colors.C+"test of credentials"+colors.W+"             |"+colors.R+"<--"+colors.W
			print "	"+colors.R+"-->"+colors.W+"|"+colors.O+"mc/gendic"+colors.W+"\t | "+colors.C+"generator dictionary"+colors.W+"            |"+colors.R+"<--"+colors.W
			print "	-------------------------------------------------------\n                     "
			katana()
		elif action[0:3] == "use":
			if action[4:14] == "web/httpbt":
				BruteForceHTTP.httpbt()
			if action[4:16] == "web/cpfinder":
				AdminFinder.adminfinder()
			if action[4:16] == "web/formbt":
				BruteForceFormBase.httpformbasebruteforce()
			if action[4:16] == "net/arplook":
				ARPLooking.arplook()
			if action[4:17] == "seng/gdreport":
				GetDataReport.getdatareport()
			if action[4:17] == "file/brutezip":
				BruteZIP.btzip()
			if action[4:17] == "file/bruterar":
				BruteRAR.btRAR()
			if action[4:11] == "clt/ftp":
				ClientFTP.cftp()
			if action[4:10] == "bt/ftp":
				BruteForceFTP.btftp()
			if action[4:17] == "wifi/hwifipwd":
				WifiDetecter.hackerwifipwd()
			if action[4:10] == "bt/ssh":
				BruteForceSSH.btssh()	
			if action[4:11] == "clt/sql":
				ClientMYSQL.cmysql()	
			if action[4:10] == "bt/sql":
				BruteForceSQL.btsql()		
			if action[4:11] == "bt/pop3":
				BruteForcePOP3.btpop3()
			if action[4:12] == "clt/pop3":
				ClientPOP3.cpop3()
			if action[4:13] == "mc/tlogin":
				TLogin.tlogin()
			if action[4:10] == "fz/ftp":
				FuzzerFTP.fftp()
			if action[4:17] == "web/joomscan":
				Joomscan.xjoomla()
			if action[4:14] == "server/sql":
				services.services('mysql')
			if action[4:14] == "server/ssh":
				services.services('ssh')
			if action[4:18] == "server/apache":
				services.services('apache2')
			if action[4:15] == "wifi/wpabtf":
				WpaBTF.wpabtf()
			if action[4:13] == "wifi/ddos":
				Wifi_DDOS.ddos()
			if action[4:13] == "mc/gendic":
				GenDic.Gendic()
			if action[4:13] == "web/whois":
				Whois.wuis()
			else:
				print " ["+colors.O+"!"+colors.W+"] module not found"
				katana()
		elif action == "exit":
			print colors.C+"   GooD"+colors.W+" bye."
			exit()
		elif action == "help":
			help.help()
		elif action == "update":
			updatekatana.update()
		else:
			print " ["+colors.O+"!"+colors.W+"] command No Accept"
			katana()
	except(KeyboardInterrupt, SystemExit):
		print("\n ["+colors.O+"!"+colors.W+"] (Ctrl + C) Detected, System Exit")
katana()