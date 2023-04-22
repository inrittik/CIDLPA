import numpy as np
import os
import networkx as nx
from sklearn import metrics

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
def conductance(G, communities):
   
    cut_size = 0
    volume = 0

    for community in communities:
        for node_i in community:
            if node_i not in G:
                continue
            neighbors = set(G.neighbors(node_i))
            cut_size += len(neighbors.difference(community))
            volume += len(neighbors)

    if volume == 0:
        return 0

    conductance = cut_size / volume
    normalized_conductance = -1 * (conductance - 1)
    return normalized_conductance



#tested
def calculate_coverage(graph, communities):
   
    # Calculate the number of edges in the graph
    num_edges = graph.number_of_edges()

    # Calculate the number of edges within the communities
    intra_community_edges = 0
    for community in communities:
        intra_community_edges += graph.subgraph(community).number_of_edges()

    # Calculate the coverage
    coverage = intra_community_edges / num_edges if num_edges > 0 else 0

    # Normalize the coverage to be between 0 and 1
    coverage = max(0, min(1, coverage))

    return coverage




def calculate_ari(graph, communities):
   
    # create a dictionary to map nodes to their corresponding community labels
    node2comm = {}
    for i, comm in enumerate(communities):
        for node in comm:
            node2comm[node] = i

    # generate the label lists
    true_labels = []
    predicted_labels = []
    for edge in graph.edges():
        if edge[0] in node2comm and edge[1] in node2comm:
            true_labels.append(node2comm[edge[0]])
            predicted_labels.append(node2comm[edge[1]])

    # calculate the Adjusted Rand Index (ARI) score
    ari_score = metrics.adjusted_rand_score(true_labels, predicted_labels)

    return ari_score




import networkx as nx

def cut_ratio(graph, communities):
    # Create a dictionary mapping nodes to their community IDs
    community_dict = {}
    for i, community in enumerate(communities):
        for node in community:
            community_dict[node] = i
    
    # Calculate the total number of edges and the number of cut edges
    total_edges = graph.number_of_edges()
    cut_edges = 0
    for edge in graph.edges():
        if edge[0] in community_dict and edge[1] in community_dict:
            if community_dict[edge[0]] != community_dict[edge[1]]:
                cut_edges += 1
    
    # Calculate and return the cut ratio
    return cut_edges / total_edges
