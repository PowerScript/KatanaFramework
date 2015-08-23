<?php
// facebrok
// 404
error_reporting(E_ALL ^ E_NOTICE);
$lang=$_POST['idio'];
if ($lang=='')
{ 
if (file_exists("croak/install/install.php")) {header("location:croak/install/");} 
include("croak/config.php");
mysql_connect($DB_SERV,$DB_USER,$DB_PASS) or die ('Failed Connection: '.mysql_error());
mysql_select_db($DB_NADB) or die ('Failed in Databases: '.mysql_error());
$sql=mysql_query("SELECT * FROM methods WHERE id=3") or die('Failed in Consult: '.mysql_error());
$row=mysql_fetch_array($sql);
$lang=''.$row['value'].''; 
} else {$lang=$lang;}
include("lang.php");
?>
<?php include(getcwd()."/head.php");                   // Head     ?>
<?php include("sky.php");                    //  ?>
<center><?php include("grop/404$lang.php");  //  ?></center>
<?php include("foot.php");                   //  ?> 
