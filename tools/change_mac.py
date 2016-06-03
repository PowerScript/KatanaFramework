# This Tool requires katana framework 
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import                  #
from core.KATANAFRAMEWORK import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES  
from core.Function import checkDevice,checkMAC
import random, sys, re, optparse, hashlib, re
# END LIBRARIES 

class init:

    Author      = "0xicl33n"
    Description = "Changemac - change mac for interface"
    var         = {}
    Arguments   = {

        'i':[True ,'interface to change mac'],
        'm':[False,'specific mac'],
        'r':[False,'ramdom mac']
    }

def Main():

    MAC=""
    picks = ['katana','k4tan4','KAtAn4','K4TanA','K4TaNA','KATANA','ANATAK','|<474/\/A']
    a = hashlib.md5(random.choice(picks))
    b = a.hexdigest()
    as_int = int(b, 16)
    random.seed(bin(as_int)[2:])

    mac = [ 0x00, 0x16, 0x3e,
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff) ]

    if init.var['r'] == "enable":MAC=':'.join(map(lambda x: "%02x" % x, mac))
    if checkMAC(init.var['m']) and init.var['m']!="null" and init.var['m']!="enable":MAC=init.var['m']
    
    if checkDevice(init.var['i']):
        printAlert(0,"Changing MAC to "+init.var['i'])
        printAlert(0,"MAC to Change "+MAC)
        sysc("sudo airmon-ng check kill")
        sysc("sudo ifconfig "+init.var['i']+" down")
        sysc("sudo ifconfig "+init.var['i']+" hw ether") 
        sysc("sudo ifconfig "+init.var['i']+" up") 
        printAlert(3,"MAC Changed")
        return
