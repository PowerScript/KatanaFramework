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
options, remainder = getopt.getopt(sys.argv[1:], 'm:')
for option, arg in options:
		if option   == '-m':
			m=arg

print ""
print " "+colors.B+"*"+colors.W+" "
print "	"+colors.R+"-->"+colors.W+""+colors.B+"*"+colors.W+"  _______?___________________________________ "
print "	"+colors.B+"*"+colors.W+""+colors.R+"-->"+colors.W+""+colors.R+"*"+colors.W+"{_| | | | I##########  "+colors.R+"KTF"+colors.W+" Run   ##########/ "
print "   "+colors.B+"*"+colors.W+""+colors.R+"-->"+colors.W+""+colors.R+"*"+colors.W+"       ^ ^ ^ ^              "+info.version
print ""+colors.B+"*"+colors.W+"  "+colors.R+"*"+colors.W
print " ktn | Checking Module"
try:
	if True:
		if True:
			if m == "web/httpbt":
				print " ktn | Running"
				BruteForceHTTP.httpbt(0)
			if m == "web/cpfinder":
				print " ktn | Running"
				AdminFinder.adminfinder(0)
			if m == "web/formbt":
				print " ktn | Running"
				BruteForceFormBase.httpformbasebruteforce(0)
			if m == "net/arplook":
				print " ktn | Running"
				ARPLooking.arplook(0)
			if m == "seng/gdreport":
				print " ktn | Running"
				GetDataReport.getdatareport(0)
			if m == "file/brutezip":
				print " ktn | Running"
				BruteZIP.btzip(0)
			if m == "file/bruterar":
				print " ktn | Running"
				BruteRAR.btRAR()
			if m == "clt/ftp":
				print " ktn | Running"
				ClientFTP.cftp(0)
			if m == "bt/ftp":
				print " ktn | Running"
				BruteForceFTP.btftp(0)
			if m == "wifi/hwifipwd":
				print " ktn | Running"
				WifiDetecter.hackerwifipwd()
			if m == "bt/ssh":
				print " ktn | Running"
				BruteForceSSH.btssh(0)	
			if m == "clt/sql":
				print " ktn | Running"
				ClientMYSQL.cmysql(0)	
			if m == "bt/sql":
				print " ktn | Running"
				BruteForceSQL.btsql(0)		
			if m == "bt/pop3":
				print " ktn | Running"
				BruteForcePOP3.btpop3(0)
			if m == "clt/pop3":
				print " ktn | Running"
				ClientPOP3.cpop3(0)
			if m == "mc/tlogin":
				print " ktn | Running"
				TLogin.tlogin(0)
			if m == "fz/ftp":
				print " ktn | Running"
				FuzzerFTP.fftp(0)
			if m == "web/joomscan":
				print " ktn | Running"
				Joomscan.xjoomla(0)
			if m == "server/sql":
				print " ktn | Running"
				services.services('mysql')
			if m == "server/ssh":
				print " ktn | Running"
				services.services('ssh')
			if m == "server/apache":
				print " ktn | Running"
				services.services('apache2')
			if m == "wifi/wpabtf":
				print " ktn | Running"
				WpaBTF.btwpa(0)
			if m == "wifi/ddos":
				print " ktn | Running"
				Wifi_DDOS.ddos(0)
			if m == "mc/gendic":
				print " ktn | Running"
				GenDic.Gendic(0)
			if m == "web/whois":
				print " ktn | Running"
				Whois.wuis(0)
			else:
				print " ["+colors.O+"!"+colors.W+"] Module not found"
				print ""
				print " ["+colors.O+"!"+colors.W+"] Use msfkatana -m Module"
				print " ["+colors.B+"*"+colors.W+"] ex: msfkatana -m wifi/ddos"
				exit()
except:
	print ""
exit()