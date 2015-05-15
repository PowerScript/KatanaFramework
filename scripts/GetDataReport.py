# KATANA
# GetDataReport
# Script by RedToor
# 02/03/2015
from core import help
import socket
import subprocess
W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'
defaultred="www.google.com"
defaultjav="true"
def getdatareport():
	global defaultred,defaultjav
	actions = raw_input(B+"   seng/gdreport > "+W)
	if actions == "show options":
		print "     ["+R+"+"+W+"] options"
		print "     redirect        : yes"
		print "     javascript      : yes/no\n"
		print "     ["+G+"+"+W+"] options current"
		print "     redirect        : ",defaultred
		print "     javascript      : ",defaultjav
	elif actions=="back":
		pass 
	elif actions=="exit":
		print C+"   GooD"+W+" bye."
		exit()
	elif actions[0:12] == "set redirect":
			defaultred = actions[13:]
			print "     redirect        : "+defaultred+" "+O+"     Saved!!!"+W
			getdatareport()
	elif actions[0:14] == "set javascript":
			defaultjav = actions[15:]
			if defaultjav == "true" or defaultjav == "false":
				print "     javascript      : "+defaultjav+" "+O+"     Saved!!!"+W
			else:
				print "     ["+O+"!"+W+"] data not allowed, just (true/false)"
			getdatareport()
	elif actions == "run":
		try:
			subprocess.call('echo "<?php \$url=\'http://'+defaultred+'\';\$javascript=\''+defaultjav+'\';?>" > /var/www/appconfig.php', shell=True)
			print("\n     ["+O+"!"+W+"] Running Apache Server")
			subprocess.call('cp /root/Desktop/katana/files/getdatareport/* /var/www/', shell=True)
			subprocess.call('chmod -c 777 /var/www/', shell=True)
			subprocess.call('service apache2 start', shell=True)
			if True:
				try:
					print("     ["+G+"+"+W+"] Apache Started")
					print("     ["+G+"+"+W+"] Script Running in http://127.0.0.1/redirect.php?id=1337")
					print("     ["+O+"!"+W+"] The Report will be save in /var/www/")
					print""
					print("     ["+G+"+"+W+"] Running GetDataReport Script...")
					raw_input("     ["+O+"!"+W+"] Press any key for Stop GetDataReport")
					print("     ["+O+"!"+W+"] Stoping Process")
					subprocess.call('apache2ctl stop', shell=True)
					print("     ["+O+"+"+W+"] Stop Apache d' GetDataReport Script")
				except(KeyboardInterrupt):
					print("     ["+G+"!"+W+"] Stoping Process")
					subprocess.call('service apache2 stop', shell=True)
					subprocess.call('rm /var/www/redirect.php', shell=True)
					subprocess.call('rm /var/www/appconfig.php', shell=True)
					subprocess.call('rm /var/www/jquery.js', shell=True)
					print "\n"
					getdatareport()
		except(KeyboardInterrupt, SystemExit):
			print("\n     ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
	getdatareport()
