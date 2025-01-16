import json
import matplotlib.pyplot as plt

def plot_evolution_from_json(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)
    generations = [d["generation"] for d in data]
    best_fitnesses = [d["best_fitness"] for d in data]
    avg_fitnesses = [d["average_fitness"] for d in data]

    plt.figure(figsize=(8,5))
    plt.plot(generations, best_fitnesses, label="Best Fitness")
    plt.plot(generations, avg_fitnesses, label="Average Fitness")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Evolution Progress over Generations")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_evolution_from_json(".//data//evolution.json")
