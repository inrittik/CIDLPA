# import dataset and make graph
import os
import networkx as nx
import metric
import numpy as np

cur_path = os.path.dirname(__file__)
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
    mod = metric.modularity(G,data)
    cond = metric.conductance(G,data)
    cov = metric.calculate_coverage(G,data)
    ari = metric.calculate_ari(G,data)
    cut_ratio = metric.cut_ratio(G,data)
    return mod,cond,cov,ari,cut_ratio

def run_cidlpa(datasetName):
    new_path = os.path.join(cur_path, 'dataset', datasetName)
    return execFile(new_path)
    
run_cidlpa('oregon2')