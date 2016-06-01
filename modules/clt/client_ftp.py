# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from core.Function import MakeTable
from ftplib import FTP
import subprocess
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.1"
	init.Description        ="Console Client for FTProtocol."
	init.CodeName           ="clt/cl.ftp"
	init.DateCreation       ="03/03/2015"      
	init.LastModification   ="18/05/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE     RQ     DESCRIPTION
		'target':[LOCAL_IP ,True ,'Host Target'],
		'port'  :[FTP_PORT ,False,'Port Target'],
		'user'  :[USERNAME ,True ,'Username'],
		'pass'  :[PASSWORD ,True ,'Password'],
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	ftp = FTP()
	ftp.connect(init.var['target'],int(init.var['port'])) 
	ftp.login(init.var['user'],init.var['pass'])

	cmd="nop"
	patch=""

	printAlert(2,"FTP Console")
	HelpBanner  = [["Commands","Description","Example"]]
	HelpBanner += [["ls","list files","ls"]]
	HelpBanner += [["cd","change dir","cd css"]]
	HelpBanner += [["mk","create dir","mk images"]]
	HelpBanner += [["rm","remove file","remove config.js"]]
	HelpBanner += [["rmd","remove dir","remove sex"]]
	HelpBanner += [["get","get file","get index.php"]]
	HelpBanner += [["put","up file","put login.php"]]
	MakeTable(HelpBanner)

	while(cmd!="exit"):
		cmd = raw_input(ClientPrompt(init.CodeName,"ftp"))
		if cmd == "ls":
			Space()
			ftp.retrlines("LIST")
			Space()
		elif cmd[0:2] == "cd":
			try:
				ftp.cwd(cmd[3:])
				if True:patch=cmd[3:]
				if patch == "..":patch=""
			except:printAlert(1,"Error: directory wrong.")
		elif cmd[0:3] == "get":
			lfile=cmd[4:].replace("\n","")
			try:
				ftp.retrbinary('RETR '+lfile,open(lfile,'wb').write)
				subprocess.Popen("cp "+lfile+" /root/Desktop/;rm "+lfile+"", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
				printAlert(3,"Saved, /root/Desktop/"+lfile)
			except:printAlert(1,"Error: file not found.")
		elif cmd[0:3] == "put":
			lfile=cmd[4:].replace("\n","")
			w = open(lfile, 'rb')
			try:
				ftp.storbinary("STOR r.r",w)
			except:printAlert(1,"Error: file wrong.")
		elif cmd[0:2] == "rm":
			try:
				ftp.delete(cmd[3:])
			except:printAlert(1,"Error: file not found.")
		elif cmd[0:3] == "rmd":
				pat=cmd[4:].replace("\n","")
				ftp.rmd(pat)
		elif cmd[0:2] == "mk":
			try:
				ftp.mkd(cmd[3:])
			except:printAlert(1,"Error: directory wrong.")
		elif cmd == "help":MakeTable(HelpBanner)

# END CODE MODULE ############################################################################################