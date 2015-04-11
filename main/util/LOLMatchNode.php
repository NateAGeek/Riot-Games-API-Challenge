<?php

  include "LOLPlayerNode.php";

  function build_LOLMatchNode($match_id, $get_timelinedata = false){
    $result = db_query("SELECT *, `participant`.id AS pid FROM `match` LEFT JOIN `participant` ON `match`.matchId = `participant`.match_id WHERE `match`.matchId = '".$match_id."' AND `participant`.id < '74421'");

    $players = array();
    while($row = mysqli_fetch_assoc($result)){
      $players[] = build_LOLPlayerNode($row['pid'], $get_timelinedata);
    }

    $match = new LOLMatchNode(array(), $players, $get_timelinedata);

    return $match;

  }

  /**
  * 
  */
  class LOLMatchNode
  {
    private $match_data = array();
    private $players_data = array();
    private $get_timelinedata = false;


    function __construct($match_data, $players_data, $get_timelinedata = false) {
      $this->$match_data = $match_data;
      $this->players_data = $players_data;
      $this->get_timelinedata = $get_timelinedata;
    }

    public function render(){
      $rendered_html = ''.
        '<div class="match-node">';

        if($this->get_timelinedata){
          $rendered_html .= '<div class="timeline-map">';
          foreach ($this->players_data as $player_index => $player) {
            $rendered_html .= $player->renderMapSpots();
          }
          $rendered_html .= '<img class="srift-map" src="http://ddragon.leagueoflegends.com/cdn/5.2.1/img/map/map11.png"/>';
          $rendered_html .= '</div>';
        }

        $rendered_html .= ''.
        '</div>';

        return $rendered_html;
    }
  }


?>