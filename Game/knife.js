class Knife {
 constructor(){
  this.r = 70;
  this.x = width;
  this.y = height - this.r;
 }
  
  show() {
   image(kImg, this.x, this.y, this.r, this.r); 
   fill(255,50);
   //ellipseMode(CORNER);
   //ellipse(this.x,this.y, this.r, this.r);
  }
  
  move(){
   this.x -= 5;
    
  }
  
  
  
}