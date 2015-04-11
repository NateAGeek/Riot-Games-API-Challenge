// var scene;
// var camera;
// var canvasElement;
// var renderer;
// var clock;

// function init(){
//   //Init the global vars
//   scene         = new THREE.Scene();
//   camera        = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
//   canvasElement = document.getElementById("main_canvas");
//   renderer      = new THREE.WebGLRenderer({canvas: canvasElement});
//   clock         = new THREE.Clock();

//   //Init the canvas and the renderer
//   canvasElement.setAttribute("width", window.innerWidth);
//   canvasElement.setAttribute("height", window.innerHeight);
//   renderer.setSize(window.innerWidth, window.innerHeight);

//   //Setting the scene's props
//   camera.position.z = 5;

// }

// function renderCanvas(){
//   requestAnimationFrame(renderCanvas);


//   //Let Three.js render the objects in the scene
//   renderer.render(scene, camera);
// }

// document.addEventListener("DOMContentLoaded", function(event) { 
//   init();
//   renderCanvas();
// });

var ChampStaticURL = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/";
var StaticChampImage = "http://ddragon.leagueoflegends.com/cdn/img/champion/loading/";
var api_key = "096de5b6-d371-41c2-a263-4db83088a4eb";
var ChampData;

jQuery(document).ready(function($) {
  
  $.getJSON('getPlayers.php', {match_id: '1778704162'}, function(json, textStatus) {
      var players;
      $.each(json, function(index, val) {
         $.getJSON(ChampStaticURL+val['championId'], {api_key : api_key, champData:'image'}, function(champ, textStatus){
          $("#game-data").append('<img src="'+StaticChampImage+champ["key"]+'_0.jpg"/>')
          console.log(champ);
         })




      });
  });

});