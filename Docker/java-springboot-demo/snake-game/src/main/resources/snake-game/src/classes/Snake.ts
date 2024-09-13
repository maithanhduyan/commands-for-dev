// src/classes/Snake.ts
export class Snake {
    snakeBody: { x: number; y: number }[];
    color: string;

    constructor(color: string) {
        this.snakeBody = [];
        this.color = color;
    }

    draw(context: CanvasRenderingContext2D, gridSize: number) {
        context.fillStyle = this.color;
        for (const segment of this.snakeBody) {
            context.fillRect(segment.x, segment.y, gridSize, gridSize);
        }
    }

    updateSnakeBody(snakeBody: { x: number; y: number }[]) {
        this.snakeBody = snakeBody;
    }
}
