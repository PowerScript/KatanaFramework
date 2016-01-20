#!/usr/bin/env python
### Katana Framework Linker
### you can redistribute it and/or modify
### it under the terms of the GNU General Public License as published by
### the Free Software Foundation, either version 3 of the License, or
### (at your option) any later version. 

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

elif m == "clt/ftp":
	if h==1:
		print "\n python "+KTFLINKER+" -m clt/ftp -t target.com -p 21 -u root -ps toor\n"
		print " -t [target]         IP or DNS target "
		print " -p [port]           Port target"
		print " -u [username]       Username"
		print " -ps [password]      Password"
		CLASS_LINKER.space()
	else:
		ClientFTP.run(target=t,port=p,username=u,password=ps)
elif m == "clt/sql":
	if h==1:
		print "\n python "+KTFLINKER+" -m clt/sql -t target.com -p 3306 -u root -ps toor\n"
		print " -t [target]         IP or DNS target "
		print " -p [port]           Port target"
		print " -u [username]       Username"
		print " -ps [password]      Password"
		CLASS_LINKER.space()
	else:
		ClientMYSQL.run(target=t,port=p,username=u,password=ps)
elif m == "clt/pop3":
	if h==1:
		print "\n python "+KTFLINKER+" -m clt/pop -t target.com -p 110 -u root@target.com -ps toor\n"
		print " -t [target]         IP or DNS target "
		print " -p [port]           Port target"
		print " -u [username]       Username"
		print " -ps [password]      Password"
		CLASS_LINKER.space()
	else:
		ClientPOP3.run(target=t,port=p,username=u,password=ps)
elif m == "btf/sql":
	if h==1:
		print "\n python "+KTFLINKER+" -m btf/sql -t target.com -p 3306 -u root -d core/db/pass.dicc\n"
		print " -t [target]         IP or DNS target "
		print " -p [port]           Port target"
		print " -u [username]       Username"
		print " -d [dictionary]     Password Wordlist"
		CLASS_LINKER.space()
	else:
		BruteForceSQL.run(target=t,port=p,username=u,dictionary=d)
elif m == "btf/ssh":
	if h==1:
		print "\n python "+KTFLINKER+" -m btf/ssh -t target.com -p 22 -u root -d core/db/pass.dicc\n"
		print " -t [target]         IP or DNS target "
		print " -p [port]           Port target"
		print " -u [username]       Username"
		print " -d [dictionary]     Password Wordlist"
		CLASS_LINKER.space()
	else:
		BruteForceSSH.run(target=t,port=p,username=u,dictionary=d)
elif m == "net/lanlive":
	if h==1:
		print "\n python "+KTFLINKER+" -m net/lanlive -t 192.168.0.1\n"
		print " -t [target]            Ip address of network to scan"
		CLASS_LINKER.space()
	else:
		LANScanner.run(nets=t, types="null")
elif m == "net/portscan":
	if h==1:
		print "\n python "+KTFLINKER+" -m net/portscan -t 192.168.0.1 -p [t-0 . t-9]\n"
		print " -t [target]         IP or DNS target "
		print " -p [profile]        type of scan [t-0,t-1,t-2,...,t-9]"
		CLASS_LINKER.space()
	else:
		PortScanner.run(target=t, types=p)
elif m == "set/facebrok":
	if h==1:
		print "\n python "+KTFLINKER+" -m set/facebrok -u root -p toor -c db_fbrok -x admin -z admin\n"
		print " -u [username]         username Mysql"
		print " -p [password]         password Mysql"
		print " -c [database]         database Mysql"
		print " -x [username]         username Panel"
		print " -z [password]         password Panel"
		CLASS_LINKER.space()
	else:
		facebrok.run(username=u,password=0,database=c,userp=x,passp=z)

#ARPPoisoning.run("192.168.1.0","192.168.1.254","wlan0")
#BruteZIP.run("core/db/test.zip","core/db/pass.dicc")
#BruteRAR.run("core/db/test.rar","core/db/pass.dicc")
#WpaBTF.run("core/test/test.cap","E8:40:F2:32:37:FD","core/db/pass.dicc")

elif m == "":
	print ""
	print "  "+KTFLINKER+"[py]"
	print ""
	print "  Katana framework Linker> "
	print "  Sub-tool for call module pass parameters diretly. "
	print "  each module contain a function (run fuction) that "
	print "  received this parameters for execution of module. "
	print ""
	print " Example:"
	print ""
	print "  ktf.linker -m category/module -h host -p port -d data"
	print ""
	print " For more information visit https://github.com/redtoor/katana/doc "
	print ""

