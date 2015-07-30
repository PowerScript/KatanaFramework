# Katana Lab

from core import colors
import subprocess            
if True:
	print " ["+colors.G+"+"+colors.W+"] Starting Katana Laboratory"
	print " ["+colors.O+"!"+colors.W+"] Coping Katana Laboratory to apache folder"
	subprocess.call('cp -R KatanaLAB /var/www/KatanaLAB', shell=True)
	print " ["+colors.O+"!"+colors.W+"] Giving privileges to folder"
	subprocess.call('chmod -c -R 777 /var/www/KatanaLAB/', shell=True)
	print " ["+colors.O+"!"+colors.W+"] Starting Apache2"
	subprocess.call('service apache2 start', shell=True)
	print " ["+colors.G+"+"+colors.W+"] Katana Lab Started"
	print ""
	print " ["+colors.B+">"+colors.W+"] Go to http://localhost/KatanaLAB"
	print ""
	raw_input(" ["+colors.R+"-"+colors.W+"] Press any key for Stop Katana Lab")
	print(" ["+colors.O+"!"+colors.W+"] Stoping Process")
	subprocess.call('rm -R /var/www/KatanaLAB', shell=True)
	subprocess.call('apache2ctl stop', shell=True)
	print " ["+colors.G+"+"+colors.W+"] Katana Lab Stoped"
