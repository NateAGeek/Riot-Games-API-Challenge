//In case I have time to do something cool with Three.js
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