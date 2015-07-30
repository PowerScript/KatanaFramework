<?php
error_reporting(0);
$module=$_GET['module'];
$module=addslashes($module);
$module=strip_tags($module);
switch ($module) {
	case 'formbt':
		$title="(formbt) HTML Form-based";
		$descriptions='
		While both HTTP access authentication schemes may appear suitable for commercial use over the Internet, particularly when used over an SSL encrypted session, many organizations have chosen to utilize custom HTML and application level authentication procedures, in order to provide a more sophisticated authentication procedure.
<br>
<pre style="background-color: #f7f7f7; border-radius: 3px; box-sizing: border-box; color: #333333; font-family: Consolas,Menlo, Courier, monospace; font-size: 13.6000003814697px; font-stretch: normal; line-height: 1.45; margin-bottom: 16px; overflow: auto; padding: 16px; word-wrap: normal;"><code style="background: transparent; border-radius: 3px; border: 0px; box-sizing: border-box; display: inline; font-family: Consolas,, Menlo, Courier, monospace; font-size: 13.6000003814697px; line-height: inherit; margin: 0px; max-width: initial; overflow: initial; padding: 0px; word-break: normal; word-wrap: normal;">
&lt;form method="POST" action="login.php"&gt;
 &lt;input type="text" name="username"&gt;
 &lt;input type="password" name="password"&gt;
&lt;/form&gt;

</code></pre>

HTTP Request

<br>
<pre style="background-color: #f7f7f7; border-radius: 3px; box-sizing: border-box; color: #333333; font-family: Consolas,Menlo, Courier, monospace; font-size: 13.6000003814697px; font-stretch: normal; line-height: 1.45; margin-bottom: 16px; overflow: auto; padding: 16px; word-wrap: normal;"><code style="background: transparent; border-radius: 3px; border: 0px; box-sizing: border-box; display: inline; font-family: Consolas,, Menlo, Courier, monospace; font-size: 13.6000003814697px; line-height: inherit; margin: 0px; max-width: initial; overflow: initial; padding: 0px; word-break: normal; word-wrap: normal;">
POST /patch/login.php HTTP/1.1
Host: 127.0.0.1
Content-Type: application/x-www-form-urlencoded
Content-Length: 27
username=test&password=test

</code></pre>

Response

<br>
<pre style="background-color: #f7f7f7; border-radius: 3px; box-sizing: border-box; color: #333333; font-family: Consolas,Menlo, Courier, monospace; font-size: 13.6000003814697px; font-stretch: normal; line-height: 1.45; margin-bottom: 16px; overflow: auto; padding: 16px; word-wrap: normal;"><code style="background: transparent; border-radius: 3px; border: 0px; box-sizing: border-box; display: inline; font-family: Consolas,, Menlo, Courier, monospace; font-size: 13.6000003814697px; line-height: inherit; margin: 0px; max-width: initial; overflow: initial; padding: 0px; word-break: normal; word-wrap: normal;">
HTTP/1.1 200 OK
Date: Fri, 24 Jul 2015 18:23:09 GMT
Server: Apache/2.4.12 (Win32) OpenSSL/1.0.1l PHP/5.5.24
X-Powered-By: PHP/5.5.24
Content-Length: 30
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html

Wrong in username or password

</code></pre>
	';
	$run='
	Now we need get login to Control panel of any Website, but this will be hard if we test one-by-one, so we do more fast just with request without forms.
	<h3>Mission</h3>

	* You have do a attack of force brute for get login.<br>

	<h1>Stage ----------------------------------------------------------------</h1><BR>

<!-- ////////////////////////////// ^^^^^^^^^^^^  ///////////////////////////////// -->
        	<h3>Admin Panel</h3>
        	<form name="formbase" method="POST" action="run.php">
        	Username: <input type="text" name="username">
            Password: <input type="text" name="password">
            <input type="submit" value="login">
<!-- ////////////////////////////////////////////////////////////////////////////// -->
 <h3>Source Code</h3>

<pre style="background-color: #f7f7f7; border-radius: 3px; box-sizing: border-box; color: #333333; font-family: Consolas,Menlo, Courier, monospace; font-size: 13.6000003814697px; font-stretch: normal; line-height: 1.45; margin-bottom: 16px; overflow: auto; padding: 16px; word-wrap: normal;"><code style="background: transparent; border-radius: 3px; border: 0px; box-sizing: border-box; display: inline; font-family: Consolas,, Menlo, Courier, monospace; font-size: 13.6000003814697px; line-height: inherit; margin: 0px; max-width: initial; overflow: initial; padding: 0px; word-break: normal; word-wrap: normal;">
&lt;form name="formbase" method="POST" action="run.php"&gt;
&lt;input type="text" name="username"&gt;
&lt;input type="password" name="password"&gt;
&lt;input type="submit" value="login"&gt;
&lt;/form&gt;

</code></pre>

	';
		break;
	case 'cpfinder':
	$title="(cpfinder) Control panel finder";
	$descriptions='find boards of directors or login is something most usual default directories used to find them.<br>
directories default
<pre style="background-color: #f7f7f7; border-radius: 3px; box-sizing: border-box; color: #333333; font-family: Consolas,Menlo, Courier, monospace; font-size: 13.6000003814697px; font-stretch: normal; line-height: 1.45; margin-bottom: 16px; overflow: auto; padding: 16px; word-wrap: normal;"><code style="background: transparent; border-radius: 3px; border: 0px; box-sizing: border-box; display: inline; font-family: Consolas,, Menlo, Courier, monospace; font-size: 13.6000003814697px; line-height: inherit; margin: 0px; max-width: initial; overflow: initial; padding: 0px; word-break: normal; word-wrap: normal;">
Admin
Administrator
cpanel 
panel
webadmin
phpmyadmin
...
</code></pre>
';
	$run="Now we need get Control panel of any Website, but this will be hard if we test one-by-one, so we do more fast just with a list of directories default.

	<h3>Mission</h3>

	* You have do a attack for find the control panel.<br>
	<h1>Stage ----------------------------------------------------------------</h1><BR>
	127.0.0.1
";
	break;
	default:
	header("location: index.html");
		break;
}
?>

<title>KTF Lab | <?php echo $title?></title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href="style.css" />
<link rel="shortcut icon" href="mask.png" />
<body><div id="page">
 <div id="bar">
            <ul>
                <b><i><li><?php echo $title?></li></i></b>
            </ul>
      </div>

<div class="contentTitle">
          <h1>Katana Lab</h1>
        </div>
        <div class="contentText">
          <p>
        <?php echo $descriptions?>
        </p></div>

<div class="contentTitle"><h1>Module</h1></div>
<div class="contentText">
<?php echo $run?><br><br><br>