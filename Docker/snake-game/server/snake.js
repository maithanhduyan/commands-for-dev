import Location from './location.js';
import { Direction } from './direction.js';
import SnakeTimer, { GRID_SIZE, PLAYFIELD_WIDTH, PLAYFIELD_HEIGHT } from './snakeTimer.js';

export default class Snake {
  constructor(id, socket) {
    this.id = id;
    this.socket = socket;
    this.direction = Direction.NONE;
    this.length = 5;
    this.tail = [];
    this.head = SnakeTimer.getRandomLocation();
    this.color = SnakeTimer.getRandomHexColor();
  }

  resetState() {
    this.direction = Direction.NONE;
    this.head = SnakeTimer.getRandomLocation();
    this.tail = [];
    this.length = 5;
  }

  update(snakes) {
    const nextLocation = this.head.getAdjacentLocation(this.direction);

    // Wrap around
    if (nextLocation.x >= PLAYFIELD_WIDTH) nextLocation.x = 0;
    if (nextLocation.y >= PLAYFIELD_HEIGHT) nextLocation.y = 0;
    if (nextLocation.x < 0) nextLocation.x = PLAYFIELD_WIDTH - GRID_SIZE;
    if (nextLocation.y < 0) nextLocation.y = PLAYFIELD_HEIGHT - GRID_SIZE;

    if (this.direction !== Direction.NONE) {
      this.tail.unshift(this.head);
      if (this.tail.length > this.length) this.tail.pop();
      this.head = nextLocation;
    }

    this.handleCollisions(snakes);
  }

  handleCollisions(snakes) {
    for (const snake of snakes) {
      if (snake.id !== this.id && snake.head.equals(this.head)) {
        this.resetState();
        snake.length++;
        if (this.socket) this.socket.emit('dead');
        if (snake.socket) snake.socket.emit('kill');
      }
    }
  }

  setDirection(direction) {
    this.direction = direction;
  }

  getLocationsJson() {
    const body = this.tail.map(location => ({ x: location.x, y: location.y }));
    return {
      id: this.id,
      body: [{ x: this.head.x, y: this.head.y }, ...body]
    };
  }
}
