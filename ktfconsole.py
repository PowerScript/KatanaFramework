#
# Katana framework 
# @Autor : RedToor
# @Based : Python  
# @Email : redtoor[at]inbox.ru
# 
# Made in Colombia, for Pentest Distro's
#

from scripts import *
from core import info
from core import help
from core import colors
from core import updatekatana
from core import splash
import random

spa=random.randint(1,3)
if spa==1:
	print splash.splash1
elif spa==2:
	print splash.splash2
elif spa==3:
	splash.splash3(0)

print """
                  |"""+colors.B+""">"""+colors.O+"""Katana Framework"""+colors.W+"""
                  |"""+colors.B+"""["""+colors.R+"""Core"""+colors.W+""" = """+info.version+"""
   >~$$$=~@@@@@:::|"""+colors.B+"""["""+colors.R+"""Tema"""+colors.W+""" = """+info.tema+"""
   >~$$$=~@@@@@:::|"""+colors.B+"""["""+colors.R+"""Modules"""+colors.W+""" = """+colors.G+""" """+info.modules+""""""+colors.W+"""
                  |"""+colors.B+"""["""+colors.R+"""Date"""+colors.W+""" = """+info.date+"""
	  """

def katana():
	if True:
		action = raw_input(colors.W+" ktn > "+colors.W)
		if action == "show modules" or action == "showm":
			print "\n 	_____________________"
			print "	|web's application|"+colors.G+"5"+colors.W+"|"
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"web/httpbt"+colors.W+"\t * "+colors.C+"Brute force to HTTP 401"+colors.W
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"web/formbt"+colors.W+"\t * "+colors.C+"Brute force to Form-based"+colors.W
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"web/cpfinder"+colors.W+"   * "+colors.C+"Admin panel finder"+colors.W
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"web/joomscan"+colors.W+"   * "+colors.C+"Scanner Vul's CMS Jommla"+colors.W
			#print "	"+colors.R+"@"+colors.W+"|"+colors.O+"web/ddos"+colors.W+"     | "+colors.C+"denial of service web"+colors.W+"           
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"web/whois"+colors.W+"      * "+colors.C+"Who-is web"+colors.W
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 	____________________"
			print "	|sniffing network|"+colors.G+"1"+colors.W+"|"
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"net/arplook"+colors.W+"\t * "+colors.C+"ARP attack detector"+colors.W         
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 	______________________"
			print "	|social engineering|"+colors.G+"1"+colors.W+"|"
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"seng/gdreport"+colors.W+"  * "+colors.C+"Getting information with web"+colors.W    
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 	_________"
			print "	|files|"+colors.G+"2"+colors.W+"|"
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"file/Brutezip"+colors.W+"  * "+colors.C+"Brute force to zip files"+colors.W      
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"file/Bruterar"+colors.W+"  * "+colors.C+"Brute force to rar files"+colors.W        
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 	___________"
			print "	|Clients|"+colors.G+"3"+colors.W+"|"
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"clt/ftp"+colors.W+"\t * "+colors.C+"Console FTP client"+colors.W                      
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"clt/sql"+colors.W+"\t * "+colors.C+"Console SQL client"+colors.W                      
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"clt/pop3"+colors.W+"\t * "+colors.C+"Console POP3 client"+colors.W                     
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 	____________"
			print "	|Services|"+colors.G+"3"+colors.W+"|"
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"server/sql"+colors.W+"\t * "+colors.C+"Start SQL Server"+colors.W                      
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"server/apache"+colors.W+"  * "+colors.C+"Start HTTP Server"+colors.W                     
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"server/ssh"+colors.W+"\t * "+colors.C+"Start SSH Server"+colors.W                      
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 	_________________________"
			print "	|Brute Force Protocols|"+colors.G+"4"+colors.W+"|"
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"bt/ftp"+colors.W+"\t * "+colors.C+"Brute force to ftp"+colors.W        
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"bt/sql"+colors.W+"\t * "+colors.C+"Brute force to sql"+colors.W              
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"bt/ssh"+colors.W+"\t * "+colors.C+"Brute force to ssh"+colors.W              
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"bt/pop3"+colors.W+"\t * "+colors.C+"Brute force to pop3"+colors.W             
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 	___________"
			print "	|Fuzzers|"+colors.G+"1"+colors.W+"|"
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"fz/ftp"+colors.W+"\t * "+colors.C+"Fuzzer to ftp"+colors.W               
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 	________"
			print "	|Wifi|"+colors.G+"2"+colors.W+"|"
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"wifi/wpabtf"+colors.W+"\t * "+colors.C+"Brute force to wpa encriptation"+colors.W
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"wifi/ddos"+colors.W+"\t * "+colors.C+"Denial of service wifi"+colors.W 
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 	_________________"
			print "	|Miscellaneous|"+colors.G+"2"+colors.W+"|"
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"mc/tlogin"+colors.W+"\t * "+colors.C+"Test of credentials"+colors.W             
			print "	"+colors.R+"@"+colors.W+"|"+colors.O+"mc/gendic"+colors.W+"\t * "+colors.C+"Generator dictionary"+colors.W            
			print "	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n                     "
			katana()
		elif action[0:3] == "use":
			if action[4:14] == "web/httpbt":
				BruteForceHTTP.httpbt(0)
			if action[4:16] == "web/cpfinder":
				AdminFinder.adminfinder(0)
			if action[4:16] == "web/formbt":
				BruteForceFormBase.httpformbasebruteforce(0)
			if action[4:16] == "net/arplook":
				ARPLooking.arplook()
			if action[4:17] == "seng/gdreport":
				GetDataReport.getdatareport(0)
			if action[4:17] == "file/Brutezip":
				BruteZIP.btzip()
			if action[4:17] == "file/Bruterar":
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
				Joomscan.xjoomla(0)
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
				Whois.wuis(0)
			else:
				katana()
		elif action == "exit" or action == "x":
			print colors.C+"   GooD"+colors.W+" bye."
			exit()
		elif action == "help" or action == "h":
			help.help()
		elif action == "update" or action == "u":
			updatekatana.update()
		else:
			print " ["+colors.R+"!"+colors.W+"] Invalid parameter use show 'help' for more information"+colors.W
			katana()
katana()