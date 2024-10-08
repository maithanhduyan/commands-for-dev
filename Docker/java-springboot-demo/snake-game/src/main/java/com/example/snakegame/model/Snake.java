package com.example.snakegame.model;

import com.example.snakegame.util.SnakeGameUtils;
import org.springframework.web.socket.TextMessage;
import org.springframework.web.socket.WebSocketSession;

import java.io.IOException;
import java.util.ArrayDeque;
import java.util.Collection;
import java.util.Deque;
import java.util.List;

public class Snake {

    private final String username;

    private static final int DEFAULT_LENGTH = 5;

    private final int id;
    private final WebSocketSession session;

    private Direction direction;
    private int length = DEFAULT_LENGTH;
    private int score = 0; // Track player's score
    private Location head;
    private final Deque<Location> tail = new ArrayDeque<>();
    private final String hexColor;

    public Snake(int id, WebSocketSession session, String username) {
        this.id = id;
        this.session = session;
        this.username = username;
        this.hexColor = SnakeGameUtils.getRandomHexColor();
        resetState();
    }

    private void resetState() {
        this.direction = Direction.NONE;
        this.head = SnakeGameUtils.getRandomLocation();
        this.tail.clear();
        this.length = DEFAULT_LENGTH;
        this.score = 0; // Reset score when snake resets
    }

    private synchronized void kill() {
        resetState();
        sendMessage("{\"type\": \"dead\"}");
    }

    private synchronized void reward() {
        length++;
        sendMessage("{\"type\": \"kill\"}");
    }

    public synchronized void update(Collection<Snake> snakes, List<Food> foods) {
        Location nextLocation = head.getAdjacentLocation(direction);
        if (nextLocation.x >= SnakeGameUtils.PLAYFIELD_WIDTH) {
            nextLocation.x = 0;
        }
        if (nextLocation.y >= SnakeGameUtils.PLAYFIELD_HEIGHT) {
            nextLocation.y = 0;
        }
        if (nextLocation.x < 0) {
            nextLocation.x = SnakeGameUtils.PLAYFIELD_WIDTH;
        }
        if (nextLocation.y < 0) {
            nextLocation.y = SnakeGameUtils.PLAYFIELD_HEIGHT;
        }
        if (direction != Direction.NONE) {
            tail.addFirst(head);
            if (tail.size() > length) {
                tail.removeLast();
            }
            head = nextLocation;
        }

        // Check for collisions with other snakes
        handleCollisions(snakes);

        // Check for collision with any food item
        for (Food food : foods) {
            if (head.equals(food.getLocation())) {
                length++; // Increase snake's length
                score++; // Increase player's score
                food.relocate(); // Relocate the food
                sendMessage("{\"type\": \"eat\", \"score\": " + score + "}"); // Notify the client with the updated
                                                                              // score
                break; // Only one food can be eaten at a time
            }
        }
    }

    private void handleCollisions(Collection<Snake> snakes) {
        for (Snake snake : snakes) {
            boolean headCollision = id != snake.id && snake.getHead().equals(head);
            boolean tailCollision = snake.getTail().contains(head);
            if (headCollision || tailCollision) {
                kill();
                if (id != snake.id) {
                    snake.reward();
                }
            }
        }
    }

    public synchronized Location getHead() {
        return head;
    }

    public synchronized Collection<Location> getTail() {
        return tail;
    }

    public synchronized void setDirection(Direction direction) {
        this.direction = direction;
    }

    public synchronized String getLocationsJson() {
        StringBuilder sb = new StringBuilder();
        sb.append(String.format("{\"x\": %d, \"y\": %d}", head.x, head.y));
        for (Location location : tail) {
            sb.append(',');
            sb.append(String.format("{\"x\": %d, \"y\": %d}", location.x, location.y));
        }
        return String.format("{\"id\":%d,\"body\":[%s]}", id, sb.toString());
    }

    public String getUsername() {
        return username;
    }

    public int getId() {
        return id;
    }

    public String getHexColor() {
        return hexColor;
    }

    public int getScore() {
        return score;
    }

    public void sendMessage(String msg) {
        try {
            synchronized (session) {
                session.sendMessage(new TextMessage(msg));
            }
        } catch (IOException e) {
            try {
                session.close();
            } catch (IOException ex) {
                // Ignore
            }
        }
    }
}
