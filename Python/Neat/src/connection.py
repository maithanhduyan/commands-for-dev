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
