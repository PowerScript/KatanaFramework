#!/usr/bin/env python
### Katana Framework Laboratory
### you can redistribute it and/or modify
### it under the terms of the GNU General Public License as published by
### the Free Software Foundation, either version 3 of the License, or
### (at your option) any later version. 

from core.design import *
from core.Setting import *   
from core import info
from core import ping 
import sys

CLASS_BANNER=DESIGN()
CLASS_BANNER.ktflab(info.version,info.build)
try:
	print ""
	print " "+Suf+" Starting Katana Laboratory"
	print " "+Alr+" Coping Katana Laboratory to apache folder",ping.status_cmd("cp -R KatanaLAB "+PATCH_WWW+"KatanaLAB","\t")
	print " "+Alr+" Giving privileges to folder",ping.status_cmd("chmod -c -R 777 "+PATCH_WWW+"KatanaLAB/","\t\t\t")
	print " "+Alr+" Starting Apache2",ping.status_cmd("service apache2 start","\t\t\t\t")
	print " "+Suf+" Katana Lab Started"
	CLASS_BANNER.go("http://localhost/KatanaLAB")
	raw_input(" "+Hlp+" Press any key for Stop Katana Lab")
	print(" "+Alr+" Stoping Process")
	print " "+Alr+" Removing files",ping.status_cmd("rm -R "+PATCH_WWW+"KatanaLAB","\t\t\t\t\t")
	print " "+Alr+" Stoping Apache2",ping.status_cmd("service apache2 stop","\t\t\t\t\t")
	print " "+Suf+" Katana Lab Stoped"
	print ""
except:
	print sys.exc_info()
