<?php
  include "util/LOLPlayerNode.php"

  
?>

<!DOCTYPE html>
<html>
  <head>
    <title>IDK</title>
    <script type="text/javascript" src="../libs/jquery.min.js"></script>
    <script type="text/javascript" src="../libs/bootstrap/dist/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="js/main.js"></script>
    <script type="text/javascript" src="js/MatchMash.js"></script>
    <script type="text/javascript" src="js/PlayerRender.js"></script>
    <link rel="stylesheet" type="text/css" href="css/style.css">
    <link rel="stylesheet" type="text/css" href="../libs/bootstrap/dist/css/bootstrap.min.css">
  </head>
  <body>
    <?php
      for ($i=11; $i <=20 ; $i++) { 
        $player = build_LOLPlayerNode($i, true);
        echo '<div>Gnet Score: '.$player->getGentScore().'</div>';
        echo $player->render();
      }

        // $player = build_LOLPlayerNode(1, true);
        // echo $player->render();

    ?>
  </body>
</html>