import sqlite3
import matplotlib.pyplot as plt

def plot_evolution_from_sqlite(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT generation, best_fitness, average_fitness FROM evolution ORDER BY generation")
    rows = cursor.fetchall()
    conn.close()

    generations = [r[0] for r in rows]
    best_fitnesses = [r[1] for r in rows]
    avg_fitnesses = [r[2] for r in rows]

    plt.figure(figsize=(8,5))
    plt.plot(generations, best_fitnesses, label="Best Fitness")
    plt.plot(generations, avg_fitnesses, label="Average Fitness")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Evolution Progress (SQLite)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_evolution_from_sqlite(".//data//evolution.db")
