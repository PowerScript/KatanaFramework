#
# Katana framework 
# @Katana Run
#

from scripts import *
from core import colors
from core import info
import getopt
import sys

m=""
h=""
options, remainder = getopt.getopt(sys.argv[1:], 'm:h')
for option, arg in options:
		if option   == '-m':
			m=arg
		if option   == '-h':
			h=1
print """
		   __   __  ___            
		  / /__/ /_/ _/"""+colors.R+"""_____ _____      """+colors.W+"""
		 /  '_/ __/ _/"""+colors.R+"""_ __/ // / _ \\   """+colors.W+"""
		/_/\_\\\\_/__/ """+colors.R+"""/_/  \_,_/_//_/  """+colors.W+"""
		Core:"""+info.version+"""
                           
"""

if h!=1:
	print " ktn | Checking Module"
try:
	if True:
		if True:
			if m == "web/httpbt":
				print " ktn | Running"
				BruteForceHTTP.httpbt(0)
				exit()
			if m == "web/cpfinder":
				print " ktn | Running"
				AdminFinder.adminfinder(0)
				exit()
			if m == "web/formbt":
				print " ktn | Running"
				BruteForceFormBase.httpformbasebruteforce(0)
				exit()
			if m == "net/arplook":
				print " ktn | Running"
				ARPLooking.arplook(0)
				exit()
			if m == "eng/gdreport":
				print " ktn | Running"
				GetDataReport.getdatareport(0)
				exit()
			if m == "fle/brutezip":
				print " ktn | Running"
				BruteZIP.btzip(0)
				exit()
			if m == "fle/bruterar":
				print " ktn | Running"
				BruteRAR.btrar(0)
				exit()
			if m == "clt/ftp":
				print " ktn | Running"
				ClientFTP.cftp(0)
				exit()
			if m == "bt/ftp":
				print " ktn | Running"
				BruteForceFTP.btftp(0)
				exit()
			if m == "wifi/hwifipwd":
				print " ktn | Running"
				WifiDetecter.hackerwifipwd()
				exit()
			if m == "bt/ssh":
				print " ktn | Running"
				BruteForceSSH.btssh(0)	
				exit()
			if m == "clt/sql":
				print " ktn | Running"
				ClientMYSQL.cmysql(0)	
				exit()
			if m == "bt/sql":
				print " ktn | Running"
				BruteForceSQL.btsql(0)
				exit()		
			if m == "bt/pop3":
				print " ktn | Running"
				BruteForcePOP3.btpop3(0)
				exit()
			if m == "clt/pop3":
				print " ktn | Running"
				ClientPOP3.cpop3(0)
				exit()
			if m == "mc/tlogin":
				print " ktn | Running"
				TLogin.tlogin(0)
				exit()
			if m == "fz/ftp":
				print " ktn | Running"
				FuzzerFTP.fftp(0)
				exit()
			if m == "web/joomscan":
				print " ktn | Running"
				Joomscan.xjoomla(0)
				exit()
			if m == "ser/sql":
				print " ktn | Running"
				services.services('mysql')
				exit()
			if m == "ser/ssh":
				print " ktn | Running"
				services.services('ssh')
				exit()
			if m == "ser/apache":
				print " ktn | Running"
				services.services('apache2')
				exit()
			if m == "wifi/wpabtf":
				print " ktn | Running"
				WpaBTF.btwpa(0)
				exit()
			if m == "wifi/dos":
				print " ktn | Running"
				Wifi_DDOS.ddos(0)
				exit()
			if m == "mc/gendic":
				print " ktn | Running"
				GenDic.Gendic(0)
				exit()
			if m == "web/whois":
				print " ktn | Running"
				Whois.wuis(0)
				exit()
			if m == "net/lanlive":
				print " ktn | Running"
				LANScanner.hostl(0)
				exit()
			if m == "eng/facebrok":
				print " ktn | Running"
				facebrok.facebrok(0)
				exit()
			if m == "net/arpspoof":
				print " ktn | Running"
				ARPPoisoning.arpp(0)
				exit()
			if m == "eng/mailboom":
				print " ktn | Running"
				smtpBombing.smtpbombing(0)
				exit()
			if m == "mc/i":
				Iandl.iandi()
				exit()
			if m == "for/imagen":
				forenseIMAGE.exiftool(0)
				exit()
			if h == 1:
				print " ktfrun"
				print ""
				print " Katana framework run, it's a sub-tool for use modules fastly"
				print " with line command."
				print ""
				print " Example:"
				print ""
				print " ktfrun -m category/module"
				print " ktfrun -m mc/gendic"
				print ""
			else:
				print " ["+colors.O+"!"+colors.W+"] Module not found"
				print ""
				print " ["+colors.O+"!"+colors.W+"] Use ktfkatana -m Module"
				print " ["+colors.B+"*"+colors.W+"] ex: ktfkatana -m wifi/dos"
				print " ["+colors.B+"*"+colors.W+"] ex: ktfkatana -h"
				exit()
except:
	print ""
exit()
