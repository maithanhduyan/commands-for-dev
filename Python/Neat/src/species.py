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
