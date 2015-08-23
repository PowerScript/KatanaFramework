<?php
// facebrok
// Set Up, Configuration.
session_start();
error_reporting(0);
if($_SESSION['user']){
include ("config.php");
mysql_connect($DB_SERV,$DB_USER,$DB_PASS) or die ('Failed Connection: '.mysql_error());
mysql_select_db($DB_NADB) or die ('Failed in Databases: '.mysql_error());
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
<title>facebrok - Set Up</title>
<link rel="shortcut icon" href="facebook.png" />
<link href="minify.css" rel="stylesheet" type="text/css"/>
<link href="login.css " rel="stylesheet" type="text/css"/>
<?php include ("bar.php"); ?>
<body class="login"><style type="text/css" media="screen">
<!--a:link   {text-decoration:none;}   -->
</style>
<div class="content">
<h4 class="form-title" title="Set UP"><center>Set Up<center></h4>
<br>
<a style='cursor: pointer;' onclick="">Clear DataBase</a>
<div id="a">
<form method="post" action="clear" target="_blank">
Pass current <input type="password" title="Password" required="required" name="pass" value="">
<input type="submit" title="Clear DataBase" name="delate" class="btn purple pull-right" value="Clear DB">
</form></div>
<a style='cursor: pointer;' onclick="">Update User</a>
<div id="b">
<form method="post" action="userup">
Pass current&nbsp <input type="password" title="Password" required="required" name="passs" value="">
User new&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" required="required" title="User" name="usern" value="">
Pass new&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="password" required="required" title="Password" name="passn" value="">
<input type="submit" title="submit" class="btn purple pull-right" value=" Update ">
</form></div>
<br><a title="Back" href="panel">
<span style="color:#666;font-size:14"><span style="font-family: Arial;">back</a>
<?php
} else {header("location:../croak");}
?>
