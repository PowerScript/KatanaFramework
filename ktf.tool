#!/usr/bin/env python
#HEADER#######################
# Katana framework           #
# ktf.tool File              #
# Last Modified: 06/04/2016  #
# Review: 0                  #
#######################HEADER#

from core.design import *
import importlib 
import argparse
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--import-module", help=" Script module to run.")
args = parser.parse_args()

Alert = DESIGN()

class Tool:
	print "\n Tool Suite for Katana Framework."
	def ImportModule(self):
		print "\n "+God+" Running Import Module"
		Alert.loading_file()
		try:
			print " INFORMATION MODULE: "
			os.system("cp '"+args.import_module+"' '/usr/share/katana/tmp/new.py'")
			os.system("echo >> /usr/share/katana/tmp/__init__.py")
			ModuleToStart = importlib.import_module("tmp.new") 
			
			print " |Author           : "+ModuleToStart.initialize.Author
			print " |Version Script   : "+ModuleToStart.initialize.Version
			print " |Description      : "+ModuleToStart.initialize.Despcription
			print " |Code Name        : "+ModuleToStart.initialize.CodeName
			print " |Creation         : "+ModuleToStart.initialize.DateCreation
			print " |Last M...        : "+ModuleToStart.initialize.LastModification
			print " ------------------- "

			NULL = raw_input(" Continue ? PRESS any key")
			New = ModuleToStart.initialize.CodeName
			New = New.split("/")
			if os.path.isdir("/usr/share/katana/scripts") == False: os.system("mkdir /usr/share/katana/scripts/"+New[0]+" & echo > /usr/share/katana/scripts/"+New[0]+"/__init__.py")
			os.system("cp "+args.import_module+" /usr/share/katana/scripts/"+New[0]+"/")
			
			os.system("rm /usr/share/katana/tmp/*")
		except Exception as e:
			print e

RUN=Tool()
RUN.ImportModule()
