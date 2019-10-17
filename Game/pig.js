class Pig {
  constructor(){
  this.r = 80;
  this.x = this.r;
  this.y = height - this.r;
    this.vy = 0;
    this.gravity = 2;
    
    
  }
  
  jump(){
    
   if (this.y == height-this.r){ 
   this.vy = -30;
   }
    
  }
  
  hits(knife) {
    
   let x1 = this.x + this.r * 0.5;
   let y1 = this.y + this.r * 0.5; 
   let x2 = knife.x + knife.r * 0.5;
   let y2 = knife.y + knife.r * 0.5; 
    
    
   return collideCircleCircle(x1, y1, this.r, x2, y2, knife.r); 
  }
  
  move(){
    this.y += this.vy;
    this.vy += this.gravity;
    this.y = constrain (this.y,0,height-this.r)
  }
  
  show(){
    image(pImg,this.x, this.y, this.r, this.r);
    fill(255,50);
    //ellipseMode(CORNER);
    //ellipse(this.x,this.y, this.r,this.r);
    
  }

}