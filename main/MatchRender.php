<?php
  include_once "util/LOLMatchNode.php";
?>

<!DOCTYPE html>
<html>
  <head>
    <title></title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
    <script type="text/javascript" src="../libs/jquery.min.js"></script>
    <script type="text/javascript" src="js/PlayerRender.js"></script>
  </head>
  <body>
    <?php
      $match = build_LOLMatchNode(1778704162, true);
      echo $match->render();
      echo $match->getBestGent()->render();
      echo $match->getTrollGent()->render();
    ?>
  </body>
</html>