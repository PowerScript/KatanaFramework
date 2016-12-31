#!/usr/bin/env python2
#HEAD#########################################################
#
# Katana Framework | Internal Core Intructions                           
# Last Modified: 24/12/2016
#
#########################################################HEAD#



from GeneralCommands import *
from Default import *
from Config import *
from Design import *

from Update import update
import xml.etree.ElementTree as ET
from xml.dom import minidom
from Information import version,build,date

import fcntl        ,struct   ,readline,rlcompleter,subprocess ,os
import threading    ,StringIO ,httplib ,commands   ,random ,re , json
import logging      ,urllib   ,Help    ,socket     ,time   ,sys

VARIABLESIP=[]
VARIABLESMAC=[]

Desing=DESIGN()
printk=printk()
G_KTFVAR=[]

### GENERAL ###
def KatanaCheckActionShowModules(action):
	if action == SHOW_MODULES or action == SHOW_MODULES_SHORT: return True

### UPDATE VARIABLES MODULE
def UpdateValue(action,matriz,real):
	for Namevalue in matriz.options:
		if action[len(SETET)+1:len(SETET)+1+len(Namevalue)] == Namevalue:
			checkValue=action[len(SETET)+2+len(Namevalue):]
			try:
				if checkValue[0:4] == "::IP" : checkValue = VARIABLESIP[int(checkValue[4:])-1]
				if checkValue[0:5] == "::MAC": checkValue = VARIABLESMAC[int(checkValue[5:])-1]
			except:printk.war("this value is recognized as an internal command but as it is not assigned to be used as value.")
			ChangeValue(Namevalue,checkValue)
			if real[Namevalue][0].isdigit():type_of_parameter = "integer"
			elif real[Namevalue][0] == "true" or real[Namevalue][0] == "false" : type_of_parameter = "boolean"
			else: type_of_parameter = "string"
			
			if checkValue.isdigit():type_of_value = "integer"
			elif checkValue == "true" or checkValue == "false" : type_of_value = "boolean"
			else: type_of_value = "string"
			
			if type_of_value != type_of_parameter:printk.war("the value you entered is not the same data type parameter.")
			matriz.options[Namevalue] = [checkValue,matriz.options[Namevalue][1],matriz.options[Namevalue][2]]
			return matriz
	try:
		for Namevalue in matriz.extra:
			if action[len(SETET)+1:len(SETET)+1+len(Namevalue)] == Namevalue:
				checkValue=action[len(SETET)+2+len(Namevalue):]
				if checkValue[0:4] == "::IP" : checkValue = VARIABLESIP[int(checkValue[4:])-1]
				if checkValue[0:5] == "::MAC": checkValue = VARIABLESMAC[int(checkValue[5:])-1]
				ChangeValue(Namevalue,checkValue)
				matriz.extra[Namevalue] = [checkValue,matriz.extra[Namevalue][1],matriz.extra[Namevalue][2]]
				return matriz
	except:Nothing=False
	NoExistsparameter()
	return matriz

def KatanaCheckActionSetValue(action):
	if action[:len(SETET)]==SETET            : return True
def KatanaCheckActionUseModule(action):
	if action[:len(SELECT)]==SELECT          : return True
def KatanaCheckActionGetInfo(action):
	if action[:len(GETINFO)]==GETINFO        : return True
def KatanaCheckActionShowOptions(action):
	if action == SHOW or action == SHOW_SHORT: return True
def KatanaCheckActionShowMOptions(action):
	if action == SHOW_MORE or action == SHOWM_SHORT: return True
def KatanaCheckActionExefunction(action):
	if action[:len("f::")] == "f::"          : return True
def KatanaCheckActionInvoke(action):
	if action[:len(INVOKE)]==INVOKE          : return True
def KatanaCheckActionSaveValue(action):
	if action[:4] == SAVEV                   : return True
def KatanaCheckActionisBack(action):
	if action==BACKING                       : return True
def KatanaCheckSession(action):
	if action[:len(SESSION)]==SESSION        : return True
def runModule(action):
	if action=="run"                         : 
		RunModule()
		return True

### SHOW INFORMATION MODULE ###
def ShowInformationModule(init):
	print "     |->Author  : "+str(init.Author)            
	print "     |->Version : "+str(init.Version)           
	print "     |->Description : "+str(init.Description)       
	print "     |->CodeName : "+str(init.CodeName)          
	print "     |->DateCreation : "+str(init.DateCreation)        
	print "     |->LastModification : "+str(init.LastModification)
	print "     |->References : "+str(init.References)         
	print "     |->License : "+str(init.License)

### GLOBAL COMMANDS ###
def KatanaCheckActionGlobalCommands(action):
	if     action[:len(EXIT)]        == EXIT   or action[:len(EXIT)]        == EXIT_SHORT  : sys.exit(1995)
	elif   action[:len(HELP)]        == HELP   or action[:len(HELP_SHORT)]  == HELP_SHORT  : Help.help()
	elif   action[:len("version")]   == "version"        :printk.suff("V:["+version+"] B:["+build+"] D:["+date+"]")
	elif   action                    == UPDATE or action                    == UPDATE_SHORT: update("functions",True)
	elif action[:len(EXECUTECOMMAND)]==EXECUTECOMMAND    :subprocess.call(action[len(EXECUTECOMMAND):], shell=True)
	elif   action[:len(CLEAR)]       == CLEAR  or action[:len(CLEAR_SHORT)] == CLEAR_SHORT : subprocess.call('clear', shell=True)
	elif   action[:len(SAVEV)]       == SAVEV            :SaveValue(action)
	elif   action                    == ""               :return
	else                                                 :CommandNotFound()


### CALL MODULE ###
def Invoke(module):
	subprocess.Popen(["xterm","-T","Invoke["+module[len(INVOKE)+1:]+"]","-e","python2","ktf.run","-m",module[len(INVOKE)+1:],"-q"])

### SHOW OPTIONS ###
def ShowOptions(Options):
	lot = False
	try:
		if Options.extra : lot = True
	except:b=0

	Desing.option(lot)

	for VAR in Options.options:
	 	Desing.description(str(VAR),Options.options[VAR][1],str(Options.options[VAR][2]),str(Options.options[VAR][0]))
	Space()
	try:
		if Options.aux:
			helpAUX()
			print Options.aux
	except:b=0

### SHOW FULL OPTIONS ###
def ShowFullOptions(Options):
	Desing.option(True)
	for VAR in Options.options:
	 	Desing.description(str(VAR),Options.options[VAR][1],str(Options.options[VAR][2]),str(Options.options[VAR][0]))
	Space()

	try:
		for VAR in Options.extra:
		 	Desing.description(str(VAR),Options.extra[VAR][1],str(Options.extra[VAR][2]),str(Options.extra[VAR][0]))
		Space()
	except:b=0
		
	try:
		if Options.aux:
			helpAUX()
			print Options.aux
	except:b=0

### GLOBALS VARIABLES ###
def SaveValue(secuence):
	try:
		if secuence[len(SAVEV):len(SAVEV)+2].lower()=="ip":
			nID  = int(secuence[len(SAVEV)+3:])-1
		 	grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', G_KTFVAR[nID])
		 	address = grab[0]
			VARIABLESIP.append(address)
		 	N=len(VARIABLESIP)
		 	GlobalVariable("+","IP",address)
			printk.suff("---> variable Saved {"+colors[8]+"::IP"+str(N)+colors[0]+"} "+address)

		if secuence[len(SAVEV):len(SAVEV)+4].lower()=="list":
			print "     |-->VARIABLES IP"
			index = 1 
			for value in VARIABLESIP:
				print "     | ::IP"+str(index)+" --> "+value
				index+=1
			print "     |-->VARIABLES MAC"
			index = 1 
			for value in VARIABLESMAC:
				print "     | ::MAC"+str(index)+" --> "+value
				index+=1

		if secuence[len(SAVEV):len(SAVEV)+3].lower()=="del":
			if secuence[len(SAVEV)+4 : len(SAVEV)+6].upper() == "IP"  : GlobalVariable("-", "IP", secuence[len(SAVEV)+6 : ])
			if secuence[len(SAVEV)+4 : len(SAVEV)+7].upper() == "MAC" : GlobalVariable("-","MAC", secuence[len(SAVEV)+7 : ])
			if secuence[len(SAVEV)+4 : len(SAVEV)+5].upper() == "*"   : GlobalVariable("-", "*" , "*")
			LoadGlobalVariables()

		if secuence[len(SAVEV):len(SAVEV)+3].lower()=="mac":
		 	nID  = int(secuence[len(SAVEV)+4:])-1
		 	p = re.compile(ur'([0-9a-f]{2}(?::[0-9a-f]{2}){5})', re.IGNORECASE)
		 	address=re.findall(p, G_KTFVAR[nID])
		 	address=str(address)
		 	address=address.replace("'","")
		 	address=address.replace("[","")
		 	address=address.replace("]","")
		 	VARIABLESMAC.append(address)
		 	N=len(VARIABLESMAC)
		 	GlobalVariable("+","MAC",address)
			printk.suff("---> variable Saved {"+colors[8]+"::MAC"+str(N)+colors[0]+"} "+address)

	except : printk.war("Check Again your Command for Global variables.")

### MAQUETAR ###
def Maquetar(matriz):
	MMM = len(matriz[0])
	NNN = len(matriz)
	MAY = []
	VAR = 0
	MAYC = 0 
	VARB = 0
	while VAR != MMM:
		while VARB != NNN:
			if MAYC < len(matriz[VARB][VAR]):MAYC=len(matriz[VARB][VAR])
			VARB+=1
		MAY+=[MAYC]
		MAYC=0
		VAR+=1 
		VARB=0

	SUM = 0
	VAR = 0
	while VAR != len(MAY):
		SUM=SUM+MAY[VAR]
		VAR+=1


	VAR = 0
	LINE = " "
	while VAR != MMM:
		VARC=0
		ADDS=" "
		DIF = MAY[VAR] - len(matriz[0][VAR])
		if DIF != 0:
			while VARC != DIF:
				ADDS+=" "
				VARC+=1
		LINE += colors[13]+colors[10]+matriz[0][VAR]+ADDS+colors[0]
		VAR+=1
	print LINE

	VAR = 1
	VARB = 0
	LINE = " "
	while VAR != NNN:
		while VARB != MMM:
			ADDS =" "
			VARC=0
			DIF  = MAY[VARB] - len(matriz[VAR][VARB])
			if DIF != 0:
				while VARC != DIF:
					ADDS+=" "
					VARC+=1
			LINE += matriz[VAR][VARB]+ADDS
			VARB+=1
		LINE+="\n "
		VARB=0
		VAR+=1

	print LINE+"\n"


### LOG's ###
def saveRegister(init, data):  
	SET = ""
	for VAR in init.options:
		SET += "["+VAR+"|"+init.options[VAR][0]+"]"
	log=open('core/logs/register.log','a')
	log.write('\n ===================================== ')
	log.write('\n Module  : '+init.CodeName)
	log.write('\n Date    : '+time.strftime('%c'))
	log.write('\n Attack  : '+SET)
	log.write('\n Data    : '+data)
	log.close()

def SaveErrorLog(event):
	log=open('core/logs/Errors.log','a')
	log.write('\n Date    : '+time.strftime('%c'))
	log.write('\n info    : '+str(event))
	log.close()


### MAKE TABLES ###
def MakeTable(matriz):
	print "   "+colors[7]+"|"+colors[0]+" "
	MMM = len(matriz[0])
	NNN = len(matriz)
	MAY = []
	VAR = 0
	MAYC = 0 
	VARB = 0
	while VAR != MMM:
		while VARB != NNN:
			if MAYC < len(matriz[VARB][VAR]):MAYC=len(matriz[VARB][VAR])
			VARB+=1
		MAY+=[MAYC]
		MAYC=0
		VAR+=1 
		VARB=0

	SUM = 0
	VAR = 0
	while VAR != len(MAY):
		SUM=SUM+MAY[VAR]
		VAR+=1

	VAR = 0
	R="----------"
	while VAR != SUM:
		R+="-"
		VAR+=1
	print "   "+colors[7]+R+colors[0]

	VAR = 0
	LINE = "   "+colors[7]+"|"+colors[0]
	while VAR != MMM:
		VARC=0
		ADDS=""
		DIF = MAY[VAR] - len(matriz[0][VAR])
		if DIF != 0:
			while VARC != DIF:
				ADDS+=" "
				VARC+=1
		LINE += " "+colors[7]+colors[3]+matriz[0][VAR]+ADDS+colors[0]+" |"
		VAR+=1
	print LINE
	print "   "+colors[7]+R+colors[0]

	VAR = 1
	VARB = 0
	LINE = "   "+colors[7]+"|"+colors[0]
	while VAR != NNN:
		while VARB != MMM:
			ADDS =""
			VARC=0
			DIF  = MAY[VARB] - len(matriz[VAR][VARB])
			if DIF != 0:
				while VARC != DIF:
					ADDS+=" "
					VARC+=1
			LINE += colors[8]+" "+matriz[VAR][VARB]+ADDS+" "+colors[0]+colors[7]+"|"+colors[0]
			VARB+=1
		LINE+="\n   "+colors[7]+"|"+colors[0]
		VARB=0
		VAR+=1

	print LINE+colors[7]+R[:-2].replace(" ","")+"|\n   |"+colors[0]

### GET NUMBER MODULES INSTALLED ###
def get_number_modules():
	tree = ET.parse('core/modules.xml')
	root = tree.getroot()
	Number=0
	for modules in root.findall('module'):
		Number+=1
	return Number

### GET NUMBER MODULES INSTALLED ###
def get_number_tools():
	tree = ET.parse('core/tools.xml')
	root = tree.getroot()
	Number=0
	for modules in root.findall('tool'):
		Number+=1
	return Number

class MyCompleter(object):  
    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  
            if text:  
                self.matches = [s for s in self.options 
                                    if s and s.startswith(text)]
            else:  
                self.matches = self.options[:]
        try: 
            return self.matches[state]
        except IndexError:
            return None

### LOAD BUFFER ###
def LoadBuffer():
	completer = MyCompleter([SETET, GETINFO, EXECUTECOMMAND, CLEAR, SHOW_MODULES, "target", "port", "version", "f::",RUN, UPDATE, SHOW_MORE, SESSION])
	readline.set_completer(completer.complete)
	readline.parse_and_bind('tab: complete')


### LIST MODULES INSTALLED ###
def ListModules():
	tree = ET.parse('core/modules.xml')
	root = tree.getroot()
	print colors[7]+colors[1]+"\n   CodeName\t\t\tDescription"+colors[0]
 	space_category = "web"
 	for modules in root.findall('module'):
		name = modules.get('name')
		if space_category !=  name[:3]:
			space_category=name[:3]
		description = modules.find('description').text
		Desing.Line(CodeName=name,Description=description)
	print ""

### GET ROOT VARIABLE MODULES INSTALLED ###
def GetRootModules():
	tree = ET.parse(FOLDER_KATANA+'core/modules.xml')
	root = tree.getroot()
	return root


### SAVE SESSIONS ###
def SaveSession(init):
	if SAVE_SESSIONS:
		time_current=time.strftime('%c')
		log="{ \"Session\" : {  \"Module\" : \""+init.CodeName+"\", \"Time\" : \""+time_current+"\" , \"Options\" : ["
		for option in init.options:
			log+="{ \""+option+"\" : \""+init.var[option]+"\"},"
		log += "{\"ktf\":\"ktf\"}] , \"Extra\" : ["
		try:
			for option in init.extra:
				log+="{ \""+option+"\" : \""+init.var[option]+"\"},"
			log += "{\"ktf\":\"ktf\"}"
		except:value=False
		log += "]}}"
		time_current=time_current.replace(" ","_")
		Modules = str(init.CodeName)
		Modules = Modules.split("/")
		time_file_name=time.strftime('%d:%m:%Y_%H:%M:%S')
		logs=open('core/sessions/'+time_file_name+'_'+Modules[0]+"-"+Modules[1]+'.session','a')
		logs.write(log)
		logs.close()

### SESSION OPTIONS ###
def SessionInterative(action,init):
	Array_list = []
	counter = 0
	if True:
		module = init.CodeName
		module = module.replace("/","-")+".session"

		a = [s for s in os.listdir("core/sessions/")
			if os.path.isfile(os.path.join("core/sessions/", s))]
		a.sort(key=lambda s: os.path.getmtime(os.path.join("core/sessions/", s)))

		for FileName in reversed(a):
			ope = len(FileName)-(len(module))
			if FileName[ope:]==module:
				Array_list.append(FileName)

	if action[(len(SESSION)+1):(len(SESSION)+3)] == "-l":
		for FileName in Array_list:
			print "     | #"+str(counter)+" "+FileName
			counter+=1

	if action[(len(SESSION)+1):(len(SESSION)+3)] == "-v":
		index = action[(len(SESSION)+4):]
		data_file   = open('core/sessions/'+Array_list[int(index)],'r')
		data_string = json.loads(data_file.read())
		data_file.close()
		print "     | Session   ["+data_string['Session']['Time']+"]"
		for opt in data_string['Session']['Options']:
			for key, value in opt.items():
				print "     | Parameter = "+key+" --> "+value
		try:
			for opt in data_string['Session']['Extra']:
				for key, value in opt.items():
					print "     | Parameter = "+key+" --> "+value
		except:extra=False

	if action[(len(SESSION)+1):(len(SESSION)+3)] == "-d":
		index = action[(len(SESSION)+4):]
		if index=="*" : subprocess.call('rm core/sessions/*.session', shell=True)
		else:subprocess.call('rm core/sessions/'+Array_list[int(index)], shell=True)

	if action[(len(SESSION)+1):(len(SESSION)+3)] == "-i":
		index = action[(len(SESSION)+4):]
		data_file   = open('core/sessions/'+Array_list[int(index)],'r')
		data_string = json.loads(data_file.read())
		data_file.close()
		for opt in data_string['Session']['Options']:
			for key, value in opt.items():
				if key != "ktf" and value != "ktf":init.options[key]=[value,init.options[key][1],init.options[key][2]]
		try:
			for opt in data_string['Session']['Extra']:
				for key, value in opt.items():
					if key != "ktf" and value != "ktf":init.options[key]=[value,init.options[key][1],init.options[key][2]]
		except:extra=False
	return init

### LOAD SESSIONS ###
def LoadSession(init):
	original = init
	
	if AUTO_LOAD_SESSION:
		try:
			return SessionInterative("session -i 0",init)
		except:err="No exists sessions."
	return original

### LOAD GLOBAL VARIABLES ###
def LoadGlobalVariables():

	for value in  VARIABLESIP:
		VARIABLESIP.remove(value)

	for value in  VARIABLESMAC:
		VARIABLESMAC.remove(value)

	data_file   = open('core/logs/variables.globals.json','r')
	data_string = json.loads(data_file.read())

	for value in  data_string['variable_IP']:
		VARIABLESIP.append(str(value))
	for value in  data_string['variable_MAC']:
		VARIABLESMAC.append(str(value))

### GLOBAL VARIABLE ###
def GlobalVariable(action,typev,variable):
	try:
		with open('core/logs/variables.globals.json', 'r+') as jsond:
			data = json.load(jsond)

			if action == "+":
				if typev == "IP"  : data["variable_IP"].append(variable)
				if typev == "MAC" : data["variable_MAC"].append(variable)

			if action == "-":
				if typev == "IP"  : del data["variable_IP"][(int(variable) - 1)]
				if typev == "MAC" : del data["variable_MAC"][(int(variable) - 1)]
				if typev == "*"   :

					for value in  data["variable_IP"]:
						data["variable_IP"].remove(value)

					for value in  data["variable_MAC"]:
						data["variable_MAC"].remove(value)

			jsond.seek(0)  
			jsond.write(json.dumps(data))
			jsond.truncate()

	except Exception as Error: printk.err(Error)

### UPDATE INTERNAL VARIABLES OF MODULE ###
def UpdateInternalModule(init):

	for Namevalue in init.options:
		init.var.update({Namevalue:init.options[Namevalue][0]})
	
	try:
		for Namevalue in init.extra:
			init.var.update({Namevalue:init.extra[Namevalue][0]})
	except:Nothing=False

	return init
