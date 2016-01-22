# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                     #
# Modules   : facebrok        #
# Script by : RedToor         #
# Date      : 23/08/2015      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                 #
from core.design import *     #
from core.Setting import *    #
from core import Errors       #
from core import help         #
from core import ping         #
import sys                    #
d=DESIGN()                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                   #
import subprocess             #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                     #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
username_sql="root"
password_sql=""
database_sql="facebrok_db"
username_cp="admin"
password_cp="admin"
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

def run(para,parb,parc,pard,pare):
	global username_sql,password_sql,database_sql,username_cp,password_cp
	username_sql=para
	password_sql=parb
	database_sql=parc
	username_cp=pard
	password_cp=pase
	facebrok(1)

def facebrok(run):
	try:
		global username_sql,password_sql,database_sql,username_cp,password_cp
		if run!=1:
			actions=raw_input(d.prompt("set/facebrok"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("usql","yes","Username sql",username_sql)
			d.descrip("psql","yes","Password sql",password_sql)
			d.descrip("dsql","yes","Database sql",database_sql)
			d.descrip("upan","no","Username CPanel",username_cp)
			d.descrip("ppan","no","Password CPanel",password_cp)
 			print ""
		elif actions[0:8] == "set usql":
			username_sql = actions[9:]
			d.change("usql",username_sql)
			facebrok(0)
		elif actions[0:8] == "set psql":
			password_sql = actions[9:]
			d.change("psql",password_sql)
			facebrok(0)
		elif actions[0:8] == "set dsql":
			database_sql = actions[9:]
			d.change("dsql",database_sql)
			facebrok(0)
		elif actions[0:8] == "set upan":
			username_cp = actions[9:]
			d.change("upan",username_cp)
			facebrok(0)
		elif actions[0:8] == "set ppan":
			password_cp = actions[9:]
			d.change("ppan",password_cp)
			facebrok(0)
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
				print("\n "+Alr+" Installing facebrok project in local server")
				print " "+Alr+" Coping files to server",ping.status_cmd("cp -R files/facebrok/* "+PATCH_WWW,"\t\t\t")
				print " "+Alr+" Giving privileges to files",ping.status_cmd("chmod -R 777 "+PATCH_WWW+"croak/","\t\t")
				if True:
					try:
						print " "+Alr+" Starting Apache Server",ping.status_cmd("service apache2 start","\t\t\t")
						print(" "+Alr+" Starting Mysql Server"),ping.status_cmd("service mysql start","\t\t\t")
						print(" "+Alr+" Installing facebrok"),ping.status_cmd('wget -b -nv --post-data "server=127.0.0.1&user='+username_sql+'&pass='+password_sql+'&data='+database_sql+'&userp='+username_cp+'&passp='+password_cp+'" 127.0.0.1/croak/install/startgame.php','\t\t\t')
						d.space()
						print(" "+Got+" Script Running in http://127.0.0.1/")
						print(" "+Got+" Control Panel in http://127.0.0.1/croak/ with "+username_cp+":"+password_cp)
						d.space()
						raw_input(" "+Hlp+" Press any key for Stop facebrok")
						d.space()
						print(" "+Alr+" Stoping Process")
						print " "+Alr+" Removing files",ping.status_cmd("rm -R "+PATCH_WWW+"*","\t\t\t\t")
						print " "+Alr+" Stoping Apache",ping.status_cmd("service apache2 stop","\t\t\t\t")
						print " "+Alr+" Stoping Mysql",ping.status_cmd("service mysql stop","\t\t\t\t")
						d.space()
					except:
						d.space()
						print(" "+Alr+" Stoping Process")
						print " "+Alr+" Removing files",ping.status_cmd("rm -R /var/www/*","\t\t\t\t")
						print " "+Alr+" Stoping Apache",ping.status_cmd("service apache2 stop","\t\t\t\t")
						print " "+Alr+" Stoping Mysql",ping.status_cmd("service mysql stop","\t\t\t\t")
						d.space()
			except:
				Errors.Errors(event=sys.exc_info()[0], info=False)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info()[0], info=False)
	facebrok(0)
