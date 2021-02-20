#!/usr/bin/python
# -*- coding: latin-1 -*-
#HEAD#########################################################
#
# Katana Framework | Banners                           
# Last Modified: 07/01/2017
#
#########################################################HEAD#

from core import colors,Information
from Internal import get_number_modules,get_number_tools
import random          


Banner1="""

            	 		     ██╗  ██╗████████╗███████╗
            			     ██║ ██╔╝╚══██╔══╝██╔════╝
            	 ░░░░░░███████ ]▄▄▄▄▄█████╔╝    ██║   █████╗  
            	 ▂▄▅█████████▅▄▃▂    ██╔═██╗    ██║   ██╔══╝  
            	 I█████████████████].██║  ██╗   ██║   ██║     
            	 ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤     ╚═╝  ╚═╝   ╚═╝   ╚═╝
            		          The Hacking Framework 
       
	       """+colors.HH+""" Core    """+colors.W+""" [ """+Information.version+""", Build: """+Information.build+""" ]
	       """+colors.HH+""" Date    """+colors.W+""" [ """+Information.date+"""    ]
	       """+colors.HH+""" Banner  """+colors.W+""" [          WAR         ]
	       """+colors.HH+""" Modules """+colors.W+"""    [ """""+str(get_number_modules())+""" ] """+colors.HH+"""Tools """+colors.W+"""[ """+str(get_number_tools())+""" ]\n"""

Banner2=colors.B+"""
                   mM@@MM@@MM@@MM@@MM@@MM@@@MMMMM@@@@Mm              
       ||========mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm===========||        
       ||        @MMMM"""+colors.W+"""MMM"""+colors.B+"""MMM"""+colors.W+"""MMM"""+colors.B+"""MM"""+colors.W+"""MMMMMMMMM"""+colors.B+"""MMM"""+colors.W+"""MMMMMMM"""+colors.B+"""MMMMm         ||
       ||        MMMMM"""+colors.W+"""MMM"""+colors.B+"""MM"""+colors.W+"""MMM"""+colors.B+"""MMM"""+colors.W+"""MMMMMMMMM"""+colors.B+"""MMM"""+colors.W+"""MMMMMMM"""+colors.B+"""MMMM@         ||
       ||        @@MMM"""+colors.W+"""MMMMMM"""+colors.B+"""MMMMMMMM"""+colors.W+"""MMM"""+colors.B+"""MMMMMM"""+colors.W+"""MMM"""+colors.B+"""MMMMMMMMM         ||
       ||        @MMMM"""+colors.W+"""MMMMM"""+colors.W+"""MMMM"""+colors.B+"""MMMMM"""+colors.W+"""MMM"""+colors.B+"""MMMMMM"""+colors.W+"""MMMMMMM"""+colors.B+"""MMMM@         ||
       ||        @@MMM"""+colors.W+"""MMM"""+colors.B+"""MMM"""+colors.W+"""MMM"""+colors.B+"""MMMMM"""+colors.W+"""MMM"""+colors.B+"""MMMMMM"""+colors.W+"""MMMMMMM"""+colors.B+"""MMMMM         ||
       ||        @MMMM"""+colors.W+"""MMM"""+colors.B+"""MMM"""+colors.W+"""MMM"""+colors.B+"""MMMMM"""+colors.W+"""MMM"""+colors.B+"""MMMMMM"""+colors.W+"""MMM"""+colors.B+"""MMMMMMMM@         ||
       ||========@MMMM"""+colors.W+"""MMM"""+colors.B+"""MMM"""+colors.W+"""MMM"""+colors.B+"""MMMMM"""+colors.W+"""MMM"""+colors.B+"""MMMMMM"""+colors.W+"""MMM"""+colors.B+"""MMMMMMMMM=========||
       ||         """+colors.HH+""""""+colors.W+"""/TT\\"""+colors.HH+colors.B+"""mMMMMMMMMMM"""+colors.W+colors.HH+"""FRAMEWORK"""+colors.W+colors.HH+colors.B+"""MMMMMMMMMMMMm           ||
       ||        """+colors.W+"""(____)"""+colors.HH+colors.B+"""@MM@@MM@@MM@@MMMMMM@@MM@@Mm"""+colors.W+"""                ||
       ||        |# P |                                           ||
       ||        |# W | """+colors.HH+""" Core    """+colors.W+""" [ """+Information.version+""", Build: """+Information.build+""" ]        ||
       ||        |#_N_| """+colors.HH+""" Date    """+colors.W+""" [ """+Information.date+"""    ]        ||
       ||        |_  _| """+colors.HH+""" Banner  """+colors.W+""" [         SPACE        ]        ||        
       ||        /|__|\\  """+colors.HH+"""Modules """+colors.W+""" [ """""+str(get_number_modules())+""" ] """+colors.HH+"""Tools """+colors.W+"""[ """+str(get_number_tools())+""" ]              ||
       """+colors.GW+"""||       /__\/__\\"""+colors.GW+""" The Hacking Framework                    ||"""+colors.W+"""
                 ()  ()\n"""

Banner3 = """    
 -----+-----+-----+-----+-----+north+-----+-----+-----+-----+-----+-----
           , _-\','|~\~      ~/      ;-'_   _-'     ,;_;_,    ~~-
  /~~-\_/-'~'--' \          ,'      /  / ~|-_\_/~/~      ~~--~~~~'--_
  /                         ,'    , '|,'|~                   ._/-, /~
  ~/-'~\_,               . '      ,\ /'~                /    /_  /~
         '|        '',\~|\       _\~     ,_  ,               /|
          '\        /'~          |_/~\\,-,~  \ "         ,_,/ |
           |       /            ._-~'\_ _~|              \ ) /
            \   __-\           '/      ~ |\  \_          /  ~
             '\ |,  ~-_     """+colors.HH+"KATANA FRAMEWORK"""+colors.W+"""|  /\  \~ ,
               ~-_'  _;       '\           '-,   \,' /\/  |
                 '\_,~'\_       \_ _,       /'    '  |, /|'
                   /     \_       ~ |      /         \  ~'; -,_.
                   |       ~\        |    |  ,        '-_, ,; ~ ~\\
                            \,      /        \    / /|            ,-, ,   -,
 """+colors.HH+"""C"""+colors.W+"""["""+Information.version+"""]B["""+Information.build+"""]   |    ,/          |  |' |/          ,-   ~ \   '.
 """+colors.HH+"""D"""+colors.W+"""["""+Information.date+"""]|   ,/           \ ,/              \       |
 """+colors.HH+"""M"""+colors.W+"""["""""+str(get_number_modules())+"""]               /    |             ~                 -~~-, /   _
 """+colors.HH+"""B"""+colors.W+"""[MAP]             |  ,-'                                    ~    /
                    / ,'                                      ~
                    ',|   
                      ~' 
 -----+-----+-----+-----+-----+south+-----+-----+-----+-----+-----+-----"""


Banner4= """              
                             _
                           _|  \______________________________________
                          - ______        ________________          \_`,
                        -(_______   ACF      -=    -=        2933       )
                                 `--------=============----------------` 
                                           -   -
 """+colors.HH+"""C"""+colors.W+"""["""+Information.version+"""]B["""+Information.build+"""]                       -   -
 """+colors.HH+"""D"""+colors.W+"""["""+Information.date+"""]             `   . .  -  -
 """+colors.HH+"""B"""+colors.W+"""[Libertadores]   .*` .* ;`*,`.,
 Year-2016                       `, ,`.*.*. *
  ________________________________*  * ` ^ *____________________________"""

Banner5= """
                      
                             ⍶⍷⍸⍹⍣⍣
                            ⍹☊⍥☌☍⍬⍿⍪
                           ⍢⍣⍤⍥⍨⍩⍦⍧⍬⍹
                      ⍢⍣⍤⍥"""+colors.GW+colors.R+colors.HH+"""MMMMMMMMMMMM"""+colors.W+"""⍧.⎋
          ██╗  ██╗ █████╗ """+colors.GW+colors.R+colors.HH+"""MMP""MM""YMM"""+colors.W+""" █████╗ ███╗   ██╗ █████╗ 
          ██║ ██╔╝██╔══██╗"""+colors.GW+colors.R+colors.HH+"""P'"""+colors.W+"""☋⍧."""+colors.GW+colors.R+colors.HH+"""MM"""+colors.W+"""⍿⍪⍦"""+colors.GW+colors.R+colors.HH+"""`7"""+colors.W+"""██╔══██╗████╗  ██║██╔══██╗
          █████╔╝ ███████║.⎋⎍⍿⎎"""+colors.GW+colors.R+colors.HH+"""MM"""+colors.W+"""⍤⎋⎍⍩⍦███████║██╔██╗ ██║███████║
          ██╔═██╗ ██╔══██║⍾⎀⍽⍧⎃"""+colors.GW+colors.R+colors.HH+"""MM"""+colors.W+"""⍣⍦⍤⍥⍨██╔══██║██║╚██╗██║██╔══██║
          ██║  ██╗██║  ██║⍦⍧.⎋⍤"""+colors.GW+colors.R+colors.HH+"""MM"""+colors.W+"""⍦⍧⍬⍿⍪██║  ██║██║ ╚████║██║  ██║
          ╚═╝  ╚═╝╚═╝  ╚═╝⍬⍿⍪"""+colors.GW+colors.R+colors.HH+""".JMML."""+colors.W+"""⎋⎍⎎╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
                        ⍢⍣⍤⍥⍢⍣⍤⍥⍨⍩⍦⍧☋⍢⍣⍤⍥     """+colors.HH+"""C"""+colors.W+"""["""+Information.version+"""]B["""+Information.build+"""] 
                            ⍹☊☋☌⍤☍⍬⍿⍪         """+colors.HH+"""D"""+colors.W+"""["""+Information.date+"""] 
                             ⍥⍨⍩⍦⍧⍬☋          """+colors.HH+"""B"""+colors.W+"""[Hieroglyphics]
                              ☌☍⍬⍿⍪        القرصنة في العالم سخيف
                                                   
"""

Banner6= """
▄ •▄  ▄▄▄· ▄▄▄▄▄ ▄▄▄·  ▐ ▄  ▄▄▄·     ·▄▄▄▄▄▄   ▄▄▄· • ▌ ▄ ·. ▄▄▄ .▄▄▌ ▐ ▄▌      ▄▄▄  ▄ •▄ 
█▌▄▌▪▐█ ▀█ •██  ▐█ ▀█ •█▌▐█▐█ ▀█     ▐▄▄·▀▄ █·▐█ ▀█ ·██ ▐███▪▀▄.▀·██· █▌▐█▪     ▀▄ █·█▌▄▌▪
▐▀▀▄·▄█▀▀█  ▐█.▪▄█▀▀█ ▐█▐▐▌▄█▀▀█     ██▪ ▐▀▀▄ ▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄██▪▐█▐▐▌ ▄█▀▄ ▐▀▀▄ ▐▀▀▄·
▐█.█▌▐█ ▪▐▌ ▐█▌·▐█ ▪▐▌██▐█▌▐█ ▪▐▌    ██▌.▐█•█▌▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌▐█▌██▐█▌▐█▌.▐▌▐█•█▌▐█.█▌
·▀  ▀ ▀  ▀  ▀▀▀  ▀  ▀ ▀▀ █▪ ▀  ▀     ▀▀▀ .▀  ▀ ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀  ▀▀▀▀ ▀▪ ▀█▄▀▪.▀  ▀·▀  ▀
	       """+colors.HH+""" Core    """+colors.W+""" [ """+Information.version+""", Build: """+Information.build+""" ]
	       """+colors.HH+""" Date    """+colors.W+""" [ """+Information.date+"""    ]
	       """+colors.HH+""" Banner  """+colors.W+""" [          WAR         ]
	       """+colors.HH+""" Modules """+colors.W+"""    [ """""+str(get_number_modules())+""" ] """+colors.HH+"""Tools """+colors.W+"""[ """+str(get_number_tools())+""" ]\n"""
"""

Banner7= """
 _______ _______ _______ _______ _______ _______     _______ _______ _______ _______ _______ _______ _______ _______ _______ 
|\     /|\     /|\     /|\     /|\     /|\     /|   |\     /|\     /|\     /|\     /|\     /|\     /|\     /|\     /|\     /|
| +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |   | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
| |   | | |   | | |   | | |   | | |   | | |   | |   | |   | | |   | | |   | | |   | | |   | | |   | | |   | | |   | | |   | |
| |K  | | |A  | | |T  | | |A  | | |N  | | |A  | |   | |F  | | |R  | | |A  | | |M  | | |E  | | |W  | | |O  | | |R  | | |K  | |
| +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |   | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ | +---+ |
|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|   |/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|/_____\|
                                                                                                                             
	       """+colors.HH+""" Core    """+colors.W+""" [ """+Information.version+""", Build: """+Information.build+""" ]
	       """+colors.HH+""" Date    """+colors.W+""" [ """+Information.date+"""    ]
	       """+colors.HH+""" Banner  """+colors.W+""" [          WAR         ]
	       """+colors.HH+""" Modules """+colors.W+"""    [ """""+str(get_number_modules())+""" ] """+colors.HH+"""Tools """+colors.W+"""[ """+str(get_number_tools())+""" ]\n"""
"""

Banner8= """
                                                                  
                                                                    
    _/    _/    _/_/    _/_/_/_/_/    _/_/    _/      _/    _/_/    
   _/  _/    _/    _/      _/      _/    _/  _/_/    _/  _/    _/   
  _/_/      _/_/_/_/      _/      _/_/_/_/  _/  _/  _/  _/_/_/_/    
 _/  _/    _/    _/      _/      _/    _/  _/    _/_/  _/    _/     
_/    _/  _/    _/      _/      _/    _/  _/      _/  _/    _/      
                                                                    
                                                                   
"""

Banner9= """
 __  __  ______  ______ ______  __  __  ______      ____    ____    ______           ____    __      __  _____   ____    __  __     
/\ \/\ \/\  _  \/\__  _/\  _  \/\ \/\ \/\  _  \    /\  _`\ /\  _`\ /\  _  \  /'\_/`\/\  _`\ /\ \  __/\ \/\  __`\/\  _`\ /\ \/\ \    
\ \ \/'/\ \ \L\ \/_/\ \\ \ \L\ \ \ `\\ \ \ \L\ \   \ \ \L\_\ \ \L\ \ \ \L\ \/\      \ \ \L\_\ \ \/\ \ \ \ \ \/\ \ \ \L\ \ \ \/'/'   
 \ \ , < \ \  __ \ \ \ \\ \  __ \ \ , ` \ \  __ \   \ \  _\/\ \ ,  /\ \  __ \ \ \__\ \ \  _\L\ \ \ \ \ \ \ \ \ \ \ \ ,  /\ \ , <    
  \ \ \\`\\ \ \/\ \ \ \ \\ \ \/\ \ \ \`\ \ \ \/\ \   \ \ \/  \ \ \\ \\ \ \/\ \ \ \_/\ \ \ \L\ \ \ \_/ \_\ \ \ \_\ \ \ \\ \\ \ \\`\  
   \ \_\ \_\ \_\ \_\ \ \_\\ \_\ \_\ \_\ \_\ \_\ \_\   \ \_\   \ \_\ \_\ \_\ \_\ \_\\ \_\ \____/\ `\___x___/\ \_____\ \_\ \_\ \_\ \_\
    \/_/\/_/\/_/\/_/  \/_/ \/_/\/_/\/_/\/_/\/_/\/_/    \/_/    \/_/\/ /\/_/\/_/\/_/ \/_/\/___/  '\/__//__/  \/_____/\/_/\/ /\/_/\/_/
                                                                                                                                    
                                                                                                                                    
"""
def LoadBanner():
	RamdonBanner=random.randint(1,9)
	if RamdonBanner==1:print Banner1
	if RamdonBanner==2:print Banner2
	if RamdonBanner==3:print Banner3
	if RamdonBanner==4:print Banner4
	if RamdonBanner==5:print Banner5
	if RamdonBanner==6:print Banner6
	if RamdonBanner==7:print Banner7
	if RamdonBanner==8:print Banner8
	if RamdonBanner==9:print Banner9
