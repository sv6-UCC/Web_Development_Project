let canvas;
let context;
let width;
let height;
let randomspeed = getRandomNumber(20,32);
let randomposition =getRandomNumber(150,350);
let interval_id;
let start_button;
let l;
let speed = 35;
let zombiespeed =6;
let my_image;
let health =100;
let score = 0;
let music_track;
let background;
let fire_image;
let game;
let gamePaused =false;


let user = {
    x : 50,
    y : 50,
    size : 30,
    moveUp : false,
    moveDown : false,
    moveLeft : false,
    moveRight : false,
    spacebar: false,
    e_key: false,
    reload: false,
}

let body = {
    x:50,
    y:80,
    z:30,
}
let arms ={
    x:60,
    y:80,
    z:16,
    a:120,
    b:130,
}
let legs = {
    y:120,
    x:50,
    a:180,
    z:15
}


let zombiehead = {
    x:600,
    y:250,
    size:30,
}
let zombiebody={
    x:595,
    y:20,
    z:280,
    size:40
}
let zombiearms={
    x:635,
    y:280,
    z:20,
    a:670,
    b:575,
}
let zombielegs={
    x:640,
    y:595,
    z:620,
    b:20,
    a:330,
}

let gun ={
    x:90,
    y:100,
}
let bullet = {
    x:gun.x +50,
    y:gun.y,
    size:20,
    speed:15,
};

document.addEventListener('DOMContentLoaded', init, false);

function init() {
    canvas = document.querySelector('canvas');
    context = canvas.getContext('2d');
    width = canvas.width;
    height = canvas.height;
    playbtn = document.getElementById("dog")
    playbtn.addEventListener("click",playPause);
    pausebtn = document.getElementById("cat")
    pausebtn.addEventListener("click",pauseGame);
    music_track =new Audio("bensound-scifi.mp3");
    music_track.play();
    window.addEventListener('keyup', movement, false);
    interval_id= window.setInterval(draw, 100);

}







function draw() {
    context.clearRect(0, 0, width, height);


    context.fillStyle = "white"
    context.fillText(("Score : " + score), 500, 20)
    context.fillText(("Health :"+ health), 350,20)
    context.font = "25px Georgia";
    context.fillText(("Press any key to equip your weapon!"), 300,50)




    //human
    //head
    context.fillStyle = "salmon";
    context.fillRect(user.x, user.y, user.size, user.size);
    context.fillStyle = "brown";
    context.fillRect(body.x,body.y,body.z,body.z)


    context.fillRect(arms.x+20, arms.y,arms.z,arms.z);
    context.fillRect(arms.x-25, arms.y,arms.z,arms.z);



    // legs
    context.fillRect(legs.x,legs.y,legs.z,legs.z)
    context.fillRect(legs.x +20,legs.y,legs.z,legs.z)

    //zombie

    context.fillStyle = "green";
    //head
    context.fillRect(zombiehead.x, zombiehead.y, zombiehead.size, zombiehead.size);
    zombiehead.x-=zombiespeed

    context.fillStyle = "grey"

    context.fillRect(zombiebody.x, zombiebody.z,zombiebody.size,zombiebody.size);//body
    context.fillRect(zombiearms.x, zombiearms.y,zombiearms.z,zombiearms.z);//right arm
    context.fillRect(zombiearms.b, zombiearms.y,zombiebody.y,zombiebody.y);//left arm
    //left arm
    context.fillRect(zombielegs.z, zombielegs.a,zombielegs.b,zombielegs.b);//left leg
    context.fillRect(zombielegs.y, zombielegs.a,zombielegs.b,zombielegs.b);//right leg
    zombiearms.b -=zombiespeed
    zombiearms.x -=zombiespeed

    zombiebody.x-=zombiespeed
    zombielegs.y -=zombiespeed
    zombielegs.z -=zombiespeed




    if (reload){

        bullet.x= gun.x +50
    }
    //shooting gun
   if (spacebar) {
       context.fillStyle = "yellow";
       context.fillRect(bullet.x, bullet.y, bullet.size, bullet.size);
       bullet.speed =50
       bullet.x+=bullet.speed

   }



   // below code is for when you shoot the zombie
   if (collbullet(bullet)) {

         score = score + 10
         zombiearms.b =785
         zombiearms.x =830
         zombiehead.x=800
         zombiebody.x=800
         zombielegs.y =795
         zombielegs.z =820
         l =getRandomNumber(150,350);
         s =getRandomNumber(20,32);
         //bullet.speed =0
         bullet.x =gun.x +50
         zombiespeed =s
         zombiehead.y=l   //80
         zombiebody.z=l +30
         zombiearms.y=l + 30
         zombielegs.a=l + 90

         //context.fillRect(bullet.x, bullet.y, bullet.size, bullet.size);
         //context.clearRect(bullet.x, bullet.y, bullet.size, bullet.size);

         //context.fillRect(arms.a, bullet.y, bullet.size, bullet.size);
         //bullet.y+=speed
      }
      if (collbullet4(bullet)) {

         score = score + 20
         zombiearms.b =785
         zombiearms.x =830
         zombiehead.x=800
         zombiebody.x=800
         zombielegs.y =795
         zombielegs.z =820
         //bullet.speed =0
         bullet.x =gun.x +50
         l =getRandomNumber(150,350);
         s =getRandomNumber(20,32);
         bullet.x =gun.x +50
         zombiespeed =s
         zombiehead.y=l   //80
         zombiebody.z=l +30
         zombiearms.y=l + 30
         zombielegs.a=l + 90

         //context.fillRect(bullet.x, bullet.y, bullet.size, bullet.size);
         //context.clearRect(bullet.x, bullet.y, bullet.size, bullet.size);

         //context.fillRect(arms.a, bullet.y, bullet.size, bullet.size);
         //bullet.y+=speed
       }

      if (collbullet5(bullet)) {
        //context.fillRect(zombiebody.x+200, zombiebody.z,zombiebody.size,zombiebody.size);//body
        //context.fillRect(zombiearms.x+200, zombiearms.y,zombiebody.y,zombiebody.y);//right arm
        //context.fillRect(zombiearms.b+200, zombiearms.y,zombiebody.y,zombiebody.y);
      //left arm
        //context.fillRect(zombielegs.z+200, zombielegs.a,zombiehead.size-20,zombiehead.size+5);
        //context.fillRect(zombielegs.y+200, zombielegs.a,zombiehead.size-20,zombiehead.size+5);
        score = score + 10
        zombiearms.b =785
        zombiearms.x =830
        zombiehead.x=800
        zombiebody.x=800
        zombielegs.y =795
        zombielegs.z =820
        s =getRandomNumber(20,32);
        bullet.x =gun.x +50
        l =getRandomNumber(150,350);
        bullet.x =gun.x +50
        zombiespeed =s
        zombiehead.y=l
        zombiebody.z=l +30
        zombiearms.y=l + 30
        zombielegs.a=l + 90
       }


     if (collbullet3(bullet)) {

        score = score + 10
        zombiearms.b =785
        zombiearms.x =830
        zombiehead.x=800
        zombiebody.x=800
        zombielegs.y =795
        zombielegs.z =820
        bullet.x =gun.x +50
        l =getRandomNumber(150,350);
        s =getRandomNumber(20,32);
        bullet.x =gun.x +50
        zombiespeed =s
        zombiehead.y=l
        zombiebody.z=l +30
        zombiearms.y=l + 30
        zombielegs.a=l + 90
      }



     //if zombie gets to your base
     if (zombiehead.x <= 0){
       health = health -20
       zombiehead.x+=width
       zombiearms.b +=width
       zombiearms.x +=width
       zombiebody.x +=width
       zombielegs.y +=width
       zombielegs.z +=width
     }





     //code for moving the user up down left right
    if (moveRight) {
        user.x += speed;
        body.x +=speed
        arms.x+=speed
        gun.x+=speed
        legs.x+=speed
    }
    if (moveLeft) {
        user.x -= speed;
        body.x -=speed
        arms.x-=speed
        gun.x -=speed
        legs.x-=speed
    }
    if (moveUp) {
        user.y -= speed;
        gun.y -=speed
        body.y-=speed;
        arms.y-=speed
        arms.b-=speed
        legs.y-=speed
        legs.a-=speed
        bullet.y-=speed



    }
    if (moveDown) {
        user.y += speed;
        gun.y +=speed
        body.y+=speed;
        arms.y+=speed
        arms.b+=speed
        legs.y+=speed
        legs.a+=speed
        bullet.y+=speed
    //prevent user going outside the canvas
    }
    if (user.x + user.size >= width +110) {//right
      stop();
      window.alert('Where do you think you are going?');
      window.location = "https://cs1.ucc.ie/~sv6/cgi-bin/lab7/nice.html";
      return;
    }
    if (user.y + user.size >= height +110) {//bottom
      stop();
      window.alert('Where do you think you are going?');
      window.location = "https://cs1.ucc.ie/~sv6/cgi-bin/lab7/nice.html";
      return;
    }
    if (user.x <= (-110)) {//left
      stop();
      window.alert('Where do you think you are going?');
      window.location = "https://cs1.ucc.ie/~sv6/cgi-bin/lab7/nice.html";
      return;
    }

    if (user.y <= (-110)) {
      stop();
      window.alert('Where do you think you are going?');
      window.location = "https://cs1.ucc.ie/~sv6/cgi-bin/lab7/nice.html";
      return;
    //If you collide with the zombie you lose health
    }
    if (collides(zombiearms)) {
      health = health-20
      return;
    }
    if (collides2(zombiearms)) {
      health = health-20
      return;
    }
    if (collides3(zombiearms)) {
      health = health-20
      return;
    }
    if (collides4(zombiehead)) {
      health = health-20
      return;
    }
    if (collides5(zombielegs)) {
      health = health-20
      return;
    }

    //If your health is 0 you lose
    if (health <= 0){
      stop();
      window.alert('YOU LOSE! You scored:'+ score);
      window.location = "https://cs1.ucc.ie/~sv6/cgi-bin/lab7/congratulations.py";
      return;
    }
    //image for the gun
    my_image =new Image();
    my_image.src ='download4.png'
    context.drawImage(my_image, gun.x, gun.y);

}


function movement() {
    moveUp = false;

    moveDown = false;
    moveLeft = false;
    moveRight = false;
    spacebar = false;
    reload = false;

    let keyCode = event.keyCode;
    if (keyCode === 87) {
        moveUp = true;
    }
    else if (keyCode === 68) {
        moveRight = true;
    }
    else if (keyCode === 65) {
        moveLeft = true;
    }
    else if (keyCode === 83) {
        moveDown = true;
    }
    else if (keyCode === 81) {
        spacebar = true;
    }

    else if (keyCode === 82) {
         reload = true;
    }

}
function collides(zombiearms) {
    if (arms.x + arms.z <zombiearms.x ||
        zombiearms.x + zombiebody.y <arms.x ||
        arms.y > zombiearms.y + zombiebody.y ||
        zombiearms.y > arms.y +arms.z) {
        return false;
    } else {
        return true;
    }
}

function collides2(zombiearms) {
    if (body.x + body.z <zombiearms.x ||
        zombiearms.x + zombiebody.y <body.x ||
        body.y > zombiearms.y + zombiebody.y ||
        zombiearms.y > body.y +body.z) {
        return false;
    } else {
        return true;
    }
}


function collbullet(bullet) {
    if(bullet.x + bullet.size <zombiearms.x ||
       zombiearms.x + zombiearms.z <bullet.x ||
       bullet.y > zombiearms.y + zombiearms.z ||
       zombiearms.y > bullet.y +bullet.size) {
    } else {
        return true;
    }
}

function collides3(zombiearms) {
  if(legs.x + legs.z <zombiearms.x ||
     zombiearms.x + zombiebody.y <legs.x ||
     legs.y > zombiearms.y + zombiebody.y ||
     zombiearms.y > legs.y +legs.z){
        return false;
    } else {
        return true;
    }
}
function collides4(zombiehead) {
  if(legs.x + legs.z <zombiehead.x ||
     zombiehead.x + zombiehead.size <legs.x ||
     legs.y > zombiehead.y + zombiehead.size ||
     zombiehead.y > legs.y +legs.z){
        return false;
    } else {
        return true;
    }
}
function collides5(zombielegs) {
  if(user.x + user.size <zombielegs.y ||
     zombielegs.y + zombielegs.b <user.x ||
     user.y > zombielegs.a + zombielegs.b ||
     zombielegs.a > user.y +user.size){
        return false;
    } else {
        return true;
    }
}

function collbullet3(bullet) {
  if(bullet.x + bullet.size <zombiebody.x ||
     zombiebody.x + zombiebody.size <bullet.x ||
     bullet.y > zombiebody.z + zombiebody.size||
     zombiebody.z > bullet.y +bullet.size){
        return false;
    } else {
        return true;
    }
}

function collbullet4(bullet) {
  if(bullet.x + bullet.size <zombiehead.x ||
     zombiehead.x + zombiehead.size <bullet.x ||
     bullet.y > zombiehead.y + zombiehead.size||
     zombiehead.y > bullet.y +bullet.size){
        return false;
    } else {
        return true;
    }
}
function collbullet5(bullet) {
  if(bullet.x + bullet.size <zombielegs.y ||
     zombielegs.y + zombielegs.b <bullet.x ||
     bullet.y > zombielegs.a + zombielegs.b||
     zombielegs.a > bullet.y +bullet.size){
        return false;
    } else {
        return true;
    }
}

function stop() {
  clearInterval(interval_id);
  let url = 'store_score.py?score=' + score;
  request = new XMLHttpRequest();
  request.addEventListener('readystatechange', handle_response, false);
  request.open('GET', url, true);
  request.send(null);
}
function handle_response() {
    // Check that the response has fully arrived
    if ( request.readyState === 4 ) {
        // Check the request was successful
        if ( request.status === 200 ) {
            if ( request.responseText.trim() === 'success' ) {
                // score was successfully stored in database
            } else  {
                // score was not successfully stored in database
            }
        }
    }
}
//Function for pausing/playing the audio
function playPause(){
		if(music_track.paused){
		    music_track.play();
	    } else {
		    music_track.pause();
	    }
	}
//function for pausing/playing the game
function pauseGame() {
  if (!gamePaused) {
    game = clearInterval(interval_id);
    gamePaused = true;
  } else{
    interval_id= window.setInterval(draw, 100);
    gamePaused = false

  }
}

function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
