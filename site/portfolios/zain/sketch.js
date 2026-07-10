let pos;
let speed = 10;

let frame = 5;
let counter = 5;


//varibles for pet sprites
let petleft;
let petright;
let sprite;

function setup() {
    createCanvas(windowWidth, windowHeight);
    pos=createVector(30, 30);

    petleft = loadImage('dog left.png');
    petright = loadImage('dog right.png');

    sprite = petleft;
}


function draw() {
    clear();

    imageMode(CENTER);

    counter = counter + 0.2;

    let distance = pos.dist(createVector(mouseX,mouseY));
    let target_dir = createVector(0,0);

    frame=1;


    if (distance>300) {
        target_dir =(createVector(mouseX, mouseY).sub(pos).normalize() );
        if ( mouseX >pos.x){
            sprite = petright;
        } else {
            sprite = petleft;

        }

        frame = floor(counter) % 4 + 4;
    }


     if(distance < 32*2){
         frame = floor(counter) % 2 + 8;

    }

    pos = pos.add(target_dir.mult(speed));

    pos.x = constrain(pos.x, 0, windowWidth-32);
    pos.y = constrain(pos.y, 0, windowHeight-32);

    image(sprite ,pos.x, pos.y, 32*4, 32*4, 0, frame*32,  32,32);

}

