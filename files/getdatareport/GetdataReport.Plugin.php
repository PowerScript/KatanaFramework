<?php
/*
   Author : [f][t][@inbox.ru] \ RedToor 
   Project: https://github.com/powerscript/GetDataReport
   Date   : 18/10/2016
   Version: 1.0.3
  
   GetDataReport PLUGIN version  
*/

error_reporting(0);       
error_log(0);            

$HTTP_S = (isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] == 'on') ? 'https://' : 'http://';
$path = dirname(__FILE__);
$position = basename($path);
$real_path =  $HTTP_S.$_SERVER['HTTP_HOST']."/".$position."/".basename(__FILE__); 
define("REAL", $real_path);

class GetDataPlugin{ 
    function os(){
        $system="unknow";                
        $os=array(
            '/Windows NT 10.0/i'    =>  'Windows 10'            , '/windows nt 6.4/i'     =>  'Windows 10'   , '/windows nt 6.3/i'     =>  'Windows 8.1',
            '/windows nt 6.2/i'     =>  'Windows 8'             , '/windows nt 6.1/i'     =>  'Windows 7'    , '/windows nt 6.0/i'     =>  'Windows Vista',
            '/windows nt 5.2/i'     =>  'Windows Server 2003/XP', '/windows nt 5.1/i'     =>  'Windows XP'   , '/windows me/i'         =>  'Windows ME',
            '/windows nt 5.0/i'     =>  'Windows 2000'          , '/win98/i'              =>  'Windows 98'   , '/win95/i'              =>  'Windows 95',
            '/windows nt 4.0/i'     =>  'Windows NT 4.0'        , '/windows nt 3.51/i'    =>  'Windows NT 3.51', '/windows nt 3.5/i'   =>  'Windows NT 3.5',
            '/windows nt 3.1/i'     =>  'Windows NT 3.1'        , '/windows nt 3.11/i'    =>  'Windows 3.11' ,  '/linux/i'             =>  'Linux',
            '/android/i'            =>  'Android'               , '/android 1.6/i'        =>  'Android 1.6'  , '/android 2.0/i'        =>  'Android 2.0',
            '/android 2.0.1/i'      =>  'Android 2.0.1'         , '/android 2.1/i'        =>  'Android 2.1' , '/android 2.2/i'         =>  'Android 2.2',
            '/android 2.2.1/i'      =>  'Android 2.2.1'         , '/android 2.2.2/i'      =>  'Android 2.2.2', '/android 2.2.3/i'      =>  'Android 2.2.3',
            '/android 2.2.4/i'      =>  'Android 2.2.4'         , '/android 2.3/i'        =>  'Android 2.3', '/android 2.3.0/i'        =>  'Android 2.0.3',
            '/android 2.3.1/i'      =>  'Android 2.3.1'         , '/android 2.3.3/i'      =>  'Android 2.3.3', '/android 2.3.4/i'      =>  'Android 2.3.4',
            '/android 2.3.5/i'      =>  'Android 2.3.5'         , '/android 2.3.6/i'      =>  'Android 2.3.6', '/android 2.3.7/i'      =>  'Android 2.3.7',
            '/android 3.0/i'        =>  'Android 3.0'           , '/android 3.1/i'        =>  'Android 3.1', '/android 3.2/i'          =>  'Android 3.1',
            '/android 3.2.1/i'      =>  'Android 3.2.1'         , '/android 3.2.2/i'      =>  'Android 3.2.2', '/android 3.2.3/i'      =>  'Android 3.2.3',
            '/android 3.2.4/i'      =>  'Android 3.2.4'         , '/android 4.0/i'        =>  'Android 4.0', '/android 4.0.0/i'        =>  'Android 4.0.0',
            '/android 4.0.1/i'      =>  'Android 4.0.1'         , '/android 4.0.2/i'      =>  'Android 4.0.2', '/android 4.0.3/i'      =>  'Android 4.0.3',
            '/android 4.0.4/i'      =>  'Android 4.0.4'         , '/android 4.2.1/i'      =>  'Android 4.2.1', '/android 4.2.2/i'      =>  'Android 4.2.2',
            '/android 4.3/i'        =>  'Android 4.3'           , '/android 4.4/i'        =>  'Android 4.4', '/android 4.4.1/i'        =>  'Android 4.4.1',
            '/android 4.4.2/i'      =>  'Android 4.4.2'         , '/android 4.4.3/i'      =>  'Android 4.4.3', '/android 4.4.4/i'      =>  'Android 4.4.4',
            '/android 5.0/i'        =>  'Android 5.0'           , '/macintosh|mac os x/i' =>  'Mac OS X', '/mac_powerpc/i'             =>  'Mac OS 9',
            '/ubuntu/i'             =>  'Ubuntu'                , '/SymbianOS/i'          =>  'SymbianOS', '/iphone/i'                 =>  'iPhone',
            '/ipod/i'               =>  'iPod'                  , '/ipad/i'               =>  'iPad', '/tablet os/i'                   =>  'Table OS',
            '/blackberry/i'         =>  'BlackBerry'            , '/bb/i'                 =>  'BlackBerry', '/webos/i'                 =>  'Mobile');
            foreach($os as $regex => $value){if(preg_match($regex, $_SERVER['HTTP_USER_AGENT'])){$system=$value;}}return $system;}

    function browser(){
        $navegator="unknow";
        $browser=array(
            '/msie/i'       =>  'Internet Explorer','/firefox/i'    =>  'Firefox'  , '/safari/i'     =>  'Safari',
            '/chrome/i'     =>  'Chrome'           ,'/opera/i'      =>  'Opera'    , '/netscape/i'   =>  'Netscape',
            '/maxthon/i'    =>  'Maxthon'          ,'/BrowserNG/i'  =>  'BrowserNG', '/konqueror/i'  =>  'Konqueror',
            '/ie/i'         =>  'Internet Explorer','/mobile/i'     =>  'Handheld Browser');            
            foreach($browser as $regex => $value){if(preg_match($regex, $_SERVER['HTTP_USER_AGENT'])){$navegator=$value;}}return $navegator;}

    function architecture(){
        $arqui="32Bits";
        $architecture=array(
            '/x86_64/i'     => '64Bits', '/amd64/i'     => '64Bits',
            '/x86-64/i'     => '64Bits', '/x64_64/i'    => '64Bits',
            '/x64/i'        => '64Bits', '/WOW64/i'     => '64Bits');
            foreach($architecture as $regex => $value){if(preg_match($regex, $_SERVER['HTTP_USER_AGENT'])){$arqui=$value;}}return $arqui;}

    function device($unix){
        $device="Computer";
        $unix=strtoupper($unix);
        if(strstr($unix,     'ANDROID')==true)    {$device="Phone";}
        elseif(strstr($unix, 'IPHONE')==true)     {$device="Phone";}
        elseif(strstr($unix, 'BLACKBERRY')==true) {$device="Phone";}
        elseif(strstr($unix, 'WEBOS')==true)      {$device="Phone";}
        elseif(strstr($unix, 'SYMBIAOS')==true)   {$device="Phone";}
        elseif(strstr($unix, 'TABLET')==true)     {$device="Tablet";}
        elseif(strstr($unix, 'IPAD')==true)       {$device="Tablet";}
        elseif(strstr($unix, 'IPOD')==true)       {$device="Portable media players ";}return $device;}

    function geo($what){
        $g=unserialize(file_get_contents('http://www.geoplugin.net/php.gp?ip='.$_SERVER['REMOTE_ADDR'].''));
        switch ($what) {
            case 'country':
                return $g['geoplugin_countryName'];
                break;
            case 'region':
                return $g['geoplugin_region'];
                break;
            case 'city':
                return $g['geoplugin_city'];
                break;
            case 'logitude':
                return $g['geoplugin_longitude'];
                break; 
            case 'latitude':
                return $g['geoplugin_latitude'];
                break; 
            case 'continent':
                return $g['geoplugin_continentCode'];
                break; 
            case 'currency':
                return $g['geoplugin_currencyCode'];
                break;    
        }
    }

    function java($get){
        $data='<script type="text/javascript">';
        switch ($get) {
            case 'height':
                $data.='document.write(window.screen.height);</script>';
                break;
            case 'width':
                $data.='document.write(window.screen.width);</script>';
                break;
            case 'javaenabled':
                $data.='if(navigator.javaEnabled()==true){document.write("true")}else{document.write("false")}</script>';
                break;
            case 'cookieenabled':
                $data.='if(navigator.cookieEnabled==true){document.write("true")}else{document.write("false")}</script>';
                break;
        }
        return $data;
    }

    function height(){return file_get_contents(REAL."?execute=height");}
    function width(){return file_get_contents(REAL."?execute=width");}
    function javaenabled(){return file_get_contents(REAL."?execute=javaenabled");}    
    function cookieenabled(){return file_get_contents(REAL."?execute=cookieenabled");}

    function ip(){
        if (isset($_SERVER['HTTP_X_FORWARDED_FOR'])) {
           $ipAddresses = explode(',', $_SERVER['HTTP_X_FORWARDED_FOR']);
           return trim(end($ipAddresses));
         }else {
            return $_SERVER['REMOTE_ADDR'];
         }
    }

    function language(){return $_SERVER['HTTP_ACCEPT_LANGUAGE'];}
    function provetor(){return gethostbyaddr($_SERVER['REMOTE_ADDR']);}
    function agent(){return $_SERVER['HTTP_USER_AGENT'];}
    function referer(){ return $_SERVER['HTTP_REFERER'];}
    function getdate(){return date("Y/m/d g:ia");}
}

if($_GET['execute']!=""){$getjava = new GetDataPlugin();print $getjava->java($_GET['execute']);}

?>
