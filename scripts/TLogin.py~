# KATANA
# Test Login
# Script by RedToor
# 23/05/2015
import pxssh
import MySQLdb  
import poplib
import socket
from lib.ftplib.ftplib import FTP
from core import help
W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'
defaulthost="127.0.0.1"
defaultdat1="root"
defaultdat2="toor"
def tlogin():
	try:
		global defaulthost,defaultport,defaultdat1,defaultdat2
		actions = raw_input(B+"   mc/tlogin > "+W)
		if actions == "show options":
			print "     ["+R+"+"+W+"] options"
			print "     host           : yes"
			print "     username       : yes"
			print "     password       : yes\n"
			print "     ["+G+"+"+W+"] options current"
			print "     host           : ",defaulthost
			print "     username       : ",defaultdat1
			print "     password       : ",defaultdat2
			tlogin()
		elif actions[0:8] == "set host":
			defaulthost = actions[9:]
			print "     host           : "+defaulthost+" "+O+"     Saved!!!"+W
			tlogin()
		elif actions[0:12] == "set username":
			defaultdat1 = actions[13:]
			print "     username       : "+defaultdat1+" "+O+"     Saved!!!"+W
			tlogin()
		elif actions[0:12] == "set password":
			defaultdat2= actions[13:]
			print "     password       : "+defaultdat2+" "+O+"     Saved!!!"+W
			tlogin()
		elif actions=="back":
			pass 
		elif actions=="exit":
			print C+"   GooD"+W+" bye."
			exit()
		elif actions == "help":
			help.help()
		elif actions == "run":
			print("\n     ["+O+"!"+W+"] Checking target")
			print "     ["+G+"+"+W+"] options current"
			print "     host           : ",defaulthost
			print "     username       : ",defaultdat1
			print "     password       : ",defaultdat2
			print ""
			print("     ["+G+"+"+W+"] Running")
			try:
				print("     ["+O+"!"+W+"] Testing in MYsql    \t\t\t[3306]")
				MySQLdb.connect(defaulthost,defaultdat1,defaultdat2,'')
				if True:
					print("     ["+G+"+"+W+"] Logged with "+defaultdat1+"/"+defaultdat2+" in Mysql")
			except:
				print("     ["+R+"-"+W+"] Service Off or No Logged.")
			try:
				print("     ["+O+"!"+W+"] Testing in SSH    \t\t\t[20]")
				connect = pxssh.pxssh()
				connect.login(defaulthost,defaultdat1,defaultdat2)
				if True:
					print("     ["+G+"+"+W+"] Logged with "+defaultdat1+"/"+defaultdat2+" in SSH")
			except:
				print "     ["+R+"-"+W+"] Service Off or No Logged."
			try:
				print("     ["+O+"!"+W+"] Testing in FTP    \t\t\t[21]")
				ftp.login(defaultdat1,defaultdat2)
				if True:
					print("     ["+G+"+"+W+"] Logged with "+defaultdat1+"/"+defaultdat2+" in FTP")
			except:
				print "     ["+R+"-"+W+"] Service Off or No Logged."
			try:
				print("     ["+O+"!"+W+"] Testing in POP3    \t\t\t[21]")
				red=poplib.POP3(defaulthost, 110)
				red.user(defaultdat1+"@"+defaulthost)
				red.pass_(defaultdat2)
				if True:
					print("     ["+G+"+"+W+"] Logged with "+defaultdat1+"/"+defaultdat2+" in POP3")
			except:
				print "     ["+R+"-"+W+"] Service Off or No Logged."
	except(KeyboardInterrupt):
		print("\n   ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
		return
	tlogin()