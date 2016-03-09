#!/usr/bin/env python
### Katana Framework Linker
### you can redistribute it and/or modify
### it under the terms of the GNU General Public License as published by
### the Free Software Foundation, either version 3 of the License, or
### (at your option) any later version. 

from core.Setting import *
from core.design import *
from scripts import *
from core import info
import argparse

CLASS_LINKER=DESIGN()

if __name__=="__main__":
	parser = argparse.ArgumentParser(description='ktf.linker:'+info.version+info.build)
	parser.add_argument("-m", "--module", help="Module")
	parser.add_argument("-t", "--target", help="Target")        
	parser.add_argument("-p", "--port", help="Port")            
	parser.add_argument("-f", "--file", help="File")            
	parser.add_argument("-u", "--user", help="Username")
	parser.add_argument("-ps","--password", help="Password")
	parser.add_argument("-x", "--userb", help="Usernameb")
	parser.add_argument("-z", "--passwordb", help="Passwordb")
	parser.add_argument("-d", "--dictionary", help="Dictionary")
	parser.add_argument("-c", "--condition", help="Condition")
	parser.add_argument("-i", "--interface", help="interface")
	parser.add_argument("-v", "--valueform", help="Form Input")
	parser.add_argument("-o", "--output", help="output")
	parser.add_argument("-g", "--gateway", help="Gateway")
	parser.add_argument("-l", "--length", help="Length")
	parser.add_argument("-q", "--query", help="Query")
	args = parser.parse_args()
	t=args.target
	p=args.port
	f=args.file
	u=args.user
	ps=args.password
	m=args.module
	d=args.dictionary
	c=args.condition
	z=args.passwordb
	x=args.userb
	i=args.interface
	v=args.valueform
	o=args.output
	g=args.gateway
	l=args.length
	q=args.query

CLASS_LINKER.linker(info.version, info.build)
if m == "web/whois":      Whois.run(target=t, port=p)
elif m == "web/joomscan": Joomscan.run(target=t, port=p)
elif m == "web/cpfinder": AdminFinder.run(target=t, port=p, dictionary=f)
elif m == "web/formbt":   BruteForceFormBase.run(target=t, port=p, patch=f, para1=x, valor=v, para2=z, dictionary=d, method=q, condition=c)
elif m == "web/httpbt":   BruteForceHTTP.run(target=t, port=p, patch=f, username=u, dictionary=d)
elif m == "web/dos":      dosweb.run(target=t, port=p)
elif m == "web/lfd-con":  LFDconsole.run(target=t, files=f, port=p)
elif m == "net/lanlive":  LANScanner.run(nets=t, types="null")
elif m == "net/portscan": PortScanner.run(target=t, types=p)
elif m == "net/arpspoof": ARPPoisoning.run(target=t, source=g, interface=i)
elif m == "set/facebrok": facebrok.run(username=u,password=ps,database="facebrok_db",userp=x,passp=z)
elif m == "set/gdreport": GetDataReport.run(target=t, js=q)
elif m == "clt/ftp":      ClientFTP.run(target=t,port=p,username=u,password=ps)
elif m == "clt/sql":      ClientMYSQL.run(target=t,port=p,username=u,password=ps)
elif m == "clt/pop":      ClientPOP3.run(target=t,port=p,username=u,password=ps)
elif m == "fbt/sql":      BruteForceSQL.run(target=t,port=p,username=u,dictionary=d)
elif m == "fbt/ssh":      BruteForceSSH.run(target=t,port=p,username=u,dictionary=d)
elif m == "fbt/ftp":      BruteForceFTP.run(target=t, port=p, username=u, dictionary=d)
elif m == "fbt/pop3":     BruteForcePOP3.run(target=t, port=p, username=u, dictionary=d)
elif m == "fle/bruterar": BruteRAR.run(files=f ,dictionary=d)
elif m == "fle/brutezip": BruteZIP.run(files=f ,dictionary=d)
elif m == "mc/tlogin":    TLogin.run(target=t, username=u, password=ps)
elif m == "mc/gendic":    GenDic.run(dictionary=o, length=l, types=t)

