# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : I and I        #
# Script by : Uknowk         #
# Adated by : RedToor        #
# Date      : 30/08/2015     #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Katana Core                #
from core.design import *    #
from core import help        #
from core import ping        #
d=DESIGN()                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Libraries                  #
import time                  #
import commands              #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #


def iandi():
	d.run()
	print ""
	print " Ip Local"
	ping.myip()
	print " Ip Public"
	ping.get_external_ip()
	print " Devices"
	ping.interfaces()
	print""
	print " Devices monitor"
	ping.monitor()
	print ""
	print " Username"
	user=commands.getoutput('whoami')
	print " user            :  "+user
	print ""
	print " Operative System "
	print " OS              :  "+commands.getoutput('uname')
	print ""
	print " Version OS"
	print " Version         :  "+commands.getoutput('uname -r')
	return 1
