import Snake from './snake.js';
import Location from './location.js'; 

export const GRID_SIZE = 10;
export const PLAYFIELD_WIDTH = 640;
export const PLAYFIELD_HEIGHT = 480;

class SnakeTimer {
  constructor() {
    this.snakes = new Map();
    this.tickDelay = 100;
    this.snakeId = 0;
    setInterval(this.tick.bind(this), this.tickDelay);
  }

  addSnake(socket) {
    const snake = new Snake(this.snakeId++, socket);
    this.snakes.set(snake.id, snake);
    return snake;
  }

  removeSnake(snake) {
    this.snakes.delete(snake.id);
  }

  getSnakes() {
    return Array.from(this.snakes.values());
  }

  tick() {
    const data = this.getSnakes().map(snake => snake.getLocationsJson());
    this.snakes.forEach((snake) => {
      snake.update(this.getSnakes());
      if (snake.socket) snake.socket.emit('update', data);
    });
  }

  getRandomLocation() {
    const x = this.roundByGridSize(Math.random() * PLAYFIELD_WIDTH);
    const y = this.roundByGridSize(Math.random() * PLAYFIELD_HEIGHT);
    return new Location(x, y);
  }

  getRandomHexColor() {
    const color = Math.floor(Math.random() * 16777215).toString(16);
    return `#${('000000' + color).slice(-6)}`;
  }

  roundByGridSize(value) {
    return Math.round(value / GRID_SIZE) * GRID_SIZE;
  }
}

export default new SnakeTimer();
