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
import xml.etree.ElementTree as ET
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
tree = ET.parse('core/modules.xml')
root = tree.getroot()

print """
	 .-.--.  
	 \  \==\ """+colors.O+"""Katana Framework"""+colors.W+"""
	 /- /==/ 
	/' /==/  """+colors.G+"""~"""+colors.R+"""Core"""+colors.W+""" = """+info.version+""", Build: """+info.build+"""
	|,|==|   """+colors.G+"""~"""+colors.R+"""Theme"""+colors.W+""" = """+info.tema+"""
	\  \==\  """+colors.G+"""~"""+colors.R+"""Modules"""+colors.W+""" = """+colors.G+""""""+info.modules+""""""+colors.W+"""
	 \ ,\==\ """+colors.G+"""~"""+colors.R+"""Date"""+colors.W+""" = """+info.date+"""
	 / -/==/ """+colors.B+""" Github: redtoor/Katana"""+colors.W+"""
	 `-'--'  
	  """

def line(module, description):
	print  colors.P+""" |\033[4m"""+colors.R+"""=="""+colors.W+"""|::|  """+module+"\t\t"+description
def katana():
	if True:
		action = raw_input(colors.W+" ktf >")
		if action == "show modules" or action == "showm":
			print """ 
  ,--.-,  
 /BY/  /  \033[1m Module                   Description                """+colors.W+"""
 """+colors.P+"""|\033[4m"""+colors.R+"""=="""+colors.W+"""|::|  web/httpbt"""+colors.W+"""\t\tBrute force to HTTP 401"""+colors.W
 			for module in root.findall('module'):
				name = module.get('name')
				description = module.find('description').text
				line(name,description)
			print """ /RT/, / 
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
				TLogin.tlogin(0)
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
			if action[4:8] == "mc/i":
				Iandl.iandi()
			if action[4:11] == "web/dos":
				dosweb.dosweb(0)
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