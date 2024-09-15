package com.example.snakegame.handler;

import com.example.snakegame.model.Direction;
import com.example.snakegame.model.Food;
import com.example.snakegame.model.Snake;
import com.example.snakegame.model.User;
import com.example.snakegame.timer.SnakeTimer;
import org.springframework.stereotype.Component;
import org.springframework.web.socket.*;
import org.springframework.web.socket.handler.TextWebSocketHandler;

import java.util.Iterator;
import java.util.List;
import java.util.Map;
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

    @SuppressWarnings("null")
    @Override
    public void afterConnectionEstablished(WebSocketSession session) throws Exception {

        // Lấy thông tin người dùng từ session
        Map<String, Object> attributes = session.getAttributes();
        User user = (User) attributes.get("user");

        if (user == null) {
            session.close(CloseStatus.NOT_ACCEPTABLE.withReason("Không xác định được người dùng"));
            return;

        }

        int id = snakeIds.incrementAndGet();
        Snake snake = new Snake(id, session,  user.getUsername());
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
        String message = String.format("{\"type\": \"join\",\"data\":[%s], \"score\": %d}", sb.toString(),
                snake.getScore());
        snakeTimer.broadcast(message);

        // Send the initial food locations to the new client
        List<Food> foods = snakeTimer.getFoods();
        StringBuilder sbFoods = new StringBuilder();
        for (int i = 0; i < foods.size(); i++) {
            Food food = foods.get(i);
            sbFoods.append(String.format("{\"x\": %d, \"y\": %d}", food.getLocation().x, food.getLocation().y));
            if (i < foods.size() - 1) {
                sbFoods.append(',');
            }
        }
        String foodMessage = String.format(
                "{\"type\": \"foods\", \"data\": [%s]}",
                sbFoods.toString());
        snake.sendMessage(foodMessage);
    }

    @SuppressWarnings("null")
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

    @SuppressWarnings("null")
    @Override
    public void afterConnectionClosed(WebSocketSession session, CloseStatus status) throws Exception {
        Snake snake = sessions.remove(session);
        if (snake != null) {
            snakeTimer.removeSnake(snake);
            String message = String.format("{\"type\": \"leave\", \"id\": %d}", snake.getId());
            snakeTimer.broadcast(message);
        }
    }

    @SuppressWarnings("null")
    @Override
    public void handleTransportError(WebSocketSession session, Throwable exception) throws Exception {
        exception.printStackTrace();
        session.close(CloseStatus.SERVER_ERROR);
    }
}