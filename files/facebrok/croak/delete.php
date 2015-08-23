<?php
session_start();
error_reporting(E_ALL^E_NOTICE);
if($_SESSION['user']){
include ("config.php");
mysql_connect($DB_SERV,$DB_USER,$DB_PASS);
mysql_select_db($DB_NADB);

$id=$_GET['id'];
mysql_query("DELETE FROM croak WHERE id=$id");
header("location:panel");
} else {header("location:../croak");}
