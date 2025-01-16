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
