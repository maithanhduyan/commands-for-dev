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
