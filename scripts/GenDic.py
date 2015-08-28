# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# @KATANA                    #
# Modules   : GenDictionary  #
# Script by : Uknowk         #
# Adated by : RedToor        #
# Date      : 07/07/2015     #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Katana Core                #
from core.design import *    #
from core import help        #
from core import ping        #
d=DESIGN()                   #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Libraries                  #
import time                  #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
# Default                    #
# :-:-:-:-:-:-:-:-:-:-:-:-:- #
defaultdic="/root/Desktop/Dictionary.txt"
defaultlon="5"
defaultstr="chars_num"
# :-:-:-:-:-:-:-:-:-:-:-:-:- #

def run(para,parb,parc):
	global defaultdic,defaultlon,defaultstr
	defaultdic=para
	defaultlon=parb
	defaultstr=parc
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
			print ""
			print " "+Hlp+" Auxiliar help\n"
			print " chars_min = [a,b,c,...,z]"
			print " chars_may = [A,B,C,...,Z]"
			print " chars_num = [0,1,2,...,9]"
			print " chars_mix = [a,b,...,0,1]"
			print ""
			Gendic(0)
		elif actions[0:8] == "set path":
				defaultdic = actions[9:]
				d.change("path",defaultdic)
				Gendic(0)
		elif actions[0:8] == "set long":
				defaultlon = actions[9:]
				d.change("long",defaultlon)
				Gendic(0)
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
				print total_chars
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
				fichero = open(defaultdic, 'w')
				bucle = True
				while bucle:
				    password = toClave(cadena)
				    fichero.write(password + '\n')
				    print " Generating "+password
				    if isMax(cadena):
				    	bucle = False
				    cadena = aumentarCadena(cadena)
				print(" "+Suf+" Complete, output file in "+defaultdic)
				fichero.close()
			except(KeyboardInterrupt, SystemExit):
				d.kbi()
	except:
		d.kbi()
		exit()
	Gendic(0)