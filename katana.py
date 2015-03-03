# KATANA Vs 0,1

from scripts import GetDataReport
from scripts import ARPLooking
from scripts import BruteForceFormBase
from scripts import BruteForceHTTP
from scripts import AdminFinder
from core import help
from core import updatekatana


W  = '\033[0m'  
R  = '\033[31m' 
G  = '\033[32m' 
O  = '\033[33m' 
B  = '\033[34m' 
P  = '\033[35m' 
C  = '\033[36m' 
GR = '\033[37m'

print """
	   
                  __                         __--
         ___  ___/  \_______________   ___  /  \---
         | .|/ ./ __ \__   ___/.....\  | | / __ \----
         | .  ./ /__\ \/../ _ \. /\..\ | |/ /__\ \-----
         | .| .\.\  /./../ /_\.\.\ \..\| |\.\  /./---
         |_.|\_.\.\/./._/./   \_\.\ \..__| \.\/./--
	    _______?_________________________________
	   {_| | | |##################################>
	      ^ ^ ^               THE FRAMEWORK, VS 0.1
	   by RedToor

	   """+R+"""Command"""+W+"""\t"""+C+"""Description"""+W+"""
	   help		: help about command
	   show modules	: modules
	   use		: use module
	   set          : set up 
	   update       : update Katana
	  """

def katana():
	action = raw_input(B+" KtN> "+W)
	if action == "show modules":
		print "\n 	___________________"
		print "	|web's application|"
		print "	---------------------------------------------"
		print "	|web/httpbt\t | HTTP Brute Force        |"
		print "	|web/formbt\t | FORM Brute Force        |"
		print "	|web/cpfinder\t | Admin Finder            |"
		print "	---------------------------------------------\n 	__________________"
		print "	|sniffing network|"
		print "	---------------------------------------------"
		print "	|net/arplook\t | ARP Attack Detect       |"
		print "	---------------------------------------------\n 	___________________"
		print "	|social engineering|"
		print "	---------------------------------------------"
		print "	|seng/gdreport\t | Getting information     |"
		katana()
	elif action[0:3] == "use":
		if action[4:14] == "web/httpbt":
			BruteForceHTTP.httpbt()
		if action[4:16] == "web/cpfinder":
			AdminFinder.adminfinder()
		if action[4:16] == "web/formbt":
			BruteForceFormBase.httpformbasebruteforce()
		if action[4:16] == "net/arplook":
			ARPLooking.arplook()
		if action[4:17] == "seng/gdreport":
			GetDataReport.getdatareport()

		else:
			katana()
	elif action == "exit":
		print C+"   GooD"+W+" bye."
		exit()
	elif action == "help":
		help.help()
	elif action == "update":
		updatekatana.update()
	else:
		print "[!] command No "+O+"ACCEPT"+W
		katana()
katana()