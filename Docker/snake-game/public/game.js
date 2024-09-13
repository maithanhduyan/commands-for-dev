const gridSize = 10;
class Snake {

    constructor(id, context) {
        this.id = id;
        this.snakeBody = [
            { x: 320, y: 240 },
            { x: 330, y: 240 },
            { x: 340, y: 240 },
            { x: 350, y: 240 },
        ];
        this.color = '#00ff00';
        this.speed = 1;
        this.context = context;
        this.direction = 'none';
        this.alive = true;
    }

    draw() {

        // Vẽ đầu rắn
        let head = this.snakeBody[0];
        this.context.fillStyle = this.color;
        this.context.fillRect(head.x, head.y, gridSize, gridSize);

        // Vẽ mắt
        this.context.fillStyle = '#ffffff';
        let eyeSize = gridSize / 4;
        let eyeOffset = gridSize / 4;

        // // Vị trí mắt phụ thuộc vào hướng di chuyển
        switch (this.direction) {
            case 'north':
                this.context.fillRect(head.x + eyeOffset, head.y + eyeOffset, eyeSize, eyeSize);
                this.context.fillRect(head.x + gridSize - eyeOffset - eyeSize, head.y + eyeOffset, eyeSize, eyeSize);
                break;
            case 'south':
                this.context.fillRect(head.x + eyeOffset, head.y + gridSize - eyeOffset - eyeSize, eyeSize, eyeSize);
                this.context.fillRect(head.x + gridSize - eyeOffset - eyeSize, head.y + gridSize - eyeOffset - eyeSize, eyeSize, eyeSize);
                break;
            case 'west':
                this.context.fillRect(head.x + eyeOffset, head.y + eyeOffset, eyeSize, eyeSize);
                this.context.fillRect(head.x + eyeOffset, head.y + gridSize - eyeOffset - eyeSize, eyeSize, eyeSize);
                break;
            case 'east':
                this.context.fillRect(head.x + gridSize - eyeOffset - eyeSize, head.y + eyeOffset, eyeSize, eyeSize);
                this.context.fillRect(head.x + gridSize - eyeOffset - eyeSize, head.y + gridSize - eyeOffset - eyeSize, eyeSize, eyeSize);
                break;
        }

        // Vẽ lưỡi
        this.context.fillStyle = '#ff0000';
        let tongueWidth = gridSize / 3;
        let tongueHeight = gridSize / 2;

        switch (this.direction) {
            case 'north':
                this.context.fillRect(head.x + gridSize / 2 - tongueWidth / 2, head.y - tongueHeight, tongueWidth, tongueHeight);
                break;
            case 'south':
                this.context.fillRect(head.x + gridSize / 2 - tongueWidth / 2, head.y + gridSize, tongueWidth, tongueHeight);
                break;
            case 'west':
                this.context.fillRect(head.x - tongueHeight, head.y + gridSize / 2 - tongueWidth / 2, tongueHeight, tongueWidth);
                break;
            case 'east':
                this.context.fillRect(head.x + gridSize, head.y + gridSize / 2 - tongueWidth / 2, tongueHeight, tongueWidth);
                break;
        }

        // Vẽ thân rắn
        for (let i = 1; i < this.snakeBody.length; i++) {
            this.context.fillStyle = this.color;
            this.context.fillRect(this.snakeBody[i].x, this.snakeBody[i].y, gridSize, gridSize);
        }
    }

    move() {
        let head = { ...this.snakeBody[0] };
        switch (this.direction) {
            case 'north':
                head.y -= this.speed;
                break;
            case 'south':
                head.y += this.speed;
                break;
            case 'west':
                head.x -= this.speed;
                break;
            case 'east':
                head.x += this.speed;
                break;
        }
        this.snakeBody.unshift(head);

        // Nếu rắn không ăn thức ăn, loại bỏ phần cuối
        if (!this.justAteFood) {
            this.snakeBody.pop();
        } else {
            this.justAteFood = false; // Reset trạng thái
        }

    }

    eat(food) {
        let head = this.snakeBody[0];
        if (head.x === food.position.x || head.y === food.position.y) {
            this.justAteFood = true;
            this.snakeBody.push({ x: food.position.x, y: food.position.y });
            return true;
        }
        return false;
    }

    // Kiểm tra va chạm với viền màn hình
    checkCollision() {
        let head = this.snakeBody[0];
        if (head.x < 0 || head.x >= 640 || head.y < 0 || head.y >= 480) {
            this.alive = false;
            this.speed = 0;
            return true;
        }
        return false;
    }

    // Kiểm tra va chạm với thân
    checkSelfCollision() {
        let head = this.snakeBody[0];
        for (let i = 1; i < this.snakeBody.length; i++) {
            if (head.x === this.snakeBody[i].x && head.y === this.snakeBody[i].y) {
                this.alive = false;
                return true;
            }
        }
        return false;
    }

    update() {
        this.draw();
        this.checkCollision();
        this.checkSelfCollision();
        this.move();
    }

    getSpeed() {
        return this.speed;
    }

    setSpeed(speed) {
        this.speed = speed;
    }
    setDirection(direction) {
        this.direction = direction;
    }
}


class Food {
    constructor(context) {
        this.context = context;
        this.size = gridSize;
        this.color = '#ff0000';
        this.speed = 1;
        this.angle = 0;
        this.moveAngle = 1;
        this.position = this.generatePosition();
    }

    generatePosition() {
        return {
            x: Math.floor(Math.random() * (640 / this.size)) * this.size,
            y: Math.floor(Math.random() * (480 / this.size)) * this.size
        };
    }

    draw() {
        this.context.fillStyle = this.color;
        this.context.fillRect(this.position.x, this.position.y, this.size, this.size);
    }

    update() {
        this.draw();
        // this.animate();
    }

    animate() {
        this.angle += this.moveAngle * Math.PI / 180;
        this.position.x += this.speed * Math.sin(this.angle);
        this.position.y -= this.speed * Math.cos(this.angle);
    }

    destroy() {
        this.position = null;
    }
}

class Game {
    constructor() {
        this.desiredFPS = 60;
        this.nextFrame = null;
        this.interval = null;
        this.direction = 'none';
        this.gridSize = 10;
        this.entities = [];
        this.snake = null;
        this.lastFrameTime = 0;
        this.frameCount = 0;
        this.currentFPS = 0;
        this.food = null;
    }

    getDirection() {
        return this.direction;
    }

    initialize() {
        let canvas = document.getElementById('playground');
        if (!canvas.getContext) {
            console.log('Error: 2d canvas not supported by this browser.');
            return;
        }
        this.context = canvas.getContext('2d');

        window.addEventListener('keydown', (e) => {
            let key = e.key;
            console.log(key)
            switch (key) {
                case 'ArrowLeft':
                    if (this.snake.direction != 'east') this.snake.setDirection('west');
                    break;
                case 'ArrowUp':
                    if (this.snake.direction != 'south') this.snake.setDirection('north');
                    break;
                case 'ArrowRight':
                    if (this.snake.direction != 'west') this.snake.setDirection('east');
                    break;
                case 'ArrowDown':
                    if (this.snake.direction != 'north') this.snake.setDirection('south');
                    break;
                case ' ': // Backspace
                    this.snake.setSpeed(5);
                    break
                default: console.log('Key Not Available.');
            }
        }, false);

        window.addEventListener('keyup', (e) => {
            let key = e.key;
            switch (key) {
                case ' ':
                    this.snake.setSpeed(1);
                    break;
            }
        }, false);

        this.addSnake('1', '#00ff00');
        this.food = new Food(this.context);
        this.start();
    }

    addSnake(id, color) {
        this.snake = new Snake(id, this.context);
        this.snake.color = color;
        this.entities.push(this.snake);
    }

    start() {
        let lastTime = 0;
        let fpsInterval = 1000; // 1 giây
        let fpsTimer = 0; // Thời gian tích lũy để tính FPS

        // Create game loop
        const gameLoop = (timestamp) => {
            if (!lastTime) {
                lastTime = timestamp;
            }
            const deltaTime = timestamp - lastTime;
            lastTime = timestamp;

            // Tăng bộ đếm khung hình
            this.frameCount++;

            // Cộng dồn fpsTimer để tính FPS
            fpsTimer += deltaTime;

            // Nếu đã trôi qua 1 giây, cập nhật currentFPS
            if (fpsTimer >= fpsInterval) {
                this.currentFPS = this.frameCount;
                this.frameCount = 0;
                fpsTimer -= fpsInterval;
            }

            // Gọi hàm cập nhật game với deltaTime
            this.update(deltaTime);

            // Tiếp tục vòng lặp
            this.nextFrame = requestAnimationFrame(gameLoop);
        };

        this.nextFrame = requestAnimationFrame(gameLoop); // Bắt đầu vòng lặp game
    }

    stop() {
        console.log('Game Over.')
        this.nextFrame = null;
        if (this.interval != null) {
            clearInterval(this.interval);
        }
    }

    update(deltaTime) {
        this.draw();
        this.food.update();
        for (let id in this.entities) {
            if (this.entities.hasOwnProperty(id)) {
                this.entities[id].update();
                // Kiểm tra va chạm với tường
                if (this.entities[id].checkCollision()) {
                    this.stop();
                    // Reset game
                    this.showGameOver();
                    // Show Menu
                }

                // Kiểm tra và xử lý ăn thức ăn
                if (this.entities[id].eat(this.food)) {
                    console.log(`snake length: ${this.snake.snakeBody.length}`);
                    this.generateFood();
                    console.log('Tạo mới thức ăn.');
                }
            }
        }
    }

    draw() {
        this.context.clearRect(0, 0, 640, 480);
        for (let id in this.entities) {
            if (this.entities.hasOwnProperty(id)) {
                this.entities[id].draw(this.context);
            }
        }
        this.drawSnakePosition();
        this.drawSpeed();
        this.drawFPS();
    }

    drawFPS() {
        this.context.fillStyle = '#ffffff';
        this.context.font = '16px Arial';
        this.context.fillText(`FPS: ${this.currentFPS}`, 10, 50);
    }

    generateFood() {
        this.food = new Food(this.context);
    }

    drawSpeed() {
        this.context.fillStyle = '#ffffff';
        this.context.font = '16px Arial';
        if (this.snake) {
            this.context.fillText(`Speed: ${this.snake.getSpeed()}`, 10, 30);
        }
    }

    drawSnakePosition() {
        this.context.fillStyle = '#ffffff';
        this.context.font = '16px Arial';
        if (this.snake.alive) {
            this.context.fillText(`Snake.X: ${this.snake.snakeBody[0].x} Y: ${this.snake.snakeBody[0].y}`, 450, 30);
        }
    }

    showGameOver() {
        this.context.fillStyle = '#ff0000';
        this.context.font = '48px Arial';
        this.context.fillText('Game Over', 200, 240);

        // Add event listener for click to reset game
        this.context.canvas.addEventListener('click', this.resetGame.bind(this), { once: true });
    }

    resetGame() {
        // Reset game state
        this.entities = [];
        this.initialize();
    }

    run() {
        let skipTicks = 1000 / this.fps,
            nextGameTick = new Date().getTime();

        return () => {
            while (new Date().getTime() > nextGameTick) {
                nextGameTick += skipTicks;
                for (let id in this.entities) {
                    if (this.entities.hasOwnProperty(id)) {
                        this.entities[id].move();
                    }
                }
            }
            this.draw();
            if (this.nextFrame != null) {
                this.nextFrame();
            }
        };
    }
}


document.addEventListener('DOMContentLoaded', function () {
    let noscripts = document.getElementsByClassName('noscript');
    for (let i = 0; i < noscripts.length; i++) {
        noscripts[i].parentNode.removeChild(noscripts[i]);
    }
    const game = new Game();
    game.initialize();
    console.log('Game Ready!');
}, false);
