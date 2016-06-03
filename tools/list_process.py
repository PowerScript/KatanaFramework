# This Tool requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

class init:
	
	Author      = "Redtoor"
	Description = "Test tool template"
	var         = {}
	Arguments   = {

		'i':[True ,'interface to change mac'],
		'm':[False,'specific mac'],
		'r':[True,'ramdom mac']
	}
	
def Main():
	print " ktf.tool -t list_process "
	print " ktf.tool -t list_process -h "
	print " ktf.tool -t list_process -i wlan0"
	print " ----------------------------------->error : -r is necesary"
	print " ktf.tool -t list_process -r"
	print " ----------------------------------->error : -r is empy and i is necesary"
	print " ktf.tool -t list_process -m -i wlan0 -r 232"
	print " ----------------------------------->good  : -m is enable, i is wlan0 , r is 232"
	print " ktf.tool -t list_process "

	print "interface "+init.var["i"]
	print "MAC       "+init.var["m"]
	print "ramdom    "+init.var["r"]
