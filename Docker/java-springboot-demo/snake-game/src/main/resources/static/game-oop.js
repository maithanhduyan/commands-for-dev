"use strict";

// Define the Snake class
class Snake {
    constructor(color) {
        this.snakeBody = [];
        this.color = color;
    }

    draw(context, gridSize) {
        context.fillStyle = this.color;
        for (let id in this.snakeBody) {
            context.fillRect(this.snakeBody[id].x, this.snakeBody[id].y, gridSize, gridSize);
        }
    }

    updateSnakeBody(snakeBody) {
        this.snakeBody = snakeBody;
    }
}

// Define the Food class
class Food {
    constructor(x, y, color = '#FF0000') {
        this.x = x;
        this.y = y;
        this.color = color;
        this.angle = 0; // New property to track rotation angle
    }

    draw(context, gridSize) {
        context.save(); // Save the current context state
        // Move the context to the food's center
        context.translate(this.x, this.y);

        // Apply the rotation based on the current angle
        context.rotate(this.angle);

        // Draw the food (rotated rectangle)
        context.fillStyle = this.color;
        context.fillRect(-gridSize / 2, -gridSize / 2, gridSize, gridSize);

        context.restore(); // Restore the context to its original state

        this.updateRotation();
    }

    // Increment the rotation angle for continuous spinning
    updateRotation() {
        this.angle += 1;
        if (this.angle >= 360) {
            this.angle = 0; // Reset rotation after a full circle
        }
    }
    
}

// Define the Game class
class Game {
    constructor() {
        this.fps = 30;
        this.socket = null;
        this.nextFrame = null;
        this.interval = null;
        this.direction = 'none';
        this.gridSize = 10;
        this.score = 0; // Current score
        this.highestScore = 0; // Highest score
        this.snakes = {}; // Store all snakes
        this.foods = []; // Store multiple food items
        this.context = null;
    }

    initialize() {
        this.entities = [];
        let canvas = document.getElementById('playground');
        if (!canvas.getContext) {
            Console.log('Error: 2D canvas not supported by this browser.');
            return;
        }
        this.context = canvas.getContext('2d');

        // Event listener for controlling the snake
        window.addEventListener('keydown', (e) => {
            let code = e.keyCode;
            if (code > 36 && code < 41) {
                switch (code) {
                    case 37: if (this.direction != 'east') this.setDirection('west'); break;
                    case 38: if (this.direction != 'south') this.setDirection('north'); break;
                    case 39: if (this.direction != 'west') this.setDirection('east'); break;
                    case 40: if (this.direction != 'north') this.setDirection('south'); break;
                }
            }
        }, false);

        // WebSocket connection
        const protocol = window.location.protocol === 'http:' ? 'ws://' : 'wss://';
        this.connect(`${protocol}${window.location.host}/examples/websocket/snake`);
        // Console.log(`${protocol}${window.location.host}/examples/websocket/snake`);
    }

    setDirection(direction) {
        this.direction = direction;
        this.socket.send(direction);
        Console.log(`Sent: Direction ${direction}`);
    }

    startGameLoop() {
        const loop = () => {
            // Main game logic and drawing should happen here
            this.draw();

            // Use requestAnimationFrame for smooth animations, fallback to setInterval if not supported
            if (window.requestAnimationFrame) {
                requestAnimationFrame(loop);
            }
        };

        // Start the loop using requestAnimationFrame if available, otherwise use setInterval
        if (window.requestAnimationFrame) {
            requestAnimationFrame(loop);  // Start the loop using requestAnimationFrame
        } else {
            this.interval = setInterval(loop, 1000 / this.fps);  // Fallback for older browsers
        }
    }

    stopGameLoop() {
        this.nextFrame = null;
        if (this.interval) {
            clearInterval(this.interval);
        }
    }

    draw() {
        this.context.clearRect(0, 0, 640, 480);

        // Draw all food items
        this.foods.forEach(food => food.draw(this.context, this.gridSize));

        // Draw all snakes
        for (let id in this.snakes) {
            this.snakes[id].draw(this.context, this.gridSize);
        }
    }

    addSnake(id, color) {
        const snake = new Snake(color);
        this.snakes[id] = snake;
    }

    updateSnake(id, snakeBody) {
        if (this.snakes[id]) {
            this.snakes[id].updateSnakeBody(snakeBody);
        }
    }

    removeSnake(id) {
        delete this.snakes[id];
    }

    updateScore(score) {
        this.score = score;
        document.getElementById('score').innerText = score;

        // Update highest score
        if (score > this.highestScore) {
            this.highestScore = score;
            document.getElementById('highestScore').innerText = this.highestScore;
        }
    }

    // WebSocket connection
    connect(host) {
        this.socket = 'WebSocket' in window ? new WebSocket(host) : new MozWebSocket(host);
        if (!this.socket) {
            Console.log('Error: WebSocket is not supported by this browser.');
            return;
        }

        this.socket.onopen = () => {
            Console.log('Info: WebSocket connection opened.');
            Console.log('Info: Press an arrow key to begin.');
            this.startGameLoop();

            setInterval(() => {
                this.socket.send('ping');
            }, 5000);
        };

        this.socket.onclose = () => {
            Console.log('Info: WebSocket closed.');
            this.stopGameLoop();
        };

        this.socket.onmessage = (message) => {
            const packet = JSON.parse(message.data);
            switch (packet.type) {
                case 'update':
                    packet.data.forEach(data => {
                        this.updateSnake(data.id, data.body);
                    });

                    if (packet.foods) {
                        this.foods = packet.foods.map(food => new Food(food.x, food.y));
                    }
                    break;

                case 'foods':
                    this.foods = packet.data.map(food => new Food(food.x, food.y));
                    break;

                case 'eat':
                    Console.log('Info: You ate food! Snake length increased.');
                    this.playPowerUpSound();
                    if (packet.score !== undefined) {
                        this.updateScore(packet.score);
                    }
                    break;

                case 'join':
                    packet.data.forEach(snake => {
                        this.addSnake(snake.id, snake.color);
                    });
                    if (packet.score !== undefined) {
                        this.updateScore(packet.score);
                    }
                    break;

                case 'leave':
                    this.removeSnake(packet.id);
                    break;

                case 'dead':
                    Console.log('Info: Your snake is dead, bad luck!');
                    this.direction = 'none';
                    this.playExplosionSound();
                    break;
            }
        };
    }

    // Sound playing functions
    playPowerUpSound() {
        const sound = new Audio('/sounds/powerUp.wav');
        sound.volume = 0.5; // Set volume to 50%
        sound.play().catch(error => {
            Console.log('Error: Unable to play sound. ' + error);
        });
    }

    playExplosionSound() {
        const sound = new Audio('/sounds/explosion.wav');
        sound.play().catch(error => {
            Console.log('Error: Unable to play sound. ' + error);
        });
    }
}

// Console utility
class Console {
    static log(message) {
        let console = document.getElementById('console');
        let p = document.createElement('p');
        p.style.wordWrap = 'break-word';
        p.innerHTML = message;
        console.appendChild(p);
        while (console.childNodes.length > 25) {
            console.removeChild(console.firstChild);
        }
        console.scrollTop = console.scrollHeight;
    }
}

// Initialize the game on document load
document.addEventListener("DOMContentLoaded", function () {
    // Remove elements with "noscript" class - <noscript> is not allowed in XHTML
    let noscripts = document.getElementsByClassName("noscript");
    for (let i = 0; i < noscripts.length; i++) {
        noscripts[i].parentNode.removeChild(noscripts[i]);
    }
    let game = new Game();
    game.initialize();
    Console.log('Game Ready!')
}, false);
