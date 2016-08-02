#!/usr/bin/env python
#HEAD#########################################################
#
# Katana Framework | ktf.tool                            
# Last Modified: 03/06/2016
#
#########################################################HEAD#

from core.Design import *
import importlib,argparse,sys,os
import xml.etree.ElementTree as ET

tree = ET.parse('core/tools.xml')
root = tree.getroot()

CLASS_BANNER=DESIGN()
CLASS_BANNER.ktftool()

VAR=0
Nametool=False

try:
	for eachArg in sys.argv:
		if eachArg=="-t":
			Nametool=sys.argv[VAR+1]
		VAR+=1

except:printAlert(1,"Check your Arguments")

class Tool:
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
								if sys.argv[-1] == "-"+Namevalue or sys.argv[VAR+1].find("-") >= 0:ToolToStart.init.var.update({Namevalue:"enable"})
								else:ToolToStart.init.var.update({Namevalue:sys.argv[VAR+1]})
							except:ToolToStart.init.var.update({Namevalue:"null"})
						VAR+=1
					VAR=0

				p=""
				for Namevalue in ToolToStart.init.Arguments:
					if ToolToStart.init.Arguments[Namevalue][0]:
						for eachArg in ToolToStart.init.var:
							if eachArg==Namevalue:
								if ToolToStart.init.var[eachArg]!="null" and ToolToStart.init.var[eachArg]!="enable":ok=True
								else:p+="["+eachArg+"]"

				if p!="":
					printAlert(1,"these arguments are necessary: '"+p+" use -h for more help.'\n")
					exit()


				ToolToStart.Main()
				Space()
				return

		if Nametool=="list":
			print " \t"+colors[7]+colors[2]+"CodeName\t\tDescription"+colors[0]
			for tool in root.findall('tool'):
				print " \t"+tool.get('name'),"\t\t",tool.find('description').text
			Space()
			return
		printAlert(1,"The Tool not exists\n")

Tool=Tool()
if Nametool:Tool.CallTool()
else:printAlert(1,"Check your Arguments\n       |Use '-t list' for tools list\n")
