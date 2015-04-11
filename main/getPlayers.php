<?php
  
  include "util/dbHandler.php";
  include "../libs/krumo/class.krumo.php";

  $match_id = ($_GET['match_id'] == null ? -1 : $_GET['match_id']);

  $result = db_query("SELECT * FROM `match` LEFT JOIN `participant` AS `part` ON `part`.match_id = `match`.matchId WHERE `match`.matchId = ".$match_id."");

  $rows = array();
  while($row = mysqli_fetch_assoc($result)){
    $rows[] = $row;
  }

  echo json_encode($rows); 

?>