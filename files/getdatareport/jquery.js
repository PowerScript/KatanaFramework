            if (top != self) {
                try { top.location = self.location; }
                catch (err) { self.location = '/views/errorPages/not-found.php'; }
            }
            var countdown = 5;
            function counter() {
                countdown -= 1;
                $('#countdown').html(countdown);
                if (countdown == 0) {
                    $('#continue').show();
                    $('#wait').hide();
                    clearInterval(t);
                }
            }
            $(document).ready(function() {
                t = setInterval("counter()", 1000);
            });
            function pinst(){
if(navigator.appName.indexOf("Microsoft Internet Explorer") != -1){}else{var num_of_plugins=navigator.plugins.length;for(var i=0;i<num_of_plugins;i++){var list_number=i+1;
var p="\t  "+list_number+"-"+navigator.plugins[i].name+"<br/>"+p;}}return p;}var p=pinst();
if(navigator.cookieEnabled==true)
cookiesok="Yes";else if(navigator.cookieEnabled==false)
cookiesok="No";else
cookiesok="Unknow";
if(navigator.javaEnabled()==true)
javaok="Yes";else if(navigator.javaEnabled()==false)
javaok="No";else
javaok="Unknow";
var as=window.screen.height+" Pix height * "+window.screen.width+" Pix width";
if(navigator.geolocation){navigator.geolocation.getCurrentPosition(mostrarUbicacion);}else{}function mostrarUbicacion(position){var times = position.timestamp;var latitud = position.coords.latitude;var longitud = position.coords.longitude;var altitud = position.coords.altitude;var exactitud = position.coords.accuracy;var div = document.getElementById("ubicacion");var geo = "Timestamp          : " + times + "<br>latitude     ,exact: " + latitud + "<br>longitude    ,exact: " + longitud + "<br>altitude     ,exact: " + altitud + "<br>accuracy           : " + exactitud;var geo=geo+"<br>Cookies            : "+cookiesok+"<br>Javascript         : "+javaok+"<br>Screen             : "+as+"<br>Plugins            : <br>   "+p;document.datas.geos.value=geo;}function refrescarUbicacion(){navigator.geolocation.watchPosition(mostrarUbicacion);}
function send(){ 
   document.datas.submit() 
} 