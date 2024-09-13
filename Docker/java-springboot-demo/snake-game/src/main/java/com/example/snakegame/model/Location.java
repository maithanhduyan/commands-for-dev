package com.example.snakegame.model;

import com.example.snakegame.util.SnakeGameUtils;

import java.util.Objects;

public class Location {

    public int x;
    public int y;

    public Location(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public Location getAdjacentLocation(Direction direction) {
        switch (direction) {
            case NORTH:
                return new Location(x, y - SnakeGameUtils.GRID_SIZE);
            case SOUTH:
                return new Location(x, y + SnakeGameUtils.GRID_SIZE);
            case EAST:
                return new Location(x + SnakeGameUtils.GRID_SIZE, y);
            case WEST:
                return new Location(x - SnakeGameUtils.GRID_SIZE, y);
            case NONE:
            default:
                return this;
        }
    }

    @Override
    public boolean equals(Object o) {
        if (this == o)
            return true;
        if (o == null || getClass() != o.getClass())
            return false;

        Location location = (Location) o;

        return x == location.x && y == location.y;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }
}