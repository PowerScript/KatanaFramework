#
# Katana framework 
# @Katana Design
#

# 
# Core::Theme>Warrior
#

import time


		#White    #Red          #Green      #Orange    #Blue       #Purple     #Cyan
colors=['\033[0m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m'
		,'\033[1m', '\033[4m', '\033[0m', '\033[40m']
		#Bold       #Underl     #ENDL       #BackBlack

# Alerts 
Bad=colors[0]+"["+colors[1]+"Err"+colors[0]+"]"
Alr=colors[0]+"["+colors[4]+"Inf"+colors[0]+"]"
God=colors[0]+"["+colors[2]+"Run"+colors[0]+"]"
Suf=colors[0]+"["+colors[2]+"SUF"+colors[0]+"]"
Hlp=colors[0]+"["+colors[7]+"HLP"+colors[0]+"]"
Got=colors[0]+"["+colors[8]+"-->"+colors[0]+"]"
Ned=colors[0]+"["+colors[1]+"Err"+colors[0]+"]"
Nrs=colors[0]+"["+colors[1]+"NRS"+colors[0]+"]"
War=colors[0]+"["+colors[3]+"WAR"+colors[0]+"]"

#print colors[0]+"0"+colors[1]+"1"+colors[2]+"2"+colors[3]+"3"+colors[4]+"4"+colors[5]+"5"+colors[6]+"6"+colors[7]+"7"+colors[8]+"8"+colors[9]+"9"+colors[10]+"10"

class DESIGN:
	def messages(self, message):
		if module == 1:
			print " test module"
	def prompt(self, module):
		promp=""+colors[0]+" \033[1mktn"+colors[0]+"::\033[4m"+colors[3]+module+colors[0]+" \033[1m\033[40m>"+colors[0]
		return promp
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
		print " "+God+" Loaded file "+colors[0]
	def filenot(self, files):
		print " "+Bad+" Dictionary Not found : '"+files+"'"+colors[0]+", Check againt the parameters.\n"
	def no_file_found(self, files):
		print " "+Bad+" File Not found : '"+files+"'"+colors[0]+", Check againt the parameters.\n"
	def Client_prompt(self,client):
		return colors[1]+" CLT~"+colors[3]+""+client+"/> "+colors[0]
	def noptions(self):
		print "\n Options ["+colors[1]+"disabled"+colors[0]+"], you relax just "+colors[2]+"run"+colors[0]+" it...\n"
	def Success(self, username, password):
		print "\n-"+Suf+" Successfully with [username="+username+"][password="+password+"]\n"
	def nodataallow(self):
		print " "+Bad+" parameter not allow"+colors[0]
	def No_match(self):
		print " "+Bad+" Username or password no match, Check againt the parameters.\n"
	def helpAUX(self):
		print "\n "+Hlp+" Auxiliar Help\n"
	def noconnect(self):
		string=" "+Ned+" Not connected to any network, this module need are connected to a network."
		return string
	def go(self,to):
		print " "+Got+" Go to : \033[40m"+to+""+colors[0]
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
		print " "+Bad+" The divice '"+device+"' not was Found.\n"
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
