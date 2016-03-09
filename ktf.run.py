#!/usr/bin/env python
### Katana Framework Runner
### you can redistribute it and/or modify
### it under the terms of the GNU General Public License as published by
### the Free Software Foundation, either version 3 of the License, or
### (at your option) any later version. 

from core.design import *
from scripts import *
from core import colors
from core import info
import argparse
import time
import sys

CLASS_BANNER=DESIGN()
CLASS_BANNER.ktfrun(info.version,info.build)

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--module", help=" Script module to run.")
args = parser.parse_args()
m=args.module

if __name__=="__main__":
	print " ktf.run | "+time.strftime('%c')
	if m == "web/httpbt":	BruteForceHTTP.httpbt(0)
	if m == "web/cpfinder": AdminFinder.adminfinder(0)
	if m == "web/formbt":   BruteForceFormBase.httpformbasebruteforce(0)
	if m == "web/joomscan": Joomscan.xjoomla(0)
	if m == "web/whois":    Whois.wuis(0)
	if m == "web/lfd-con":  LFDconsole.LFDconsole(0)
	if m == "net/arplook":  ARPLooking.arplook(0)
	if m == "net/lanlive":  LANScanner.hostl(0)
	if m == "net/arpspoof": ARPPoisoning.arpp(0)
	if m == "net/portscan": PortScanner.PortScanner(0)
	if m == "set/gdreport": GetDataReport.getdatareport(0)
	if m == "set/facebrok": facebrok.facebrok(0)
	if m == "set/mailboom": smtpBombing.smtpbombing(0)
	if m == "fle/brutezip":	BruteZIP.btzip(0)
	if m == "fle/bruterar": BruteRAR.btrar(0)
	if m == "fbt/ssh":      BruteForceSSH.btssh(0)	
	if m == "fbt/sql":      BruteForceSQL.btsql(0)
	if m == "fbt/pop3":	BruteForcePOP3.btpop3(0)
	if m == "fbt/ftp":      BruteForceFTP.btftp(0)
	if m == "clt/ftp":      ClientFTP.cftp(0)
	if m == "clt/sql":      ClientMYSQL.cmysql(0)	
	if m == "clt/pop3":     ClientPOP3.cpop3(0)
	if m == "mc/tlogin":    TLogin.tlogin(0)
	if m == "fzz/ftp":      FuzzerFTP.fftp(0)
	if m == "ser/sql":      services.services('mysql')
	if m == "ser/ssh":      services.services('ssh')
	if m == "ser/apache":   services.services('apache2')
	if m == "wifi/wpabtf":  WpaBTF.btwpa(0)
	if m == "wifi/dos":     Wifi_DDOS.ddos(0)
	if m == "mc/gendic":	GenDic.Gendic(0)
	if m == "mc/i":         Iandl.iandi()
	if m == "for/imagen":   forenseIMAGE.exiftool(0)
