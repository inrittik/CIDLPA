import numpy as np
import os
import networkx as nx

def calculate_modularity(adj_matrix, communities):
    m = adj_matrix.sum() / 2
    Q = 0
    for i in range(len(communities)):
        for j in range(len(communities)):
            print(communities[j])
            if i == j:
                delta = 1
            else:
                delta = 0
            ki = adj_matrix[communities[i], :].sum()
            kj = adj_matrix[communities[j], :].sum()
            eij = adj_matrix[np.ix_(communities[i], communities[j])].sum()
            aij = (ki * kj) / (2 * m)
            Q += (eij - aij * delta) / (2 * m)
    return Q
