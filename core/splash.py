#
# Katana framework 
# @Katana Splashs
#

from core import colors
import random
import subprocess            
spa=random.randint(1,2)
subprocess.call('clear', shell=True)

splash2=colors.B+"""
          mM@@MM@@MM@@MM@@MM@@MM@@@MMM@@MM@@@@Mm
         mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm
         @MMMM"""+colors.GR+"""MMM"""+colors.B+"""MMM"""+colors.GR+"""MMM"""+colors.B+"""MM"""+colors.GR+"""MMMMMMMMM"""+colors.B+"""MMM"""+colors.GR+"""MMMMMMM"""+colors.B+"""MMMMm
         MMMMM"""+colors.GR+"""MMM"""+colors.B+"""MM"""+colors.GR+"""MMM"""+colors.B+"""MMM"""+colors.GR+"""MMMMMMMMM"""+colors.B+"""MMM"""+colors.GR+"""MMMMMMM"""+colors.B+"""MMMM@
         @MMMM"""+colors.GR+"""MMMMMM"""+colors.B+"""MMMMMMMM"""+colors.GR+"""MMM"""+colors.B+"""MMMMMM"""+colors.GR+"""MMM"""+colors.B+"""MMMMMMMMM
         MMMMM"""+colors.GR+"""MMM"""+colors.B+"""MM"""+colors.GR+"""MMMM"""+colors.B+"""MMMMM"""+colors.GR+"""MMM"""+colors.B+"""MMMMMM"""+colors.GR+"""MMMMMMM"""+colors.B+"""MMMM@
         @MMMM"""+colors.GR+"""MMM"""+colors.B+"""MMM"""+colors.GR+"""MMM"""+colors.B+"""MMMMM"""+colors.GR+"""MMM"""+colors.B+"""MMMMMM"""+colors.GR+"""MMMMMMM"""+colors.B+"""MMMMM
         MMMMM"""+colors.GR+"""MMM"""+colors.B+"""MMM"""+colors.GR+"""MMM"""+colors.B+"""MMMMM"""+colors.GR+"""MMM"""+colors.B+"""MMMMMM"""+colors.GR+"""MMM"""+colors.B+"""MMMMMMMM@
         @MMMM"""+colors.GR+"""MMM"""+colors.B+"""MMM"""+colors.GR+"""MMM"""+colors.B+"""MMMMM"""+colors.GR+"""MMM"""+colors.B+"""MMMMMM"""+colors.GR+"""MMM"""+colors.B+"""MMMMMMMMM
         mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm
           @@MM@@MM@@MM@@MM@@MM@@MM@@MM@@MM@@Mm
	   """+colors.GR


splash4="""
     __                __                                
    /\ \              /\ \__                             
    \ \ \/'\      __  \ \ ,_\    __      ___      __     
     \ \ , <    /'__`\ \ \ \/  /'__`\  /' _ `\  /'__`\   
      \ \  \`\ /\ \L\.\_\ \ \_/\ \L\.\_/\ \/\ \/\ \L\.\_ 
       \ \_\ \_\ \__/.\_\ \__\ \__/.\_\ \_\ \_\ \__/.\_
        \/_/\/_/\/__/\/_/ \/__/\/__/\/_/\/_/\/_/\/__/\/_/"""

if spa==1:
	print splash2
elif spa==2:
	print splash4
