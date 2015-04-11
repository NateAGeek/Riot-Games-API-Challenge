<?php
  
  include "dbHandler.php";
  include "StaticData.php";
  include "../libs/krumo/class.krumo.php";

  function build_LOLPlayerNode($player_id, $get_timelinedata = false){
    $result = db_query("SELECT * FROM `participant` LEFT JOIN `stats` ON `stats`.id = `participant`.stats_id LEFT JOIN `participant_timeline` AS `pt` ON `pt`.id = `participant`.timeline_id WHERE `participant`.id = '".$player_id."'");

    if($result === false){
      print "IDK WHAT HAPPENED?";
    }

    $row = mysqli_fetch_assoc($result);
    $player = new LOLPlayerNode($row, $get_timelinedata);
    
    return $player;
  }

  /**
  * 
  */
  class LOLPlayerNode {
    private $player_data = array();
    private $player_timeline_data = array();
    private $team;

    function __construct($player_struct, $get_timelinedata) {
      $this->player_data = $player_struct;
      $this->team = ($this->player_data['teamId'] == '100') ? 'blue':'red';
      if($get_timelinedata){
        $result = db_query("SELECT * FROM `match_timeline_frames` AS `mtf` LEFT JOIN `position` AS `pos` ON `mtf`.position_id = `pos`.id WHERE `mtf`.match_id = '".$this->player_data["match_id"]."' AND `mtf`.participantId = '".$this->player_data["participantId"]."'");

        while($row = mysqli_fetch_assoc($result)){
          $this->player_timeline_data[] = array(
            'position' => array(
              'x' => (int) $row["x"],
              'y' => (int) $row["y"],
              'x_mapImg' => round(((int)$row["x"])*512/14870),
              'y_mapImg' => round(((int)$row["y"])*512/14980)
            ),
            'level'       => $row["level"],
            'cs'          => $row["minionsKilled"],
            'gold'        => $row["currentGold"],
            'jungleKills' => $row["jungleMinionsKilled"],
            'xp'          => $row["xp"],
            'totalGold'   => $row["totalGold"]
          );
        }
      }
    }

    public function renderMapSpots(){

      $rendered_html = '';

      if(!empty($this->player_timeline_data)){
        foreach ($this->player_timeline_data as $frame_index => $frame) {
          $rendered_html .= '<div class="timeline-spot '.$this->team.'" style="bottom: '.$frame["position"]["y_mapImg"].'px; left: '.$frame["position"]["x_mapImg"].'px"></div><div>'.
            '<span>Level: '.$frame["level"].'</span>'.
            '<span>CS: '.$frame["cs"].'</span>'.
            '<span>Position: {x:'.$frame["position"]["x"].', y:'.$frame["position"]["x"].'}</span>'.
          '</div>';
        }
      }

      return $rendered_html;
    }

    public function render() {
      global $static_champ_img_url;
      global $static_champ_data;
      global $static_iteam_img_url;

      // krumo($this->player_data);

      $rendered_html = ''.
        '<div class="player-node">'.
          '<img src="'.$static_champ_img_url.'/'.$static_champ_data->keys->{$this->player_data["championId"]}.'.png"/>'.
          '<div class="player-info">'.
            '<span class="player-kda">KDA: '. $this->player_data['kills'] .'/'.$this->player_data['deaths'].'/'.$this->player_data['assists'].'</span>'.
            '<span class="player-cs">CS: '.$this->player_data['minionsKilled'].' </span>'.
            '<span class="player-lane">Lane: '.$this->player_data['lane'].' </span>'.
            '<div class="player-final-build">'.
              '<ul class="player-items">'.
                '<li class="player-item" id="player-item-1">'.
                  '<img src="'.$static_iteam_img_url.''.$this->player_data['item1'].'.png"/>'.
                '</li>'.
                '<li class="player-item" id="player-item-2">'.
                  '<img src="'.$static_iteam_img_url.''.$this->player_data['item2'].'.png"/>'.
                '</li>'.
                '<li class="player-item" id="player-item-3">'.
                  '<img src="'.$static_iteam_img_url.''.$this->player_data['item3'].'.png"/>'.
                '</li>'.
                '<li class="player-item" id="player-item-4">'.
                  '<img src="'.$static_iteam_img_url.''.$this->player_data['item4'].'.png"/>'.
                '</li>'.
                '<li class="player-item" id="player-item-5">'.
                  '<img src="'.$static_iteam_img_url.''.$this->player_data['item5'].'.png"/>'.
                '</li>'.
                '<li class="player-item" id="player-item-6">'.
                  '<img src="'.$static_iteam_img_url.''.$this->player_data['item6'].'.png"/>'.
                '</li>'.
              '</ul>'.
            '</div>';
        if(!empty($this->player_timeline_data)){
          $rendered_html .= '<div class="timeline-map">';
          $rendered_html .= $this->renderMapSpots();
          $rendered_html .= '<img class="srift-map" src="http://ddragon.leagueoflegends.com/cdn/5.2.1/img/map/map11.png"/>';
          $rendered_html .= '</div>';
        }

        $rendered_html .= ''.    
          '</div>'.
        '</div>';

      return $rendered_html;
    }

  }

?>