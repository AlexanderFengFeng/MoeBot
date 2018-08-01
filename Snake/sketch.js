var snake;              // Snake object
var scl = 20;           // Scale of objects and speed
var food;               // 2D vector for food position
var speed = 1;
var pressed;
var paused;
var dead;
var touch;
var cols;
var rows;

function setup() {
	createCanvas(600, 600);
    snake = new Snake();
    snake.update()
    frameRate(12);
    pickLocation();
    paused = false;
    pressed = false;
    dead = false;
    touch = false;
}

function draw() {
	background(51);
    pressed = false;
    
    if (paused === false && dead === false) {
        snake.update();
        if (snake.dies()) {
            dead = true;
        }
    }
    
    if (dead === true) {
        fill(255);  
        text("YOU DIED SNAKE", width/2 - 50, height/2 - 20);
        text("You scored " + snake.total + " points", width/2 - 52, height/2 - 5);
        text("Hit ENTER to start again", width/2 - 65, height/2 + 10);
    }
    
    if (paused === true) {
        fill(255);
        text("PAUSED", width/2 - 25, height/2 - 5);
    }
    
    snake.show();
    
    if (snake.eat(food)) {
        pickLocation();
    }

    fill(255, 0, 120);
    rect(food.x, food.y, scl, scl);
}

// Randomizes location of new food and stores location in food
function pickLocation() {
    cols = floor(width/scl);
    rows = floor(height/scl);
    generate();
    
    touch = true;
    while (touch === true) {
        touch = false;
        for (var i = 0; i < snake.tail.length; i++) {
            if (dist(food.x, food.y, snake.tail[i].x, snake.tail[i].y) < 1) {
                touch = true;
                generate();
            }
        }
        if (snake.touch(food)) {
            touch = true;
            generate();
        }
    }
}

function generate() {
    food = createVector(floor(random(cols)), floor(random(rows)));
    food.mult(scl);
}

// Calls turn and updates 
function keyPressed() {
    if (pressed === false) {
        if (keyCode === UP_ARROW) {
            if (!(snake.total > 0 && snake.down == true)) {
                snake.turn(0, -speed);
                snake.clear();
                snake.up = true;
                paused = false;
            }
        }
        if (keyCode === RIGHT_ARROW) {
            if (!(snake.total > 0 && snake.left == true)) {
                snake.turn(speed, 0);
                snake.clear();
                snake.right = true;
                paused = false;
           }
        }
        if (keyCode === DOWN_ARROW) {
            if (!(snake.total > 0 && snake.up == true)) {
                snake.turn(0, speed);
                snake.clear();
                snake.down = true;
                paused = false;
          }
        }
        if (keyCode === LEFT_ARROW) {
            if (!(snake.total > 0 && snake.right == true)) {
                snake.turn(-speed, 0);
                snake.clear();
                snake.left = true;
                paused = false;
            }
        }
        pressed = true;
    }
    if (keyCode === ENTER) {
        if (paused === false) {
            paused = true;
        } else {
            paused = false;
        }
        if (dead === true) {
            setup();
        }
    }
}
