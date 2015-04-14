<?php
  $arrContextOptions = array(
    "ssl" => array(
        "verify_peer" => false,
        "verify_peer_name" => false,
    ),
  );
  $api_key = "096de5b6-d371-41c2-a263-4db83088a4eb";
  $static_champ_img_url = "https://ddragon.leagueoflegends.com/cdn/5.7.2/img/champion/";
  $static_iteam_img_url = "https://ddragon.leagueoflegends.com/cdn/5.7.2/img/item/";
  $static_spell_img_url = "https://ddragon.leagueoflegends.com/cdn/5.7.2/img/spell/";
  $static_champ_data = json_decode(file_get_contents("https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/?champData=all&api_key=".$api_key."", false, stream_context_create($arrContextOptions)));
  $static_spell_data = json_decode(file_get_contents("https://global.api.pvp.net/api/lol/static-data/na/v1.2/summoner-spell?dataById=true&spellData=all&api_key=".$api_key."", false, stream_context_create($arrContextOptions)))

?>