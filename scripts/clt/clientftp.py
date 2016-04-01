# This module requires katana framework 
# https://github.com/RedToor/Katana
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                 #
from core.design import *     #
from core.Setting import *    #
from core import Errors       #
from core import getFunction  #
import sys                    #
Message=DESIGN()              #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                   #
from lib.ftplib.ftplib import FTP
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="RedToor"
	initialize.Version            ="1.1"
	initialize.Despcription       ="Console Client for FTProtocol."
	initialize.CodeName           ="clt/cl.ftp"
	initialize.DateCreation       ="03/03/2015"      
	initialize.LastModification   ="31/03/2016"

	# DEFAULT VARIABLES             VALUE                  NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[[LOCAL_IP            , "target" , "yes" , "IP or DNS"]]         #[0][0]
	initialize.DEFAULT_VARIABLE  +=[[FTP_PORT            , "port"   , "no"  , "Service port"]]      #[1][0]
	initialize.DEFAULT_VARIABLE  +=[[USERNAME            , "user"   , "yes" , "Username target"]]   #[2][0]
	initialize.DEFAULT_VARIABLE  +=[[PASSWORD            , "pass"   , "yes" , "Password target"]]   #[3][0]
initialize()
# END INFORMATION MODULE

# MAIN FUNCTION
def main(run):
	try:
		# HEAD MODULE
		if run:	actions=raw_input(Message.prompt(initialize.CodeName))
		else  : actions="run"
		if getFunction.KatanaCheckActionShowOptions(actions)  :getFunction.ShowOptions(initialize.DEFAULT_VARIABLE)
		elif getFunction.KatanaCheckActionSetValue(actions)   :initialize.DEFAULT_VARIABLE=getFunction.UpdateValue(actions,initialize.DEFAULT_VARIABLE)
		elif getFunction.KatanaCheckActionisBack(actions)     :return
		# END HEAD MODULE
		elif getFunction.runModule(actions):
			Message.run()
			# CODE MODULE    ############################################################################################
			try:
				getFunction.live(initialize.DEFAULT_VARIABLE[0][0],initialize.DEFAULT_VARIABLE[1][0])
				if True:
					try:
						ftp.login(initialize.DEFAULT_VARIABLE[0][0],initialize.DEFAULT_VARIABLE[1][0])									
						if True:
							try:
								cmd="nop"
								patch=""
								print "\n "+Hlp+" FTP Client help"
								print " ----------------------------------------"
								print " |"+colors[6]+"Commd"+colors[0]+"| "+colors[6]+"Description"+colors[0]+" | "+colors[6]+"Examples"+colors[0]+"         |"
								print " ----------------------------------------"
								print " |ls	| list files  | ls               |" 
								print " |cd	| change dir  | cd css           |"
								print " |mk	| create dir  | mk images        |"
								print " |rm	| remove file | remove config.js | "
								print " |rmd  | remove dir  | remove sex       |"
								print " |get  | get file    | get index.php    |"
								print " |put  | up file     | put login.php    |"
								print " ----------------------------------------"
								print ""
								while(cmd!="exit"):
									cmd = raw_input(Message.Client_prompt('ftp'))
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
											print " "+Bad+" Error: directory wrong."
									if cmd[0:3] == "get":
										lfile=cmd[4:].replace("\n","")
										try:
											ftp.retrbinary('RETR '+lfile,open(lfile,'wb').write)
											if True:
												subprocess.Popen("cp "+lfile+" /root/Desktop/;rm "+lfile+"", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
												print " "+Suf+" Saved, /root/Desktop/"+lfile
										except:
											print " "+Bad+" Error: file not found."
									if cmd[0:3] == "put":
										lfile=cmd[4:].replace("\n","")
										w = open(lfile, 'rb')
										try:
											ftp.storbinary("STOR r.r",w)
										except:
											print " "+Bad+" Error: file wrong."
									if cmd[0:2] == "rm":
										try:
											ftp.delete(cmd[3:])
										except:
											print " "+Bad+" Error: file not found."
									if cmd[0:3] == "rmd":
										pat=cmd[4:].replace("\n","")
										ftp.rmd(pat)
									if cmd[0:2] == "mk":
										try:
											ftp.mkd(cmd[3:])
										except:
											print " "+Bad+" Error: directory wrong."

							except Exception,e:
								print(" "+Bad+" Timeout, Error:", e)
					except:
						Errors.Errors(event=sys.exc_info(), info=initialize.DEFAULT_VARIABLE[2][0]+":"+initialize.DEFAULT_VARIABLE[3][0])
			except:
				Errors.Errors(event=sys.exc_info(), info=initialize.DEFAULT_VARIABLE[0][0]+":"+initialize.DEFAULT_VARIABLE[1][0])			# END CODE MODULE ############################################################################################
			# END CODE MODULE ############################################################################################
		else:
			getFunction.KatanaCheckActionGlobalCommands(actions)
	# ERROR GENERAL
	except:
		Errors.Errors(event=sys.exc_info(), info=sys.exc_traceback.tb_lineno)
	# END ERROR GENERAL
	main(True)
# END MAIN FUNCTION

# LINKER FUNCTION
def run(target,port,username,password):
	initialize.DEFAULT_VARIABLE[0][0] = target
	initialize.DEFAULT_VARIABLE[1][0] = port
	initialize.DEFAULT_VARIABLE[2][0] = username
	initialize.DEFAULT_VARIABLE[3][0] = password
	main(False)
# END LINKER FUNCTION