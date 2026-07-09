let petp;
let mousep;
let petdir;
let petspeed = 1;
let petv;
let petframe = 0;
let counter = 0;
let blinkcounter = 0;
let blink = false;
let petflip = false;
let petpet = false;

let canvas;

let petsprite;

let petspritef;

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}


async function setup() {

  petsprite = await loadImage('pet/lilcatflip.png');
  petspritef = await loadImage('pet/lilcat.png');

  canvas = createCanvas(400, 400);
   petp = createVector(25, 25);
   mousep = createVector(0,0);
  petv = createVector(0,0);


  // setTimeout(windowResized, 1000);
  createCanvas(displayWidth, displayHeight);
  resizeCanvas(windowWidth, windowHeight);


}

function draw() {
  mousep = createVector(mouseX, mouseY );
  clear();
  pet_update();
  pet_draw();
}

function pet_draw(x, y){

  let mousedist = p5.Vector.dist(mousep, petp);

  imageMode(CENTER);

  counter += 0.1;
  petflip = petv.x > 0 ? true: false;

  cursor('pointer');
  canvas.style('pointer-events:none');

  if (petv.mag() > 0.5){
    petframe = (floor(counter) % 4) + 4;
  }
  else{
      if (mousedist < 20) {
        petframe = (floor(counter) % 2) + 8;
        canvas.style('pointer-events:auto');
        cursor('grab');
      }

      else{
        if (random(3) == 1) {
          petframe = 1;
        }
        else{
          petframe = 2;
        }

    }
  }

  if (petflip){
    image(petsprite, petp.x, petp.y, 32, 32, 0, petframe * 32, 32, 32);
  }
  else {
    image(petspritef, petp.x, petp.y, 32, 32, 0, petframe * 32, 32, 32);
  }
  
}

function pet_update(){

  let mousedist = p5.Vector.dist(mousep, petp);
  let petdir = createVector(0,0);
  let targetdir = createVector(0,0);
  
  if (mousedist > 150) {
    targetdir = (mousep.sub(petp)).normalize();
  }


  petdir = petdir.lerp(targetdir, 0.1).normalize();
  petv = petv.add(petdir.mult(petspeed));

  if (!targetdir.length) {
    petv = petv.mult(0.9);
  }
  
  petp = petp.add(petv);
  
}
