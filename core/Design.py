#!/usr/bin/env python2
# -*- coding: latin-1 -*-
#HEAD#########################################################
#
# Katana Framework | Design                            
# Last Modified: 14/03/2017
#
#########################################################HEAD#

import time
import Information
from Config import VERBOSE

colors=['\033[0m',   # 0}  WHITE
		'\033[31m',  # 1}  RED
		'\033[32m',  # 2}  YELLOW
		'\033[33m',  # 3}  PURPLE
		'\033[34m',  # 4}  CYAN
		'\033[35m',  # 5}  MAGENT
		'\033[36m',  # 6}  CURL ____
		'\033[1m',   # 7}  WHITE LOW
		'\033[4m',   # 8}  WHITE HIGH
		'\033[0m',   # 9}  WHITE (FUCK)
		'\033[40m',  # 10} BACKGROUND GREY
		'\033[41m',  # 11} BACKGROUND RED
		'\033[42m',  # 12} BACKGROUND GREEN
		'\033[43m']  # 13} BACKGROUND YELLOW

error      =colors[0]+"  ["+colors[7]+colors[1]+"err"+colors[0]+"]"
step       =colors[0]+"  ["+colors[1]+"stp"+colors[0]+"]"
information=colors[0]+"  ["+colors[4]+"inf"+colors[0]+"]"
success    =colors[0]+"  ["+colors[7]+colors[2]+"suf"+colors[0]+"]"
help       =colors[0]+"  ["+colors[7]+"hlp"+colors[0]+"]"
warning    =colors[0]+"  ["+colors[7]+colors[3]+"war"+colors[0]+"]"
runing     =colors[0]+"  ["+colors[2]+"run"+colors[0]+"]"
wait       =colors[0]+"  ["+colors[8]+"wait"+colors[0]+"]"
press      =colors[0]+"  ["+colors[8]+"press-key"+colors[0]+"]"


def MainPrompt()                    :return colors[7]+" [ktf]:"+colors[0]
def ClientPrompt(module,client)     :return colors[0]+" [ktf]("+colors[7]+colors[1]+module+colors[0]+":"+colors[9]+client+colors[0]+"):"+colors[0]
def Prompt(module)                  :return colors[0]+"  +[ktf]("+colors[7]+colors[1]+module+colors[0]+"):"+colors[0]
def ChangeValue(option, value)      :print "             ↳--------> "+option+" = "+value
def RunModule()                     :print " "+runing+" The module was launched...\n"+colors[0]+" "+information+" "+time.strftime('%c')+colors[0]

def Loadingfile(filename)           :print " "+information+" Loading file ["+filename+"]"+colors[0]
def Space()                         :print ""
def ModuleNotFound(nameModule)      :print " "+error+" The `"+nameModule+"` is Not Installed or not Exist.\n"
def NoExistsparameter()             :print " "+error+" The parameter is not Exist, type `show options`."
def helpAUX()                       :print " "+help+" Auxiliar module support"
def NoDeviceFound(device)           :print " "+error+" The device '"+device+"' not was Found.\n"
def CommandNotFound()               :print " "+warning+" Invalid parameter use show 'help' for more information"+colors[0]
def functionNotFound()              :print " "+warning+" The function not Exists"+colors[0]
def FunctionNoEnableForThisModule() :print " "+error+" This Commands just work in ktf.console mode."

class printk():
	def inf(self,msg):
		if VERBOSE==True:print " "+information+" "+str(msg)
	def err(self,msg):
		print " "+error+" "+str(msg)
	def suff(self,msg):
		print " "+success+" "+str(msg)
	def step(self,msg):
		print " "+step+" "+str(msg)
	def war(self,msg):
		print " "+warning+" "+str(msg)
	def wait(self,msg):
		print " "+wait+" "+str(msg)
	def pkey(self,msg):
		return "   | "+press+" "+str(msg)+"\n   |"

class DESIGN:
	
	def Line(self,CodeName,Description):
		appent_tab = ""
		if len(CodeName) < 14 : appent_tab = "\t"
		print colors[0]+"  "+colors[7]+CodeName+colors[0]+appent_tab+"\t\t"+Description
		
	def option(self,lot):
		more=""
		if lot == True : more = "["+colors[1]+"+"+colors[0]+"]"
		print "\n  [options]\t[RQ]\t[description]\t\t[value]"+more
		print "  ---------\t----\t-------------\t\t-------"

	def description(self, option, rq, description, value):
		if rq == True:
			rq=colors[2]+"yes"+colors[0]
		else:
			rq=colors[1]+"no"+colors[0]
		
		if len(option) > 5:
			option=option+"  "
		else:option=option+"\t"

		if len(description) > 15:
			description=description
		else:description=description+"\t"

		if len(description) < 8:
			description=description+"\t"

		print "  "+option+"\t"+rq+"\t"+description+"\t"+colors[8]+value+colors[0]

	def linker(self):print " \n [ktf]↣[linker]↘"
	def ktftool(self):print " \n [ktf]↣[tool]↘"
	def ktfktf(self):print " \n [ktf]↣[ktf]↘"
