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
