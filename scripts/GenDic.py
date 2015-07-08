# KATANA
# GenDic
# Script by Uknowk
# 07/07/2015

from core import help
import time
W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'
defaultdic="/root/Desktop/Dictionary.txt"
defaultlon=5
defaultstr="chars_num"
def Gendic():
	global defaultdic,defaultlon,defaultstr
	actions = raw_input(O+"     ktn/mc/gendic > "+W)
	if actions == "show options":
		print ""
		print "     ["+R+"+"+W+"] options"
		print "     |Dictionary type : yes/no"
		print "     |Longitude       : yes/no"
		print "     |Dictionary      : yes/no\n"
		print ""
		print "     ["+G+"+"+W+"] options current"
		print "     |type            : ",defaultstr
		print "     |longitude       : ",defaultlon
		print "     |dictionary      : ",defaultdic
		print "\n"
		print "     ["+G+"+"+W+"] Auxiliar help"
		print "     |Dictionary type : chars_min {a,b,c,d,...,z}"
		print "			chars_may {A,B,C,D,...,Z}"
		print "			chars_num {0,1,2,3,...,9}"
		print ""
	elif actions=="back":
		pass 
	elif actions=="exit":
		print C+"     GooD"+W+" bye."
		exit()
	elif actions[0:8] == "set type":
			defaultstr = actions[9:]
			#if defaultstr != "chars_min" or defaultstr != "chars_may" or defaultstr != "chars_num":
			#	print "     ["+O+"!"+W+"] Error to set type"
			#	defaultstr="chars_num"
			#else:
			print "     Dictionary type : "+defaultstr+" "+O+"     Saved!!!"+W
			Gendic()
	elif actions[0:13] == "set longitude":
			defaultlon = actions[14:]
			print "     Longitude       : "+defaultlon+" "+O+"     Saved!!!"+W
			Gendic()
	elif actions[0:14] == "set dictionary":
			defaultdic = actions[15:]
			print "     Dictionary      : "+defaultdic+" "+O+"     Saved!!!"+W
			Gendic()
	elif actions == "help":
			help.help()
	elif actions == "run":
		try:
			print ""
			print "     ["+G+"+"+W+"] options current"
			print "     |type            : ",defaultstr
			print "     |longitude       : ",defaultlon
			print "     |dictionary      : ",defaultdic
			print ""
			print("     ["+G+"+"+W+"] Running")
			long_max = defaultlon 
			long_min = defaultlon
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
			    print "     generating "+password
			    if isMax(cadena):
			    	bucle = False
			    cadena = aumentarCadena(cadena)
			print("     ["+G+"+"+W+"] Complete")
			fichero.close()
		except(KeyboardInterrupt, SystemExit):
			print("\n     ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
	Gendic()
