# import dataset and make graph
import make_graph
import community
import metric
import os
import networkx as nx
import os

cur_path = os.path.dirname(__file__)

def evaluate_network(dataset:str):
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

# print(evaluate_network("../dataset/15node/15node_t0"))

inputFile = 'input.txt'
outputFile = 'output.txt'
def execFile(filename):
    file = open(os.path.join(filename, 'input.txt'),'r')
    data = file.read()
    with open(inputFile, 'w+') as filetowrite:
        filetowrite.write(data)
    os.system('python algo.py')
    with open(outputFile, 'r') as filetoread:
        data = [[int(num) for num in line.split()] for line in filetoread]
    with open(os.path.join(filename, 't1.txt'), 'r') as gFile:
        edgelist = [[int(num) for num in line.split()] for line in gFile]
        G = nx.from_edgelist(edgelist)
        print(G)

new_path = os.path.join(cur_path, 'dataset', 'demo')
execFile(new_path)
    