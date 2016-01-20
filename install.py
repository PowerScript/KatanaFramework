#!/usr/bin/env python
#    
#    About Author :
#    
#    Founder : Javier Franco (RedToor)
#    Location : Colombia
#    Email : redtoor[at]inbox.ru
#    Project In Github : https://github.com/redtoor/katana
#
# ------- Katana Installation Script. --------
# 
#  Description File: The file Script Make a Folder in (usr/share) named katana
#                    for install katana framework, copy all file to the folder
#                    and make shortcups for fast access and after give privileges
#                    a All files of project. 
#
# you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.                                  @ LICENSE
#

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
print "                   "+colors.B+"\\"+colors.W+"___TTTTT___"+colors.B+"/"+colors.W+"         CODE: KATANA  "#                   \___TTTTT___/                  
print "                ::::\ "+colors.R+"|"+colors.W+"_____"+colors.R+"|"+colors.W+" /::::      DATE: "+info.date+""#                ::::\ "+colors.R+"|"+colors.W+"_____"+colors.R+"|"+colors.W+" /::::               
print "                (+  _"+colors.R+"|"+colors.W+" __"+colors.R+"|"+colors.W+"__ "+colors.R+"|"+colors.W+"_  +)      CORE: "+info.version+", BUILD: "+info.build #                (+  _"+colors.R+"|"+colors.W+" __"+colors.R+"|"+colors.W+"__ "+colors.R+"|"+colors.W+"_  +)               
print "                "+colors.R+"|"+colors.W+"  I_"+colors.R+"|"+colors.W+"KATANA."+colors.R+"|"+colors.W+"_I  "+colors.R+"|"+colors.W+"                               "#                "+colors.R+"|"+colors.W+"  I_"+colors.R+"|"+colors.W+".ANATAK"+colors.R+"|"+colors.W+"_I  "+colors.R+"|"+colors.W+"               
print "                "+colors.R+"|"+colors.W+"  I_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"  "+colors.R+"|"+colors.W+"               				 "#                "+colors.R+"|"+colors.W+"  I_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"  "+colors.R+"|"+colors.W+"               
print "    __________?_________________________________  				 "#    __________?_________________________________  
print "   {_"+colors.C+"B|"+colors.W+" "+colors.C+"Y|"+colors.W+" "+colors.R+"R|"+colors.W+" "+colors.W+"T|"+colors.W+" I"+colors.GR+"#################################"+colors.W+"/  				 "#   {_"+colors.R+"|"+colors.W+" "+colors.R+"|"+colors.W+" "+colors.R+"|"+colors.W+" "+colors.R+"|"+colors.W+" I#################################/  
print "     ^ ^ ^ ^   ,ww   "+colors.O+"FRAMEWORK"+colors.W+"   ww,                   				 "#     ^ ^ ^ ^ EHT KROWEMARF, dliuB      
print "                   I_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_I                  				 "#                   I_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_I                  
print "                   \_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_/                  				 "#                   \_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_"+colors.R+"|"+colors.W+"_/                  
print ""
print ""

if os.getuid() != 0:
	print " ["+colors.R+"-"+colors.W+"] ERROR:"+colors.B+" Katana Install"+colors.B+" must be run as "+colors.R+"root"+colors.W+"."
	print " ["+colors.R+"-"+colors.W+"] login as root ("+colors.R+"sudo"+colors.W+") or try "+colors.W+"sudo python install.py"+colors.W+"\n"
	exit(1)
time.sleep(1)

Shortcuts="""
ln -f -r -s /usr/share/katana/core/ShortCuts/ktf.console /usr/bin/ktf.console ;
ln -f -r -s /usr/share/katana/core/ShortCuts/ktf.linker  /usr/bin/ktf.linker  ;
ln -f -r -s /usr/share/katana/core/ShortCuts/ktf.update  /usr/bin/ktf.update  ;
ln -f -r -s /usr/share/katana/core/ShortCuts/ktf.lab     /usr/bin/ktf.lab     ;
ln -f -r -s /usr/share/katana/core/ShortCuts/ktf.run     /usr/bin/ktf.run     ;
""" 

Files="""
cd /usr/share/katana/files;tar -xf /usr/share/katana/files/exiftool.tar      >/dev/null 2>&1;
cd /usr/share/katana/files;tar -xf /usr/share/katana/files/facebrok.tar      >/dev/null 2>&1;
cd /usr/share/katana/files;tar -xf /usr/share/katana/files/getdatareport.tar >/dev/null 2>&1;
cd /usr/share/katana/files;tar -xf /usr/share/katana/files/hulk.tar          >/dev/null 2>&1;rm -R *.tar
"""

print colors.W+" \033[1m\033[41mKatana framework\033[49m                    date {"+time.strftime('%c')+"}"
print colors.W+"\n Creating Folder. ",    ping.status_cmd('mkdir -p '+PATCH_INTALL+'katana',   "\t\t\t\t\t\t")
print " Coping files. ",                  ping.status_cmd('cp -r * '+PATCH_INTALL+'katana',    "\t\t\t\t\t\t")
print " Creating Shortcuts. ",            ping.status_cmd(Shortcuts,                           "\t\t\t\t\t\t")
print " Extracting Files. ",              ping.status_cmd(Files,                               "\t\t\t\t\t\t")
print " Giving privileges. ",             ping.status_cmd('chmod -R -c 777 /usr/share/katana/',"\t\t\t\t\t\t")
print "\n Done, Enjoy. !!!\n"

