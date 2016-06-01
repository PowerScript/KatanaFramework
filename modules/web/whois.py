# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
from core.Function import isLive
from lib import whois
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.1"
	init.Description        ="Whois, DNS lookup. DNS Information"
	init.CodeName           ="web/whois"
	init.DateCreation       ="09/07/2015"      
	init.LastModification   ="12/06/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE                RQ     DESCRIPTION
		'target':[LOCAL_IP            ,True ,'Host Target'],
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	isLive(init.var['target'],HTTP_PORT)

	w = whois.whois(init.var['target'])
	wd = w.__dict__
	for k, v in wd.items():
		print(colors[10]+'%20s\t"%s"' % (k, v))
		print colors[0]

# END CODE MODULE ############################################################################################