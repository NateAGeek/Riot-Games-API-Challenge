<?php
  include "util/LOLPlayerNode.php"

  
?>

<!DOCTYPE html>
<html>
  <head>
    <title>IDK</title>
    <script type="text/javascript" src="../libs/jquery.min.js"></script>
    <script type="text/javascript" src="js/PlayerRender.js"></script>
    <link rel="stylesheet" type="text/css" href="css/style.css">
  </head>
  <body>
    <?php
      for ($i=1; $i <=10 ; $i++) { 
        $player = build_LOLPlayerNode($i, true);
        echo $player->render();
      }

        // $player = build_LOLPlayerNode(1, true);
        // echo $player->render();

    ?>
  </body>
</html>