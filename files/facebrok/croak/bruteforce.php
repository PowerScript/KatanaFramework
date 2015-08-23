<?php
// facebrok 
// Spammer, templates.
// Credits Mauritania Attacker&Noname-Hax0r
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
<title>facebrok - Brute force</title>
<link rel="shortcut icon" href="facebook.png" />
<link href="minify.css" rel="stylesheet" type="text/css"/>
<link href="login.css " rel="stylesheet" type="text/css"/>
<body class="login">
<style type="text/css" media="screen"><!--a:link   {text-decoration:none;}   --></style>
<?php include ("bar.php"); ?>
<div class="content">
<h4 class="form-title" title="methods"><center>brute force<center></h4>
<div id="a">
<form method="post" action="cracking" target="_blank">

<span style="color:#666;font-size:14"><span style="font-family: Arial;"><pre>

username's
<textarea cols='22' class='area'  rows='9' name='username' style="width:100%"></textarea> 
password's
<textarea cols='22' class='area'  rows='9' name='password' style="width:100%"></textarea><br>
</pre>
<center>
<br>
<input type="submit" title="launch" name="launch" class="btn purple pull-right" value="Launch"></center></form></div>

<br>
<br><a title="Back" href="panel">
<span style="color:#666;font-size:14"><span style="font-family: Arial;">back</a>
<?php } else {header("location:../croak");} ?>