<?php

/* https://github.com/PowerScript/GetDataReport */

include(__DIR__."/GetdataReport.Plugin.php");
$data = new GetDataPlugin();

$dataBeed ="\n\t|IP               ".$data->ip();
$dataBeed.="\n\t|Operative System ".$data->os();
$dataBeed.="\n\t|Browser          ".$data->browser();
$dataBeed.="\n\t|Screen height    ".$data->height();
$dataBeed.="\n\t|Screen width     ".$data->width();
$dataBeed.="\n\t|Java enabled     ".$data->javaenabled();
$dataBeed.="\n\t|Cookie enabled   ".$data->cookieenabled();
$dataBeed.="\n\t|Language         ".$data->language();
$dataBeed.="\n\t|Architecture     ".$data->architecture();
$dataBeed.="\n\t|Device           ".$data->device();
$dataBeed.="\n\t|Country          ".$data->geo('country');
$dataBeed.="\n\t|Region           ".$data->geo('region');
$dataBeed.="\n\t|Continent        ".$data->geo('continent');
$dataBeed.="\n\t|City             ".$data->geo('city');
$dataBeed.="\n\t|Logitude         ".$data->geo('logitude');
$dataBeed.="\n\t|Latitude         ".$data->geo('latitude');
$dataBeed.="\n\t|Currency         ".$data->geo('currency');
$dataBeed.="\n\t|Provetor         ".$data->provetor();
$dataBeed.="\n\t|Agent            ".$data->agent();
$dataBeed.="\n\t|Referer          ".$data->referer();
$dataBeed.="\n\t|Date             ".$data->getdate();

$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
$result = socket_connect($socket, "localhost", 6464);
socket_write($socket, $dataBeed, strlen($dataBeed));
socket_close($socket);
header("location: ".$url);

 ?>
