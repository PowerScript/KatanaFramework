# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
from lib.rarfile.RARfile import *
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="LeSZO ZerO"
	init.Version            ="2.0"
	init.Description        ="Brute Force to RAR file."
	init.CodeName           ="fle/bt.rar"
	init.DateCreation       ="28/02/2015"      
	init.LastModification   ="01/06/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE               RQ     DESCRIPTION
		'file':["files/test/test.rar",True ,'RAR file to Crack'],
		'dict':[DITIONARY_PASSWORDS  ,False,'Wordlist']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	Loadingfile(init.var['dict'])
	Arch = open(init.var['dict'],"r")
	leeArchivo = Arch.readlines()
	RARarch = RarFile(init.var['file'])
	for palabra in leeArchivo:
		palabraLlegada = palabra.split("\n")
		try:
			RARarch.extractall(pwd=str(palabraLlegada[0]),path="/root/home/")
			printk.suff("Successfully with ["+palabraLlegada[0]+"] -> /root/home/")
			UTIL.sRegister(init,palabraLlegada[0])
			return
		except:printk.inf(" | Checking '"+palabraLlegada[0]+"'")

# END CODE MODULE ############################################################################################
