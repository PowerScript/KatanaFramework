# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
from core.Function import status_cmd
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.0"
	init.Description        ="facebrok project Launcher."
	init.CodeName           ="set/facebrok"
	init.DateCreation       ="23/08/2015"      
	init.LastModification   ="24/03/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE      RQ     DESCRIPTION
		'u_sql':["root"     ,True ,'User Mysql'],
		'p_sql':[""         ,True ,'Pass Mysql']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):

	printAlert(0,"Installing facebrok project in local server")
	printAlert(0,"Coping files to server            "+status_cmd("cp -R files/facebrok/* "+PATCH_WWW))
	printAlert(0,"Giving privileges to files        "+status_cmd("chmod -R 777 "+PATCH_WWW+"croak/"))
	printAlert(0,"Starting Apache Server            "+status_cmd("service apache2 start"))
	printAlert(0,"Starting Mysql Server             "+status_cmd("service mysql start"))
	printAlert(0,"Installing facebrok               "+status_cmd('cd tmp;wget -b -nv --post-data "server=127.0.0.1&user='+init.var['u_sql']+'&pass='+init.var['p_sql']+'&data=facebrok&userp=fbrok&passp=fbrok" 127.0.0.1/croak/install/startgame.php'))
	Space()
	printAlert(7,"Control Panel in http://127.0.0.1/croak/ With: user[fbrok] pass[fbrok]")
	raw_input(printAlert(8,"Press [ENTER] key for Stop facebrok"))
	printAlert(0,"Stoping Process")
	printAlert(0,"Removing files                    "+status_cmd("rm -R "+PATCH_WWW+"*"))
	printAlert(0,"Stoping Apache                    "+status_cmd("service apache2 stop"))
	printAlert(0,"Stoping Mysql                     "+status_cmd("service mysql stop"))

# END CODE MODULE ############################################################################################