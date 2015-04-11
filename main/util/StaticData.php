<?php
  $arrContextOptions = array(
    "ssl" => array(
        "verify_peer" => false,
        "verify_peer_name" => false,
    ),
  );
  $api_key = "096de5b6-d371-41c2-a263-4db83088a4eb";
  $static_champ_img_url = "http://ddragon.leagueoflegends.com/cdn/5.2.1/img/champion/";
  $static_iteam_img_url = "http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/";
  $static_champ_data = json_decode(file_get_contents("https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/?champData=all&api_key=".$api_key."", false, stream_context_create($arrContextOptions)));

?>