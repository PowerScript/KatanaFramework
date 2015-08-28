#
# Katana framework 
# @Katana help
#

def help():
	W  = '\033[0m'  
	R  = '\033[31m' 
	G  = '\033[32m' 
	O  = '\033[33m' 
	B  = '\033[34m' 
	P  = '\033[35m' 
	C  = '\033[36m' 
	GR = '\033[37m'
	BO = '\033[1m'
	print BO+"""
				  _          _       
				 | |        | |      
				 | |__   ___| |_ __  
				 | '_ \ / _ \ | '_ \ 
				 | | | |  __/ | |_) |
				 |_| |_|\___|_| .__/ 
				              | |    
				              |_|    
"""+W
	print "     Katana is a framework for Hackers, Pentesters, Proffesional Security, Etc"
	print "     a framework multi-tool very util for pentest (penetrec test)"
	print ""
	print "     show modules or showm             <--- Show modules "
	print "     use                               <--- Use modules "
	print "     show options or sop               <--- Show Options of Module"
	print "     set                               <--- Change valor of a parameter"
	print "     run or r                          <--- Run Module"
	print "     update or u                       <--- Update framework"
	print "     back or b                         <--- Backing or return"
	print "     exit or x                         <--- Exit of framework"
	print "     help or h                         <--- Show help (this)"
	print "     clear or c                        <--- Clear screen)"
	print "    ~_______________________________________________________________~ "
	print """
	 [options]	[RQ]	[description]		[value]
	 ---------	----	-------------		-------
	 target		yes	IP or DNS		127.0.0.1
	 port		no	Port of target		21
""" 
	print ""
	print "     ["+G+"+"+W+"]Section of Options"  
	print "     |target    | the parameter is target"
	print "     |port      | the parameter is port" 
	print ""
	print "     ["+G+"+"+W+"]Section of RQ"  
	print "     |yes       | the parameter is need"
	print "     |no        | the parameter is'n need" 
	print ""
	print "     ["+G+"+"+W+"]Section of values"  
	print "     |127.0.0.1 | the value is 127.0.0..1"
	print "     |8080      | the value is 8080" 
	print ""
	print "     ["+G+"+"+W+"]Section of Configuration"
	print "     |set target 127.0.0.1    | the parameter was set up in 127.0.0.1"
	print "     |set port 80             | the parameter was set up in 80"
	print ""
	print "     Alerts "
	print ""
	print "     ["+G+"+"+W+"] Good or Successfully"
	print "     ["+B+"!"+W+"] Notification"
	print "     ["+R+"-"+W+"] Error"
	print "     ["+BO+"*"+W+"] Help Area"
	print ""
	print "     Parameter not allow      | the parameter not exists"
	print "     Dictionary Not found     | path wrong"
	print "     Keyboard Interrupt       | Ctrol+C"
	print "     ..."
	print ""
	print "     for more info go to github project https://github.com/redtoor/katana"
	print "     or send a email to redtoor[at]inbox.ru"
	print "     fb.com/redtoor - twitter.com/redtoor - plus.google.com/+redtoor"
	print ""
	print "     Based in "+G+"Python"+W+" with "+R+"<3"+W+" from "+O+"Col"+B+"om"+R+"bia "+W+"by "+R+"Red"+W+"Toor"
	print ""