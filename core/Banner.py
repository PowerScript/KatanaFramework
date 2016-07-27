#!/usr/bin/python
# -*- coding: latin-1 -*-
#HEADER#######################
# Katana framework           #
# Splash File                #
# Last Modified: 27/07/2016  #
# Review: 1                  #
#######################HEADER#

from core import colors,Information
from Function import get_number_modules,get_number_tools
import random          

tema="Army ...theme"

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
	       """+colors.HH+""" Theme   """+colors.W+""" [ """+tema+"""        ]
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
       ||        |_  _| """+colors.HH+""" Theme   """+colors.W+""" [ """+tema+"""        ]        ||        
       ||        /|__|\\  """+colors.HH+"""Modules """+colors.W+""" [ """""+str(get_number_modules())+""" ] """+colors.HH+"""Tools """+colors.W+"""[ """+str(get_number_tools())+""" ]              ||
       """+colors.GW+"""||       /__\/__\\"""+colors.GW+""" The Hacking Framework                    ||"""+colors.W+"""
                 ()  ()\n"""

def LoadBanner():
	RamdonBanner=random.randint(1,2)
	if RamdonBanner==1:print Banner1
	if RamdonBanner==2:print Banner2

