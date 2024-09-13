package com.example.snakegame.handler;

import com.example.snakegame.model.Direction;
import com.example.snakegame.model.Snake;
import com.example.snakegame.timer.SnakeTimer;
import org.springframework.stereotype.Component;
import org.springframework.web.socket.*;
import org.springframework.web.socket.handler.TextWebSocketHandler;

import java.util.Iterator;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicInteger;

@Component
public class SnakeWebSocketHandler extends TextWebSocketHandler {

    private static final AtomicInteger snakeIds = new AtomicInteger(0);
    private final ConcurrentHashMap<WebSocketSession, Snake> sessions = new ConcurrentHashMap<>();

    private final SnakeTimer snakeTimer;

    public SnakeWebSocketHandler(SnakeTimer snakeTimer) {
        this.snakeTimer = snakeTimer;
    }

    @Override
    public void afterConnectionEstablished(WebSocketSession session) throws Exception {
        int id = snakeIds.incrementAndGet();
        Snake snake = new Snake(id, session);
        sessions.put(session, snake);
        snakeTimer.addSnake(snake);

        // Notify all clients about the new snake
        StringBuilder sb = new StringBuilder();
        Iterator<Snake> iterator = snakeTimer.getSnakes().iterator();
        while (iterator.hasNext()) {
            Snake s = iterator.next();
            sb.append(String.format("{\"id\": %d, \"color\": \"%s\"}", s.getId(), s.getHexColor()));
            if (iterator.hasNext()) {
                sb.append(',');
            }
        }
        String message = String.format("{\"type\": \"join\",\"data\":[%s]}", sb.toString());
        snakeTimer.broadcast(message);
    }

    @Override
    protected void handleTextMessage(WebSocketSession session, TextMessage message) throws Exception {
        String payload = message.getPayload();
        Snake snake = sessions.get(session);
        if (snake != null) {
            switch (payload) {
                case "west":
                    snake.setDirection(Direction.WEST);
                    break;
                case "north":
                    snake.setDirection(Direction.NORTH);
                    break;
                case "east":
                    snake.setDirection(Direction.EAST);
                    break;
                case "south":
                    snake.setDirection(Direction.SOUTH);
                    break;
                default:
                    break;
            }
        }
    }

    @Override
    public void afterConnectionClosed(WebSocketSession session, CloseStatus status) throws Exception {
        Snake snake = sessions.remove(session);
        if (snake != null) {
            snakeTimer.removeSnake(snake);
            String message = String.format("{\"type\": \"leave\", \"id\": %d}", snake.getId());
            snakeTimer.broadcast(message);
        }
    }

    @Override
    public void handleTransportError(WebSocketSession session, Throwable exception) throws Exception {
        exception.printStackTrace();
        session.close(CloseStatus.SERVER_ERROR);
    }
}