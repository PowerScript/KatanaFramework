<?php
$user=$_POST['user'];
$pass=$_POST['pass']; 
$user=   addslashes($user);
$pass=   addslashes($pass);
if ($user=='' or $pass=='') {header("Location:lost");} 
include ("config.php");
mysql_connect($DB_SERV,$DB_USER,$DB_PASS) or die ("Failed Connections: ".mysql_error());
mysql_select_db($DB_NADB) or die ("Failed: ".mysql_error());
$var=mysql_query("SELECT * FROM users WHERE user='$user' AND pass='$pass'");
$raw=mysql_fetch_assoc($var);
$sii=$raw['user'];
$nii=$raw['pass'];
if ($user==$sii | $pass==$nii){
	session_start();
	$_SESSION['user'] = $raw['user'];
	$_SESSION['pass'] = $raw['pass'];
	header("location:panel");
}else{header("Location:lost");}
?>



