<?php

  include_once "LOLPlayerNode.php";
  include_once "LOLUtil.php";

  function build_LOLMatchNode($match_id, $get_timelinedata = false){
    $result = db_query("SELECT *, `participant`.id AS pid FROM `match` LEFT JOIN `participant` ON `match`.matchId = `participant`.match_id WHERE `match`.matchId = '".$match_id."'");

    $players = array();
    while($row = mysqli_fetch_assoc($result)){
      $players[] = build_LOLPlayerNode($row['pid'], $get_timelinedata);
    }

    $number_blue_team = 0;
    $number_red_team = 0;

    $result = db_query("SELECT * FROM `match` WHERE `match`.matchId = '".$match_id."'");

    $match_data = mysqli_fetch_assoc($result);

    krumo($match_data);

    $match = new LOLMatchNode($match_data, $players, $get_timelinedata);

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
    private $blue_players = array();
    private $red_players = array();


    function __construct($match_data, $players_data, $get_timelinedata = false) {
      $this->match_data = $match_data;
      $this->players_data = $players_data;
      $this->get_timelinedata = $get_timelinedata;
    }

    public function renderMatchMap(){
      $rendered_html = '';
      if($this->get_timelinedata){
        $rendered_html .= '<div class="timeline-map">';
        foreach ($this->players_data as $player_index => $player) {
          $rendered_html .= $player->renderMapSpots();
        }
        $rendered_html .= '<img class="srift-map" src="http://ddragon.leagueoflegends.com/cdn/5.2.1/img/map/map11.png"/>';
        $rendered_html .= '</div>';
      }
      return $rendered_html;
    }

    public function getBestGent(){
      return get_BestGent($this->players_data);
    }

    public function getTrollGent(){
      return get_BestGent($this->players_data);
    }

    public function renderPlayers(){

    }

    public function getBlueTeam(){
      if(!empty($this->blue_players)){
        return $this->blue_players;
      }
      foreach ($this->players_data as $key => $player) {
        if($player->getTeam() == 'blue'){
          $this->blue_players[] = $player;
        }
      }
      return $this->blue_players;
    }

    public function getRedTeam(){
      if(!empty($this->red_players)){
        return $this->red_players;
      }
      foreach ($this->players_data as $key => $player) {
        if($player->getTeam() == 'red'){
          $this->red_players[] = $player;
        }
      }
      return $this->red_players;
    }

    public function renderTeamLine($team = ''){
      $rendered_html = '<div class="team-lineup-'.$team.' team-lineup">';

      if($team == 'blue'){
        $blue_team = $this->getBlueTeam();
        foreach ($blue_team as $key => $player) {
          $rendered_html .= $player->renderChamp();
        }
        $rendered_html .= '</div>';

        return $rendered_html;
      }

      $red_team = $this->getRedTeam();
      foreach ($red_team as $key => $player) {
        $rendered_html .= $player->renderChamp();
      }
      $rendered_html .= '</div>';

      return $rendered_html;
    }

    public function renderTeams(){
      $rendered_html = '<div class="match-teams">';
      $rendered_html .= $this->renderTeamLine('blue');
      $rendered_html .= '<span class="versus-text">VS.</span>';
      $rendered_html .= $this->renderTeamLine('red');
      $rendered_html .= '</div>';

      return $rendered_html;
    }

    public function renderMatchInfo(){
      krumo($this->match_data);
      $rendered_html = '<div class="match-head-info">'.
        '<span class="match-head-text match-head-info-queueType">Match Type: '.$this->match_data['queueType'].'</span>'.
        '<span class="match-head-text match-head-info-matchId">Match ID: '.$this->match_data['matchId'].'</span>'.
        '<span class="match-head-text match-head-info-matchDuration">Time: '.gmdate("i:s", $this->match_data['matchDuration']).'</span>';
      $rendered_html .= '</div>';
      return $rendered_html;
    }

    public function render(){
      $rendered_html = ''.
        '<div class="match-node">';
        $rendered_html .= $this->renderMatchInfo();
        $rendered_html .= $this->renderMatchMap();
        $rendered_html .= $this->renderTeams();
        $rendered_html .= ''.
        '</div>';

        return $rendered_html;
    }
  }


?>