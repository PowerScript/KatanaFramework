# KATANA
# ZIP Brute Force
# Script by LeSZO ZerO
# 28/02/2015
import zipfile
import optparse
import sys
import os
from core import help
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
def btzip():
	global defaultarc,defaultdic
	actions = raw_input(B+"   file/brutezip > "+W)
	if actions == "show options":
		print "     ["+R+"+"+W+"] options"
		print "     file           : yes"
		print "     dictionary     : no/yes\n"
		print "     ["+G+"+"+W+"] options current"
		print "     file           : ",defaultarc
		print "     dictionary     : ",defaultdic
		btzip()
	elif actions=="back":
		return 
	elif actions=="exit":
		print C+"   GooD"+W+" bye."
		exit()
	elif actions[0:8] == "set file":
		defaultarc = actions[9:]
		print "     file          : "+defaultarc+" "+O+"     Saved!!!"+W
		btzip()
	elif actions[0:14] == "set dictionary":
		defaultdic = actions[16:]
		print "     dictionary    : "+defaultdic+" "+O+"     Saved!!!"+W
		btzip()
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
						ZIParch = zipfile.ZipFile(defaultarc)
						try:
							ZIParch.extractall(pwd=str(palabraLlegada[0]))
							print "     ["+G+"+"+W+"] Craked with ",str(palabraLlegada[0])
							break
						except:
							print "     ["+O+"!"+W+"] Checking with ",str(palabraLlegada[0])
					except:
						print "     ["+O+"!"+W+"] Error to open file"
						break
		except:
			print "     ["+O+"!"+W+"] Error to open dictionary"
	btzip()