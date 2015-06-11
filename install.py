# KATANA
# Redtoor
# Install build 0.0.0.3
from core import colors
import os
import subprocess
import time
print ""
print "                    "+colors.B+",:"+colors.W+"       "+colors.B+":,"+colors.W+"                   				 "#                    ,:       :,                   
print "                   "+colors.B+",/./"+colors.W+" _8_  "+colors.B+"\.\                  				 "#                   /./  _8_  \.\                  
print "                   "+colors.B+",\ \\"+colors.W+"/"+colors.P+"("+colors.R+"O"+colors.P+")"+colors.W+"\\"+colors.B+"/ /                  				 "#                   \ \/( O )\/ /                  
print "                    "+colors.B+",\ \:::/ /                   				 "#                    \ \:::::/ /                   
print "                     /"+colors.O+"__"+colors.G+"---"+colors.O+"__"+colors.B+"\                   				 "#                     /__---__\                    
print "                    ("+colors.O+"/__\ /__\\"+colors.B+")"+colors.W+"                   				 "#                    (/__\ /__\)                   
print "                    "+colors.B+"/"+colors.W+"\  .V.  /"+colors.B+"\\"+colors.W+"                   				 "#                    /\  .V.  /\                   
print "                   "+colors.B+"/"+colors.W+"  \,---,/  "+colors.B+"\\"+colors.W+"                  				 "#                   /  \,---,/  \                  
print "                   "+colors.B+"\\"+colors.W+"___TTTTT___"+colors.B+"/"+colors.W+"                   SETUP: KATANA  "#                   \___TTTTT___/                  
print "                ::::\ "+colors.R+"|"+colors.W+"_____"+colors.R+"|"+colors.W+" /::::                DATE:  28/05/15"#                ::::\ "+colors.R+"|"+colors.W+"_____"+colors.R+"|"+colors.W+" /::::               
print "                (+  _"+colors.R+"|"+colors.W+" __"+colors.R+"|"+colors.W+"__ "+colors.R+"|"+colors.W+"_  +)                BUILD: 0.0.0.3 "#                (+  _"+colors.R+"|"+colors.W+" __"+colors.R+"|"+colors.W+"__ "+colors.R+"|"+colors.W+"_  +)               
print "                "+colors.R+"|"+colors.W+"  I_"+colors.R+"|"+colors.W+"KATANA."+colors.R+"|"+colors.W+"_I  "+colors.R+"|"+colors.W+"                               "#                "+colors.R+"|"+colors.W+"  I_"+colors.R+"|"+colors.W+".ANATAK"+colors.R+"|"+colors.W+"_I  "+colors.R+"|"+colors.W+"               
print "                "+colors.R+"|"+colors.W+"  I_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"  "+colors.R+"|"+colors.W+"               				 "#                "+colors.R+"|"+colors.W+"  I_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"  "+colors.R+"|"+colors.W+"               
print "    __________?_________________________________  				 "#    __________?_________________________________  
print "   {_"+colors.C+"|"+colors.W+" "+colors.C+"|"+colors.W+" "+colors.C+"|"+colors.W+" "+colors.C+"|"+colors.W+" I"+colors.GR+"#################################"+colors.W+"/  				 "#   {_"+colors.R+"|"+colors.W+" "+colors.R+"|"+colors.W+" "+colors.R+"|"+colors.W+" "+colors.R+"|"+colors.W+" I#################################/  
print "     ^ ^ ^ ^         "+colors.O+"FRAMEWORK"+colors.W+"                    				 "#     ^ ^ ^ ^ EHT KROWEMARF, dliuB (0.0.0.3)       
print "                   I_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_I                  				 "#                   I_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_I                  
print "                   \_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_/                  				 "#                   \_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_/                  
print ""
print ""

if os.getuid() != 0:
	print R+' [!]'+O+' ERROR:'+G+' wifite'+O+' must be run as '+R+'root'+W
	print R+' [!]'+O+' login as root ('+W+'su root'+O+') or try '+W+'sudo ./wifite.py'+W
	exit(1)

if not os.uname()[0].startswith("Linux") and not 'Darwin' in os.uname()[0]: # OSX support, 'cause why not?
	print O+' [!]'+R+' WARNING:'+G+' wifite'+W+' must be run on '+O+'linux'+W
	exit(1)

print colors.O+" Wait... "
time.sleep(2)
print colors.B+" Katana framework, installing"
print colors.W+" Coping files..."
subprocess.call('mkdir -p /usr/share/katana', shell=True)
subprocess.call('cp -r * /usr/share/katana', shell=True)
print colors.W+" Giving privileges"
subprocess.call('chmod -c -R 777 /usr/share/katana/', shell=True)
print colors.W+" Creating Link"
subprocess.call('cp katana /usr/bin/katana', shell=True)
subprocess.call('chmod -c 777 /usr/bin/katana', shell=True)
subprocess.call('rm /usr/share/katana/install', shell=True)
subprocess.call('rm /usr/share/katana/install.py', shell=True)
subprocess.call('rm /usr/share/katana/readme', shell=True)
subprocess.call('rm /usr/share/katana/katana', shell=True)
print " Now you can remove this diretory."
print " Done !!!"
print ""
print " Path    : /usr/share/katana"
print " Modules : /usr/share/katana/scripts"
print ""
print colors.G+" Now you can run katana directly in console #kanata [ENTER]"
print colors.G+" For update katana use 'update' when you are run it."
print colors.O+" Completed Install"
print ""
# Thanks 
