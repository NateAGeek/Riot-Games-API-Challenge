<?php
  
  require_once "dbHandler.php";
  include_once "../../libs/krumo/class.krumo.php";

  function get_BestGent($players = array()){
    if(empty($players)){
      return false;
    }

    $highest_gent_score_index = 0;

    foreach ($players as $key => $player) {
      if($players[$highest_gent_score_index]->getGentScore() > $player->getGentScore()){
        $highest_gent_score_index = $key;
      }
    }

    return $players[$highest_gent_score_index];
  }

  function get_TrollGent($players = array()){
    if(empty($players)){
      return false;
    }

    $highest_gent_score_index = 0;

    foreach ($players as $key => $player) {
      if($players[$highest_gent_score_index]->getGentScore() < $player->getGentScore()){
        $highest_gent_score_index = $key;
      }
    }
    
    return $players[$highest_gent_score_index];
  }

  function get_ListOfMatches($start = 0, $end = 10, $json = false, $format = true){
    $list_matches = array();
    $list_matches_results = db_query("SELECT `match`.id AS ID, `match`.queueType AS match_type, `match`.matchId AS match_id, `match`.region AS region, `match`.matchDuration AS duration, `match`.matchCreation AS creation FROM `match` LIMIT ".$start.", ".$end);

    while($row = mysqli_fetch_assoc($list_matches_results)){
      
      if($format){
        $row["duration"] = gmdate('i:s', $row["duration"]);
        $row["creation"] = gmdate('m/d/y H:i:s', $row["creation"]);
        if($row["region"] == 'NA'){
          $row["region"] = 'North America';
        }
        if($row["match_type"] == "URF_5x5"){
          $row["match_type"] = "UltraRapidFire Mode 5x5";
        }
      }

      $list_matches[] = $row;

    }

    if($json){
      return json_encode($list_matches);
    }

    return $list_matches;
  }

?>