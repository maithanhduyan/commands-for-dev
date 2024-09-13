// src/classes/Game.ts
import { Snake } from './Snake';
import { Food } from './Food';
import { Console } from './Console';

interface SnakeData {
    id: string;
    body: { x: number; y: number }[];
    color?: string;
}

interface Packet {
    type: string;
    data: any;
    foods?: any[];
    id?: string;
    score?: number;
}
const explosion_sound = './assets/sounds/explosion.wav';
const powerUp_sound = './assets/sounds/powerUp.wav';

export class Game {
    fps: number;
    socket: WebSocket | null;
    interval: number | null;
    direction: string;
    gridSize: number;
    score: number;
    highestScore: number;
    snakes: { [key: string]: Snake };
    foods: Food[];
    context: CanvasRenderingContext2D | null;
    canvas: HTMLCanvasElement | null;

    constructor() {
        this.fps = 30;
        this.socket = null;
        this.interval = null;
        this.direction = 'none';
        this.gridSize = 10;
        this.score = 0;
        this.highestScore = 0;
        this.snakes = {};
        this.foods = [];
        this.context = null;
        this.canvas = null;
    }

    initialize() {
        this.canvas = document.getElementById('playground') as HTMLCanvasElement;
        if (!this.canvas.getContext) {
            Console.log('Error: 2D canvas not supported by this browser.');
            return;
        }
        this.context = this.canvas.getContext('2d');

        window.addEventListener(
            'keydown',
            (e) => {
                const code = e.keyCode;
                if (code >= 37 && code <= 40) {
                    switch (code) {
                        case 37:
                            if (this.direction !== 'east') this.setDirection('west');
                            break;
                        case 38:
                            if (this.direction !== 'south') this.setDirection('north');
                            break;
                        case 39:
                            if (this.direction !== 'west') this.setDirection('east');
                            break;
                        case 40:
                            if (this.direction !== 'north') this.setDirection('south');
                            break;
                    }
                }
            },
            false
        );

        const protocol = window.location.protocol === 'http:' ? 'ws://' : 'wss://';
        const server = 'localhost';
        const port = '8080';
        this.connect(`${protocol}${server}:${port}/examples/websocket/snake`);
    }

    setDirection(direction: string) {
        this.direction = direction;
        this.socket?.send(direction);
        Console.log(`Sent: Direction ${direction}`);
    }

    startGameLoop() {
        const loop = () => {
            this.draw();
            requestAnimationFrame(loop);
        };
        requestAnimationFrame(loop);
    }

    stopGameLoop() {
        if (this.interval) {
            clearInterval(this.interval);
        }
    }

    draw() {
        if (!this.context || !this.canvas) return;
        this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);

        this.foods.forEach((food) => food.draw(this.context!, this.gridSize));

        for (const id in this.snakes) {
            this.snakes[id].draw(this.context!, this.gridSize);
        }
    }

    addSnake(id: string, color: string) {
        const snake = new Snake(color);
        this.snakes[id] = snake;
    }

    updateSnake(id: string, snakeBody: { x: number; y: number }[]) {
        if (this.snakes[id]) {
            this.snakes[id].updateSnakeBody(snakeBody);
        }
    }

    removeSnake(id: string) {
        delete this.snakes[id];
    }

    updateScore(score: number) {
        this.score = score;
        const scoreElement = document.getElementById('score');
        if (scoreElement) scoreElement.innerText = score.toString();

        if (score > this.highestScore) {
            this.highestScore = score;
            const highestScoreElement = document.getElementById('highestScore');
            if (highestScoreElement) highestScoreElement.innerText = this.highestScore.toString();
        }
    }

    connect(host: string) {
        this.socket = new WebSocket(host);

        this.socket.onopen = () => {
            Console.log('Info: WebSocket connection opened.');
            Console.log('Info: Press an arrow key to begin.');
            this.startGameLoop();

            setInterval(() => {
                this.socket?.send('ping');
            }, 5000);
        };

        this.socket.onclose = () => {
            Console.log('Info: WebSocket closed.');
            this.stopGameLoop();
        };

        this.socket.onmessage = (message) => {
            const packet: Packet = JSON.parse(message.data);
            switch (packet.type) {
                case 'update':
                    packet.data.forEach((data: SnakeData) => {
                        this.updateSnake(data.id, data.body);
                    });

                    if (packet.foods) {
                        this.foods = packet.foods.map((food: any) => new Food(food.x, food.y));
                    }
                    break;

                case 'foods':
                    this.foods = packet.data.map((food: any) => new Food(food.x, food.y));
                    break;

                case 'eat':
                    Console.log('Info: You ate food! Snake length increased.');
                    this.playPowerUpSound();
                    if (packet.score !== undefined) {
                        this.updateScore(packet.score);
                    }
                    break;

                case 'join':
                    packet.data.forEach((snake: SnakeData) => {
                        this.addSnake(snake.id, snake.color!);
                    });
                    if (packet.score !== undefined) {
                        this.updateScore(packet.score);
                    }
                    break;

                case 'leave':
                    if (packet.id) {
                        this.removeSnake(packet.id);
                    }
                    break;

                case 'dead':
                    Console.log('Info: Your snake is dead, bad luck!');
                    this.direction = 'none';
                    this.playExplosionSound();
                    break;
            }
        };
    }

    playPowerUpSound() {
        const sound = new Audio(powerUp_sound);
        sound.volume = 0.5;
        sound.play().catch((error) => {
            Console.log('Error: Unable to play sound. ' + error);
        });
    }

    playExplosionSound() {
        const sound = new Audio(explosion_sound);
        sound.play().catch((error) => {
            Console.log('Error: Unable to play sound. ' + error);
        });
    }
}
