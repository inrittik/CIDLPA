# implementation of the evaluation metric/metrics

import community
from sklearn.metrics import f1_score, normalized_mutual_info_score
import networkx as nx

# Metric used to evaluate the quality of the network commumites
def modularity_metric(G, comm):
    mod = community.modularity(comm, G)
    return mod

def conductance_metric(G, communities):
    conductances = []
    for community in communities.values():
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


# Metric used to evaluate the accuracy of the network commumites
def nmi_metric(G, comm):
    # Create a list of the true labels of the nodes in the network
    labels_true = [comm[node] for node in G.nodes()]

    # Partition the graph into communities using a community detection algorithm
    part = community.best_partition(G)
    labels_pred = [part[node] for node in G.nodes()]

    # Calculate the NMI score between the true labels and the predicted labels
    nmi = normalized_mutual_info_score(labels_true, labels_pred)
    return nmi


def fscore_metric(G, comm):
    ground_truth = [comm[node] for node in G.nodes()]
    f_score = f1_score(list(comm.values()), ground_truth, average='micro')
    return f_score