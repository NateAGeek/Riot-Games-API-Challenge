<?php
  include "util/LOLMatchNode.php";
?>

<!DOCTYPE html>
<html>
  <head>
    <title></title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
  </head>
  <body>
    <?php
      $match = build_LOLMatchNode(1778704162, true);
      echo $match->render();
    ?>
  </body>
</html>