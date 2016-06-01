#!/usr/bin/env python
#HEAD#########################################################
#
# Katana Framework | ktf.tool                            
# Building...
#
# 
# Last Modified: 24/05/2016
#
#########################################################HEAD#

from core.design import *
import importlib,argparse,sys,os

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--import-module", help=" file module to import.")
parser.add_argument("-t", "--tool", help=" Tool [PL] Process List.")
args = parser.parse_args()


CLASS_BANNER=DESIGN()
CLASS_BANNER.ktftool()

class Tool:
	def ImportModule(self):
		printAlert(0,"Import Module")
		Loadingfile(args.import_module)
		try:
			printAlert(0,"Information Module")
			ModuleToStart = importlib.import_module(args.import_module) 
			init=ModuleToStart.init()
			print "       |>Author           : "+init.Author
			print "       |>Version Script   : "+init.Version
			print "       |>Description      : "+init.Description
			print "       |>Code Name        : "+init.CodeName
			print "       |>Creation         : "+init.DateCreation
			print "       |>Last Modification: "+init.LastModification

			New = init.CodeName
			New = New.split("/")
			printAlert(0,"Installing module")
			if os.path.isdir("/usr/share/KatanaFramework/scripts/"+New[0]+"/") == False: 
				os.system("mkdir /usr/share/KatanaFramework/scripts/"+New[0]+"/")
				os.system("echo > /usr/share/KatanaFramework/scripts/"+New[0]+"/__init__.py")
			os.system("cp "+args.import_module+".py /usr/share/KatanaFramework/scripts/"+New[0]+"/")
			if True:printAlert(3,"Module installed")

		except Exception as e:printAlert(1,e)

RUN=Tool()
RUN.ImportModule()
