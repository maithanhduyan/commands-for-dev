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
