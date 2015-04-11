<?php
  
  function db_connect(){
    static $connection;

    if(!isset($connection)){
      $connection = mysqli_connect('127.0.0.1', 'root', '', 'urf-data');
    }
    if($connection === false){
      $connection = null;
      return mysqli_connect_error();
    }
    return $connection;
  }

  function db_query($query){
    $connection = db_connect();

    $result = mysqli_query($connection, $query);

    return $result;
  }

  function db_close(){
    $connection = db_connect();

    if($connection === false){
      return -1;
    }

    mysqli_close($connection);
  }

?>