# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
from lib.postfile import postfile
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.0"
	init.Description        ="Report of Virus Scan file API (VirusTotal.com)."
	init.CodeName           ="fle/scan.file"
	init.DateCreation       ="09/11/2016"      
	init.LastModification   ="27/12/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE                                                             RQ     DESCRIPTION
		'file':["files/test/test.zip"                                              ,True ,'file to scan'],
		'api' :["58b5c32650a6bc2e7ba2ec91b0d837efc2acf3d08b4f1081927d8df2dfc6b59b" ,True ,'API key secret']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):

	Loadingfile(init.var['file'])
	v = postfile.VirusTotal(init.var['api'])
	report = v.get(init.var['file'])
	print "   | Resource's UID:", report.id
	print "   | Scan's UID:", report.scan_id
	print "   | Permalink:", report.permalink
	print "   | Resource's SHA1:", report.sha1
	print "   | Resource's SHA256:", report.sha256
	print "   | Resource's MD5:", report.md5
	print "   | Resource's status:", report.status
	print "   | Antivirus' total:", report.total
	print "   | Antivirus's positives:", report.positives
	for antivirus, malware in report:
	    if malware is not None:
	        print "   | Antivirus:", colors[2]+antivirus[0]+" version:", antivirus[1]+colors[0]
	        print "   | Malware:", colors[1]+malware+colors[0]

# END CODE MODULE ############################################################################################
