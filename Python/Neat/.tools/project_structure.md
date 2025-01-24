# Cấu trúc Dự án như sau:

```
├── game
│   └── snake
│       ├── __pycache__
│       │   ├── main_snake.cpython-312.pyc
│       │   └── snake_game.cpython-312.pyc
│       ├── main_snake.py
│       └── snake_game.py
├── graph
│   ├── plot_evolution.py
│   └── plot_evolution_sqlite.py
├── main.py
├── src
│   ├── __pycache__
│   │   ├── config.cpython-312.pyc
│   │   ├── connection.cpython-312.pyc
│   │   ├── genome.cpython-312.pyc
│   │   ├── network.cpython-312.pyc
│   │   ├── node.cpython-312.pyc
│   │   ├── population.cpython-312.pyc
│   │   ├── species.cpython-312.pyc
│   │   └── utils.cpython-312.pyc
│   ├── config.py
│   ├── connection.py
│   ├── genome.py
│   ├── network.py
│   ├── node.py
│   ├── population.py
│   ├── species.py
│   └── utils.py
└── test
```

# Danh sách Các Tệp Dự án:

## ../main.py

```
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

```

 ## ../game\snake\main_snake.py

```
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

```

 ## ../game\snake\snake_game.py

```
# game/snake/snake_game.py

import pygame
import random

# ---------------------------
# Các lớp hướng đối tượng
# ---------------------------

class Food:
    """
    Đại diện cho thức ăn trong game Snake.
    """
    def __init__(self, grid_width, grid_height, snake_body):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.position = self.random_position(snake_body)

    def random_position(self, snake_body):
        """
        Đặt thức ăn ở vị trí ngẫu nhiên mà không trùng với thân rắn.
        """
        while True:
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            if (x, y) not in snake_body:
                return (x, y)

    def reset(self, snake_body):
        """
        Thay đổi vị trí thức ăn (khi bị ăn).
        """
        self.position = self.random_position(snake_body)


class Snake:
    """
    Đại diện cho rắn: đầu rắn + danh sách thân (các ô).
    Hướng di chuyển (dx, dy).
    """
    def __init__(self, x, y):
        # Khởi tạo thân rắn: 1 segment
        self.body = [(x, y)]
        # Hướng mặc định: đi lên
        self.direction = (0, -1)
        self.score = 0

    def turn_left(self):
        dx, dy = self.direction
        # up (0,-1) -> left (-1,0)
        self.direction = (-dy, dx)

    def turn_right(self):
        dx, dy = self.direction
        # up (0,-1) -> right (1,0)
        self.direction = (dy, -dx)

    def move_straight(self):
        # Giữ nguyên hướng
        pass

    def move(self):
        """
        Di chuyển rắn 1 bước. Trả về (new_x, new_y) là vị trí đầu mới.
        """
        dx, dy = self.direction
        head_x, head_y = self.body[0]
        new_x = head_x + dx
        new_y = head_y + dy
        # Thêm đầu mới vào body
        self.body.insert(0, (new_x, new_y))
        return new_x, new_y

    def grow(self):
        """
        Khi ăn thức ăn, rắn sẽ không xóa đuôi => tăng chiều dài.
        """
        # Không pop đuôi => rắn dài thêm 1
        pass

    def shrink_tail(self):
        """
        Xóa đuôi (nếu không ăn).
        """
        self.body.pop()


class SnakeGame:
    """
    Lớp quản lý game Snake (màn hình pygame, logic va chạm, vẽ...).
    """
    def __init__(self, width=20, height=20, cell_size=20, max_steps=400, fps=15):
        pygame.init()

        self.width = width             # số ô ngang
        self.height = height           # số ô dọc
        self.cell_size = cell_size     # kích thước mỗi ô (pixel)
        self.max_steps = max_steps     # giới hạn bước di chuyển
        self.fps = fps

        self.screen = pygame.display.set_mode(
            (self.width * self.cell_size, self.height * self.cell_size)
        )
        pygame.display.set_caption("Snake NEAT")

        self.clock = pygame.time.Clock()

        # Reset game
        self.reset()

    def reset(self):
        # Vị trí khởi tạo rắn (giữa màn hình)
        start_x = self.width // 2
        start_y = self.height // 2

        self.snake = Snake(start_x, start_y)
        self.food = Food(self.width, self.height, self.snake.body)

        self.steps = 0
        self.done = False

    def get_state(self):
        """
        Lấy thông tin môi trường để cung cấp cho AI:
        Ở đây ví dụ 4 features: khoảng cách food, hướng snake
        """
        (food_x, food_y) = self.food.position
        (head_x, head_y) = self.snake.body[0]
        dist_food_x = (food_x - head_x) / self.width
        dist_food_y = (food_y - head_y) / self.height
        dir_x, dir_y = self.snake.direction

        return [
            dist_food_x,
            dist_food_y,
            dir_x,
            dir_y
        ]

    def step(self, action):
        """
        action = 0 (turn left), 1 (straight), 2 (turn right)
        Di chuyển rắn, kiểm tra va chạm, tính reward.
        """
        if action == 0:
            self.snake.turn_left()
        elif action == 2:
            self.snake.turn_right()
        else:
            self.snake.move_straight()

        # Di chuyển rắn
        new_x, new_y = self.snake.move()

        # Kiểm tra va tường
        if not (0 <= new_x < self.width and 0 <= new_y < self.height):
            self.done = True
            return -10, True

        # Kiểm tra va thân
        if (new_x, new_y) in self.snake.body[1:]:
            self.done = True
            return -10, True

        reward = 0
        # Kiểm tra ăn
        if (new_x, new_y) == self.food.position:
            self.snake.score += 1
            reward = 10
            self.snake.grow()  # không pop đuôi => dài thêm
            self.food.reset(self.snake.body)
        else:
            self.snake.shrink_tail()
            reward = -0.5  # mỗi bước không ăn => phạt nhẹ

        self.steps += 1
        if self.steps >= self.max_steps:
            self.done = True

        return reward, self.done

    def render(self):
        self.screen.fill((0, 0, 0))

        # Vẽ thức ăn
        food_x, food_y = self.food.position
        pygame.draw.rect(
            self.screen,
            (255, 0, 0),
            pygame.Rect(
                food_x * self.cell_size,
                food_y * self.cell_size,
                self.cell_size,
                self.cell_size
            )
        )

        # Vẽ rắn
        for (sx, sy) in self.snake.body:
            pygame.draw.rect(
                self.screen,
                (0, 255, 0),
                pygame.Rect(
                    sx * self.cell_size,
                    sy * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
            )

        pygame.display.set_caption(f"Snake NEAT | Score: {self.snake.score}")
        pygame.display.flip()
        self.clock.tick(self.fps)

    def close(self):
        pygame.quit()

```

 ## ../graph\plot_evolution.py

```
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

```

 ## ../graph\plot_evolution_sqlite.py

```
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

```

 ## ../src\config.py

```
# src/config.py

class Config:
    def __init__(self):
        # Quy mô quần thể
        self.population_size = 150
        
        # Tỷ lệ đột biến
        self.mutation_rate = 0.01
        self.mutation_rate_weight = 0.8
        self.mutation_rate_add_node = 0.03
        self.mutation_rate_add_connection = 0.05

        # Tham số lai ghép (crossover)
        self.crossover_rate = 0.75
        
        # Các tham số để tách loài (speciation)
        self.compatibility_threshold = 3.0
        self.excess_coefficient = 1.0
        self.disjoint_coefficient = 1.0
        self.weight_diff_coefficient = 0.5

        # Số thế hệ không cải thiện thì dừng
        self.stagnation_threshold = 15

        # Elitism: số cá thể hàng đầu được giữ lại mỗi loài
        self.elitism = 2

        # Các hàm kích hoạt hỗ trợ
        self.available_activations = ["sigmoid", "tanh", "relu"]
        self.default_activation = "sigmoid"

        # Mục tiêu fitness
        self.target_fitness = 0.99
        self.max_generations = 1000

```

 ## ../src\connection.py

```
# src/connection.py

class ConnectionGene:
    def __init__(self, in_node, out_node, weight, enabled=True, innovation_num=0):
        self.in_node = in_node
        self.out_node = out_node
        self.weight = weight
        self.enabled = enabled
        self.innovation_num = innovation_num

    def copy(self):
        conn_copy = ConnectionGene(
            self.in_node, 
            self.out_node, 
            self.weight, 
            self.enabled, 
            self.innovation_num
        )
        return conn_copy

```

 ## ../src\genome.py

```
# src/genome.py

import random
from .node import NodeGene
from .connection import ConnectionGene
from .utils import random_weight

class Genome:
    global_innovation_number = 0

    def __init__(self, config):
        self.config = config
        self.nodes = {}
        self.connections = {}
        self.fitness = 0.0

    def initialize_nodes(self, input_size, output_size):
        """Khởi tạo input node, output node."""
        # Tạo input nodes
        for i in range(input_size):
            node_id = i
            self.nodes[node_id] = NodeGene(node_id, "input", activation="sigmoid")

        # Tạo output nodes
        for i in range(output_size):
            node_id = input_size + i
            self.nodes[node_id] = NodeGene(node_id, "output", activation="sigmoid")

    def add_connection(self):
        """Đột biến thêm connection giữa 2 node chưa kết nối."""
        possible_pairs = []
        node_ids = list(self.nodes.keys())
        for i in range(len(node_ids)):
            for j in range(len(node_ids)):
                if i != j:
                    in_id = node_ids[i]
                    out_id = node_ids[j]
                    # Kiểm tra chưa có connection
                    if (in_id, out_id) not in self.connections:
                        possible_pairs.append((in_id, out_id))

        if not possible_pairs:
            return

        in_id, out_id = random.choice(possible_pairs)
        weight = random_weight()
        Genome.global_innovation_number += 1
        innovation_num = Genome.global_innovation_number

        self.connections[(in_id, out_id)] = ConnectionGene(
            in_id, out_id, weight, enabled=True, innovation_num=innovation_num
        )

    def add_node(self):
        """Đột biến thêm node mới. Chọn 1 connection cũ, 'chia' nó thành 2."""
        if not self.connections:
            return
        conn_key = random.choice(list(self.connections.keys()))
        connection = self.connections[conn_key]

        if not connection.enabled:
            return

        # vô hiệu hóa connection cũ
        connection.enabled = False

        # Tạo node mới
        new_node_id = len(self.nodes)  # đơn giản
        activation = random.choice(self.config.available_activations)
        self.nodes[new_node_id] = NodeGene(new_node_id, "hidden", activation=activation)

        # Tạo 2 connection mới
        Genome.global_innovation_number += 1
        in_to_new = ConnectionGene(
            connection.in_node, new_node_id, 1.0, True, Genome.global_innovation_number
        )

        Genome.global_innovation_number += 1
        new_to_out = ConnectionGene(
            new_node_id, connection.out_node, connection.weight, True, Genome.global_innovation_number
        )

        self.connections[(connection.in_node, new_node_id)] = in_to_new
        self.connections[(new_node_id, connection.out_node)] = new_to_out

    def mutate(self):
        # Đột biến trọng số
        for conn in self.connections.values():
            if random.random() < self.config.mutation_rate_weight:
                conn.weight += random.uniform(-0.5, 0.5)
                # Clip trọng số
                conn.weight = max(-10, min(conn.weight, 10))

        # Thêm node
        if random.random() < self.config.mutation_rate_add_node:
            self.add_node()

        # Thêm connection
        if random.random() < self.config.mutation_rate_add_connection:
            self.add_connection()

    @staticmethod
    def crossover(parent1, parent2, config):
        """Crossover giữa 2 genome. Giữ gene tốt hơn (hoặc ngẫu nhiên)."""
        child = Genome(config)
        # Sao chép node
        for node_id in parent1.nodes:
            child.nodes[node_id] = parent1.nodes[node_id].copy()

        # Gộp connection
        for key, conn1 in parent1.connections.items():
            if key in parent2.connections:
                conn2 = parent2.connections[key]
                # Chọn ngẫu nhiên connection
                chosen_conn = random.choice([conn1, conn2]).copy()
            else:
                chosen_conn = conn1.copy()

            if not chosen_conn.enabled:
                # Xác suất nhỏ để bật lại gene bị disable
                if random.random() < 0.25:
                    chosen_conn.enabled = True
            child.connections[key] = chosen_conn

        return child

```

 ## ../src\network.py

```
# src/network.py

from .utils import activation_function

class Network:
    def __init__(self, genome):
        self.genome = genome
        self.node_values = {}
        self.sorted_nodes = []

        # Topological sort hoặc một thứ tự xử lý để forward pass
        self._build_network()

    def _build_network(self):
        """Sắp xếp node để tính forward pass. 
           Ở đây minh họa tối giản, có thể dùng topological sort."""
        self.sorted_nodes = sorted(self.genome.nodes.keys())
        # Khởi tạo node_values
        for nid in self.sorted_nodes:
            self.node_values[nid] = 0.0

    def forward(self, inputs):
        """inputs: list đầu vào cho input nodes.
           trả về list đầu ra từ output nodes."""
        # Gán giá trị cho input node
        input_nodes = [n for n in self.genome.nodes.values() if n.type == "input"]
        for i, node in enumerate(input_nodes):
            self.node_values[node.id] = inputs[i]

        # Tính giá trị cho tất cả node theo thứ tự
        for node_id in self.sorted_nodes:
            node_gene = self.genome.nodes[node_id]
            
            # Nếu là node input, bỏ qua, vì đã set ở trên
            if node_gene.type == "input":
                continue

            # Tính tổng đầu vào
            total_input = 0.0
            for (in_id, out_id), conn in self.genome.connections.items():
                if out_id == node_id and conn.enabled:
                    total_input += self.node_values[in_id] * conn.weight

            # Kích hoạt
            self.node_values[node_id] = activation_function(node_gene.activation, total_input)

        # Lấy giá trị ở các node output
        output_nodes = [n for n in self.genome.nodes.values() if n.type == "output"]
        outputs = [self.node_values[n.id] for n in output_nodes]
        return outputs

```

 ## ../src\node.py

```
# src/node.py

class NodeGene:
    def __init__(self, node_id, node_type, activation="sigmoid"):
        """
        node_type: "input", "hidden", or "output"
        """
        self.id = node_id
        self.type = node_type
        self.activation = activation

    def copy(self):
        return NodeGene(self.id, self.type, self.activation)

```

 ## ../src\population.py

```
# src/population.py

import random
from .genome import Genome
from .species import Species
from .utils import calculate_compatibility_distance

class Population:
    def __init__(self, config, input_size, output_size, fitness_function):
        self.config = config
        self.input_size = input_size
        self.output_size = output_size
        self.fitness_function = fitness_function

        self.generation = 0
        self.species_list = []
        self.genomes = []

        # Khởi tạo quần thể
        for _ in range(config.population_size):
            g = Genome(config)
            g.initialize_nodes(input_size, output_size)
            # Kết nối sơ bộ (có thể random 1 số connection)
            for _ in range(5):  # random 1 vài connection
                g.add_connection()
            self.genomes.append(g)

    def speciate(self):
        """Phân loại genome vào species dựa trên compatibility distance."""
        self.species_list = []
        for genome in self.genomes:
            found_species = False
            for sp in self.species_list:
                distance = calculate_compatibility_distance(
                    genome, sp.representative, self.config
                )
                if distance < self.config.compatibility_threshold:
                    sp.add_member(genome)
                    found_species = True
                    break
            if not found_species:
                new_sp = Species(genome, self.config)
                new_sp.add_member(genome)
                self.species_list.append(new_sp)

    def calculate_fitness(self):
        """Tính fitness cho mỗi genome (và cập nhật fitness ở species)."""
        for genome in self.genomes:
            genome.fitness = self.fitness_function(genome)

        for sp in self.species_list:
            sp.best_fitness = max(g.fitness for g in sp.members)
            # Kiểm tra stagnation
            if sp.best_fitness > sp.representative.fitness:
                sp.stagnation_count = 0
                sp.representative = max(sp.members, key=lambda x: x.fitness)
            else:
                sp.stagnation_count += 1

    def reproduce(self):
        """Tạo ra quần thể mới từ quần thể cũ."""
        new_genomes = []

        # Loại bỏ species kém (stagnation)
        self.species_list = [sp for sp in self.species_list if sp.stagnation_count < self.config.stagnation_threshold]

        # Tính tổng fitness
        total_fitness = sum(sp.get_average_fitness() for sp in self.species_list)
        if total_fitness == 0:
            total_fitness = 1e-9  # tránh chia 0

        for sp in self.species_list:
            avg_fit = sp.get_average_fitness()
            # Số lượng con được phân bổ
            offspring_count = int((avg_fit / total_fitness) * self.config.population_size)

            # Elitism: giữ lại vài cá thể tốt nhất
            sp.members.sort(key=lambda x: x.fitness, reverse=True)
            elites = sp.members[:self.config.elitism]
            for elite in elites:
                child = Genome(self.config)
                # copy tất cả gene từ elite
                child.nodes = {k: v.copy() for k, v in elite.nodes.items()}
                child.connections = {(k): v.copy() for k, v in elite.connections.items()}
                child.fitness = elite.fitness
                new_genomes.append(child)

            # Tạo offspring
            for _ in range(offspring_count - self.config.elitism):
                parent1 = random.choice(sp.members)
                parent2 = random.choice(sp.members)
                if random.random() < self.config.crossover_rate:
                    child = Genome.crossover(parent1, parent2, self.config)
                else:
                    # copy 1
                    child = Genome(self.config)
                    child.nodes = {k: v.copy() for k, v in parent1.nodes.items()}
                    child.connections = {(k): v.copy() for k, v in parent1.connections.items()}

                # Đột biến
                child.mutate()
                new_genomes.append(child)

        # Nếu chưa đủ population_size, random thêm
        while len(new_genomes) < self.config.population_size:
            g = Genome(self.config)
            g.initialize_nodes(self.input_size, self.output_size)
            for _ in range(5):
                g.add_connection()
            new_genomes.append(g)

        self.genomes = new_genomes

    def evolve(self):
        """Tiến hóa 1 thế hệ."""
        self.speciate()
        self.calculate_fitness()
        # Kiểm tra dừng sớm nếu đã đạt ngưỡng
        best_genome = max(self.genomes, key=lambda x: x.fitness)
        if best_genome.fitness >= self.config.target_fitness:
            return True, best_genome
        
        self.reproduce()
        self.generation += 1
        return False, best_genome

```

 ## ../src\species.py

```
# src/species.py

class Species:
    def __init__(self, representative, config):
        self.config = config
        self.representative = representative  # genome đại diện
        self.members = []
        self.best_fitness = -1
        self.stagnation_count = 0

    def add_member(self, genome):
        self.members.append(genome)

    def update_representative(self):
        # Lựa chọn đại diện mới, ở đây chọn ngẫu nhiên
        if self.members:
            from random import choice
            self.representative = choice(self.members)

    def get_average_fitness(self):
        if not self.members:
            return 0
        return sum(g.fitness for g in self.members) / len(self.members)

```

 ## ../src\utils.py

```
# src/utils.py

import math
import random

def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

def safe_sigmoid(x, limit=20.0):
    if x > limit:
        return 1.0
    elif x < -limit:
        return 0.0
    else:
        return 1.0 / (1.0 + math.exp(-x))


def tanh(x):
    return math.tanh(x)

def relu(x):
    return max(0.0, x)

def activation_function(name, x):
    if name == "tanh":
        return tanh(x)
    elif name == "relu":
        return relu(x)
    else:
        # Sử dụng safe_sigmoid
        return safe_sigmoid(x, limit=20.0)

def calculate_compatibility_distance(genome1, genome2, config):
    """
    Tính độ chênh lệch giữa 2 genome để quyết định xem có cùng species hay không.
    Dựa trên các gene khác biệt (excess, disjoint) và chênh lệch trọng số.
    """
    # Giả sử ta có sẵn danh sách connection gene. 
    # Đây chỉ là ví dụ tối giản, người dùng tự hoàn thiện thêm.
    matching = 0
    weight_diff_sum = 0
    disjoint_excess = 0
    
    # Lấy ra các keys connection
    con_keys1 = set(genome1.connections.keys())
    con_keys2 = set(genome2.connections.keys())
    
    # Connection chung (matching)
    matching_keys = con_keys1.intersection(con_keys2)
    for key in matching_keys:
        matching += 1
        weight_diff_sum += abs(genome1.connections[key].weight - genome2.connections[key].weight)

    # Connection không trùng (excess + disjoint)
    disjoint_excess = (len(con_keys1 - con_keys2) + len(con_keys2 - con_keys1))

    # Tính trung bình độ chênh lệch trọng số
    if matching == 0:
        avg_weight_diff = 100  # nếu không trùng gene nào, penalty cao
    else:
        avg_weight_diff = weight_diff_sum / matching

    # Công thức NEAT: 
    # distance = c1*E/N + c2*D/N + c3*W
    # Ở đây E+D gộp chung cho disjoint_excess, chia cho N = số lượng genome cao hơn
    n = max(len(con_keys1), len(con_keys2))
    if n < 20:
        n = 1  # tránh chia nhỏ nếu quá ít gene
    distance = (config.excess_coefficient * disjoint_excess / n) + \
               (config.weight_diff_coefficient * avg_weight_diff)
    
    return distance

def random_weight():
    return random.uniform(-1.0, 1.0)

```

 