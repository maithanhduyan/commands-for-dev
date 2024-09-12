import express from 'express';
import { createServer } from 'http';
import { Server } from 'socket.io';
import SnakeTimer from './snakeTimer.js';

const app = express();
const server = createServer(app);
const io = new Server(server);

// Serve static files (HTML, JS, CSS) from public folder
app.use(express.static('public'));

// WebSocket connection
io.on('connection', (socket) => {
    console.log('A user connected');
    const snake = SnakeTimer.addSnake(socket);

    socket.on('move', (direction) => {
        snake.setDirection(direction);
        console.log(`direction:${direction}`);
    });

    socket.on('disconnect', () => {
        SnakeTimer.removeSnake(snake);
        console.log('User disconnected');
    });

    socket.on('error', (error) => {
        console.log('WebSocket error:', error);
    });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
