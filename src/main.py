# import dataset and make graph
import make_graph
import community
import metric

def evaluate_network(dataset):
    for i in range(1, 5):
        path = dataset + str(i) + ".csv"
        G = make_graph.convert_input_to_graph(path)
        part = community.best_partition(G)
        communities = {}
        for key, value in part.items():
            communities[value] = []
        for key, value in part.items():
            communities[value].append(key)
        print(metric.modularity_metric(G, part), metric.conductance_metric(G, communities), metric.fscore_metric(G,part))

print(evaluate_network("../dataset/15node/15node_t0"))
