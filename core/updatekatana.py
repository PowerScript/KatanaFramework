# KATANA
# Update
# Script by RedToor
# 28/02/2015
import subprocess
import os
W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'
def update():
	print "     ["+O+"!"+W+"] Updating KATANA..."
	try:
		subprocess.Popen("cd /tmp;git clone https://github.com/RedToor/katana.git;cp -R test/ /usr/share;rm -rf /tmp/test/", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
	except Exception, e:
		print("     ["+R+"-"+W+"] Error")
		pass
	print "     ["+G+"+"+W+"] SUCCESSFUL KATANA Updated"
