#!/usr/bin/env python
#HEAD#########################################################
#
# Katana Framework | ktf.tool                            
# Building...
#
# 
# Last Modified: 03/06/2016
#
#########################################################HEAD#

from core.Design import *
import importlib,argparse,sys,os
import xml.etree.ElementTree as ET
import importlib , sys

tree = ET.parse('core/tools.xml')
root = tree.getroot()

CLASS_BANNER=DESIGN()
CLASS_BANNER.ktftool()

VAR=0
Nametool=False

for eachArg in sys.argv:
	if eachArg=="-t":
		Nametool=sys.argv[VAR+1]
	VAR+=1

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

	def CallTool(self):
		for tool in root.findall('tool'):
			if Nametool == tool.get('name'):
				filename = tool.find('filename').text
				ToolToStart = importlib.import_module("tools."+filename)

				for eachArg in sys.argv:
					if eachArg=="-h":

						print colors[10]+" "+tool.get('name')+colors[0]
						print " Author "+ToolToStart.init.Author+" \n Description "+ToolToStart.init.Description+"\n"
						print " Args\tRQ\tDescription"
						ARGSTRUE=""
						for Namevalue in ToolToStart.init.Arguments:
							print " ["+Namevalue+"]\t"+str(ToolToStart.init.Arguments[Namevalue][0])+"\t"+str(ToolToStart.init.Arguments[Namevalue][1])
							if ToolToStart.init.Arguments[Namevalue][0]:
								ARGSTRUE+="-"+Namevalue+" value "
						print "\n USE: ktf.tool -m "+tool.get('name')+" "+ARGSTRUE+"\n"
						exit()

				VAR=0
				for Namevalue in ToolToStart.init.Arguments:
					ToolToStart.init.var.update({Namevalue:"null"})
					for eachArg in sys.argv:
						if eachArg=="-"+Namevalue:
							try:
								if sys.argv[VAR+1].find("-") >= 0 :ToolToStart.init.var.update({Namevalue:"enable"})
								else:ToolToStart.init.var.update({Namevalue:sys.argv[VAR+1]})
							except:ToolToStart.init.var.update({Namevalue:"null"})
						VAR+=1
					VAR=0

				ok=False
				p=""
				for Namevalue in ToolToStart.init.Arguments:
					if ToolToStart.init.Arguments[Namevalue][0]:
						for eachArg in ToolToStart.init.var:
							if eachArg==Namevalue:
								if ToolToStart.init.var[eachArg]!="null":ok=True
								else:p+="["+eachArg+"]"

				if p!="":
					printAlert(1,"These args is necesay '"+p+" use -h for more help.'\n")
					exit()


				ToolToStart.Main()
				Space()
				return
		printAlert(1,"The Tool not exists\n")

Tool=Tool()

if Nametool:Tool.CallTool()
