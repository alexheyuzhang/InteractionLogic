let pig;
let pImg;
let kImg;
let bImg;
let knifes = [];
//let soundClassifier;

function preload(){
  /*const options = { probabilityThreshold:0.95};
  soundClassifier = ml5,soundClassifier('SpeechCommands18w',options);*/
  pImg = loadImage('pig.png');
  kImg = loadImage('knife.png');
  bImg = loadImage('background.png');
}
function setup() {
  createCanvas(600, 400);
  pig = new Pig();
  //soundClassifier.classify(gotCommand);
}

/*function gotCommand(error,results){
 if(error) {
   console.error(error);
 }
  console.log(results[0].label, results[0].confidence);
  if (results[0].label =='up'){
    pig.jump();
  }
}*/

function keyPressed() {
  if(key == ' '){
   pig.jump();
  }
}

function draw() {
  
  if (random(1)<0.007){
   knifes.push(new Knife()); 
  }
  //collideRectRect(200,200,100,150,mouseX,mouseY,50,75);
  background(bImg);
  
  for (let k of knifes) {
    k.move();
    k.show();
    if (pig.hits(k)){
      console.log('game over');
      noLoop();
    }
  }
     
  
  pig.show();
  pig.move();
  
  
  
}