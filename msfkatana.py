# katana
# MFS

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
print "	"+colors.B+"*"+colors.W+""+colors.R+"-->"+colors.W+""+colors.R+"*"+colors.W+"{_| | | | I########## "+colors.R+"MSF"+colors.W+" Katana ##########/ "
print "   "+colors.B+"*"+colors.W+""+colors.R+"-->"+colors.W+""+colors.R+"*"+colors.W+"       ^ ^ ^ ^              "+info.version
print ""+colors.B+"*"+colors.W+"  "+colors.R+"*"+colors.W
print "     ["+colors.O+"!"+colors.W+"] Checking Module"
try:
	if True:
		if True:
			if m == "web/httpbt":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				BruteForceHTTP.httpbt()
			if m == "web/cpfinder":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				AdminFinder.adminfinder()
			if m == "web/formbt":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				BruteForceFormBase.httpformbasebruteforce()
			if m == "net/arplook":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				ARPLooking.arplook()
			if m == "seng/gdreport":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				GetDataReport.getdatareport()
			if m == "file/brutezip":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				BruteZIP.btzip()
			if m == "file/bruterar":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				BruteRAR.btRAR()
			if m == "clt/ftp":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				ClientFTP.cftp()
			if m == "bt/ftp":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				BruteForceFTP.btftp()
			if m == "wifi/hwifipwd":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				WifiDetecter.hackerwifipwd()
			if m == "bt/ssh":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				BruteForceSSH.btssh()	
			if m == "clt/sql":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				ClientMYSQL.cmysql()	
			if m == "bt/sql":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				BruteForceSQL.btsql()		
			if m == "bt/pop3":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				BruteForcePOP3.btpop3()
			if m == "clt/pop3":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				ClientPOP3.cpop3()
			if m == "mc/tlogin":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				TLogin.tlogin()
			if m == "fz/ftp":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				FuzzerFTP.fftp()
			if m == "web/joomscan":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				Joomscan.xjoomla()
			if m == "server/sql":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				services.services('mysql')
			if m == "server/ssh":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				services.services('ssh')
			if m == "server/apache":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				services.services('apache2')
			if m == "wifi/wpabtf":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				WpaBTF.wpabtf()
			if m == "wifi/ddos":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				Wifi_DDOS.ddos()
			if m == "mc/gendic":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				GenDic.Gendic()
			if m == "web/whois":
				print "     ["+colors.G+"+"+colors.W+"] Running"
				Whois.wuis()
			else:
				print "     ["+colors.O+"!"+colors.W+"] Module not found"
				print ""
				print "     ["+colors.O+"!"+colors.W+"] Use msfkatana -m Module"
				print "     ["+colors.B+"*"+colors.W+"] ex: msfkatana -m wifi/ddos"

				exit()
except:
	print ""
exit()




