# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
import zipfile
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="LeSZO ZerO"
	init.Version            ="2.0"
	init.Description        ="Brute Force to ZIP file."
	init.CodeName           ="fle/bt.zip"
	init.DateCreation       ="28/02/2015"      
	init.LastModification   ="27/12/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE               RQ     DESCRIPTION
		'file':["files/test/test.zip",True ,'ZIP file to Crack'],
		'dict':[DITIONARY_PASSWORDS  ,False,'Wordlist']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	Loadingfile(init.var['dict'])
	Arch = open(init.var['dict'],"r")
	leeArchivo = Arch.readlines()
	ZIParch = zipfile.ZipFile(init.var['file'])
	for palabra in leeArchivo:
		palabraLlegada = palabra.split("\n")
		try:
			ZIParch.extractall(pwd=str(palabraLlegada[0]),path="/root/home/")
			printk.suff("Successfully with ["+palabraLlegada[0]+"] -> /root/home/")
			UTIL.sRegister(init,palabraLlegada[0])
			return
		except:printk.inf(" | Checking '"+palabraLlegada[0]+"'")

# END CODE MODULE ############################################################################################
