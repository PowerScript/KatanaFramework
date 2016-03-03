# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : Client FTP     #
# Script by : RedToor        #
# Date      : 03/03/2015     #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Katana Core                #
from core.design import *    #
from core import help        #
from core import ping        #
d=DESIGN()                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Libraries                  #
from lib.ftplib.ftplib import FTP
import subprocess            #
import os                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaulthost="127.0.0.1"
defaultport="21"
defaultuser="anonymous"
defaultpass="pass"
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(target,port,username,password):
	global defaulthost,defaultport,defaultuser,defaultpass
	defaulthost=target
	defaultport=port
	defaultuser=username
	defaultpass=password
	cftp(1)

def cftp(run):
	try:
		global defaulthost,defaultport,defaultuser,defaultpass
		if run!=1:
			actions=raw_input(d.prompt("clt/ftp"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("target","yes","IP or DNS",defaulthost)
			d.descrip("port","no","Port of target",defaultport)
 			d.descrip("user","yes","Username",defaultuser)
 			d.descrip("pass","yes","Password",defaultpass)
			print ""
			cftp(0)
		elif actions[0:10] == "set target":
			defaulthost = actions[11:]
			defaulthost = defaulthost.replace("http://", "")
			d.change("target",defaulthost)
			cftp(0)
		elif actions[0:8] == "set port":
			defaultport = actions[9:]
			d.change("port",defaultport)
			cftp(0)
		elif actions[0:8] == "set user":
			defaultuser = actions[9:]
			d.change("user",defaultuser)
			cftp(0)
		elif actions[0:8] == "set pass":
			defaultpass = actions[9:]
			d.change("pass",defaultpass)
			cftp(0)
		elif actions=="exit" or actions=="x":
			d.goodbye()
			exit()
		elif actions=="help" or actions=="h":
			help.help()
		elif actions=="back" or actions=="b":
			return
		elif actions=="run"  or actions=="r":
			d.run()
			try:
				ftp = FTP(defaulthost) 
				if True:
					try:
						ftp.login(defaultuser,defaultpass)									
						if True:
							try:
								cmd="nop"
								patch=""
								print "\n "+Hlp+" FTP Client help\n"
								print "  ----------------------------------------"
								print "  |"+colors[6]+"Commd"+colors[0]+"| "+colors[6]+"Description"+colors[0]+" | "+colors[6]+"Examples"+colors[0]+"         |"
								print "  ----------------------------------------"
								print "  |ls	| list files  | ls               |" 
								print "  |cd	| change dir  | cd css           |"
								print "  |mk	| create dir  | mk images        |"
								print "  |rm	| remove file | remove config.js | "
								print "  |rmd  | remove dir  | remove sex       |"
								print "  |get  | get file    | get index.php    |"
								print "  |put  | up file     | put login.php    |"
								print "  ----------------------------------------"
								print ""
								while(cmd!="exit"):
									cmd = raw_input(colors[1]+" CLT~"+colors[3]+"ftp/"+patch+"> "+colors[0])
									if cmd == "ls":
										ftp.retrlines("LIST")
									if cmd[0:2] == "cd":
										try:
											ftp.cwd(cmd[3:])
											if True:
												patch=cmd[3:]
												if patch == "..":
													patch=""
										except:
											print " ["+colors[1]+"-"+colors[0]+"] Error: directory wrong."
									if cmd[0:3] == "get":
										lfile=cmd[4:].replace("\n","")
										try:
											ftp.retrbinary('RETR '+lfile,open(lfile,'wb').write)
											if True:
												subprocess.Popen("cp "+lfile+" /root/Desktop/;rm "+lfile+"", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
												print " ["+colors[1]+"-"+colors[0]+"] Saved, /root/Desktop/"+lfile
										except:
											print " ["+colors[1]+"-"+colors[0]+"] Error: file not found."
									if cmd[0:3] == "put":
										lfile=cmd[4:].replace("\n","")
										w = open(lfile, 'rb')
										try:
											ftp.storbinary("STOR r.r",w)
										except:
											print " ["+colors[1]+"-"+colors[0]+"] Error: file wrong."
									if cmd[0:2] == "rm":
										try:
											ftp.delete(cmd[3:])
										except:
											print " ["+colors[1]+"-"+colors[0]+"] Error: file not found."
									if cmd[0:3] == "rmd":
										pat=cmd[4:].replace("\n","")
										ftp.rmd(pat)
									if cmd[0:2] == "mk":
										try:
											ftp.mkd(cmd[3:])
										except:
											print " ["+colors[1]+"-"+colors[0]+"] Error: directory wrong."

							except(KeyboardInterrupt):
								d.kbi()
							except Exception,e:
								print(" ["+colors[1]+"-"+colors[0]+"] Timeout.", e)
					except:
						d.nomatch()
			except:
				d.off()
		else:
			d.nocommand()
	except:
		d.kbi()
		exit()
	cftp(0)
