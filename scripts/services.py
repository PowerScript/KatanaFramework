# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                       #
# Module    : Services          #
# Script by : RedToor           #
# Date      : 11/06/2015        #
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
import subprocess               #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

def services(process):
	try:
		d.run()
		print " "+Alr+" Starting "+process+"",ping.status_cmd("service "+process+" start","\t\t\t\t")
		d.space()
		raw_input(" "+Hlp+" Press any key for Stop Service")
		print " "+Alr+" Stopping "+process+"",ping.status_cmd("service "+process+" stop","\t\t\t\t")
		d.space()
		return
	except:
		Errors.Errors(event=sys.exc_info()[0], info=False)
	services(process)