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
import subprocess            
spa=random.randint(2,5)
subprocess.call('clear', shell=True)
if spa==2:
	print splash.splash2
elif spa==3:
	print splash.splash3
elif spa==4:
	print splash.splash4
elif spa==5:
	print splash.splash5

print """
	 .-.--.  
	 \  \==\ """+colors.O+"""Katana Framework"""+colors.W+"""
	 /- /==/ 
	/' /==/  """+colors.G+"""~"""+colors.R+"""Core"""+colors.W+""" = """+info.version+"""
	|,|==|   """+colors.G+"""~"""+colors.R+"""Tema"""+colors.W+""" = """+info.tema+"""
	\  \==\  """+colors.G+"""~"""+colors.R+"""Modules"""+colors.W+""" = """+colors.G+""" """+info.modules+""""""+colors.W+"""
	 \ ,\==\ """+colors.G+"""~"""+colors.R+"""Date"""+colors.W+""" = """+info.date+"""
	 / -/==/ """+colors.B+""" Github: redtoor/Katana"""+colors.W+"""
	 `-'--'  
	  """


def line(module, description):
	print """ |==| .| """+colors.R+"""@"""+colors.W+"""|"""+colors.O+module+colors.W+"""\t\t | """+colors.C+description+colors.W
def separator():
	print """ |==| .|  """
def katana():
	if True:
		action = raw_input(colors.W+" ktn "+colors.G+"~"+colors.W+" "+colors.W)
		if action == "show modules" or action == "showm":
			print """ 
  ,--.-,  ____________________________________________________
 /==/  /  \033[4m| Module               | Description                """+colors.W+"""| 
 |==|, | """+colors.R+"""@"""+colors.W+"""|"""+colors.O+"""web/httpbt"""+colors.W+"""\t\t | """+colors.C+"""Brute force to HTTP 401"""+colors.W
			line("web/formbt","Brute force to form-based")
			line("web/cpfinder","Admin panel finder")
			line("web/joomscan","Scanner vul's cms joomla")
			line("web/dos","Denial of service web")
			line("web/whois","Who-is web")
			separator()
			line("net/arpspoof","ARP-Spoofing attack")
			line("net/arplook","ARP-Spoofing detector")
			line("net/lanlive","Host live's in my Network")
			separator()
			line("eng/gdreport","Getting information with web")
			line("eng/mailboom","E-mail boombing")
			line("eng/facebrok","facebook phishing plataform")
			separator()
			line("fle/brutezip","Brute force to zip files")
			line("fle/bruterar","Brute force to rar files")
			separator()
			line("clt/ftp","Console ftp client")
			line("clt/sql","Console sql client")
			line("clt/pop3","Console pop3 client")
			separator()
			line("ser/sql","Start sql server")
			line("ser/apache","Start http server")
			line("ser/ssh","Start ssh server")
			separator()
			line("bt/ftp","Brute force to ftp")
			line("bt/sql","Brute force to sql")
			line("bt/ssh","Brute force to ssh")
			line("bt/pop3","Brute force to pop3")
			separator()
			line("fz/ftp","Fuzzer to ftp")
			separator()
			line("wifi/wpabtf","Brute force to wpa encriptation")
			line("wifi/dos","Denial of service wifi")
			separator()
			line("mc/tlogin","Test of credentials")
			line("mc/gendic","Generator dictionary")
			separator()
			print """ /==/, / 
 `--`-' \n""" 
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
			if action[4:17] == "eng/gdreport":
				GetDataReport.getdatareport(0)
			if action[4:17] == "fle/brutezip":
				BruteZIP.btzip(0)
			if action[4:17] == "fle/bruterar":
				BruteRAR.btrar(0)
			if action[4:11] == "clt/ftp":
				ClientFTP.cftp(0)
			if action[4:10] == "bt/ftp":
				BruteForceFTP.btftp(0)
			if action[4:17] == "wifi/hwifipwd":
				WifiDetecter.hackerwifipwd()
			if action[4:10] == "bt/ssh":
				BruteForceSSH.btssh(0)	
			if action[4:11] == "clt/sql":
				ClientMYSQL.cmysql(0)	
			if action[4:10] == "bt/sql":
				BruteForceSQL.btsql(0)		
			if action[4:11] == "bt/pop3":
				BruteForcePOP3.btpop3(0)
			if action[4:12] == "clt/pop3":
				ClientPOP3.cpop3(0)
			if action[4:13] == "mc/tlogin":
				TLogin.tlogin()
			if action[4:10] == "fz/ftp":
				FuzzerFTP.fftp()
			if action[4:17] == "web/joomscan":
				Joomscan.xjoomla(0)
			if action[4:14] == "ser/sql":
				services.services('mysql')
			if action[4:14] == "ser/ssh":
				services.services('ssh')
			if action[4:18] == "ser/apache":
				services.services('apache2')
			if action[4:15] == "wifi/wpabtf":
				WpaBTF.wpabtf(0)
			if action[4:12] == "wifi/dos":
				Wifi_DDOS.ddos(0)
			if action[4:13] == "mc/gendic":
				GenDic.Gendic(0)
			if action[4:13] == "web/whois":
				Whois.wuis(0)
			if action[4:15] == "net/lanlive":
				LANScanner.hostl(0)
			if action[4:16] == "eng/facebrok":
				facebrok.facebrok(0)
			if action[4:16] == "net/arpspoof":
				ARPPoisoning.arpp(0)
			if action[4:16] == "eng/mailboom":
				smtpBombing.smtpbombing(0)
			else:
				katana()
		elif action == "exit" or action == "x":
			print colors.C+"   GooD"+colors.W+" bye."
			exit()
		elif action == "help" or action == "h":
			help.help()
			katana()
		elif action == "update" or action == "u":
			updatekatana.update()
		elif action == "clear" or action == "c":
			subprocess.call('clear', shell=True)
			katana()			
		else:
			print " ["+colors.R+"!"+colors.W+"] Invalid parameter use show 'help' for more information"+colors.W
			katana()
katana()
