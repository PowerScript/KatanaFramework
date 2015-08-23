<?php
// facebrok
// Login, login.
if (file_exists("install/install.php")) {header("location:install/");} 
session_start();
error_reporting(0);
if($_SESSION['user']){header("location:panel");}else{
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
<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/html"> 
<head>
<meta charset="utf-8" />
<title>facebrok</title>
<link href="minify.css" rel="stylesheet" type="text/css"/>
<link href="login.css " rel="stylesheet" type="text/css"/>
<link rel="shortcut icon" href="facebook.png" />
<table width="100%" border="0" height="100%" cellspacing="0">
<td valign="middle">
<div align="center">
<OBJECT classid>
</head>
<body class="login">
<div class="content">
<form method="POST" class="form-vertical login-form preloader-submit" action="whois">
<style type="text/css" media="screen"><!--a:link{text-decoration:none;}--></style>
 <h3 class="form-title" title="facebrok ;)"><center>facebrok</center></h3>
<div class="control-group">
<label class="control-label visible-ie8 visible-ie9">Username</label>
<div class="controls">
<div class="input-icon left">
<i class="icon-user"></i>
<input class="m-wrap placeholder-no-fix" type="text" title="Username" placeholder="username" name="user" value="" required="required"/>
</div>
</div>
</div>
<div class="control-group">
<label class="control-label visible-ie8 visible-ie9">Password</label>
<div class="controls">
<div class="input-icon left">
<i class="icon-lock"></i>
<input class="m-wrap placeholder-no-fix" type="password" title="Password" placeholder="password" name="pass" value="" required="required"/>
</div>
</div>
</div>
<input type="hidden" name="login_secret" value="">
<input type="hidden" name="r" value="index/index">
<div class="form-actions" style="padding-bottom:0px;">
<button type="submit" title="login" class="btn purple pull-right"><i class="preloader" style="display: none"></i>
Log in<i class="m-icon-swapright m-icon-white"></i>
</button>
</div>
</div></div></span>
</center>
</html>
<?php } ?>