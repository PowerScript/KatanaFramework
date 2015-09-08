#
# Katana framework 
# @Katana Kab
#

from core import colors
from core import info
from core import ping 
from core.design import *
d=DESIGN()



if True:
	d.lab(info.version)
	print ""
	print " "+Suf+" Starting Katana Laboratory"
	print " "+Alr+" Coping Katana Laboratory to apache folder",ping.status_cmd("cp -R KatanaLAB /var/www/KatanaLAB","\t")
	print " "+Alr+" Giving privileges to folder",ping.status_cmd("chmod -c -R 777 /var/www/KatanaLAB/","\t\t\t")
	print " "+Alr+" Starting Apache2",ping.status_cmd("service apache2 start","\t\t\t\t")
	print " "+Suf+" Katana Lab Started"
	print ""
	d.go("http://localhost/KatanaLAB")
	print ""
	raw_input(" "+Hlp+" Press any key for Stop Katana Lab")
	print(" "+Alr+" Stoping Process")
	print " "+Alr+" Removing files",ping.status_cmd("rm -R /var/www/KatanaLAB","\t\t\t\t\t")
	print " "+Alr+" Stoping Apache2",ping.status_cmd("service apache2 stop","\t\t\t\t\t")
	print " "+Suf+" Katana Lab Stoped"
	print ""