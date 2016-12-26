#!/usr/bin/env python
#HEAD#########################################################
#
# Katana Framework | Errors                           
# Last Modified: 23/12/2016
#
#########################################################HEAD#

from Design import *
from Config import ERROR_LOG
from Internal import SaveErrorLog

import sys
d=DESIGN()                   

def Errors():
	try:
		event = sys.exc_info()
		Alert        = "Nothing"
		Error        = str(event[0]).replace("<class '","").replace("'>","").replace("<type '","")
		ClassError   = Error.split(".")

		#DEBUG
		#print event
		#print sys.exc_traceback.tb_lineno
		#print sys.exc_traceback.tb_frame.f_code.co_filename

		if ClassError[0] == "socket"      :     
			if ClassError[1] == "error"   : Alert = " ["+colors[3]+"Socket"+colors[0]+"]"+error
			elif ClassError[1] == "timeout" : Alert = " ["+colors[3]+"Socket"+colors[0]+"]"+warning
			elif ClassError[1] == "gaierror": Alert = " ["+colors[3]+"Socket"+colors[0]+"]"+warning

		elif ClassError[0] == "ftplib"      :
			if ClassError[1] == "error_perm"       : Alert = " ["+colors[3]+"Ftp"+colors[0]+"]"+warning

		elif ClassError[0] == "_mysql_exceptions":
			if ClassError[1] == "OperationalError" : Alert = " ["+colors[3]+"Sql"+colors[0]+"]"+error
			if ClassError[1] == "ProgrammingError" : Alert = " ["+colors[3]+"Sql"+colors[0]+"]"+error

		elif ClassError[0] == "exceptions"  : 
			if ClassError[1] == "ValueError"                : Alert = " ["+colors[3]+"Exception"+colors[0]+"]"+error
			elif ClassError[1] == "IOError"                   : Alert = " ["+colors[3]+"Exception"+colors[0]+"]"+error
			elif ClassError[1] == "NameError"                 : Alert = " ["+colors[3]+"Exception"+colors[0]+"]"+error+"[Line #"+str(sys.exc_traceback.tb_lineno)+"]"
			elif ClassError[1] == "UnboundLocalError"         : Alert = " ["+colors[3]+"Exception"+colors[0]+"]"+error+"[Line #"+str(sys.exc_traceback.tb_lineno)+"]"
			elif ClassError[1] == "AttributeError"            : Alert = " ["+colors[3]+"Exception"+colors[0]+"]"+error+"[Line #"+str(sys.exc_traceback.tb_lineno)+"]"
			elif ClassError[1] == "KeyboardInterrupt"         : Alert = "\n ["+colors[3]+"Exception"+colors[0]+"]"+warning
			elif ClassError[1] == "DeprecationWarning"        : Alert = " ["+colors[3]+"Exception"+colors[0]+"]"+warning
			elif ClassError[1] == "PendingDeprecationWarning" : Alert = " ["+colors[3]+"Exception"+colors[0]+"]"+warning
			elif ClassError[1] == "RuntimeWarning"            : Alert = " ["+colors[3]+"Exception"+colors[0]+"]"+warning
			elif ClassError[1] == "SyntaxWarning"             : Alert = " ["+colors[3]+"Exception"+colors[0]+"]"+warning
			elif ClassError[1] == "UserWarning"               : Alert = " ["+colors[3]+"Exception"+colors[0]+"]"+warning
			elif ClassError[1] == "FutureWarning"             : Alert = " ["+colors[3]+"Exception"+colors[0]+"]"+warning
			elif ClassError[1] == "ImportWarning"             : Alert = " ["+colors[3]+"Exception"+colors[0]+"]"+warning
			elif ClassError[1] == "UnicodeWarning"            : Alert = " ["+colors[3]+"Exception"+colors[0]+"]"+warning
			elif ClassError[1] == "BytesWarning"              : Alert = " ["+colors[3]+"Exception"+colors[0]+"]"+warning
		else:
			print " ["+colors[3]+"Exception"+colors[0]+"]"+"("+str(event[1])+")\n"
			return

		if str(event[1]) == "1995" : sys.exit(0)
		print Alert+"("+str(event[1])+")\n"
	except Exception as E:print E
	finally:
		if ERROR_LOG:SaveErrorLog(str(event)+"#"+str(sys.exc_traceback.tb_lineno)+":"+str(sys.exc_traceback.tb_frame.f_code.co_filename))