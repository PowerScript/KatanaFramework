def help():
	W  = '\033[0m'  
	R  = '\033[31m' 
	G  = '\033[32m' 
	O  = '\033[33m' 
	B  = '\033[34m' 
	P  = '\033[35m' 
	C  = '\033[36m' 
	GR = '\033[37m'
	print ""
	print "     show modules                      <--- Show modules "
	print "     show options                      <--- Show Options of Module"
	print "     set                               <--- Change valor of a parameter"
	print "     run                               <--- Run Module"
	print "     update                            <--- Update framework"
	print ""
	print "     ["+R+"+"+W+"] options             <--- Section of information"  
	print "     |parameter 1  : yes          | the parameter is need"
	print "     |parameter 2  : yes/no       | the parameter is'n need" 
	print ""
	print "     ["+G+"+"+W+"] options current     <--- Section of Configuration"
	print "     |parameter_1  : 127.0.0.1    | the parameter was set in 127.0.0.1"
	print "     |parameter_2  : 80           | the parameter was set in 80"
	print ""