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
	else:
		print "Event : %s \n Info: %s "  % (event,info)