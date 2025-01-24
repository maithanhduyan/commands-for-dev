# game/snake/main_snake.py

import os
import json
import sqlite3
import pygame

from src.config import Config
from src.population import Population
from src.network import Network
from .snake_game import SnakeGame

def snake_fitness_function(genome):
    """
    Chạy 1 episode game Snake (không render) để tính fitness.
    """
    game = SnakeGame(width=20, height=20, cell_size=20, max_steps=300, fps=9999)
    # fps đặt cao để "chạy ngầm" nhanh (bỏ qua hiển thị).
    net = Network(genome)

    total_reward = 0
    while not game.done:
        # Lấy state
        state = game.get_state()
        # Forward
        output = net.forward(state)  # output_size = 3
        action = output.index(max(output))  # argmax

        reward, done = game.step(action)
        total_reward += reward

    # Bonus tuỳ theo số thức ăn đã ăn
    fitness = total_reward + (game.snake.score * 50)
    game.close()
    return fitness

def run_snake_neat():
    config = Config()
    # Số input = 4 (dist_food_x, dist_food_y, dir_x, dir_y)
    # Số output = 3 (turn_left, straight, turn_right)
    input_size = 4
    output_size = 3

    population = Population(config, input_size, output_size, snake_fitness_function)

    if not os.path.exists("data"):
        os.makedirs("data")

    db_path = os.path.join("data", "evolution_snake.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS evolution_snake (
            generation INTEGER,
            best_fitness REAL,
            average_fitness REAL,
            species_count INTEGER
        )
    """)
    conn.commit()

    evolution_records = []

    for generation in range(config.max_generations):
        done, best_genome = population.evolve()

        avg_fitness = sum(g.fitness for g in population.genomes) / len(population.genomes)
        print(f"Generation: {population.generation}, "
              f"Best Fitness: {best_genome.fitness:.2f}, "
              f"Average Fitness: {avg_fitness:.2f}, "
              f"Species: {len(population.species_list)}")

        record = {
            "generation": population.generation,
            "best_fitness": best_genome.fitness,
            "average_fitness": avg_fitness,
            "species_count": len(population.species_list)
        }
        evolution_records.append(record)

        cursor.execute(
            "INSERT INTO evolution_snake VALUES (?, ?, ?, ?)",
            (population.generation, best_genome.fitness, avg_fitness, len(population.species_list))
        )
        conn.commit()

        if done:
            print("Reached target fitness. Stopping evolution.")
            break

    conn.close()

    # Ghi log ra file json
    json_path = os.path.join("data", "evolution_snake.json")
    with open(json_path, "w") as f:
        json.dump(evolution_records, f, indent=4)

    # Sau khi training xong, chạy thử best_genome với hiển thị
    test_snake_with_render(best_genome)

def test_snake_with_render(genome):
    """
    Demo chạy game Snake với hiển thị pygame,
    cho genome tốt nhất điều khiển (để xem AI chơi thế nào).
    """
    game = SnakeGame(width=20, height=20, cell_size=20, max_steps=1000, fps=15)
    net = Network(genome)

    running = True
    while running:
        # Xử lý event pygame (để thoát)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game.done:
            state = game.get_state()
            output = net.forward(state)
            action = output.index(max(output))
            reward, done = game.step(action)

        # Hiển thị
        game.render()

    game.close()

if __name__ == "__main__":
    run_snake_neat()
