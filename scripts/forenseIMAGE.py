# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : exiftool runer #
# Script by : RedToor        #
# Date      : 28/09/2015     #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Katana Core                #
from core.design import *    #
from core.Setting import *   #
from core import Errors      #
from core import help        #
from core import ping        #
import sys                   #
d=DESIGN()                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Libraries                  #
import subprocess            #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaultimg="core/test/test.jpg"
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(image):
	global defaultimg
	defaultimg=image
	exiftool(1)

def exiftool(run):
	try:
		global defaultimg
		if run!=1:
			actions=raw_input(d.prompt("for/imagen"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("imagen","yes","img for forence",defaultimg)
			print ""
		elif actions[0:10] == "set imagen":
			defaultimg=ping.update(defaultimg,actions,"imagen")
			d.change("target",defaultimg)
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
				d.loading_file()
				try:
					with open(defaultimg,'r') as comprossed:
						if True:
							try:
								print "\n "+Hlp+" Forence Imagen Client help\n"
								print "  ------------------------------------------"
  								print "  |extrat_all | extrat all MD  | ls        |" 
  								print "  ------------------------------------------"	  												
								cmd="nop"
								while(cmd!="exit"):
									cmd = raw_input(d.Client_prompt('forence{IMAGEN}'))
									if(cmd=="extract_all"):
										subprocess.call("perl files/exiftool/exiftool "+defaultimg, shell=True)
							except:
								Errors.Errors(event=sys.exc_info()[0], info=False)
				except:
					Errors.Errors(event=sys.exc_info()[0], info=defaultimg)
			except:
				Errors.Errors(event=sys.exc_info()[0], info=False)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info()[0], info=False)
	exiftool(0)
