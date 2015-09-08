#
# Katana framework 
# @Katana Linker
#

import getopt
import sys
from scripts import *
from core import colors
from core import info
from core.design import *
CLASS_LINKER=DESIGN()

t=""
p=""
f=""
u=""
ps=""
m=""
s=""
h=""
v=""
z=""
x=""
d=""
c=""
q=""

options, remainder = getopt.getopt(sys.argv[1:], 'd:t:p:f:u:ps:m:s:c:z:x:v:q:h')
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
		if option   == '-d':
			d=arg
		if option 	== '-h':
			h=1
		if option   == '-c':
			c=arg
		if option   == '-z':
			z=arg
		if option   == '-x':
			x=arg
		if option   == '-v':
			v=arg
		if option   == '-q':
			q=arg

CLASS_LINKER.linker(info.version)

if m == "web/whois":
	if h==1:
		print "\n python ktflinker.py -m web/whois -t target.com -p 80\n"
		print " -t [target]  127.0.0.1"
		print " -p [port]    80"
		print ""
	else:
		Whois.run(target=t, port=p)
elif m == "web/joomscan":
	if h==1:
		print "\n python ktflinker.py -m web/joomscan -t target.com -p 80\n"
		print " -t [target]  127.0.0.1"
		print " -p [port]    80"
		print ""
	else:
		Joomscan.run(target=t, port=p)
elif m == "web/cpfinder":
	if h==1:
		if f == "":
			f="core/db/commons-dir-admin.tbl"
		print "\n python ktflinker.py -m web/cpfinder -t target.com -p 80 -f core/db/commons-dir-admin.tbl\n"
		print " -t [target]  target.com"
		print " -p [port]    80"
		print " -f [file]    'core/db/commons-dir-admin.tbl'"
		print ""
	else:
		AdminFinder.run(target=t, port=p, dictionary=f)
elif m == "web/formbt":
	if h==1:
		print "\n python ktflinker.py -m web/formbt -t target.com -p 80 -f /admin/login.php -x username -v root -z password -d core/db/pass.dicc -m POST -c Wrong\n"
		print " -t [target]         target.com"
		print " -p [port]           80"
		print " -f [file]           /admin/login.php"
		print " -x [parameter one] username"
		print " -v [value one]      root"
		print " -z [parameter two] password"
		print " -d [ditionary]      core/db/pass.dicc"
		print " -q [method]         POST/GET"
		print " -c [condition]      Wrong"		
		print ""
	else:		
		BruteForceFormBase.run(target=t, port=p, patch=f, para1=x, valor=v, para2=z, dictionary=d, method=q, condition=c)
elif m == "web/httpbt":
	if h==1:
		print "\n python ktflinker.py -m web/httpbt -t target.com -p 80 -f '/cpanel/' -u username -d core/db/pass.dicc\n"
		print " -t [target]         target.com"
		print " -p [port]           80"
		print " -f [folder]         /cpanel/"
		print " -u [username]       admin"
		print " -d [ditionary]      core/db/pass.dicc"
		print ""		
	else:
		BruteForceHTTP.run(target=t, port=p, patch=f, username=u, dictionary=d)
elif m == "web/dos":
	if h==1:
		print "\n python ktflinker.py -m web/dos -t target.com -p 80\n"
		print " -t [target]  127.0.0.1"
		print " -p [port]    80"
		print ""	
	else:
		dosweb.run(target=t, port=p)
elif m == "bt/pop3":
	if h==1:
		print "\n python ktflinker.py -m bt/pop3 -t target.com -p 110 -u root@localhost -d core/db/pass.dicc\n"
		print " -t [target]  127.0.0.1"
		print " -p [port]    110"
		print " -d [ditionary]      core/db/pass.dicc"
		print ""
	else:
		BruteForcePOP3.run(target=t, port=p, username=u, dictionary=d)
elif m == "bt/ftp":
	if h==1:
		print "\n python ktflinker.py -m bt/ftp -t target.com -p 21 -u root -d core/db/pass.dicc\n"
		print " -t [target]  127.0.0.1"
		print " -p [port]    21"
		print " -d [ditionary]      core/db/pass.dicc"
		print ""
	else:
		BruteForceFTP.run(target=t, port=p, username=u, dictionary=d)

#elif m == "eng/gdreport"
#GetDataReport.run("google.com","false")
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


