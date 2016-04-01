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

# INFORMATION MODULE
def initialize():
	initialize.Author             ="RedToor"
	initialize.Version            ="1.0"
	initialize.Despcription       ="facebrok project Launcher."
	initialize.CodeName           ="set/facebrok"
	initialize.DateCreation       ="23/08/2015"      
	initialize.LastModification   ="24/03/2016"

	# DEFAULT VARIABLES             VALUE                NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[["root"          , "u_sql"  ,  "yes" , "User Mysql"]]   #[0][0]
	initialize.DEFAULT_VARIABLE  +=[[""              , "p_sql"  ,  "no"  , "Pass Mysql"]]   #[1][0]
initialize()
# END INFORMATION MODULE

# MAIN FUNCTION
def main(run):
	try:
		# HEAD MODULE
		if run:	actions=raw_input(Message.prompt(initialize.CodeName))
		else  : actions="run"
		if   getFunction.KatanaCheckActionShowOptions(actions):getFunction.ShowOptions(initialize.DEFAULT_VARIABLE)
		elif getFunction.KatanaCheckActionSetValue(actions)   :initialize.DEFAULT_VARIABLE=getFunction.UpdateValue(actions,initialize.DEFAULT_VARIABLE)
		elif getFunction.KatanaCheckActionisBack(actions)     :return
		# END HEAD MODULE
		elif getFunction.runModule(actions):
			Message.run()
			# CODE MODULE    ############################################################################################
			print(" "+Alr+" Installing facebrok project in local server")
			print " "+Alr+" Coping files to server",getFunction.status_cmd("cp -R files/facebrok/* "+PATCH_WWW,"\t\t\t")
			print " "+Alr+" Giving privileges to files",getFunction.status_cmd("chmod -R 777 "+PATCH_WWW+"croak/","\t\t")
			if True:
				try:
					print " "+Alr+" Starting Apache Server",getFunction.status_cmd("service apache2 start","\t\t\t")
					print(" "+Alr+" Starting Mysql Server"),getFunction.status_cmd("service mysql start","\t\t\t")
					print(" "+Alr+" Installing facebrok"),getFunction.status_cmd('wget -b -nv --post-data "server=127.0.0.1&user='+initialize.DEFAULT_VARIABLE[0][0]+'&pass='+initialize.DEFAULT_VARIABLE[1][0]+'&data=facebrok&userp=fbrok&passp=fbrok" 127.0.0.1/croak/install/startgame.php','\t\t\t')
					Message.space()
					print(" "+Got+" Project Running in http://127.0.0.1/")
					print(" "+Got+" Control Panel in http://127.0.0.1/croak/ With: user[fbrok] pass[fbrok]")
					Message.space()
					raw_input(" "+Hlp+" Press [ENTER] key for Stop facebrok")
					Message.space()
					print(" "+Alr+" Stoping Process")
					print " "+Alr+" Removing files",getFunction.status_cmd("rm -R "+PATCH_WWW+"*","\t\t\t\t")
					print " "+Alr+" Stoping Apache",getFunction.status_cmd("service apache2 stop","\t\t\t\t")
					print " "+Alr+" Stoping Mysql",getFunction.status_cmd("service mysql stop","\t\t\t\t")
					Message.space()
				except:
					Message.space()
					print(" "+Alr+" Stoping Process")
					print " "+Alr+" Removing files",getFunction.status_cmd("rm -R /var/www/*","\t\t\t\t")
					print " "+Alr+" Stoping Apache",getFunction.status_cmd("service apache2 stop","\t\t\t\t")
					print " "+Alr+" Stoping Mysql",getFunction.status_cmd("service mysql stop","\t\t\t\t")
					Message.space()
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
def run(username,password):
	initialize.DEFAULT_VARIABLE [0][0] = username
	initialize.DEFAULT_VARIABLE [1][0] = password
	main(False)
# END LINKER FUNCTION