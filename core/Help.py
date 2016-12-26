#!/usr/bin/env python2
#HEAD#########################################################
#
# Katana Framework | Help File                         
# Last Modified: 23/12/2016
#
#########################################################HEAD#

from GeneralCommands import *

def help():
	print """ 
     #General Commands.

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
     """+INVOKE+"""\t\t\t\t<--- Open a module in one new console 
     """+HELP+"""\t\t"""+HELP_SHORT+"""\t\t<--- Show help (this)
     """+CLEAR+"""\t\t"""+CLEAR_SHORT+"""\t\t<--- Clear screen
     """+SAVEV+"""\t\t"""+SAVEV+"""\t\t<--- Save Result
     """+SESSION+"""\t\t""""""\t\t<--- Session
     """+EXECUTECOMMAND+"""\t\t"""+EXECUTECOMMAND+"""\t\t<--- Execute System Commands
     f::\t\tf::\t\t<--- Execute Functions

     Version\t\t\t\t<--- Show Version framework

     #Functions(f::).

     [Name]\t\t [Parameters]\t\t[Description]
     get_aps()\t\t Interface, timeout\tScan Access point's
     get_interfaces()\t None\t\t\tGet Network Interfaces
     get_monitors_mode() None\t\t\tGet Monitor Interfaces Wireless
     start_monitor()\t Interface\t\tStart Monitor Mode in Interface
     get_local_ip()\t None\t\t\tGet local IP
     get_external_ip()\t None\t\t\tGet External IP
     get_gateway()\t None\t\t\tGet Gateway/Router IP

     ##USE.
     f::Functions(Parameters)   <-->  f::get_aps(mon0,10)
     f::Functions               <-->  f::get_local_ip
     
     #Save Result("""+SAVEV+""").
     if exist a output list in a module, you can save a item of list.
     
     Elements |#| ip        | mac               | ...
     item 0   [0] 127.0.0.1 | FF:FF:FF:FF:FF:FF | ...
     item 1   [1] 10.10.1.1 | FF:FF:FF:FF:FF:FC | ...
     
     ##USE (Type of elements allowed).
     ip:{index}                 <--> """+SAVEV+"""ip:0  --> save <-- 127.0.0.1
     mac:{index}                <--> """+SAVEV+"""mac:1 --> save <-- FF:FF:FF:FF:FF:FC
                                                    |
     Variable saved in ::{element}{index} <---------!

     list                       <--> List Global variables
     del:{element}:{index}      <--> delete a Global variable, (*) for all
     
     ### Examples.
     """+SAVEV+"""ip:0
     set target ::IP4
     """+SAVEV+"""list
     """+SAVEV+"""del:IP4 or """+SAVEV+"""del:*

     #Session.
     """+SESSION+""" -l                 <--> list sessions of module
     """+SESSION+""" -v {ID}            <--> view a session
     """+SESSION+""" -i {ID}            <--> Use a session
     """+SESSION+""" -d {ID}            <--> Delete a session , (*) for all

     ### Examples.
     """+SESSION+""" -v 3
     """+SESSION+""" -d *

     #TODO.
     Please go to https://github.com/PowerScript/KatanaFramework 
     for more information go to doc folder.
     """