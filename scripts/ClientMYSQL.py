# KATANA
# client MYSQL 
# Script by RedToor
# 15/05/2015

from core import help
from lib import MySQLdb
import socket
W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'
defaulthost="127.0.0.1"
defaultport="3306"
defaultdat1="root"
defaultdat2=""
def cmysql():
	try:
		global defaulthost,defaultport,defaultdat1,defaultdat2
		actions = raw_input(O+"     ktn/clt/sql > "+W)
		if actions == "show options":
			print ""
			print "     ["+R+"+"+W+"] options"
			print "     |host           : yes"
			print "     |port           : no/yes"
			print "     |username       : yes"
			print "     |password       : yes\n"
			print ""
			print "     ["+G+"+"+W+"] options current"
			print "     |host           : ",defaulthost
			print "     |port           : ",defaultport
			print "     |username       : ",defaultdat1
			print "     |password       : ",defaultdat2
			print ""
			cmysql()
		elif actions[0:8] == "set host":
			defaulthost = actions[9:]
			print "     host           : "+defaulthost+" "+O+"     Saved!!!"+W
			cmysql()
		elif actions[0:8] == "set port":
			defaultport= actions[9:]
			print "     port           : "+defaultport+" "+O+"     Saved!!!"+W
			cmysql()
		elif actions[0:12] == "set username":
			defaultdat1 = actions[13:]
			print "     username       : "+defaultdat1+" "+O+"     Saved!!!"+W
			cmysql()
		elif actions[0:12] == "set password":
			defaultdat2= actions[13:]
			print "     password       : "+defaultdat2+" "+O+"     Saved!!!"+W
			cmysql()
		elif actions=="back":
			pass 
		elif actions=="exit":
			print C+"     GooD"+W+" bye."
			exit()
		elif actions == "help":
			help.help()
		elif actions == "run":
			print("\n     ["+O+"!"+W+"] Checking target")
			print "     ["+G+"+"+W+"] options current"
			print "     host           : ",defaulthost
			print "     port           : ",defaultport
			print "     username       : ",defaultdat1
			print "     password       : ",defaultdat2
			print ""
			try:
				red=socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
				red.connect((defaulthost, int(defaultport)))
				if True:
					try:
						print("     ["+G+"+"+W+"] host LIVE")
						print("     ["+G+"+"+W+"] Running")
						con=MySQLdb.connect(defaulthost,defaultdat1,defaultdat2,'')
						if True:
							try:
								cmd="nop"
								print "\n     ["+B+"*"+W+"] SQL Client help\n"
								print "          show databases: list databases      ex: show databases"    
								print "          use         	: select database     ex: use user_table" 
								print "          show tables	: list tables         ex: show tables" 
								print ""
								print "          create database: create databases    ex: create database USERS"
								print "          create table   : create tables       ex: create table EMAILS ( id INT PRIMARY KEY, name VARCHAR(20));" 
								print "          drop database  : drop databases      ex: drop database USERS"   
								print "          insert         : insert data         ex: insert into EMAILS values ( '2', 'Dean' )"
								print "          update         : update data         ex: update EMAILS set name='Willy' where id=1"
								print "          select         : select data         ex: select id, name from EMAILS;"   
								print ""
								while(cmd!="exit"):
									cmd = raw_input(O+" sql/> "+W)	
									cur=con.cursor() 
									try:
										tor=cur.execute(cmd)
										if True:
											for x in range(tor):
	   											print cur.fetchone()
	   								except:
	   									print "     ["+O+"!"+W+"] Error: Command"				
							except:
								print "Error"
					except(KeyboardInterrupt):
						print("\n     ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
					except:
						print("     ["+R+"-"+W+"] username or password Wrong")
			except(KeyboardInterrupt):
				print("\n     ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
			except:
				print("     ["+R+"-"+W+"] target off")
		else:
			print "     ["+O+"!"+W+"] command No Accept"+W
	except(KeyboardInterrupt):
		print("\n     ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
	cmysql()