# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                       #
# Modules   : ZIP Brute Force   #
# Script by : LeSZO ZerO        #
# Date      : 28/02/2015        #
# Version   : 2.0
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                   #
from core.design import *       #
from core.Setting import *      #
from core import Errors         #
from core import help           #
from core import ping           #
import sys                      #
d=DESIGN()                      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                     #
import zipfile                  #
import optparse                 #
import os                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
defaultarch="core/test/test.zip"
defaultdicc=DITIONARY_PASSWORDS
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #


def run(files,dictionary):
	global defaultarch,defaultdicc
	defaultarch=files
	defaultdicc=dictionary
	btzip(1)

def btzip(run):
	try:
		global defaultarch,defaultdicc
		if run!=1:
			actions=raw_input(d.prompt("fle/zip"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("file","yes","file with pass",defaultarch)
 			d.descrip("dict","yes","Dictionary pass",defaultdicc)
			print ""
			btzip(0)
		elif actions[0:8] == "set file":
			defaultarch=ping.update(defaultarch,actions,"file")
			d.change("file",defaultarch)
		elif actions[0:8] == "set dict":
			defaultdicc=ping.update(defaultdicc,actions,"dict")
			d.change("dict",defaultdicc)
		elif actions=="exit" or actions=="x":
			d.goodbye()
			exit()
		elif actions=="help" or actions=="h":
			help.help()
		elif actions=="back" or actions=="b":
			pass
		elif actions=="run"  or actions=="r":
			d.run()
			try:
				d.loading_file()
				Arch = open(defaultdicc,"r")
				if True:
					leeArchivo = Arch.readlines()
					try:
						ZIParch = zipfile.ZipFile(defaultarch)
						if True:
							for palabra in leeArchivo:
								palabraLlegada = palabra.split("\n")
								try:
									ZIParch.extractall(pwd=str(palabraLlegada[0]))
									if True:
										ping.savetwo("BruteForceZIP",defaultarch,palabraLlegada[0])
										print "\n-"+Suf+" file Cracked with =",str(palabraLlegada[0])+"\n"
										return 1
								except:
									print " "+Alr+" Checking with ",str(palabraLlegada[0])
					except:
						Errors.Errors(event=sys.exc_info(), info=defaultarch)
			except:
				Errors.Errors(event=sys.exc_info(), info=defaultdicc)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info(), info=False)
	btzip(0)
