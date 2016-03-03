# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : GenDictionary  #
# Script by : Uknowk         #
# Adated by : RedToor        #
# Date      : 07/07/2015     #
# Version   : 2.1            #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Katana Core                #
from core.design import *    #
from core.Setting import *   #
from core import Errors      #
from core import help        #
from core import ping        #
import sys                   #
d=DESIGN()                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Libraries                  #
import time                  #
import os                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaultdic="/root/password-gen-katana.txt"
defaultlon=DEFAUTL_LONGITED
defaultstr="chars_min"
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(dictionary, length, types):
	global defaultdic,defaultlon,defaultstr
	defaultdic=dictionary
	defaultlon=defaultlon
	defaultstr=types
	Gendic(1)

def Gendic(run):
	try:
		global defaultdic,defaultlon,defaultstr
		if run!=1:
			actions=raw_input(d.prompt("mc/gendic"))
		else:
			actions="run"
		if actions == "show options" or actions == "sop":
			d.option()
			d.descrip("path","yes","Output file",defaultdic)
			d.descrip("long","yes","Longitude",defaultlon)
 			d.descrip("type","yes","Type matrix",defaultstr)
			d.helpAUX()
			print " "+colors[7]+"Type        Description"+colors[0]
			print " chars_min = [a,b,c,...,z]"
			print " chars_may = [A,B,C,...,Z]"
			print " chars_num = [0,1,2,...,9]"
			print " chars_mix = [a,b,...,0,1]"
			d.space()
			Gendic(0)
		elif actions[0:8] == "set path":
			defaultdic=ping.update(defaultdic,actions,"path")
			d.change("path",defaultdic)
		elif actions[0:8] == "set long":
			defaultlon=ping.update(defaultstr,actions,"long")
			d.change("long",defaultlon)
		elif actions[0:8] == "set type":
				defaultstr = actions[9:]
				if defaultstr != "chars_min" and defaultstr != "chars_may" and defaultstr != "chars_num" and defaultstr != "chars_mix":
					print " "+Alr+" Error to set type, use chars_min, chars_mix, chars_may or chars_num"
					defaultstr="chars_num"
					Gendic(0)
				else:
					defaultstr=defaultstr
					d.change("type",defaultstr)
					Gendic(0)
		elif actions=="exit" or actions=="x":
			d.goodbye()
			exit()
		elif actions=="help" or actions=="h":
			help.help()
		elif actions=="back" or actions=="b":
			return
		elif actions=="run"  or actions=="r":
			d.run()
			try:
				Maxima=1
				long_max = long(defaultlon) 
				long_min = long(defaultlon)
				char_null = ['']
				chars_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
				chars_may = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
				chars_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
				chars_spe = ['.', '-', '_', '/', '@']
				permitidos = []
				permitidos += char_null
				if defaultstr == "chars_num":
					permitidos += chars_num
				if defaultstr == "chars_may":
					permitidos += chars_may
				if defaultstr == "chars_min":
					permitidos += chars_min
				if defaultstr == "chars_mix":
					permitidos +=chars_min
					permitidos +=chars_num
				total_chars = len(permitidos)
				char_n_max = total_chars - 1
				cadena = []
				for chars in range(0, long_max):
					cadena += [0]
				for i in range (1, long_min+1):
					cadena[-(i)] = 1
				cadena_max = []
				for chars in range(0, long_max):
					cadena_max += [ total_chars -1 ]
				def toClave(cadena1):
					password = ""
					for indice in cadena1:
						password += permitidos[indice]
					return password
				def isMax(cadena1):
					if toClave(cadena1) != toClave(cadena_max):
						return False
					return True
				def aumentarCadena(cadena1):
					unidad = 1
					acarreo = 0
					for digito in range(1,long_max +1):
						if cadena[-(digito)] < char_n_max:
							if unidad == 1:
								cadena[-(digito)] += 1
								unidad = 0
								return cadena1
							elif acarreo == 1:
								cadena[-(digito)] += 1
								acarreo = 0
								return cadena1
						else: 
							cadena[-(digito)] = 1
							acarreo = 1
					return cadena1
				for number_total in cadena_max:
					Maxima=Maxima*number_total
				procent=int(Maxima)/10
				counter=0
				porcent=0
				print " "+Alr+" Creating file...      ",ping.status_cmd("echo  >"+defaultdic, "\t\t\t")
				print " "+Alr+" Generating... ["+str(Maxima)+"] Words to Generate "+str(porcent)+"% Complete"
				fichero = open(defaultdic, 'w')
				bucle = True
				while bucle:
				    password = toClave(cadena)
				    fichero.write(password + '\n')
				    counter=counter+1
				    if procent == counter:
				    	procent=procent+procent
				    	porcent=porcent+20
				    	print " "+War+" "+str(porcent)+"% Porcent Complete"
				    if isMax(cadena):
				    	porcent=porcent+20
				    	print " "+War+" "+str(porcent)+"% Porcent Complete"
				    	bucle = False
				    cadena = aumentarCadena(cadena)
				print(" "+Suf+" Completed, output file in "+defaultdic)
				d.space()
				fichero.close()
			except:
				Errors.Errors(event=sys.exc_info(), info=False)
		else:
			d.No_actions()
	except:
		Errors.Errors(event=sys.exc_info(), info=False)
	Gendic(0)
