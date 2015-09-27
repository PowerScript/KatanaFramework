# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Module    : I and I        #
# Script by : RedToor        #
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
	d.space()
	print " IP Local   : ",ping.myip()
        ping.interfaces(1)
        ping.get_gateway(1)
        ping.my_mac_address(1)	
	ping.get_external_ip()
	print " Username   : ",commands.getoutput('whoami')
	print " OS         : ",commands.getoutput('uname')
	print " Version    : ",commands.getoutput('uname -r')
	return 1
