<?php

?>

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>URF Match Mash</title>

    <link rel="stylesheet" type="text/css" href="main/css/style.css">
    <link rel="stylesheet" type="text/css" href="libs/bootstrap/dist/css/bootstrap.min.css">
    <script type="text/javascript" src="libs/jquery.min.js"></script>
    <script type="text/javascript" src="libs/three.min.js"></script>
    <script type="text/javascript" src="libs/bootstrap/dist/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="main/js/main.js"></script>
    <script type="text/javascript" src="main/js/MatchMash.js"></script>
    <script type="text/javascript" src="main/js/PlayerRender.js"></script>
  </head>
  <body>
    <nav role="navigation" class="navbar navbar-default navbar-fixed-top">
      <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
            <button type="button" data-target="#navbarCollapse" data-toggle="collapse" class="navbar-toggle">
              <span class="sr-only">Toggle navigation</span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
            <a href="#" class="navbar-brand">Brand</a>
        </div>
        <!-- Collection of nav links and other content for toggling -->
        <div id="navbarCollapse" class="collapse navbar-collapse">
            <ul class="nav navbar-nav">
              <li class="active"><a href="#">Match Mash</a></li>
              <li><a href="#">Stats</a></li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
              <li><a href="https://github.com/NateAGeek/Riot-Games-API-Challenge">Created by: NateAGeek, LTrain</a></li>
            </ul>
          </div>
      </div>
    </nav>

    <section class="content container">
      <div class="row">
        <div class="col-sm-12" id="list_of_matchs">
          <table class="table table-hover" id="match_table">
            <thead>
              <tr>
                <th>
                  Match Type
                </th>
                <th>
                  Match ID
                </th>
                <th>
                  Region
                </th>
                <th>
                  Duration
                </th>
                <th>
                  Creation
                </th>
              </tr>
            </thead>
            <tbody id="match-items">
              
            </tbody>
          </table>
          <nav id="match_list_select">
            <ul>
              <?php
                for($i = 1; $i < 6; $i++){
                  if($i == 1){
                    echo '<li><a class="active">'.$i.'</a></li>';
                  }else{
                    echo '<li><a>'.$i.'</a></li>';
                  }
                }
              ?>
              <li><a>></a></li>
            </ul>
          </nav>
        </div>
      </div>
    </section>

  </body>
</html>