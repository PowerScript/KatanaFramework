### Katana Framework Install
### you can redistribute it and/or modify
### it under the terms of the GNU General Public License as published by
### the Free Software Foundation, either version 3 of the License, or
### (at your option) any later version. 

from core.Setting import * 
from core import info
from core import colors
from core import ping
import os
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
print "                   "+colors.B+"\\"+colors.W+"___TTTTT___"+colors.B+"/"+colors.W+"                SETUP: KATANA  "#                   \___TTTTT___/                  
print "                ::::\ "+colors.R+"|"+colors.W+"_____"+colors.R+"|"+colors.W+" /::::             DATE:  "+info.date+""#                ::::\ "+colors.R+"|"+colors.W+"_____"+colors.R+"|"+colors.W+" /::::               
print "                (+  _"+colors.R+"|"+colors.W+" __"+colors.R+"|"+colors.W+"__ "+colors.R+"|"+colors.W+"_  +)             CORE: "+info.version+", BUILD: "+info.build #                (+  _"+colors.R+"|"+colors.W+" __"+colors.R+"|"+colors.W+"__ "+colors.R+"|"+colors.W+"_  +)               
print "                "+colors.R+"|"+colors.W+"  I_"+colors.R+"|"+colors.W+"KATANA."+colors.R+"|"+colors.W+"_I  "+colors.R+"|"+colors.W+"                               "#                "+colors.R+"|"+colors.W+"  I_"+colors.R+"|"+colors.W+".ANATAK"+colors.R+"|"+colors.W+"_I  "+colors.R+"|"+colors.W+"               
print "                "+colors.R+"|"+colors.W+"  I_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"  "+colors.R+"|"+colors.W+"               				 "#                "+colors.R+"|"+colors.W+"  I_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"  "+colors.R+"|"+colors.W+"               
print "    __________?_________________________________  				 "#    __________?_________________________________  
print "   {_"+colors.C+"|"+colors.W+" "+colors.C+"|"+colors.W+" "+colors.C+"|"+colors.W+" "+colors.C+"|"+colors.W+" I"+colors.GR+"#################################"+colors.W+"/  				 "#   {_"+colors.R+"|"+colors.W+" "+colors.R+"|"+colors.W+" "+colors.R+"|"+colors.W+" "+colors.R+"|"+colors.W+" I#################################/  
print "     ^ ^ ^ ^   ,ww   "+colors.O+"FRAMEWORK"+colors.W+"   ww,                   				 "#     ^ ^ ^ ^ EHT KROWEMARF, dliuB      
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
print " Configuration in /core/Setting.py"
print colors.W+" Creating Folder ", ping.status_cmd('mkdir -p '+PATCH_INTALL+'katana',"\t\t\t\t\t\t")
print colors.W+" Coping files ktf ", ping.status_cmd('cp -r * '+PATCH_INTALL+'katana',"\t\t\t\t\t\t")
print colors.W+" Giving privileges ", ping.status_cmd('chmod -c -R 777 '+PATCH_INTALL+'katana/',"\t\t\t\t\t\t")
print colors.W+" Creating Link [1] ", ping.status_cmd('cp core/ktf.console /usr/bin/ktf.console',"\t\t\t\t\t\t")
print colors.W+" Creating Link [2] ", ping.status_cmd('cp core/ktf.run /usr/bin/ktf.run',"\t\t\t\t\t\t")
print colors.W+" Creating Link [3] ", ping.status_cmd('cp core/ktf.lab /usr/bin/ktf.lab',"\t\t\t\t\t\t")
print colors.W+" Creating Link [4] ", ping.status_cmd('cp core/ktf.linker /usr/bin/ktf.linker',"\t\t\t\t\t\t")
print colors.W+" Giving privileges [1] ", ping.status_cmd('chmod -c 777 /usr/bin/ktf.console',"\t\t\t\t\t")
print colors.W+" Giving privileges [2] ", ping.status_cmd('chmod -c 777 /usr/bin/ktf.lab',"\t\t\t\t\t")
print colors.W+" Giving privileges [3] ", ping.status_cmd('chmod -c 777 /usr/bin/ktf.run',"\t\t\t\t\t")
print colors.W+" Giving privileges [4] ", ping.status_cmd('chmod -c 777 /usr/bin/ktf.linker',"\t\t\t\t\t")
print ""
print " Now you can remove this diretory."
print " Done !!!"
print ""
print " Usage: "
print ""
print " "+colors.R+"\033[1mktf.console"+colors.W+" > for mode console"
print " "+colors.R+"\033[1mktf.run    "+colors.W+" > use modules fastly"
print " "+colors.R+"\033[1mktf.lab    "+colors.W+" > start laboratory"
print " "+colors.R+"\033[1mktf.linker "+colors.W+" > use modules fastly and pass parameter directly"
print ""
print " Path    : "+PATCH_INTALL+"katana"
print " Modules : "+PATCH_INTALL+"katana/scripts"
print ""
print ""
