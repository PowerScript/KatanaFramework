#
# Katana framework 
# @Katana Linker
#

from core.Setting import *
from core.design import *
from scripts import *
from core import colors
from core import info
import getopt
import sys
CLASS_LINKER=DESIGN()
options, remainder = getopt.getopt(sys.argv[1:], 'd:t:p:f:u:ps:m:s:c:z:x:v:q:h')
for option, arg in options:
		if option     == '-t':
			t=arg
		if option     == '-p':
			p=arg
		if option     == '-f':
			f=arg
		if option     == '-u':
			u=arg
		if option     == '-ps':
			ps=arg
		if option     == '-m':
			m=arg
		if option     == '-s':
			s=arg
		if option     == '-d':
			d=arg
		if option     == '-h':
			h=1
		if option     == '-c':
			c=arg
		if option     == '-z':
			z=arg
		if option     == '-x':
			x=arg
		if option     == '-v':
			v=arg
		if option     == '-q':
			q=arg

CLASS_LINKER.linker(info.version, info.build)

if m == "web/whois":
	if h==1:
		print "\n python "+KTFLINKER+" -m web/whois -t target.com -p 80\n"
		print " -t [target]  IP or DNS target "
		print " -p [port]    Port target"
		CLASS_LINKER.space()
	else:
		Whois.run(target=t, port=p)
elif m == "web/joomscan":
	if h==1:
		print "\n python "+KTFLINKER+" -m web/joomscan -t target.com -p 80\n"
		print " -t [target]  IP or DNS target "
		print " -p [port]    Port target"
		CLASS_LINKER.space()
	else:
		Joomscan.run(target=t, port=p)
elif m == "web/cpfinder":
	if h==1:
		print "\n python "+KTFLINKER+" -m web/cpfinder -t target.com -p 80 -f core/db/commons-dir-admin.tbl\n"
		print " -t [target]  IP or DNS target "
		print " -p [port]    Port target"
		print " -f [file]    Tables commons admin panel file"
		CLASS_LINKER.space()
	else:
		AdminFinder.run(target=t, port=p, dictionary=f)
elif m == "web/formbt":
	if h==1:
		print "\n python "+KTFLINKER+" -m web/formbt -t target.com -p 80 -f /KatanaLAB/run.php -x username -v administrator -z password -d core/db/pass.dicc -q POST -c Wrong\n"
		print " -t [target]         IP or DNS target "
		print " -p [port]           Port target"
		print " -f [file]           File for petition"
		print " -x [parameter one]  Parameter name form/input"
		print " -v [value one]      Input value"
		print " -z [parameter two]  Parameter name form/input"
		print " -d [ditionary]      Dictionary"
		print " -q [method]         POST/GET Method"
		print " -c [condition]      Condition [IF != FAILED LOGGIN]"		
		CLASS_LINKER.space()
	else:		
		BruteForceFormBase.run(target=t, port=p, patch=f, para1=x, valor=v, para2=z, dictionary=d, method=q, condition=c)
elif m == "web/httpbt":
	if h==1:
		print "\n python "+KTFLINKER+" -m web/httpbt -t target.com -p 80 -f '/cpanel/' -u username -d core/db/pass.dicc\n"
		print " -t [target]         IP or DNS target "
		print " -p [port]           Port target"
		print " -f [folder]         Folder"
		print " -u [username]       Username"
		print " -d [ditionary]      Dictionary"
		CLASS_LINKER.space()		
	else:
		BruteForceHTTP.run(target=t, port=p, patch=f, username=u, dictionary=d)
elif m == "web/dos":
	if h==1:
		print "\n python "+KTFLINKER+" -m web/dos -t target.com -p 80\n"
		print " -t [target]         IP or DNS target "
		print " -p [port]           Port target"
		CLASS_LINKER.space()	
	else:
		dosweb.run(target=t, port=p)
elif m == "bt/pop3":
	if h==1:
		print "\n python "+KTFLINKER+" -m bt/pop3 -t target.com -p 110 -u root@localhost -d core/db/pass.dicc\n"
		print " -t [target]         IP or DNS target "
		print " -p [port]           Port target"
		print " -u [user]           E-mail"
		print " -d [ditionary]      Dictionary"
		CLASS_LINKER.space()
	else:
		BruteForcePOP3.run(target=t, port=p, username=u, dictionary=d)
elif m == "bt/ftp":
	if h==1:
		print "\n python "+KTFLINKER+" -m bt/ftp -t target.com -p 21 -u root -d core/db/pass.dicc\n"
		print " -t [target]         IP or DNS target "
		print " -p [port]           Port target"
		print " -u [user]           User"
		print " -d [ditionary]      Dictionary"
		CLASS_LINKER.space()
	else:
		BruteForceFTP.run(target=t, port=p, username=u, dictionary=d)
elif m == "set/gdreport":
	if h==1:
		print "\n python "+KTFLINKER+" -m set/gdreport -t youtube.com/?v=W3kr3w -q false\n"
		print " -t [URL]            URL Redirect"
		print " -q [Javascript]     TRUE/FALSE enable Javascript"
		CLASS_LINKER.space()
	else:
		GetDataReport.run(target=t, js=q)
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

elif m == "":
	print ""
	print "  "+KTFLINKER+"[py]"
	print ""
	print "  Katana framework Linker> "
	print "  Sub-tool for call module pass parameters diretly. "
	print "  each module contain a function (run fuction) that "
	print "  received this parameters for execution of module "
	print ""
	print " Example:"
	print ""
	print "  ktf.linker -m category/module -h host -p port -d data"
	print ""
	print " For more information visit https://github.com/redtoor/katana "
	print ""

