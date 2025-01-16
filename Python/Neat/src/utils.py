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
