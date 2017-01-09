# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES 

# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="2.1"
	init.Despcription       ="Generator of Dictionaries."
	init.CodeName           ="msc/gn.words"
	init.DateCreation       ="07/07/2015"      
	init.LastModification   ="09/01/2017"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME        VALUE                           RQ     DESCRIPTION
		'output'    :["/root/password-gen-katana.txt",True ,'Output File'],
		'longited'  :["6"                            ,False,'Longited key'],
		'charset'   :["chars_num"                    ,False,'Charset type']
	}

	init.aux  = "\n    (Chars)     descriptions"
	init.aux += " -> [chars_min] a,b,c,...,z"
	init.aux += " -> [chars_may] A,B,C,...,Z"
	init.aux += " -> [chars_num] 0,1,2,...,9"
	init.aux += " -> [chars_mix] a,b,...,0,1\n"
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):

	if init.var['charset'] != "chars_min" and init.var['charset'] != "chars_may" and init.var['charset'] != "chars_num" and init.var['charset'] != "chars_mix":
			printk.err("Error to set chars, use chars_min, chars_mix, chars_may or chars_num")
			init.var['charset']="chars_num"
			return

	Maxima=1
	long_max = long(init.var['longited']) 
	long_min = long(init.var['longited'])
	char_null = ['']
	chars_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	chars_may = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	chars_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	chars_spe = ['.', '-', '_', '/', '@']
	permitidos = []
	permitidos += char_null
	if init.var['charset'] == "chars_num":permitidos += chars_num
	if init.var['charset'] == "chars_may":permitidos += chars_may
	if init.var['charset'] == "chars_min":permitidos += chars_min
	if init.var['charset'] == "chars_mix":
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
	SYSTEM.Command_exe("Creating file...      ","echo  >"+init.var['output'], std=False)
	printk.inf("Generating... ["+str(Maxima)+"] Words to Generate "+str(porcent)+"% Complete")
	fichero = open(init.var['output'], 'w')
	bucle = True
	while bucle:
	    password = toClave(cadena)
	    fichero.write(password + '\n')
	    counter=counter+1
	    if procent == counter:
	    	procent=procent+procent
	    	porcent=porcent+20
	    	printk.inf(str(porcent)+"% Porcent Complete")
	    if isMax(cadena):
	    	porcent=porcent+20
	    	printk.inf(str(porcent)+"% Porcent Complete")
	    	bucle = False
	    cadena = aumentarCadena(cadena)
	printk.suff("Completed, output file in "+init.var['output'])
	Space()
	fichero.close()	

# END CODE MODULE ############################################################################################
