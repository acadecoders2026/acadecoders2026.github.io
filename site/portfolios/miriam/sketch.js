//behavior
//walk towards mouse until its within a certain distance
//change sprites to animate walk
//change sprites when hovered by mouse (pet)

//pet position
let pos;
//pet speed
let speed = 9;


let petleft;
let petright;

let frame = 5;
let counter = 0;
let sprite;


async function setup() {
  createCanvas(windowWidth, windowHeight);

 //spawn pet at corrdi
  pos = createVector(30,50);

  petleft = await loadImage('Mew left.png');
  petright = await loadImage('Mew right.png');
  sprite = petright;

}

function draw() {
  clear();

  imageMode(CENTER);
  counter = counter + 0.1;


  let distance = pos.dist(createVector(mouseX, mouseY));
  let target_dir = createVector(0,0);

  frame = floor(counter) % 2;

  if (distance > 80) {
  target_dir = ( createVector(mouseX, mouseY).sub(pos).normalize());

    if (mouseX > pos.x) {//point right
        sprite = petright;
    }
    else {//point right
      sprite = petleft

    }


    frame = floor(counter) % 4 +5;

  }

  if(distance < 33) {
    frame = floor(counter) % 2 +8;
  }

  pos = pos.add(target_dir.mult(speed));

  pos.x = constrain(pos.x, 0, windowWidth-48);
  pos.y = constrain(pos.y, 0, windowHeight-48);


  image(sprite, pos.x, pos.y, 48*2, 48*2, 0, frame*48, 48,48);
}
