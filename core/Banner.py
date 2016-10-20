#!/usr/bin/python
# -*- coding: latin-1 -*-
#HEAD#########################################################
#
# Katana Framework | Banners                           
# Last Modified: 20/10/2016
#
#########################################################HEAD#

from core import colors,Information
from Function import get_number_modules,get_number_tools
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
                   |       ~\        |    |  ,        '-_, ,; ~ ~\
                            \,      /        \    / /|            ,-, ,   -,
 """+colors.HH+"""C"""+colors.W+"""["""+Information.version+"""]B["""+Information.build+"""]   |    ,/          |  |' |/          ,-   ~ \   '.
 """+colors.HH+"""D"""+colors.W+"""["""+Information.date+"""]|   ,/           \ ,/              \       |
 """+colors.HH+"""M"""+colors.W+"""["""""+str(get_number_modules())+"""]               /    |             ~                 -~~-, /   _
 """+colors.HH+"""B"""+colors.W+"""[MAP]             |  ,-'                                    ~    /
                    / ,'                                      ~
                    ',|   
                      ~' 
 -----+-----+-----+-----+-----+south+-----+-----+-----+-----+-----+-----"""



def LoadBanner():
	RamdonBanner=random.randint(1,3)
	if RamdonBanner==1:print Banner1
	if RamdonBanner==2:print Banner2
	if RamdonBanner==3:print Banner3


