from scripts import BruteForceHTTP
from core import help


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
	   help		:help about Katana
	   show modules	:modules
	   use		:use module
	  """

def catana():
	action = raw_input(B+" KtN> "+W)
	if action == "show modules":
		print "		modules\n"
		print "		web/httpbt\tHTTP Brute Force"
		catana()
	elif action[0:3] == "use":
		if action[4:14] == "web/httpbt":
			BruteForceHTTP.httpbt()
		else:
			print "[!] module "+O+"UNKNOW"
			catana()

	elif action == "exit":
		print C+"   GooD"+W+" bye."
		exit()
	elif action == "help":
		help.help()
	else:
		print "[!] command No "+O+"ACCEPT"+W
		catana()
	
catana()