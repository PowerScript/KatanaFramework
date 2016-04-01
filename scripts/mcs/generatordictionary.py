# This module requires katana framework 
# https://github.com/RedToor/Katana
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                 #
from core.design import *     #
from core.Setting import *    #
from core import Errors       #
from core import getFunction  #
import sys                    #
Message=DESIGN()              #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="RedToor"
	initialize.Version            ="2.1"
	initialize.Despcription       ="Generator of Dictionaries."
	initialize.CodeName           ="msc/gn.words"
	initialize.DateCreation       ="07/07/2015"      
	initialize.LastModification   ="25/03/2016"

	# DEFAULT VARIABLES             VALUE                              NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[["/root/password-gen-katana.txt" , "output" , "yes" , "Output file"]]  #[0][0]
	initialize.DEFAULT_VARIABLE  +=[[DEFAUTL_LONGITED                , "long"   , "no"  , "Longited"]]     #[1][0]
	initialize.DEFAULT_VARIABLE  +=[["chars_min"                     , "chars"  , "no"  , "Chars word"]]   #[2][0]
initialize()
# END INFORMATION MODULE

# MAIN FUNCTION
def main(run):
	try:
		# HEAD MODULE
		if run:	actions=raw_input(Message.prompt(initialize.CodeName))
		else  : actions="run"
		if   getFunction.KatanaCheckActionShowOptions(actions):
			getFunction.ShowOptions(initialize.DEFAULT_VARIABLE)
			Message.helpAUX()
			print " "+colors[7]+"Type        Description"+colors[0]
			print " chars_min = [a,b,c,...,z]"
			print " chars_may = [A,B,C,...,Z]"
			print " chars_num = [0,1,2,...,9]"
			print " chars_mix = [a,b,...,0,1]"
			Message.space()
		elif getFunction.KatanaCheckActionSetValue(actions)   :initialize.DEFAULT_VARIABLE=getFunction.UpdateValue(actions,initialize.DEFAULT_VARIABLE)
		elif getFunction.KatanaCheckActionisBack(actions)     :return
		# END HEAD MODULE
		elif getFunction.runModule(actions):
			Message.run()
			# CODE MODULE    ############################################################################################
			if initialize.DEFAULT_VARIABLE[2][0] != "chars_min" and initialize.DEFAULT_VARIABLE[2][0] != "chars_may" and initialize.DEFAULT_VARIABLE[2][0] != "chars_num" and initialize.DEFAULT_VARIABLE[2][0] != "chars_mix":
					print " "+Alr+" Error to set chars, use chars_min, chars_mix, chars_may or chars_num"
					initialize.DEFAULT_VARIABLE[2][0]="chars_num"
					main(True)
			if True:
				Maxima=1
				long_max = long(initialize.DEFAULT_VARIABLE[1][0]) 
				long_min = long(initialize.DEFAULT_VARIABLE[1][0])
				char_null = ['']
				chars_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
				chars_may = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
				chars_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
				chars_spe = ['.', '-', '_', '/', '@']
				permitidos = []
				permitidos += char_null
				if initialize.DEFAULT_VARIABLE[2][0] == "chars_num":
					permitidos += chars_num
				if initialize.DEFAULT_VARIABLE[2][0] == "chars_may":
					permitidos += chars_may
				if initialize.DEFAULT_VARIABLE[2][0] == "chars_min":
					permitidos += chars_min
				if initialize.DEFAULT_VARIABLE[2][0] == "chars_mix":
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
				print " "+Alr+" Creating file...      ",getFunction.status_cmd("echo  >"+initialize.DEFAULT_VARIABLE[0][0], "\t\t\t")
				print " "+Alr+" Generating... ["+str(Maxima)+"] Words to Generate "+str(porcent)+"% Complete"
				fichero = open(initialize.DEFAULT_VARIABLE[0][0], 'w')
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
				print(" "+Suf+" Completed, output file in "+initialize.DEFAULT_VARIABLE[0][0])
				Message.space()
				fichero.close()	
			# END CODE MODULE ############################################################################################
		else:
			getFunction.KatanaCheckActionGlobalCommands(actions)
	# ERROR GENERAL
	except:
		Errors.Errors(event=sys.exc_info(), info=sys.exc_traceback.tb_lineno)
	# END ERROR GENERAL
	main(True)
# END MAIN FUNCTION

# LINKER FUNCTION
def run(output,longited,chars):
	initialize.DEFAULT_VARIABLE [0][0] = output
	initialize.DEFAULT_VARIABLE [1][0] = longited
	initialize.DEFAULT_VARIABLE [2][0] = chars
	main(False)
# END LINKER FUNCTION