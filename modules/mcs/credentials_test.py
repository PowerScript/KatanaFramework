# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
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
	init.LastModification   ="23/12/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE     RQ     DESCRIPTION
		'target':[LOCAL_IP,True ,'Hostname Target'],
		'user'  :[USERNAME,False,'Username Target'],
		'pass'  :[PASSWORD,False,'Password Target']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):

	try:
		printk.inf("Testing Mysql protocol [3306]")
		MySQLdb.connect(init.var['target'],init.var['user'],init.var['pass'],'')
		printk.suff("Logged with "+init.var['user']+"/"+init.var['pass']+" in Mysql")
	except:printk.err("Service Off or No Logged.")

	try:
		printk.inf("Testing SSH protocol [22]")
		connect = pxssh.pxssh()
		connect.login(init.var['target'],init.var['user'],init.var['pass'])
		printk.suff("Logged with "+init.var['user']+"/"+init.var['pass']+" in SSH")
	except:printk.err("Service Off or No Logged.")

	try:
		printk.inf("Testing FTP protocol [21]")
		ftp.login(init.var['user'],init.var['pass'])
		printk.suff("Logged with "+init.var['user']+"/"+init.var['pass']+" in FTP")
	except:printk.err("Service Off or No Logged.")

	try:
		printk.inf("Testing POP3 protocol [110]")
		red=poplib.POP3(init.var['target'], 110)
		red.user(init.var['user']+"@"+init.var['target'])
		red.pass_(init.var['pass'])
		printk.suff("Logged with "+init.var['user']+"/"+init.var['pass']+" in POP3")
	except:printk.err("Service Off or No Logged.")
	Space()

# END CODE MODULE ############################################################################################
