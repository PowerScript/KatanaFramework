#
# Katana framework 
# @Katana Update
#

from core import colors
from core import info
import subprocess
import socket
import os

def update():
	print ""
	print "     ["+colors.O+"!"+colors.W+"] Update"
	print "     ["+colors.O+"!"+colors.W+"] Version Current : "+info.version+", Build: "+info.build
	try:
		red=socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
		red.connect(("github.com", int(80))) 
		if True:
			print "     ["+colors.O+"!"+colors.W+"] Downloading project"
			subprocess.Popen("cd /tmp;git clone https://github.com/RedToor/katana.git;cp -R /tmp/katana/* /usr/share/katana/;rm -rf /tmp/katana/*", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
			subprocess.Popen("cd /usr/share/katana/core;python upgrade.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
			print "     ["+colors.O+"!"+colors.W+"] Upgrading."
			pass
			print "     ["+colors.G+"+"+colors.W+"] Katana framework was Updated"
			print ""
	except:
		print("     ["+colors.R+"-"+colors.W+"] Error, No connneted to Internet. ")
		print""