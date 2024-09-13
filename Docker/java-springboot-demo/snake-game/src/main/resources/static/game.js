"use strict";

let Game = {};

Game.fps = 30;
Game.socket = null;
Game.nextFrame = null;
Game.interval = null;
Game.direction = 'none';
Game.gridSize = 10;
Game.score = 0; // Current score
Game.highestScore = 0; // Highest score

function Snake() {
    this.snakeBody = [];
    this.color = null;
}

Snake.prototype.draw = function (context) {
    //Ensure that the snake's color is correctly set when a new snake joins.
    context.fillStyle = this.color;

    for (let id in this.snakeBody) {
        context.fillStyle = this.color;
        context.fillRect(this.snakeBody[id].x, this.snakeBody[id].y, Game.gridSize, Game.gridSize);
    }
};

// Add Food to the Game object
Game.foods = [];

Game.initialize = function () {
    this.entities = [];
    let canvas = document.getElementById('playground');
    if (!canvas.getContext) {
        Console.log('Error: 2d canvas not supported by this browser.');
        return;
    }
    this.context = canvas.getContext('2d');
    window.addEventListener('keydown', function (e) {
        let code = e.keyCode;
        if (code > 36 && code < 41) {
            switch (code) {
                case 37:
                    if (Game.direction != 'east') Game.setDirection('west');
                    break;
                case 38:
                    if (Game.direction != 'south') Game.setDirection('north');
                    break;
                case 39:
                    if (Game.direction != 'west') Game.setDirection('east');
                    break;
                case 40:
                    if (Game.direction != 'north') Game.setDirection('south');
                    break;
            }
        }
    }, false);
    if (window.location.protocol == 'http:') {
        Game.connect('ws://' + window.location.host + '/examples/websocket/snake');
    } else {
        Game.connect('wss://' + window.location.host + '/examples/websocket/snake');
    }
};

Game.setDirection = function (direction) {
    Game.direction = direction;
    Game.socket.send(direction);
    Console.log('Sent: Direction ' + direction);
};

Game.startGameLoop = function () {
    if (window.webkitRequestAnimationFrame) {
        Game.nextFrame = function () {
            webkitRequestAnimationFrame(Game.run);
        };
    } else if (window.mozRequestAnimationFrame) {
        Game.nextFrame = function () {
            mozRequestAnimationFrame(Game.run);
        };
    } else {
        Game.interval = setInterval(Game.run, 1000 / Game.fps);
    }
    if (Game.nextFrame != null) {
        Game.nextFrame();
    }
};

Game.stopGameLoop = function () {
    Game.nextFrame = null;
    if (Game.interval != null) {
        clearInterval(Game.interval);
    }
};

Game.draw = function () {
    this.context.clearRect(0, 0, 640, 480);

    // Draw all the food items
    for (let i = 0; i < Game.foods.length; i++) {
        let food = Game.foods[i];
        this.context.fillStyle = food.color;
        this.context.fillRect(food.x, food.y, Game.gridSize, Game.gridSize);
    }

    // Draw the snake
    for (let id in this.entities) {
        this.entities[id].draw(this.context);
    }
};

Game.addSnake = function (id, color) {
    let snake = new Snake();
    snake.color = color;
    Game.entities[id] = snake;
};

// Modify Game.addSnake to include the color
Game.updateSnake = function (id, snakeBody) {
    if (typeof Game.entities[id] != "undefined") {
        Game.entities[id].snakeBody = snakeBody;
    }
};

Game.removeSnake = function (id) {
    Game.entities[id] = null;
    // Force GC.
    delete Game.entities[id];
};

Game.run = (function () {
    let skipTicks = 1000 / Game.fps, nextGameTick = (new Date).getTime();

    return function () {
        while ((new Date).getTime() > nextGameTick) {
            nextGameTick += skipTicks;
        }
        Game.draw();
        if (Game.nextFrame != null) {
            Game.nextFrame();
        }
    };
})();

// Update the score on the UI
Game.updateScore = function (score) {
    Game.score = score;
    document.getElementById('score').innerText = score;

    // Update the highest score if current score is higher
    if (score > Game.highestScore) {
        Game.highestScore = score;
        document.getElementById('highestScore').innerText = Game.highestScore;
    }
};

Game.connect = (function (host) {
    if ('WebSocket' in window) {
        Game.socket = new WebSocket(host);
    } else if ('MozWebSocket' in window) {
        Game.socket = new MozWebSocket(host);
    } else {
        Console.log('Error: WebSocket is not supported by this browser.');
        return;
    }

    Game.socket.onopen = function () {
        // Socket open.. start the game loop.
        Console.log('Info: WebSocket connection opened.');
        Console.log('Info: Press an arrow key to begin.');
        Game.startGameLoop();
        setInterval(function () {
            // Prevent server read timeout.
            Game.socket.send('ping');
        }, 5000);
    };

    Game.socket.onclose = function () {
        Console.log('Info: WebSocket closed.');
        Game.stopGameLoop();
    };

    Game.socket.onmessage = function (message) {
        let packet = JSON.parse(message.data);
        switch (packet.type) {
            case 'update':

                for (let i = 0; i < packet.data.length; i++) {
                    Game.updateSnake(packet.data[i].id, packet.data[i].body);
                }

                // Update the food locations
                if (packet.foods) {
                    Game.foods = []; // Clear existing foods
                    for (var i = 0; i < packet.foods.length; i++) {
                        var foodData = packet.foods[i];
                        Game.foods.push({
                            x: foodData.x,
                            y: foodData.y,
                            color: '#FF0000' // Red color
                        });
                    }
                }

                break;
            case 'foods':
                // Initial food data when a client connects
                Game.foods = []; // Clear existing foods
                for (var i = 0; i < packet.data.length; i++) {
                    var foodData = packet.data[i];
                    Game.foods.push({
                        x: foodData.x,
                        y: foodData.y,
                        color: '#FF0000' // Red color
                    });
                }
                break;
            case 'food':
                // Single food update (if needed)
                break;
            case 'eat':
                Console.log('Info: You ate food! Snake length increased.');

                // Play the power-up sound
                Game.playPowerUpSound();

                // Update the score
                if (packet.score !== undefined) {
                    Game.updateScore(packet.score);
                }
                break;
            case 'join':
                for (let j = 0; j < packet.data.length; j++) {
                    Game.addSnake(packet.data[j].id, packet.data[j].color);
                }

                // Handle initial score
                if (packet.score !== undefined) {
                    Game.updateScore(packet.score);
                }
                break;
            case 'leave':
                Game.removeSnake(packet.id);
                break;
            case 'dead':
                Console.log('Info: Your snake is dead, bad luck!');
                Game.direction = 'none';

                // Play the explosion sound
                Game.playExplosionSound();
                break;
            case 'kill':
                Console.log('Info: Head shot!');
                break;
        }
    };
});

// Load the power-up sound
Game.powerUpSound = new Audio('/sounds/powerUp.wav');
// Ensure the sound is allowed to play (user interaction may be required)
Game.powerUpSound.load();

// Load the explosion sound
Game.explosionSound = new Audio('/sounds/explosion.wav');
Game.explosionSound.load();

Game.playPowerUpSound = function () {
    // Check if the audio can be played
    if (Game.powerUpSound) {
        // Play the sound
        Game.powerUpSound.currentTime = 0; // Reset to start
        Game.powerUpSound.play().catch(function (error) {
            // Handle any errors (e.g., due to browser policies)
            Console.log('Error: Unable to play sound. ' + error);
        });
    }
};

// Function to play the explosion sound
Game.playExplosionSound = function () {
    if (Game.explosionSound) {
        Game.explosionSound.currentTime = 0; // Reset to start
        Game.explosionSound.play().catch(function (error) {
            Console.log('Error: Unable to play explosion sound. ' + error);
        });
    }
};

let Console = {};

Console.log = (function (message) {
    let console = document.getElementById('console');
    let p = document.createElement('p');
    p.style.wordWrap = 'break-word';
    p.innerHTML = message;
    console.appendChild(p);
    while (console.childNodes.length > 25) {
        console.removeChild(console.firstChild);
    }
    console.scrollTop = console.scrollHeight;
});




document.addEventListener("DOMContentLoaded", function () {
    // Remove elements with "noscript" class - <noscript> is not allowed in XHTML
    let noscripts = document.getElementsByClassName("noscript");
    for (let i = 0; i < noscripts.length; i++) {
        noscripts[i].parentNode.removeChild(noscripts[i]);
    }

    Game.initialize();
}, false);