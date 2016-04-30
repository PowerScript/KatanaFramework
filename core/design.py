#!/usr/bin/env python
#HEADER#######################
# Katana framework           #
# Design file (Theme)        #
# Last Modified: 30/04/2016  #
# Review: 1                  #
#######################HEADER#

import time
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

# ALERTs
Bad=colors[0]+"["+colors[1]+"ERR"+colors[0]+"]"
Alr=colors[0]+"["+colors[4]+"INF"+colors[0]+"]"
God=colors[0]+"["+colors[2]+"RUN"+colors[0]+"]"
Suf=colors[0]+"["+colors[2]+"SUF"+colors[0]+"]"
Hlp=colors[0]+"["+colors[7]+"HLP"+colors[0]+"]"
Got=colors[0]+"["+colors[8]+"-->"+colors[0]+"]"
Nrs=colors[0]+"["+colors[1]+"NRS"+colors[0]+"]"
War=colors[0]+"["+colors[3]+"WAR"+colors[0]+"]"

class DESIGN:
	def Line(self,CodeName,Description):
		print colors[0]+" |"+colors[1]+"=="+colors[0]+"|::|  "+colors[7]+CodeName+colors[0]+"\t\t"+Description
	def MainPrompt(self):
		return colors[11]+" KTF>"+colors[0]
	def prompt(self, module):
		return colors[11]+" KTF>"+colors[10]+colors[7]+module+colors[0]+">"+colors[0]
	def option(self):
		print "\n [options]\t[RQ]\t[description]\t\t[value]"
		print " ---------\t----\t-------------\t\t-------"
	def descrip(self, option, rq, description, value):
		if rq == "yes":
			rq=colors[2]+"yes"+colors[0]
		else:
			rq=colors[1]+"no"+colors[0]
		print " "+option+"\t""\t"+rq+"\t"+description+"\t\t"+colors[8]+value+colors[0]
	def change(self, option, value):
		print "\n "+option+"\t\t==> "+value+"\n"
	def goodbye(self):
		print "\n "+colors[0]+"Exiting...      Goodbye, My Sr.\n"
	def run(self):
		print "\n "+God+" Running..."+colors[0]
		print " "+Alr+" "+time.strftime('%c')+colors[0]
	def target_off(self, target):
		print " "+Bad+" target Off-line ["+target+"]"+colors[0]+"\n"
	def No_actions(self):
		print " "+Alr+" Invalid parameter use show 'help' for more information"+colors[0]
	def kbi(self):
		print "\n "+Alr+" Keyboard Interrupt"+colors[0]
	def loading_file(self):
		print " "+Alr+" Loading files..."+colors[0]
	def loaded(self):
		print " "+Suf+" Loaded file "+colors[0]
	def filenot(self, files):
		print " "+Bad+" Dictionary Not found : '"+files+"'"+colors[0]+", Check againt the parameters.\n"
	def no_file_found(self, files):
		print " "+Bad+" File Not found : '"+files+"'"+colors[0]+", Check againt the parameters.\n"
	def Client_prompt(self,client):
		return colors[11]+" KTF>"+colors[10]+colors[7]+client+colors[0]+">"+colors[0]
	def noptions(self):
		print "\n Options ["+colors[1]+"disabled"+colors[0]+"], you relax just "+colors[2]+"run"+colors[0]+" it...\n"
	def Success(self, username, password):
		print "\n-"+Suf+" Successfully with [username="+username+"][password="+password+"]\n"
	def nodataallow(self):
		print " "+Bad+" parameter not allow"+colors[0]
	def ModuleNotFound(self,nameModule):
		print " "+Bad+" The `"+nameModule+"` is Not Installed or not Exist.\n"
	def No_match(self):
		print " "+Bad+" Username or password no match, Check againt the parameters.\n"
	def helpAUX(self):
		print "\n "+Hlp+" Auxiliar Help\n"
	def KtfRun(self):
		print colors[11]+" KTF.RUN "+colors[0]+colors[7]+time.strftime('%c')+colors[0]
	def Noconnect(self):
		print " "+Ned+" Not connected to any network, this module need are connected to a network."
	def go(self,to):
		print " "+Got+" Go to : \033[40m"+to+""+colors[0]
	def Helper(self):
		print " ["+colors[1]+"!"+colors[0]+"] Invalid parameter use show 'help' for more information"+colors[0]
	def testing(self, protocol, port):
		print " "+Alr+" Testing "+protocol+" protocol \t\t\t ["+port+"]"
	def live_protocol(self):
		print " "+God+" Service LIVE "
	def space(self):
		print ""
	def nocommandCLT(self, string):
		return "parameter '"+string+"' not allow."
	def VError(self):
		print " "+Bad+" Value Error: [LINKER] is necesary all parameters, type 'sop'."
	def NoDeviceFound(self, device):
		print " "+Bad+" The device '"+device+"' not was Found.\n"
	def Nosuchdevice(self):
		print " "+Bad+" No such device.\n"
	def Noresult(self):
		print " "+Nrs+" Attack ended without any results."
	def ktflab(self,version,build):
		print """
		   __   __  ___"""+colors[3]+"""__     __     """+colors[0]+"""
		  / /__/ /_/ _/"""+colors[3]+""" /__ _/ /     """+colors[0]+"""
		 /  '_/ __/ _/"""+colors[3]+""" / _ `/ _ \\   """+colors[0]+"""
		/_/\_\\\\__/_/"""+colors[3]+"""/_/\_,_/_.__/  """+colors[0]+"""
		Core:"""+version+"""/build:"""+build 
	def linker(self,version, build):
		print """
		   __   __  ___"""+colors[4]+"""___      __             """+colors[0]+"""
		  / /__/ /_/ _/"""+colors[4]+""" (_)__  / /_____ ____   """+colors[0]+"""
		 /  '_/ __/ _/"""+colors[4]+""" / / _ \/  '_/ -_) __/   """+colors[0]+"""
		/_/\_\\\\__/_/"""+colors[4]+"""/_/_/_//_/_/\_\\\\__/_/  """+colors[0]+"""
		Core:"""+version+"/Build:"+build
	def ktfrun(self,version,build):
		print """
		   __   __  ___            
		  / /__/ /_/ _/"""+colors[1]+"""_____ _____      """+colors[0]+"""
		 /  '_/ __/ _/"""+colors[1]+"""_ __/ // / _ \\   """+colors[0]+"""
		/_/\_\\\\_/__/ """+colors[1]+"""/_/  \_,_/_//_/  """+colors[0]+"""
		Core:"""+version+"""/Build:"""+build+"\n"
