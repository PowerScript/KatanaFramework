# KATANA Vs 0.0.0.3
# Date  : 28/05/15
# Autor : RedToor
# Tool  : Python  
# Coders: RedToor, LeSZO ZerO, cl34r 
# 
# Made in Colombia, for KALI Distro ;) 
#
# KATANA Framework, Make for Kali Linux (Distribution) 
# it's Projects can be share 'd edicted, No Commerce

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
	      ^ ^ ^ ^THE FRAMEWORK, Build (0.0.0.3)
	   by """+colors.W+"""Red"""+colors.GR+"""Toor"""+colors.W+"""

	   """+colors.R+"""Command"""+colors.W+"""\t"""+colors.C+"""Description"""+colors.W+"""
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
			print "\n 	___________________"
			print "	|web's application|"
			print "	---------------------------------------------"
			print "	|"+colors.O+"web/httpbt"+colors.W+"\t | "+colors.C+"HTTP Brute Force"+colors.W+"        |"
			print "	|"+colors.O+"web/formbt"+colors.W+"\t | "+colors.C+"FORM Brute Force"+colors.W+"        |"
			print "	|"+colors.O+"web/cpfinder"+colors.W+"\t | "+colors.C+"Admin Finder"+colors.W+"            |"
			print "	|"+colors.O+"web/joomscan"+colors.W+"\t | "+colors.C+"Scan Vul's CMS Jommla"+colors.W+"   |"
			print "	---------------------------------------------\n 	__________________"
			print "	|sniffing network|"
			print "	---------------------------------------------"
			print "	|"+colors.O+"net/arplook"+colors.W+"\t | "+colors.C+"ARP Attack Detect"+colors.W+"       |"
			print "	---------------------------------------------\n 	____________________"
			print "	|social engineering|"
			print "	---------------------------------------------"
			print "	|"+colors.O+"seng/gdreport"+colors.W+"\t | "+colors.C+"Getting information"+colors.W+"     |"
			print "	---------------------------------------------\n 	_______"
			print "	|files|"
			print "	---------------------------------------------"
			print "	|"+colors.O+"file/brutezip"+colors.W+"\t | "+colors.C+"ZIP Brute Force"+colors.W+"         |"
			print "	|"+colors.O+"file/bruterar"+colors.W+"\t | "+colors.C+"RAR Brute Force"+colors.W+"         |"
			print "	---------------------------------------------\n 	_________"
			print "	|Clients|"
			print "	---------------------------------------------"
			print "	|"+colors.O+"clt/ftp"+colors.W+"\t | "+colors.C+"FTP Client"+colors.W+"              |"
			print "	|"+colors.O+"clt/sql"+colors.W+"\t | "+colors.C+"SQL Client"+colors.W+"              |"
			print "	|"+colors.O+"clt/pop3"+colors.W+"\t | "+colors.C+"POP3 Client"+colors.W+"             |"
			print "	---------------------------------------------\n 	_______________________"
			print "	|Brute Force Protocols|"
			print "	---------------------------------------------"
			print "	|"+colors.O+"bt/ftp"+colors.W+"\t 	 | "+colors.C+"FTP Brute Force"+colors.W+"         |"
			print "	|"+colors.O+"bt/sql"+colors.W+"\t 	 | "+colors.C+"SQL Brute Force"+colors.W+"         |"
			print "	|"+colors.O+"bt/ssh"+colors.W+"\t 	 | "+colors.C+"SSH Brute Force"+colors.W+"         |"
			print "	|"+colors.O+"bt/pop3"+colors.W+"\t | "+colors.C+"POP3 Brute Force"+colors.W+"        |"
			print "	---------------------------------------------\n 	________"
			print "	|Fuzzers|"
			print "	---------------------------------------------"
			print "	|"+colors.O+"fz/ftp"+colors.W+"\t 	 | "+colors.C+"FTP Fuzzer"+colors.W+"              |"
			print "	---------------------------------------------\n 	_______________"
			print "	|Miscellaneous|"
			print "	---------------------------------------------"
			print "	|"+colors.O+"mc/tlogin"+colors.W+"\t | "+colors.C+"Test of Credentials"+colors.W+"     |"
			print "	---------------------------------------------\n                     "
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