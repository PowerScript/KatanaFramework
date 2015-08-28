#
# Katana framework 
# @Katana Linker
#

from scripts import *
import getopt
import sys

t=""
p=""
f=""
u=""
p=""
m=""
s=""
h=""
options, remainder = getopt.getopt(sys.argv[1:], 't:p:f:u:ps:m:s:h')
for option, arg in options:
		if option   == '-t':
			t=arg
		if option 	== '-p':
			p=arg
		if option   == '-f':
			f=arg
		if option 	== '-u':
			u=arg
		if option   == '-ps':
			ps=arg
		if option 	== '-m':
			m=arg
		if option 	== '-s':
			s=arg
		if option 	== '-h':
			h=1
if s == "web/whois":
	if h==1:
		print "\n web/whois: who-is domain name service, information juice of domains.\n"
		print " -t [target]  127.0.0.1"
		print " -p [port]    80"
		print ""
	else:
		Whois.run(t,p)
elif s == "web/joomscan":
	Joomscan.run(t,p)
elif s == "web/cpfinder":
	AdminFinder.run(t,p,"core/db/commons-dir-admin.tbl")
#BruteForceFormBase.run("127.0.0.1","80","/admin/login.php","core/db/user.dicc","core/db/pass.dicc","username","password","POST","no")
#BruteForceHTTP.run("127.0.0.1","80","/admin/","core/db/user.dicc","core/db/pass.dicc")
#GetDataReport.run("googles.com","false")
#BruteForcePOP3.run("127.0.0.1","110","admin@127.0.0.1","core/db/pass.dicc")
#BruteForceFTP.run("127.0.0.1","21","admin","core/db/pass.dicc")
#ClientFTP.run("127.0.0.1","80","anonymous","password")
#ClientMYSQL.run("127.0.0.1","3306","admin","admin")
#ClientPOP3.run("127.0.0.1","110","admin","admin")
#BruteForceSQL.run("127.0.0.1","3306","admin","admin")
#BruteForceSSH.run("127.0.0.1","22","admin","admin")
#BruteZIP.run("core/db/test.zip","core/db/pass.dicc")
#BruteRAR.run("core/db/test.rar","core/db/pass.dicc")
#WpaBTF.run("core/test/test.cap","E8:40:F2:32:37:FD","core/db/pass.dicc")
#LANScanner.run("192.168.1.0")
#facebrok.run("root","toor","db_fbrok","admin","admin")
#ARPPoisoning.run("192.168.1.0","192.168.1.254","wlan0")