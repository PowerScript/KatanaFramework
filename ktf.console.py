#!/usr/bin/env python
### Katana Framework 
### you can redistribute it and/or modify
### it under the terms of the GNU General Public License as published by
### the Free Software Foundation, either version 3 of the License, or
### (at your option) any later version. 

from scripts import *
from core import info
from core import help
from core import colors
from core import updatekatana
from core import splash
from core import Errors
import xml.etree.ElementTree as ET
import sys 

tree = ET.parse('core/modules.xml')
root = tree.getroot()

def Line(module, description):
	print  colors.W+""" |\033[4m"""+colors.R+"""=="""+colors.W+"""|::|  """+module+"\t\t"+description

def katanaFrameworkMainFunction():
	try:
		action = raw_input(colors.W+" \033[1mktf\033[40m>"+colors.W)
		if action == "show modules" or action == "showm":
			print """ 
  ,--.-,  
 /BY/  /  \033[1m Module                   Description                """+colors.W+"""
 """+colors.W+"""|\033[4m"""+colors.R+"""=="""+colors.W+"""|::|  web/httpbt"""+colors.W+"""\t\tBrute force to HTTP 401"""+colors.W
 			for module in root.findall('module'):
				name = module.get('name')
				description = module.find('description').text
				Line(name,description)
			print """ /RT/, / 
 `--`-' \n""" 
			katanaFrameworkMainFunction()

		elif action[0:3] == "use":
			# WEB : Web Tools
			if action[4:14] == "web/httpbt":
				BruteForceHTTP.httpbt(0)
			if action[4:16] == "web/cpfinder":
				AdminFinder.adminfinder(0)
			if action[4:16] == "web/formbt":
				BruteForceFormBase.httpformbasebruteforce(0)
			if action[4:17] == "web/joomscan":
				Joomscan.xjoomla(0)
			if action[4:11] == "web/dos":
				dosweb.dosweb(0)
			if action[4:13] == "web/whois":
				Whois.wuis(0)
			if action[4:15] == "web/lfd-con":
				LFDconsole.LFDconsole(0)
			# NET : Networks Tools
			if action[4:16] == "net/arplook":
				ARPLooking.arplook(0)
			if action[4:15] == "net/lanlive":
				LANScanner.hostl(0)
			if action[4:16] == "net/arpspoof":
				ARPPoisoning.arpp(0)
			if action[4:16] == "net/portscan":
				PortScanner.PortScanner(0)
			# SET : Social Enginnering tools
			if action[4:17] == "set/gdreport":
				GetDataReport.getdatareport(0)
			if action[4:16] == "set/mailboom":
				smtpBombing.smtpbombing(0)
			if action[4:16] == "set/facebrok":
				facebrok.facebrok(0)
			# FLE : Files Tools
			if action[4:17] == "fle/brutezip":
				BruteZIP.btzip(0)
			if action[4:17] == "fle/bruterar":
				BruteRAR.btrar(0)
			# CLT : Clients Console Tools
			if action[4:11] == "clt/ftp":
				ClientFTP.cftp(0)
			if action[4:12] == "clt/pop3":
				ClientPOP3.cpop3(0)
			if action[4:11] == "clt/sql":
				ClientMYSQL.cmysql(0)
			# FBT : Force Brute Tools
			if action[4:11] == "fbt/ftp":
				BruteForceFTP.btftp(0)
			if action[4:11] == "fbt/ssh":
				BruteForceSSH.btssh(0)	
			if action[4:11] == "fbt/sql":
				BruteForceSQL.btsql(0)		
			if action[4:12] == "fbt/pop3":
				BruteForcePOP3.btpop3(0)
			# SER : Services Tools
			if action[4:14] == "ser/sql":
				services.services('mysql')
			if action[4:14] == "ser/ssh":
				services.services('ssh')
			if action[4:18] == "ser/apache":
				services.services('apache2')
			# WIFI : Wifi Tools
			if action[4:15] == "wifi/wpabtf":
				WpaBTF.wpabtf(0)
			if action[4:12] == "wifi/dos":
				Wifi_DDOS.ddos(0)
			# MC : MICCESELANIUS
			if action[4:13] == "mc/tlogin":
				TLogin.tlogin(0)
			if action[4:13] == "mc/gendic":
				GenDic.Gendic(0)
			if action[4:8] == "mc/i":
				Iandl.iandi()
			# FZZ : Fuzzing Tools
			if action[4:11] == "fzz/ftp":
				FuzzerFTP.fftp()
			# FOR : Forence Tools
			if action[4:13] == "for/image":
				forenseIMAGE.exiftool(0)
				exit()
			else:
				katanaFrameworkMainFunction()
		elif action == "exit" or action == "x":
			exit()
		elif action == "help" or action == "h":
			help.help()
			katanaFrameworkMainFunction()
		elif action == "update" or action == "u":
			updatekatana.update()
		elif action == "clear" or action == "c":
			subprocess.call('clear', shell=True)
			katanaFrameworkMainFunction()			
		else:
			print " ["+colors.R+"!"+colors.W+"] Invalid parameter use show 'help' for more information"+colors.W
			katanaFrameworkMainFunction()
	except:
		Errors.Errors(event=sys.exc_info()[0], info=False)

print """
	 .-.--.  
	 \  \==\ 
	 /- /==/ """+colors.W+"""\033[41m Katana Framework                    """+colors.W+"""
	/' /==/  """+colors.W+"""\033[1m Core    """+colors.W+""" = """+info.version+""", Build: """+info.build+"""
	|,|==|   """+colors.W+"""\033[1m Date    """+colors.W+""" = """+info.date+"""
	\  \==\  """+colors.W+"""\033[1m Theme   """+colors.W+""" = """+info.tema+"""
	 \ ,\==\ """+colors.W+"""\033[1m Modules """+colors.W+""" = """""+info.modules+""" Scritp's"""+colors.W+"""
	 / -/==/ """+colors.W+""" By RedToor"""+colors.W+"""
	 `-'--'  
	  """
	  
if __name__=="__main__":
	katanaFrameworkMainFunction()
