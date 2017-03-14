# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
from lib import whois
import json
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="2.0"
	init.Description        ="Whois, DNS lookup. DNS Information"
	init.CodeName           ="web/whois"
	init.DateCreation       ="09/07/2015"      
	init.LastModification   ="14/03/2017"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE                RQ     DESCRIPTION
		'target':[LOCAL_IP            ,True ,'Host Target']
	}
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
	
	result = whois.whois(init.var['target'])
	result_parse = json.loads(str(result))
	print "     |"
	print "     | Date: "+str(result_parse["updated_date"])
	print "     | Status: "
	#print result_parse["status"]
	for u in result_parse["status"]:
		if len(u) == 1:
			print "     |        "+str(result_parse["status"])
			break
		print "     |        "+str(u)
	print "     | Name: "+str(result_parse["name"])
	print "     | Dnssec: "+str(result_parse["dnssec"])
	print "     | City:   "+str(result_parse["city"])
	print "     | Expiration date: "+str(result_parse["expiration_date"])
	print "     | Zipcode: "+str(result_parse["zipcode"])
	print "     | Domain names:"
	for n in result_parse["domain_name"]:
		if len(n) == 1:
			print "     |        "+str(result_parse["domain_name"])
			break
		print "     |        "+str(n)	
	print "     | Whois servers: "+str(result_parse["whois_server"])
	print "     | State: "+str(result_parse["state"])
	print "     | Registrar: "+str(result_parse["registrar"])
	print "     | Referral url: "+str(result_parse["referral_url"]) 
	print "     | Country: "+str(result_parse["country"])
	print "     | Name servers:"
	for s in result_parse["name_servers"]:
                if len(s) == 1:
                        print "     |        "+str(result_parse["name_servers"])
                        break
		print "     |        "+str(s)
	print "     | Org: "+str(result_parse["org"])
	print "     | Creation date: "+str(result_parse["creation_date"])
	print "     | Emails:"
	for e in result_parse["emails"]:
                if len(e) == 1:
                        print "     |        "+str(result_parse["emails"])
                        break
		print "     |        "+str(e)
	print "     |"

# END CODE MODULE ############################################################################################
