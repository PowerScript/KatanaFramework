#!/usr/bin/env python
#HEADER#######################
# Katana framework           #
# Help File                  #
# Last Modified: 26/03/2016  #
# Review: 0                  #
#######################HEADER#

def help():
	print """\n
     Katana framework help, General Commands:

     show                              <--- Show modules 
     use                               <--- Use modules 
     set                               <--- Change valor of a parameter
     run                               <--- Run Module
     update                            <--- Update framework
     back                              <--- Backing or return
     exit                              <--- Exit of framework
     help                              <--- Show help (this)
     clear                             <--- Clear screen
	 save                              <--- Save Variable
    ~_______________________________________________________________~ 

	 [options]	[RQ]	[description]		[value]
	 ---------	----	-------------		-------
	 target		yes	    IP or DNS		    127.0.0.1
	 port		no   	Port of target		21
    ~_______________________________________________________________~ 

     []Section of Options
     |target    | the parameter is target
     |port      | the parameter is port

     []Section of RQ
     |yes       | the parameter is need
     |no        | the parameter is'n need

     []Section of values
     |127.0.0.1 | the value is 127.0.0..1
     |8080      | the value is 8080

     []Section of Configuration
     |set target 127.0.0.1    | the parameter was set up in 127.0.0.1
     |set port 80             | the parameter was set up in 80


     for more info go to github project https://github.com/redtoor/katana\n"""