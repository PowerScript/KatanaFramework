<?php


error_reporting(0);
include ("geoiploc.php");
$id=$_GET['id'];


$country=getCountryFromIP("".$_SERVER['REMOTE_ADDR']."", " NamE ");

$data.="<pre>";
$data.="Target   : ".$id."<br>";
$data.="Ip       : ".$_SERVER['REMOTE_ADDR']."<br>";
$data.="Port     : ".$_SERVER['REMOTE_PORT']."<br>";
$data.="Country  : ".$country."<br>";
$data.="Language : ".$_SERVER['HTTP_ACCEPT_LANGUAGE']."<br>";
print $data;

$netspeed = geoip_id_by_name('186.0.111.62');

echo 'El tipo de conexión es';

switch ($netspeed) {
    case GEOIP_DIALUP_SPEED:
        echo 'módem';
        break;
    case GEOIP_CABLEDSL_SPEED:
        echo 'cable o ADSL';
        break;
    case GEOIP_CORPORATE_SPEED:
        echo 'corporativo';
        break;
    case GEOIP_UNKNOWN_SPEED:
    default:
        echo 'desconocido';
}

?>