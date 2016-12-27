# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from core.Errors import Errors
from ftplib import FTP
import commands, os
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.1"
	init.Description        ="Console Client for FTProtocol."
	init.CodeName           ="clt/cl.ftp"
	init.DateCreation       ="03/03/2015"      
	init.LastModification   ="20/07/2016"
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

	printk.inf("FTP Console")
	HelpBanner  = [["Commands","Description","Example"]]
	HelpBanner += [["ls","list files","ls"]]
	HelpBanner += [["cd","change dir","cd css"]]
	HelpBanner += [["mk","create dir","mk images"]]
	HelpBanner += [["rm","remove file","remove config.js"]]
	HelpBanner += [["rnm","rename file","rnm maria.jpg"]]
	HelpBanner += [["rmd","remove dir","remove sex"]]
	HelpBanner += [["get","download file","get index.php"]]
	HelpBanner += [["put","upload file","put login.php"]]
	GRAPHICAL.CreateTable(HelpBanner)

	cmd="nop"
	path=""

	while(cmd!="exit"):
		try:
			cmd = raw_input(ClientPrompt(init.CodeName,"ftp/"+path))
			if cmd == "ls":
				Space()
				ftp.retrlines("LIST")
				Space()
			elif cmd[0:2] == "cd":
				ftp.cwd(cmd[3:])
				if cmd[3:] != "..": path+=cmd[3:]+"/"
				if cmd[3:] == "..": 
					head, tail = os.path.split(os.path.split(path)[0])
					path=str(head)
			elif cmd[0:3] == "get":
				lfile=cmd[4:].replace("\n","")
				ftp.retrbinary('RETR '+lfile,open(lfile,'wb').write)
				commands.getoutput("cp "+lfile+" /root/Desktop/;rm "+lfile)
				printk.suff("File was Saved, /root/Desktop/"+lfile)
			elif cmd[0:3] == "put":
				lfile=cmd[4:].replace("\n","")
				w = open(lfile, 'rb')
				ftp.storbinary("STOR "+os.path.basename(w.name),w)
			elif cmd[0:3] == "rnm":
				newname=raw_input(" New name:")
				ftp.rename(cmd[4:],newname)
			elif cmd[0:3] == "rmd":ftp.rmd(cmd[4:])
			elif cmd[0:2] == "rm" :ftp.delete(cmd[3:])
			elif cmd[0:2] == "mk" :ftp.mkd(cmd[3:])
			elif cmd == "help":GRAPHICAL.CreateTable(HelpBanner)
		except : Errors() 

# END CODE MODULE ############################################################################################
