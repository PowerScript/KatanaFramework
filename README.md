<center>
<img src="http://web.alsa.org/images/content/pagebuilder/KTF_Logo.jpg" title="Python" align="center">
</center>
---
[![Gitter chat](https://badges.gitter.im/totaljs/framework.png)](https://gitter.im/RedToor/Katana) ![Supported OS](https://img.shields.io/badge/Supported%20OS-Linux-yellow.svg) ![License](https://img.shields.io/badge/license-GPLv3-blue.svg) 
---
# ABOUT

katana is a framework written in python for making penetration testing, based on a simple and comprehensive structure for anyone to use, modify and share, the goal is to unify tools serve for professional when making a penetration test or simply as a routine tool, The current version is not completely stable, not complete. 

The project is open to partners.

# SOURCE CODE ORGANIZATION
The Katana source code is organized as follows:

<i>-[KatanaGUI/](https://github.com/RedToor/Katana/tree/master/KatanaGUI)</i> > Source code for graphical user interface<br>
<i>-[KatanaLAB/](https://github.com/RedToor/Katana/tree/master/KatanaLAB)</i> > Source code for katana laboratory<br>
<i>-[core/](https://github.com/RedToor/Katana/tree/master/core)</i> > Source code core<br>
<i>--[core/db/](https://github.com/RedToor/Katana/tree/master/core/db)</i> > Dictionaries and tables<br>
<i>--[core/logs/](https://github.com/RedToor/Katana/tree/master/core/logs)</i> > Registers of modules<br>
<i>-[files/](https://github.com/RedToor/Katana/tree/master/files)</i> > Files necessary for some modules<br>
<i>-[tmp/](https://github.com/RedToor/Katana/tree/master/tmp)</i> > Temp files<br>
<i>-[lib/](https://github.com/RedToor/Katana/tree/master/lib)</i> > Libraries<br>
<i>-[doc/](https://github.com/RedToor/Katana/tree/master/doc)</i> > Documentation<br>
<i>-[scripts/](https://github.com/RedToor/Katana/tree/master/scripts)</i> > Scripts(modules)<br>

# REQUIREMENTS
OS requirement:
        <img src="http://www.question-defense.com/wp-content/themes/qd/backtrack-menu/backtrack-logo.png"> Kali Linux

# INSTALLATION
Installation of Katana framework:
<i><b><br><br>
	git clone https://github.com/RedToor/katana.git<br>
        cd Katana<br>
        chmod 777 install.py<br>
        python install.py</i>
</i></b>

# USAGE
Commands
```
        Stable ------------------------------------------------------------------
        sudo ktfconsole                                     98% Builded - Enabled
        sudo ktfrun -m net/arpspoof                         95% Builded - Enabled
        Building ----------------------------------------------------------------
        ktflab                                              30% Builded - No yet.
        ktflinker -m web/whois -t google.com -p 80          30% Builded - No yet.
```
# MODULES (SCRIPTS)

Code Name | Description | Autor | Version
----------|-------------|-------|--------
web/httpbt|Brute force to http 403|Redtoor|1.0
web/formbt|Brute force to form-based|Redtoor|1.0
web/cpfinder|Admin panel finder|Redtoor|1.0
web/joomscan|Scanner vul's cms joomla|Redtoor|1.0
web/dos|Denial of service web|Redtoor|1.0
web/whois|Who-is web|Redtoor|1.0
net/arpspoof|ARP-Spoofing attack|Redtoor|1.0
net/arplook|ARP-Spoofing detector|cl34r|1.0
eng/gdreport|Getting information with web|RedToor|3.0
eng/mailboom|E-mail boombing SPAM|RedToor|3.0
eng/facebrok|facebook phishing plataform|RedToor|1.7
fle/brutezip|Brute force to zip files|LeSZO ZerO|1.0
fle/bruterar|Brute force to rar files|LeSZO ZerO|1.0
clt/ftp|Console ftp client|Redtoor|1.0
clt/sql|Console sql client|Redtoor|1.0
clt/pop3|Console pop3 client|Redtoor|1.0
clt/ftp|Console ftp client|Redtoor|1.0
ser/sql|Start SQL server|Redtoor|1.0
ser/apache|Start Apache server|Redtoor|1.0
ser/ssh|Start SSH server|Redtoor|1.0
bt/ftp|Brute force to ftp|Redtoor|1.0
bt/ssh|Brute force to ssh|Redtoor|1.0
bt/sql|Brute force to sql|Redtoor|1.0
bt/pop3|Brute force to pop3|Redtoor|1.0

# LICENSE
Katana is licensed. 
See [LICENSE](https://github.com/RedToor/Katana/blob/master/LICENSE) for more information.

We need partners, if you're interested in support or help contact.

from <img src="http://www.euromonitor.com/medialibrary/Image/Flag_20x20_Colombia.png" title="Colombia"> made in <img src="https://developer.ibm.com/predictiveanalytics/wp-content/uploads/sites/48/2015/04/python-icon.png" title="Python"> with <img src="http://cdn0.bodas.com.mx/img/smileys/smiley_heart.png" title="Love"> by <font color="red">Red</font>Toor, if you want Donate <img src="http://www.wbtcb.com/frontend/webroot/gfx/bitcoin-ico.gif" title="Bitcoins"> 1Hw2SSTpAZ7kSccvoYfvyQewGgMhtmya3u
