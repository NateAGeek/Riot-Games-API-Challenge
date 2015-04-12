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
    private $winner;

    function __construct($player_struct, $get_timelinedata) {
      $this->player_data = $player_struct;
      $this->team = ($this->player_data['teamId'] == '100') ? 'blue' : 'red';
      $this->winner = ($this->player_data['winner'] == '1') ? true : false;
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
          $rendered_html .= ''.
          '<div class="timeline-spot '.$this->team.'" style="bottom: '.$frame["position"]["y_mapImg"].'px; left: '.$frame["position"]["x_mapImg"].'px" player-delta-data="'.$this->player_data['participantId'].'">'.
            '<div class="timeframe-stat-node">'.
              '<span class="timeframe-stat-level timeframe-stat">Level: '.$frame["level"].'</span>'.
              '<span class="timeframe-stat-cs timeframe-stat">Minions Killed: '.$frame["cs"].'</span>'.
              '<span class="timeframe-stat-pos timeframe-stat">Position: {x:'.$frame["position"]["x"].', y:'.$frame["position"]["x"].'}</span>'.
              '<span class="timeframe-stat-gold timeframe-stat">Gold: '.$frame['gold'].'</span>'.
              '<span class="timeframe-stat-jgkills timeframe-stat">Jungle Minions Killed: '.$frame['jungleKills'].'</span>'.
            '</div>'.
          '</div>';
        }
      }

      return $rendered_html;
    }

    public function renderFinalBuild(){
      global $static_iteam_img_url;
      $rendered_html = '<div class="player-final-build">'.
              '<ul class="player-items">';
      for ($i = 1; $i <= 6; $i++) { 
        $rendered_html .= ''.
        '<li class="player-item" id="player-item-'.$i.'">';
          if($this->player_data['item'.$i] == '0'){
            $rendered_html .= '<div class="no-item"></div>';
          }else{
            $rendered_html .= '<img src="'.$static_iteam_img_url.''.$this->player_data['item'.$i].'.png"/>';
          }
        $rendered_html .= '</li>';
      }

      $rendered_html .= '</ul>'.
            '</div>';
      return $rendered_html;
    }

    public function renderMap(){
      $rendered_html = '';
      if(!empty($this->player_timeline_data)){
        $rendered_html .= '<div class="timeline-map">';
        $rendered_html .= $this->renderMapSpots();
        $rendered_html .= '<img class="srift-map" src="http://ddragon.leagueoflegends.com/cdn/5.2.1/img/map/map11.png"/>';
        $rendered_html .= '</div>';
      }

      return $rendered_html;
    }

    public function renderStats(){
      global $static_champ_data;
      $rendered_html = '<div class="player-stats">'.
        '<span class="player-id player-stat">Player '.$this->player_data['participantId'].'</span>'.
        '<span class="">Champion: '.$static_champ_data->keys->{$this->player_data["championId"]}.'</span>'.
        '<span class="player-kda player-stat">KDA: '. $this->player_data['kills'] .'/'.$this->player_data['deaths'].'/'.$this->player_data['assists'].'</span>'.
        '<span class="player-cs player-stat">CS: '.$this->player_data['minionsKilled'].' </span>'.
        '<span class="player-lane player-stat">Lane: '.$this->player_data['lane'].' </span>'.
        '<span class="player-visionwardsbought player-stat">Vision Wards Bought: '.$this->player_data['visionWardsBoughtInGame'].'</span>'.
        '<span class="player-sightwardsbought player-stat">Sight Wards Bought: '.$this->player_data['sightWardsBoughtInGame'].'</span>'.
        '<span class="player-wardsplaced player-stat">Wards Placed: '.$this->player_data['wardsPlaced'].'</span>'.
        '<span class="player-wardskilled player-stat">Wards Destroyed: '.$this->player_data['wardsKilled'].'</span>'.
        '<span class="player-goldearned player-stat">Gold Earned: '.$this->player_data['goldEarned'].'</span>'.
        '<span class="player-goldspent player-stat">Gold Spent: '.$this->player_data['goldSpent'].'</span>'.
      '</div>';

      return $rendered_html;
    }

    public function renderChamp(){
      global $static_champ_img_url;
      global $static_champ_data;
      return '<img class="champ-img" src="'.$static_champ_img_url.'/'.$static_champ_data->keys->{$this->player_data["championId"]}.'.png"/>';
    }

    public function renderSpells(){
      global $static_spell_data;
      global $static_spell_img_url;

      return ''.
        '<img id="spell-1" class="spells" src="'.$static_spell_img_url.''.$static_spell_data->data->{$this->player_data["spell1Id"]}->image->full.'"/>'.
        '<img id="spell-2" class="spells" src="'.$static_spell_img_url.''.$static_spell_data->data->{$this->player_data["spell2Id"]}->image->full.'"/>';
    }

    public function render() {
      $rendered_html = ''.
        '<div class="player-node">';
          $rendered_html .= $this->renderMap();
          $rendered_html .= '<div class="top-info">'.
            '<span class="player-id">Player '.$this->player_data['participantId'].'</span>'.
            '<span class="player-match-status-'.(($this->winner) ? 'victory':'defeat').'">'.(($this->winner) ? 'Victory':'Defeat').'</span>'.
          '</div>';
          $rendered_html .= $this->renderChamp();
          $rendered_html .= '<div class="summoner-spells">'.
            '<span class="summoner-spell-text">Spells: </span>';
            $rendered_html .= $this->renderSpells();
          $rendered_html .= '</div>';
          $rendered_html .= '<div class="full-build">'.
            '<span class="item-text">Full Build: </span>';
            $rendered_html .= $this->renderFinalBuild();
          $rendered_html .= '</div>';
          $rendered_html .= $this->renderStats();
      $rendered_html .= ''.
        '</div>';

      return $rendered_html;
    }

  }

?>