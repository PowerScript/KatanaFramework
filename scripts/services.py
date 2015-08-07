# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                       #
# Modules   : Services          #
# Script by : RedToor           #
# Date      : 11/06/2015        #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                   #
from core.design import *       #
from core import help           #
from core import ping           #
d=DESIGN()                      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                     #
import subprocess               #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

def services(process):
	try:
		d.run()
		print(" "+Alr+" Starting Service "+process)
		subprocess.call('service '+process+' start > nul', shell=True)
		print(" "+God+" Service started")
		print ""
		raw_input(" "+Hlp+" Press any key for Stop Service")
		print(" "+Alr+" Stopping Service "+process)
		subprocess.call('service '+process+' stop > nul ', shell=True)
		print(" "+God+" Service Stoped")
		print ""
		return
	except(KeyboardInterrupt):
		d.kbi()
	services(process)
