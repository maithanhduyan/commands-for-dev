// src/classes/Food.ts
export class Food {
    x: number;
    y: number;
    color: string;
    angle: number;

    constructor(x: number, y: number, color = '#FF0000') {
        this.x = x;
        this.y = y;
        this.color = color;
        this.angle = 0;
    }

    draw(context: CanvasRenderingContext2D, gridSize: number) {
        context.save();
        context.translate(this.x, this.y);
        context.rotate(this.angle);

        context.fillStyle = this.color;
        context.fillRect(-gridSize / 2, -gridSize / 2, gridSize, gridSize);

        context.restore();

        this.updateRotation();
    }

    updateRotation() {
        this.angle += 1;
        if (this.angle >= 360) {
            this.angle = 0;
        }
    }
}
