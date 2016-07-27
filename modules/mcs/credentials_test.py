# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from lib.ftplib.ftplib import FTP
from pexpect import pxssh
import poplib,MySQLdb,socket
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.1"
	init.Description        ="Test Credentials protocols."
	init.CodeName           ="mcs/ts.login"
	init.DateCreation       ="03/05/2015"      
	init.LastModification   ="14/06/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE     RQ     DESCRIPTION
		'target':[LOCAL_IP,True ,'Hostname Target'],
		'user'  :[USERNAME,False,'Username Target'],
		'pass'  :[PASSWORD,False,'Password URL'],
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):

	try:
		printAlert(0,"Testing Mysql protocol [3306]")
		MySQLdb.connect(init.var['target'],init.var['user'],init.var['pass'],'')
		printAlert(3,"Logged with "+init.var['user']+"/"+init.var['pass']+" in Mysql")
	except:printAlert(1,"Service Off or No Logged.")

	try:
		printAlert(0,"Testing SSH protocol [22]")
		connect = pxssh.pxssh()
		connect.login(init.var['target'],init.var['user'],init.var['pass'])
		printAlert(3,"Logged with "+init.var['user']+"/"+init.var['pass']+" in SSH")
	except:printAlert(1,"Service Off or No Logged.")

	try:
		printAlert(0,"Testing FTP protocol [21]")
		ftp.login(init.var['user'],init.var['pass'])
		printAlert(3,"Logged with "+init.var['user']+"/"+init.var['pass']+" in FTP")
	except:printAlert(1,"Service Off or No Logged.")

	try:
		printAlert(0,"Testing POP3 protocol [110]")
		red=poplib.POP3(init.var['target'], 110)
		red.user(init.var['user']+"@"+init.var['target'])
		red.pass_(init.var['pass'])
		printAlert(3,"Logged with "+init.var['user']+"/"+init.var['pass']+" in POP3")
	except:printAlert(1,"Service Off or No Logged.")
	Space()

# END CODE MODULE ############################################################################################
