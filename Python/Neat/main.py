# main.py

from src.config import Config
from src.population import Population
from src.network import Network
import math

# Bài toán XOR: 2 input -> 1 output
xor_dataset = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0)
]

def xor_fitness_function(genome):
    # Xây network từ genome
    net = Network(genome)
    error_sum = 0.0
    for inputs, target in xor_dataset:
        output = net.forward(inputs)[0]
        error_sum += (target - output) ** 2
    # Dùng MSE -> muốn minimize error -> fitness = 1 / (1 + error_sum)
    return 1.0 / (1.0 + error_sum)

def run_xor_neat():
    config = Config()
    # 2 input node, 1 output node
    population = Population(config, 2, 1, xor_fitness_function)

    for generation in range(config.max_generations):
        done, best_genome = population.evolve()
        print(f"Generation: {population.generation}, Best Fitness: {best_genome.fitness:.4f}")
        if done:
            print("Reached target fitness. Stopping evolution.")
            break

    # Test thử best_genome
    best_net = Network(best_genome)
    for inputs, target in xor_dataset:
        output = best_net.forward(inputs)[0]
        print(f"Input: {inputs}, Output: {output:.4f}, Target: {target}")

if __name__ == "__main__":
    run_xor_neat()
