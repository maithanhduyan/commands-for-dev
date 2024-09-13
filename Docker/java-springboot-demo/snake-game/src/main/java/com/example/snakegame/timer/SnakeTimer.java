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

    // Change to a list to hold multiple Food items
    private final List<Food> foods = new ArrayList<>();

    private static final int NUM_FOOD_ITEMS = 5; // Number of food items

    private ScheduledExecutorService scheduler;
    private ScheduledFuture<?> gameLoop;

    public SnakeTimer() {
        scheduler = Executors.newSingleThreadScheduledExecutor();

        // Initialize multiple food items
        for (int i = 0; i < NUM_FOOD_ITEMS; i++) {
            foods.add(new Food());
        }
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
        StringBuilder sbSnakes = new StringBuilder();
        Iterator<Snake> iterator = getSnakes().iterator();
        while (iterator.hasNext()) {
            Snake snake = iterator.next();
            snake.update(getSnakes(), foods);
            sbSnakes.append(snake.getLocationsJson());
            if (iterator.hasNext()) {
                sbSnakes.append(',');
            }
        }
        // Prepare food data
        StringBuilder sbFoods = new StringBuilder();
        for (int i = 0; i < foods.size(); i++) {
            Food food = foods.get(i);
            sbFoods.append(String.format("{\"x\": %d, \"y\": %d}", food.getLocation().x, food.getLocation().y));
            if (i < foods.size() - 1) {
                sbFoods.append(',');
            }
        }

        // Include foods in the broadcast message
        String message = String.format(
                "{\"type\": \"update\", \"data\" : [%s], \"foods\": [%s]}",
                sbSnakes.toString(),
                sbFoods.toString());

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

    public List<Food> getFoods() {
        return Collections.unmodifiableList(foods);
    }
}
