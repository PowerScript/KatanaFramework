#
# Katana framework 
# @Katana Errors
#


from design import *
d=DESIGN()                   

def Errors(event, info):
	#DEBUG
	#print event, info

	string=str(event)
	if string.find("IOError") >= 0:
		return d.no_file_found(info)
	if string.find("socket") >= 0:
		return d.target_off(info)
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
		print "Event : %s \n Info: %s "  % (event,info)
		exit(0)
