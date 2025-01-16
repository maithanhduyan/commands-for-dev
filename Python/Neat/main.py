# main.py

from src.config import Config
from src.population import Population
from src.network import Network
import json
import sqlite3
import math
import os

# Bài toán XOR: 2 input -> 1 output
xor_dataset = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0)
]

def xor_fitness_function(genome):
    net = Network(genome)
    error_sum = 0.0
    for inputs, target in xor_dataset:
        output = net.forward(inputs)[0]
        error_sum += (target - output) ** 2
    # Fitness = 1 / (1 + error_sum)
    return 1.0 / (1.0 + error_sum)

def run_xor_neat():
    config = Config()
    population = Population(config, 2, 1, xor_fitness_function)

    # Tạo thư mục data nếu chưa có
    if not os.path.exists("data"):
        os.makedirs("data")

    # Đường dẫn đến file .db trong thư mục data
    db_path = os.path.join("data", "evolution.db")

    # Kết nối SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Tạo bảng để lưu log tiến hoá
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS evolution (
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

        # Tính average fitness của quần thể
        avg_fitness = sum(g.fitness for g in population.genomes) / len(population.genomes)

        print(f"Generation: {population.generation}, "
              f"Best Fitness: {best_genome.fitness:.4f}, "
              f"Avg Fitness: {avg_fitness:.4f}, "
              f"Species: {len(population.species_list)}")

        # Lưu vào list (để ghi JSON)
        record = {
            "generation": population.generation,
            "best_fitness": best_genome.fitness,
            "average_fitness": avg_fitness,
            "species_count": len(population.species_list)
        }
        evolution_records.append(record)

        # Ghi log vào SQLite
        cursor.execute(
            "INSERT INTO evolution VALUES (?, ?, ?, ?)",
            (
                population.generation,
                best_genome.fitness,
                avg_fitness,
                len(population.species_list)
            )
        )
        conn.commit()

        if done:
            print("Reached target fitness. Stopping evolution.")
            break

    # Đóng kết nối SQLite
    conn.close()

    # Lưu log ra file JSON (có thể cũng đặt vào thư mục data hoặc tùy ý)
    json_path = os.path.join("data", "evolution.json")
    with open(json_path, "w") as f:
        json.dump(evolution_records, f, indent=4)

    # Kiểm thử best_genome
    best_net = Network(best_genome)
    for inputs, target in xor_dataset:
        output = best_net.forward(inputs)[0]
        print(f"Input: {inputs}, Output: {output:.4f}, Target: {target}")

if __name__ == "__main__":
    run_xor_neat()
