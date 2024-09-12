import { GRID_SIZE } from './snakeTimer.js';
import { Direction } from './direction.js';

export default class Location {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  getAdjacentLocation(direction) {
    switch (direction) {
      case Direction.NORTH:
        return new Location(this.x, this.y - GRID_SIZE);
      case Direction.SOUTH:
        return new Location(this.x, this.y + GRID_SIZE);
      case Direction.EAST:
        return new Location(this.x + GRID_SIZE, this.y);
      case Direction.WEST:
        return new Location(this.x - GRID_SIZE, this.y);
      default:
        return this;
    }
  }
}
