#
# Katana framework 
# @Katana Install
#

from core import info
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
print "                ::::\ "+colors.R+"|"+colors.W+"_____"+colors.R+"|"+colors.W+" /::::                DATE:  "+info.date+""#                ::::\ "+colors.R+"|"+colors.W+"_____"+colors.R+"|"+colors.W+" /::::               
print "                (+  _"+colors.R+"|"+colors.W+" __"+colors.R+"|"+colors.W+"__ "+colors.R+"|"+colors.W+"_  +)                BUILD: "+info.version+" "#                (+  _"+colors.R+"|"+colors.W+" __"+colors.R+"|"+colors.W+"__ "+colors.R+"|"+colors.W+"_  +)               
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
	print " ["+colors.R+"-"+colors.W+"] ERROR:"+colors.B+" Katana Install"+colors.B+" must be run as "+colors.R+"root"+colors.W+"."
	print " ["+colors.R+"-"+colors.W+"] login as root ("+colors.R+"sudo"+colors.W+") or try "+colors.W+"sudo python install.py"+colors.W+"\n"
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
subprocess.call('cp core/ktfconsole /usr/bin/ktfconsole', shell=True)
subprocess.call('cp core/ktfrun /usr/bin/ktfrun', shell=True)
subprocess.call('cp core/ktflab /usr/bin/ktflab', shell=True)
subprocess.call('chmod -c 777 /usr/bin/ktfconsole', shell=True)
subprocess.call('chmod -c 777 /usr/bin/ktfrun', shell=True)
subprocess.call('chmod -c 777 /usr/bin/ktflab', shell=True)
subprocess.call('rm /usr/share/katana/install.py', shell=True)
print " Now you can remove this diretory."
print " Done !!!"
print ""
print " USE: "
print " ktfconsole > for mode console"
print " ktfrun     > use modules fastly"
print " ktflab     > start laboratory"
print ""
print " Path    : /usr/share/katana"
print " Modules : /usr/share/katana/scripts"
print ""
print colors.G+" Now you can run katana directly in console #kanata [ENTER]"
print colors.G+" For update katana use 'update' when you are run it."
print colors.O+" Completed Install"
print ""