

# 
# Core::design>Warrior
#


		#White    #Red          #Green      #Orange    #Blue       #Purple     #Cyan
colors=['\033[0m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m'
		,'\033[1m', '\033[4m', '\033[0m', '\033[40m']
		#Bold       #Underl     #ENDL       #BackBlack

#print colors[0]+"0"+colors[1]+"1"+colors[2]+"2"+colors[3]+"3"+colors[4]+"4"+colors[5]+"5"+colors[6]+"6"+colors[7]+"7"+colors[8]+"8"+colors[9]+"9"+colors[10]+"10"

class DESIGN:
	def messages(self, message):
		if module == 1:
			print " test module"
	def prompt(self, module):
		promp=""+colors[0]+" ktn"+colors[0]+" | "+colors[3]+module+colors[0]+" > "
		return promp
	def option(self):
		print "\n [options]\t[RQ]\t[description]\t\t[value]"
		print " ---------\t----\t-------------\t\t-------"
	def descrip(self, option, rq, description, value):
		if rq == "yes":
			rq=colors[2]+"yes"+colors[0]
		else:
			rq=colors[1]+"no"+colors[0]
		print " "+option+"\t""\t"+rq+"\t"+description+"\t\t"+colors[8]+value+colors[0]
	def change(self, option, value):
		print "\n "+option+"\t\t==> "+value+"\n"
	def goodbye(self):
		print "\n "+colors[0]+"G"+colors[1]+"0"+colors[2]+"0"+colors[3]+"d"+colors[4]+" "+colors[5]+"B"+colors[6]+"y"+colors[7]+"e"+colors[0]+", Sr.\n"
	def run(self):
		print "\n ["+colors[2]+"+"+colors[0]+"] Running..."+colors[0]
		print " ["+colors[4]+"!"+colors[0]+"] Checking..."+colors[0]
	def off(self):
		print " ["+colors[1]+"-"+colors[0]+"] target Off-line"+colors[0]+"\n"
	def nocommand(self):
		print " ["+colors[4]+"!"+colors[0]+"] Invalid parameter use show 'help' for more information"+colors[0]
	def kbi(self):
		print "\n ["+colors[4]+"!"+colors[0]+"] Keyboard Interrupt"+colors[0]
	def loading(self):
		print " ["+colors[4]+"!"+colors[0]+"] Loading files..."+colors[0]
	def loaded(self):
		print " ["+colors[2]+"+"+colors[0]+"] Loaded file "+colors[0]
	def filenot(self):
		print " ["+colors[1]+"-"+colors[0]+"] Dictionary Not found"+colors[0]+"\n"
	def noptions(self):
		print "\n Options ["+colors[1]+"disabled"+colors[0]+"], you relax just "+colors[2]+"run"+colors[0]+" it...\n"
	def sucess(self, username, passwork):
		print "\n-["+colors[2]+"*"+colors[0]+"] Successfully with (username="+username+")(password="+password+")\n"
	def nodataallow(self):
		print " ["+colors[4]+"!"+colors[0]+"] parameter not allow"+colors[0]