<?php
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

?>