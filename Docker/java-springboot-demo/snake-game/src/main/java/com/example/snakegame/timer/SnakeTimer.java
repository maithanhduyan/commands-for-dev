package com.example.snakegame.timer;

import com.example.snakegame.model.Food;
import com.example.snakegame.model.Snake;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

import java.util.*;
import java.util.concurrent.*;

@Component
public class SnakeTimer {

    private static final Logger log = LoggerFactory.getLogger(SnakeTimer.class);

    private static final long TICK_DELAY = 100;

    private final Map<Integer, Snake> snakes = new ConcurrentHashMap<>();

    private Food food;
    private ScheduledExecutorService scheduler;
    private ScheduledFuture<?> gameLoop;

    public SnakeTimer() {
        scheduler = Executors.newSingleThreadScheduledExecutor();
        this.food = new Food();
    }

    public synchronized void addSnake(Snake snake) {
        if (snakes.isEmpty()) {
            startTimer();
        }
        snakes.put(snake.getId(), snake);
    }

    public synchronized void removeSnake(Snake snake) {
        snakes.remove(snake.getId());
        if (snakes.isEmpty()) {
            stopTimer();
        }
    }

    public Collection<Snake> getSnakes() {
        return Collections.unmodifiableCollection(snakes.values());
    }

    private synchronized void startTimer() {
        gameLoop = scheduler.scheduleAtFixedRate(() -> {
            try {
                tick();
            } catch (Exception e) {
                log.error("Error in game loop", e);
            }
        }, TICK_DELAY, TICK_DELAY, TimeUnit.MILLISECONDS);
    }

    private synchronized void stopTimer() {
        if (gameLoop != null) {
            gameLoop.cancel(true);
        }
    }

    private void tick() {
        StringBuilder sb = new StringBuilder();
        Iterator<Snake> iterator = getSnakes().iterator();
        while (iterator.hasNext()) {
            Snake snake = iterator.next();
            snake.update(getSnakes(), food);
            sb.append(snake.getLocationsJson());
            if (iterator.hasNext()) {
                sb.append(',');
            }
        }
        // Include food location in the broadcast message
        String message = String.format(
                "{\"type\": \"update\", \"data\" : [%s], \"food\": {\"x\": %d, \"y\": %d}}",
                sb.toString(),
                food.getLocation().x,
                food.getLocation().y);

        broadcast(message);
    }

    public void broadcast(String message) {
        for (Snake snake : getSnakes()) {
            try {
                snake.sendMessage(message);
            } catch (Exception e) {
                // Ignore
            }
        }
    }

    public Food getFood() {
        return food;
    }
}