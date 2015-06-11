# KATANA
# RAR Brute Force
# Script by LeSZO ZerO
# 28/02/2015

from core import help
from lib.rarfile import RARfile
import optparse
import sys
import os
import time
W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'
defaultarc="empy"
defaultdic="core/db/pass.dicc"
def btRAR():
	global defaultarc,defaultdic
	actions = raw_input(O+"     ktn/file/bruterar > "+W)
	if actions == "show options":
		print ""
		print "     ["+R+"+"+W+"] options"
		print "     |file           : yes"
		print "     |dictionary     : no/yes\n"
		print ""
		print "     ["+G+"+"+W+"] options current"
		print "     |file           : ",defaultarc
		print "     |dictionary     : ",defaultdic
		print ""
		btRAR()
	elif actions=="back":
		return 
	elif actions=="exit":
		print C+"     GooD"+W+" bye."
		exit()
	elif actions[0:8] == "set file":
		defaultarc = actions[9:]
		print "     file          : "+defaultarc+" "+O+"     Saved!!!"+W
		btRAR()
	elif actions[0:14] == "set dictionary":
		defaultdic = actions[16:]
		print "     dictionary    : "+defaultdic+" "+O+"     Saved!!!"+W
		btRAR()
	if actions == "run":
		print("\n     ["+O+"!"+W+"] Checking file")
		try:
			Arch = open(defaultdic,"r")
			if True:
				print "     ["+G+"+"+W+"] options current"
				print "     file         : ",defaultarc
				print "     dictionary   : ",defaultdic
				print 
				leeArchivo = Arch.readlines()
				for palabra in leeArchivo:
					palabraLlegada = palabra.split("\n")
					try:
						RARarch = RARfile.RARFile(defaultarc)
						try:
							log=open('core/logs/logsBruteForce.log','a')
							log.write('\n ===================================== ')
							log.write('\n Module  : BruteForceRAR')
							log.write('\n Data    : '+time.strftime('%c'))
							log.write('\n file    : '+defaultarc)
							log.write('\n Cracked : password : ',str(palabraLlegada[0]))
							log.close()
							RARarch.extractall(pwd=str(palabraLlegada[0]))
							print "     ["+G+"+"+W+"] Cracked with ",str(palabraLlegada[0])
							break
						except:
							print "     ["+O+"!"+W+"] Checking with ",str(palabraLlegada[0])
					except:
						print "     ["+O+"!"+W+"] Error to open file"
						break
		except:
			print "     ["+O+"!"+W+"] Error to open dictionary"
	else:
		print "     ["+O+"!"+W+"] command No Accept"+W
	btRAR()