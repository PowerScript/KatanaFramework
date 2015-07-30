<?php
error_reporting(0);


$username=$_POST['username'];
$username=addslashes($username);
$username=strip_tags($username);

$password=$_POST['password'];
$password=addslashes($password);
$password=strip_tags($password);

if ($password=="toor" and $username=="administrator"){
	print " Welcome Administrator";
}else{
	print " Wrong in username or password";
}

?>