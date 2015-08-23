<?php
// are you man? ---------------------
session_start();
error_reporting(E_ALL^E_NOTICE);
if($_SESSION['user']){
//-----------------------------------
$texto="";
include ("config.php");
$con_base=mysql_connect($DB_SERV,$DB_USER,$DB_PASS);
$base=$DB_NADB;$mitabla="croak";
$datos=mysql_query("select * from $base.$mitabla;",$con_base);
$campos=mysql_num_fields($datos);
$regs=mysql_num_rows($datos);
for($i=0;$i<$regs;$i++)
{
$inserta="insert into $mitabla(";
for($j=0;$j<$campos;$j++)
{
$nombre=mysql_field_name($datos,$j);
$inserta.="$nombre,";
}
$inserta=substr($inserta,0,strlen($inserta)-1).") values(";
for($j=0;$j<$campos;$j++)
{
$tipo=mysql_field_type($datos,$j);
$valor=mysql_result($datos,$i,$j);
switch($tipo)
{
case "string":
case "date":
case "time":
$valor="'$valor'";
break;
}
$inserta.="$valor,";
}
$inserta=substr($inserta,0,strlen($inserta)-1).");";
$texto.=$inserta."\n";
}
$archivo= "Croak.sql";
header("Content-disposition: attachment;filename=$archivo");
header("Content-Type: text/plain");
echo '
CREATE TABLE `croak` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `Email` varchar(255) COLLATE utf8_spanish2_ci NOT NULL,
  `Password` varchar(255) COLLATE utf8_spanish2_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 COLLATE=utf8_spanish2_ci;';
echo $texto;} else {header("location:../croak");}
?>