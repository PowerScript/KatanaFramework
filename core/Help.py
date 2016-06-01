#!/usr/bin/env python
#HEADER#######################
# Katana framework           #
# Help File                  #
# Last Modified: 21/05/2016  #
# Review: 1                  #
#######################HEADER#

from GeneralCommands import *

def help():
	print """ 
     #General Commands

     [Command]\t\t[Quick Command]\t[Description]
     """+SHOW_MODULES+"""\t"""+SHOW_MODULES_SHORT+"""\t\t<--- Show modules 
     """+SHOW+"""\t"""+SHOW_SHORT+"""\t\t<--- Show options module
     """+SHOW_MORE+"""\t"""+SHOWM_SHORT+"""\t\t<--- Show full options module
     """+SELECT+"""\t\t"""+SELECT+"""\t\t<--- Use module 
     """+GETINFO+"""\t\t"""+GETINFO+"""\t\t<--- Show information of module
     """+SETET+"""\t\t"""+SETET+"""\t\t<--- Change valor of a parameter
     """+BACKING+"""\t\t"""+BACKING+"""\t\t<--- Backing or return
     """+RUN+"""\t\t"""+RUN+"""\t\t<--- Run Module
     """+UPDATE+"""\t\t"""+UPDATE_SHORT+"""\t\t<--- Update framework
     """+EXIT+"""\t\t"""+EXIT_SHORT+"""\t\t<--- Exit of framework
     """+HELP+"""\t\t"""+HELP_SHORT+"""\t\t<--- Show help (this)
     """+CLEAR+"""\t\t"""+CLEAR_SHORT+"""\t\t<--- Clear screen
     """+SAVEV+"""\t\t"""+SAVEV+"""\t\t<--- Save Variable
     """+EXECUTECOMMAND+"""\t\t"""+EXECUTECOMMAND+"""\t\t<--- Execute System Commands
     f::\t\tf::\t\t<--- Execute Functions

     Version\t\t\t\t<--- Show Version framework

     #Functions(f::)

     [Name]\t\t [Parameters]\t\t[Description]
     get_aps()\t\t Interface, timeout\tScan Access point's
     get_interfaces()\t None\t\t\tGet Network Interfaces
     get_monitors_mode() None\t\t\tGet Monitor Interfaces Wireless
     start_monitor()\t Interface\t\tStart Monitor Mode in Interface
     get_local_ip()\t None\t\t\tGet local IP
     get_external_ip()\t None\t\t\tGet External IP
     get_gateway()\t None\t\t\tGet Gateway/Router IP

     ##USE
     f::Functions(Parameters)   <-->  f::get_aps(mon0,10)
     f::Functions               <-->  f::get_local_ip

     #LINKS
     Please go to 
     https://github.com/PowerScript/KatanaFramework 
     for more information.
     """
