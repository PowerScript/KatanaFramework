# This module requires katana framework
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
from time import sleep
from core.Function import get_interfaces,checkDevice,get_monitors_mode,get_gateway
# END LIBRARIES

# END LIBRARIES
def init():
	init.Author             ="Thomas TJ (TTJ)"
	init.Version            ="1.0"
	init.Description        ="Bettercap integration"
	init.CodeName           ="net/bettercap"
	init.DateCreation       ="26/11/2016"
	init.LastModification   ="26/11/2016"
	init.References         =None
	init.License            =KTF_LINCENSE
	init.var                ={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME       VALUE               RQ     DESCRIPTION
		'interface'  :[INTERFACE_ETHERNET,True ,'Interface'],
		'gateway'    :[get_gateway()    ,True,'Gateway address'],
		'sniffer'    :["true"              ,False,'Acitvate sniffer'],
		'spoofer'    :["ARP"              ,False,'Spoof: ARP, ICMP, NONE'],
		'proxy'      :["true"              ,False,'HTTP proxy'],
		'target'     :["false"               ,False,'Target IPs'],
		'logfile'     :[""               ,False,'Logfile name'],
	    'path'       :["/usr/bin/bettercap"               ,True,'Path to bettercap']
	}

	init.aux = """
 (filter) options
 -> taget: Target IP addresses, if not specified the whole subnet will be targeted. (ADDRESS1,ADDRESS2)
 -> proxy: Enable HTTP proxy and redirects all HTTP requests to it. Downgrade HTTPS to HTTP for sniffing.
 -> spoofer: Spoofer module to use, available: ARP, NONE, ICMP - default: ARP.
 -> logfile: Log all messages into a file, if not specified the log messages will be only print into the shell.

 Devices Founds: """+str(get_interfaces())+"""
 Monitors Inter: """+str(get_monitors_mode())+"""
 Functions     : For Start Monitor Mode, type 'f::start_monitor(Interface)'
"""
	return init
# END INFORMATION MODULE

# CODE MODULE    ############################################################################################
def main(run):
    i = init.var['interface']
    if i:
        opt_com = '--interface ' + i + ' '

    g = init.var['gateway']
    if g:
        opt_com = opt_com + '--gateway ' + g + ' '

    s = init.var['sniffer']
    if s.lower() == 'true':
        opt_com += '--sniffer' + ' '

    p = init.var['proxy']
    if p.lower() == 'true':
        opt_com += '--proxy' + ' '

    s = init.var['spoofer']
    if s == 'ARP':
        opt_com += '--spoofer ARP' + ' '
    elif s == 'ICMP':
        opt_com += '--spoofer ICMP' + ' '
    else:
        opt_com += '--spoofer NONE' + ' '

    t = init.var['target']
    if t:
        opt_com += '--target ' + t + ' '

    l = init.var['logfile']
    if l:
        opt_com += '--log ' + l + ' ' + '--log-timestamp' + ' '

    command = (init.var['path'] + ' ' + opt_com)

    print("")
    printAlert(0, "Loading     : Bettercap")
    printAlert(0, "Command     : " + command)
    printAlert(0, "Stop        : Ctrl + C (and wait)")
    printAlert(0, "Starting in : 3 seconds")

    n = 3
    while n > 0:
        printAlert(0, "\t" + str(n) + "..  ")
        n = n-1
        sleep(1)
    print("\n\n")

    os.system(command)
    print("\n\n")
