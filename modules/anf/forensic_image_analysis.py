# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES 
import commands
# END LIBRARIES

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.1"
	init.Description        ="Forensic Image Analysis with exiftool."
	init.CodeName           ="anf/af.imagen"
	init.DateCreation       ="28/09/2015"      
	init.LastModification   ="27/12/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE                 RQ     DESCRIPTION
		'target':["files/test/test.jpg",True ,'Path file']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	Loadingfile(init.var['target'])
	open(init.var['target'],'rw')
	printk.inf("Forensic Image Analysis Console [exiftool]")
	HelpBanner  = [["Commands","Description","Example"]]
	HelpBanner += [["extract_all","extract all MD","extract_all"]]
	HelpBanner += [["comment","comment whatever","comment Hello zzz"]]
	GRAPHICAL.CreateTable(HelpBanner)
	cmd="nop"
	while(cmd!="exit"):
		cmd = raw_input(ClientPrompt(init.CodeName,"anf.imagen"))
		if(cmd=="extract_all"):
			output=commands.getoutput("perl files/exiftool/exiftool "+init.var['target'])
			output=output.split("\n")
			for lineperline in output:
				print " |"+lineperline
		elif(cmd[:7]=="comment"):
			output=commands.getoutput("perl files/exiftool/exiftool -comment="+cmd[8:]+" "+init.var['target'])
			output=output.split("\n")
			for lineperline in output:
				print " |"+lineperline
		elif cmd == "help":GRAPHICAL.CreateTable(HelpBanner)

# END CODE MODULE ############################################################################################
