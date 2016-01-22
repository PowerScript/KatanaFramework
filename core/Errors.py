#
# Katana framework 
# @Katana Errors
#


from design import *
d=DESIGN()                   

def Errors(event, info):
	#DEBUG
	#print event, info
	info=str(info)
	string=str(event)
	if string.find("IOError") >= 0:
		return d.no_file_found(str(info))
	if string.find("OperationalError(1045") >= 0:
		d.No_match()
		return
	if string.find("_mysql_exceptions.OperationalError") >= 0:
		print ' '+Bad+' Host '+info+' is not allowed to connect to this MySQL server.\n'
		return
	if string.find("socket") >= 0:
		return d.target_off(str(info))
	if string.find("KeyboardInterrupt") >= 0 and info!=False:
		d.kbi()
		return
	if string.find("KeyboardInterrupt") >= 0 and info==False:
		d.kbi()
		exit(0)
	if string.find("SystemExit") >= 0 and info==False:
		exit(0)
	if string.find("ValueError") >= 0:
		d.VError()
	else:
		print "\n Event : %s \n Info: %s "  % (event,info)
		exit(0)
