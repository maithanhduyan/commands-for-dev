package com.example.snakegame.model;

import com.example.snakegame.util.SnakeGameUtils;

public class Food {

    private Location location;
    private final String color = "#FF0000"; // Red color for food

    public Food() {
        this.location = SnakeGameUtils.getRandomLocation();
    }

    public Location getLocation() {
        return location;
    }

    public synchronized void relocate() {
        this.location = SnakeGameUtils.getRandomLocation();
    }
    
    public String getColor() {
        return color;
    }
}
