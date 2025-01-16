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
