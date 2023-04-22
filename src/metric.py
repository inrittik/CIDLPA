import numpy as np
import os
import networkx as nx

#tested
def modularity(G, communities):
    m = G.number_of_edges()
    Q = 0
    for c in communities:
        for i in c:
            for j in c:
                if i != j:
                    Aij = 1 if G.has_edge(i,j) else 0
                    ki = G.degree(i)
                    kj = G.degree(j)
                    Q += (Aij - ki*kj/(2*m))
    return Q/(2*m)


# tested
def conductance_metric(G, communities):
    conductances = []
    for community in communities:
        S = set(community)
        T = set(G.nodes()) - S
        conductance = nx.conductance(G, S, T)
        conductances.append(conductance)

    min_conductance = min(conductances)
    max_conductance = max(conductances)
    range_conductance = max_conductance - min_conductance

    if range_conductance == 0:
        normalized_conductances = conductances
    else:
        normalized_conductances = [(conductance - min_conductance) / range_conductance for conductance in conductances]

    sum = 0
    for val in normalized_conductances:
        sum += val
    return sum/len(normalized_conductances)

def conductance(G, communities):

    cut_size = 0
    volume = 0

    for community in communities:
        for i in range(len(community)):
            node_i = community[i]
            neighbors = set(G.neighbors(node_i))
            cut_size += len(neighbors.difference(community))
            volume += len(neighbors)

    if volume == 0:
        return 0

    conductance = cut_size / volume
    normalized_conductance = -1 * (conductance - 1)
    return normalized_conductance