# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
from lib.adb.adb import adb_commands,common_cli
import stat,os
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.0"
	init.Description        ="Console Client for ADB."
	init.CodeName           ="clt/cl.adb"
	init.DateCreation       ="18/08/2015"      
	init.LastModification   ="31/08/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE               RQ     DESCRIPTION
		'device':["16xxxxxxxxxxxxxx" ,True ,'Device Target']
	}

	init.aux = "\n List Device Connected:\n "+str(COM.ListDevicesConnectADB())+"\n"

	return init
# END INFORMATION MODULE

def List(self, device_path):
  files = adb_commands.AdbCommands.List(self, device_path)
  files.sort(key=lambda x: x.filename)
  maxname = max(len(f.filename) for f in files)
  maxsize = max(len(str(f.size)) for f in files)
  for f in files:
    mode = (
      ('d' if stat.S_ISDIR(f.mode) else '-') +
      ('r' if f.mode & stat.S_IRUSR else '-') +
      ('w' if f.mode & stat.S_IWUSR else '-') +
      ('x' if f.mode & stat.S_IXUSR else '-') +
      ('r' if f.mode & stat.S_IRGRP else '-') +
      ('w' if f.mode & stat.S_IWGRP else '-') +
      ('x' if f.mode & stat.S_IXGRP else '-') +
      ('r' if f.mode & stat.S_IROTH else '-') +
      ('w' if f.mode & stat.S_IWOTH else '-') +
      ('x' if f.mode & stat.S_IXOTH else '-'))
    t = time.gmtime(f.mtime)
    yield '   [%s] %*d %04d-%02d-%02d %02d:%02d:%02d %-*s\n' % (
        mode, maxsize, f.size,
        t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec,
        maxname, f.filename)

# CODE MODULE    ############################################################################################
def main(run):

	printk.inf("ADB Console (Android USB)")
	HelpBanner  = [["Commands","Description","Example"]]
	HelpBanner += [["devices","list devices","devices"]]
	HelpBanner += [["reboot","reboot device","reboot"]]
	HelpBanner += [["push","push a file to the device","push /root/text.txt /text.txt"]]	
	HelpBanner += [["pull","pull a file from the device","pull /text.txt /root/text.txt"]]	
	HelpBanner += [["cd","browser directories","cd data"]]
	HelpBanner += [["ls","list files","ls"]]
	GRAPHICAL.CreateTable(HelpBanner)

	cmd="nop"
	path="/"

	while(cmd!="exit"):
		main.command_name='list'
		main.positional=[path]
		main.auth_timeout_s=600.0
		main.timeout_ms=10000
		main.device_path=None
		main.rsa_key_path=[]
		main.port_path=None
		main.serial=None
		main.verbose=False

		cmd = raw_input(ClientPrompt(init.CodeName,"adb/"+path))
		if cmd[:2] == "cd":
			main.method=List			
			if cmd[3:] != "..": path+=cmd[3:]+"/"
			if cmd[3:] == "..": 
				head, tail = os.path.split(os.path.split(path)[0])
				path=str(head)+"/"
			main.positional=[path]
			Execute(main)
		if cmd[:2] == "ls":
			main.method=List
			if cmd[3:]=="":lsto=path
			else:lsto=cmd[3:]
			main.positional=[lsto]
			Execute(main)
		if cmd[:4] == "push":
			main.method=adb_commands.AdbCommands.Push
			cmd = cmd.split(" ")
			main.positional=[cmd[1],cmd[2],'0']
			Execute(main)
		if cmd[:4] == "pull":
			main.method=adb_commands.AdbCommands.Pull
			cmd = cmd.split(" ")
			main.positional=[cmd[1],cmd[2],'0']
			Execute(main)
		if cmd == "reboot":
			main.command_name='reboot'
			main.method=adb_commands.AdbCommands.Reboot
			Execute(main)
		if cmd == "devices":print COM.ListDevicesConnectADB()
		if cmd[:3] == "cat":print "ver"
		if cmd == "help"   :GRAPHICAL.CreateTable(HelpBanner)

# END CODE MODULE ###########################################################################################

def Execute(data):
	common_cli.StartCli(
      data,
      adb_commands.AdbCommands.ConnectDevice,
      auth_timeout_ms=data.auth_timeout_s * 1000,
      rsa_keys=[rsa_signer(path) for path in data.rsa_key_path])
