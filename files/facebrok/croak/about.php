<?php
// facebrok 
// about, about.
session_start();
error_reporting(0);
if($_SESSION['user']){
?>
<!--
 ______
 | ___|
 | |_____________________  ___ _______  __
 |  ______ | ___|  __ | |__| |/ /_ | | / /
 | || |  | | |  | ____| __ | | / | | |/ /
 | || |__| | |__| |___||_| |  /|_| |   |
 |_||____,,|____|_____|____|__|____|_|\_\
        one tool awesome for you.
-->
<title>facebrok - about</title>
<link rel="shortcut icon" href="facebook.png" />
<link href="minify.css" rel="stylesheet" type="text/css"/>
<link href="login.css " rel="stylesheet" type="text/css"/>
<?php include ("bar.php"); ?>
<body class="login"><style type="text/css" media="screen">
<!--a:link   {text-decoration:none;}   -->
</style>
<div class="content">
<h4 class="form-title" title="methods"><center>about<center></h4>
<div id="a">
	<pre>
Name      : facebrok
Version   : 1.7
Autor     : RedToor
Country   : Colombia
Contact   : redtoor@inbox.ru
W project : facebrok.sourceforge.net
	</pre>
	<br>
<br><a title="Back" href="panel">
<span style="color:#666;font-size:14"><span style="font-family: Arial;">back</a>
<?php } else {header("location:../croak");} ?>