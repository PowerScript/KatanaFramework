#
# Katana framework 
# @Katana Splash
#

from core import colors
import random
import subprocess            
spa=random.randint(1,2)
subprocess.call('clear', shell=True)

splash2=colors.B+"""
          mM@@MM@@MM@@MM@@MM@@MM@@@MMM@@MM@@@@Mm
         mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm
         @MMMM"""+colors.W+"""MMM"""+colors.B+"""MMM"""+colors.W+"""MMM"""+colors.B+"""MM"""+colors.W+"""MMMMMMMMM"""+colors.B+"""MMM"""+colors.W+"""MMMMMMM"""+colors.B+"""MMMMm
         MMMMM"""+colors.W+"""MMM"""+colors.B+"""MM"""+colors.W+"""MMM"""+colors.B+"""MMM"""+colors.W+"""MMMMMMMMM"""+colors.B+"""MMM"""+colors.W+"""MMMMMMM"""+colors.B+"""MMMM@
         @MMMM"""+colors.W+"""MMMMMM"""+colors.B+"""MMMMMMMM"""+colors.W+"""MMM"""+colors.B+"""MMMMMM"""+colors.W+"""MMM"""+colors.B+"""MMMMMMMMM
         MMMMM"""+colors.W+"""MMM"""+colors.B+"""MM"""+colors.W+"""MMMM"""+colors.B+"""MMMMM"""+colors.W+"""MMM"""+colors.B+"""MMMMMM"""+colors.W+"""MMMMMMM"""+colors.B+"""MMMM@
         @MMMM"""+colors.W+"""MMM"""+colors.B+"""MMM"""+colors.W+"""MMM"""+colors.B+"""MMMMM"""+colors.W+"""MMM"""+colors.B+"""MMMMMM"""+colors.W+"""MMMMMMM"""+colors.B+"""MMMMM
         MMMMM"""+colors.W+"""MMM"""+colors.B+"""MMM"""+colors.W+"""MMM"""+colors.B+"""MMMMM"""+colors.W+"""MMM"""+colors.B+"""MMMMMM"""+colors.W+"""MMM"""+colors.B+"""MMMMMMMM@
         @MMMM"""+colors.W+"""MMM"""+colors.B+"""MMM"""+colors.W+"""MMM"""+colors.B+"""MMMMM"""+colors.W+"""MMM"""+colors.B+"""MMMMMM"""+colors.W+"""MMM"""+colors.B+"""MMMMMMMMM
         mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm
           @@MM@@MM@@MM@@MM@@MM@@MM@@MM@@MM@@Mm
	   """+colors.W


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
