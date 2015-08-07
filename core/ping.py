#
# Katana framework 
# @Katana Ping
#

import socket
import time 

def live(defaulthost, defaultport):
	red=socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
	red.connect((defaulthost, int(defaultport))) 
	red.close()
def save(module, target, port, dat1, dat2):
	log=open('core/logs/logsBruteForce.log','a')
	log.write('\n ===================================== ')
	log.write('\n Module  : '+module)
	log.write('\n Data    : '+time.strftime('%c'))
	log.write('\n target  : '+target)
	log.write('\n port    : '+port)
	log.write('\n Cracked : username : '+dat1+' , password : '+dat2)
	log.close()
def savetwo(module, files, password):
	log=open('core/logs/logsBruteForce.log','a')
	log.write('\n ===================================== ')
	log.write('\n Module  : '+module)
	log.write('\n Data    : '+time.strftime('%c'))
	log.write('\n file    : '+files)
	log.write('\n Cracked : password : '+password)
	log.close()