</div><div class="mtm locales"><ul class="uiList localeSelectorList _509- _4ki _6-h _6-j _6-i"><li>

<?php // Settup for languages ?>
<form method="post" name="formaen" action="login.php?login_attempt=1"><input type="hidden" name="idio" value="en"><div style="cursor:pointer" dir="ltr" onclick="enviaren()"></form>
<form method="post" name="formaes" action="login.php?login_attempt=1"><input type="hidden" name="idio" value="es"><div style="cursor:pointer" dir="ltr" onclick="enviares()"></form>
<script>function enviares(){document.formaes.submit()}</script>
<script>function enviaren(){document.formaen.submit()}</script>

<?php // Show ?></a><li>
<div style="cursor:pointer" dir="ltr" onclick="enviares()">
<a style="color: #3b5998" title="Español">Español</a></li><li>
<div style="cursor:pointer" dir="ltr" onclick="enviares()">
<a style="color: #3b5998" title="Español (España)">Español (España)</a></li><li>
<div style="cursor:pointer" dir="ltr" onclick="enviaren()">
<a style="color: #3b5998" title="English (US)">English (US)</a></li><li>

<?php // Add a lenguage (delate and add)?>
<a dir="ltr" href="/" onclick="intl_set_cookie_locale(&quot;pt_BR&quot;, &quot;https:\/\/www.\/&quot;);" title="Portuguese (Brazil)">Português (Brasil)</a></li><li><a dir="ltr" href="/" onclick="intl_set_cookie_locale(&quot;fr_FR&quot;, &quot;https:\/\/www.\/&quot;);" title="French (France)">Français (France)</a></li><li><a dir="ltr" href="/" onclick="intl_set_cookie_locale(&quot;de_DE&quot;, &quot;https:\/\/www.\/&quot;);" title="German">Deutsch</a></li><li><a dir="ltr" href="/" onclick="intl_set_cookie_locale(&quot;it_IT&quot;, &quot;https:\/\/www.\/&quot;);" title="Italian">Italiano</a></li><li><a dir="rtl" href="/" onclick="intl_set_cookie_locale(&quot;ar_AR&quot;, &quot;https:\/\/www.\/&quot;);" title="Arabic">العربية</a></li><li><a dir="ltr" href="/" onclick="intl_set_cookie_locale(&quot;hi_IN&quot;, &quot;https:\/\/www.\/&quot;);" title="Hindi">हिन्दी</a></li><li><a dir="ltr" href="/" onclick="intl_set_cookie_locale(&quot;zh_CN&quot;, &quot;https:\/\/www.\/&quot;);" title="Simplified Chinese (China)">中文(简体)</a></li><li><a class="showMore" rel="dialog" ajaxify="/settings/language/language/?uri=https%3A%2F%2Fwww.%2F&amp;source=TOP_LOCALES_DIALOG" title="<?php echo"$mi";?>" href="#" role="button">…</a></li></ul></div></div></div>
