# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                       #
# Modules   : RAR Brute Force   #
# Script by : LeSZO ZerO        #
# Date      : 28/02/2015        #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                   #
from core.design import *       #
from core import help           #
from core import ping           #
d=DESIGN()                      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                     #
from lib.rarfile import RARfile #
import optparse                 #
import sys                      #
import os                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
defaultarch="core/test/test.rar"
defaultdicc="core/db/pass.dicc"
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #


def run(para,parb):
	global defaultarch,defaultdicc
	defaultarch=para
	defaultdicc=parb
	btrar(1)

def btrar(run):
	try:
		global defaultarch,defaultdicc
		if run!=1:
			actions=raw_input(d.prompt("fle/rar"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("file","yes","file with pass",defaultarch)
 			d.descrip("dict_1","yes","Dictionary pass",defaultdicc)
			print ""
			btrar(0)
		elif actions[0:8] == "set file":
			defaultarch = actions[11:]
			d.change("file",defaultarch)
			btrar(0)
		elif actions[0:10] == "set dict_1":
			defaultdicc = actions[11:]
			d.change("dict_1",defaultdicc)
			btrar(0)
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
				d.loading()
				Arch = open(defaultdicc,"r")
				if True:
					leeArchivo = Arch.readlines()
					for palabra in leeArchivo:
						palabraLlegada = palabra.split("\n")
						try:
							RARarch = RARfile.RARFile(defaultarch)
							try:
								RARarch.extractall(pwd=str(palabraLlegada[0]))
								if True:
									ping.savetwo("BruteForceRAR",defaultarch,palabraLlegada[0])
									print "\n-"+Suf+" file Cracked with =",str(palabraLlegada[0])+"\n"
									return 1
							except:
								print " "+Alr+" Checking with ",str(palabraLlegada[0])
						except:
							d.arcnot(defaultarch)
							btrar(0)
			except:
				d.filenot(defaultdicc)
				btrar(0)
		else:
			d.nocommand()
	except:
		d.kbi()
		exit()
	btrar(0)