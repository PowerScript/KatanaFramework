# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : WPA Brute Force#
# Script by : RedToor        #
# Date      : 11/06/2015     #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Katana Core                #
from core.design import *    #
from core import help        #
from core import ping        #
d=DESIGN()                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Libraries                  #
import subprocess            #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaultcap="core/test/test.cap"
defaultdic="core/db/pass.dicc"
defaultmac="E8:40:F2:32:37:FD"
# :-:-:-:-:-:-:-:-:-:-:-:-:- #


def run(para,parb,parc):
	global defaultcap,defaultdic,defaultmac
	defaultcap=para
	defaultdic=parb
	defaultmac=parc
	btwpa(1)

def btwpa(run):
	try:
		global defaultcap,defaultdic,defaultmac
		if run!=1:
			actions=raw_input(d.prompt("wifi/wpabtf"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("file","yes","file .CAP",defaultcap)
			d.descrip("maca","yes","Mac address",defaultmac)
			d.descrip("dict_1","yes","Dictionary pass",defaultdic)
			print ""
			btwpa(0)
		elif actions[0:8] == "set file":
			defaultcap = actions[9:]
			d.change("file",defaultcap)
			btwpa(0)
		elif actions[0:7] == "set mac":
			defaultmac = actions[8:]
			d.change("maca",defaultmac)
			btwpa(0)
		elif actions[0:10] == "set dict_1":
			defaultdic = actions[11:]
			d.change("dict_1",defaultdic)
			btwpa(0)
		elif actions=="exit" or actions=="x":
			d.goodbye()
			exit()
		elif actions=="help" or actions=="h":
			help.help()
		elif actions=="back" or actions=="b":
			return
			return
		elif actions=="run"  or actions=="r":
			d.run()
			try:
				d.loading()
				Arch = open(defaultdic,"r")
				try:
					Arch = open(defaultcap,"r")
					if True:
						try:
							subprocess.call('aircrack-ng -w '+defaultdic+' -b '+defaultmac+' '+defaultcap, shell=True)
						except Exception,e:
							print " "+Bad+" Error: "+e
				except:
					d.arcnot(defaultarch)
					btwpa(0)
			except:
				d.filenot(defaultdic)
				btwpa(0)
		else:
			d.nocommand()
	except:
		d.kbi()
		exit()
	btwpa(0)