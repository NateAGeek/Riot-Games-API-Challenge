<?php
  
  include_once "LOLUtil.php";
  include_once "LOLMatchNode.php";

  $json  = false;
  $query = "list_matches";
  $html  = false;

  if(isset($_GET["json"])){
    $json =  $_GET["json"];
  }
  if(isset($_GET["query"])){
    $query = $_GET["query"];
  }
  if(isset($_GET["html"])){
    $html = $_GET["html"];
  }

  if($query == 'list_matches'){
    if(isset($_GET["start"]) && isset($_GET["end"]) && is_int((int)$_GET["start"]) && is_int((int)$_GET["end"])){
      echo get_ListOfMatches((int)$_GET["start"], (int)$_GET["end"], $json);
    }
  }
  elseif ($query == 'get_match') {
    if(isset($_GET["match_id"]) && is_int((int)$_GET["match_id"])){
      $match = build_LOLMatchNode($_GET["match_id"], true);
      if($html){
        echo $match->render();
      }else{
        echo json_encode($match);
      }
    }
  }
  else{
    echo "";
  }

?>