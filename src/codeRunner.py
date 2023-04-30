# import dataset and make graph
import os
import networkx as nx
import metric
import plot
import time

cur_path = os.path.dirname(__file__)
# print(evaluate_network("../dataset/15node/15node_t0"))

# input file to read the input from
inputFile = 'input.txt'
# output file to write the output
outputFile = 'output.txt'

# execute the algorithm for the given dataset
def execFile(filename):
    file = open(os.path.join(filename, 'input.txt'),'r')
    data = file.read()
    with open(inputFile, 'w+') as filetowrite:
        filetowrite.write(data)
    start = time.time() # start time
    os.system('python algo.py') # run the algorithm
    end = time.time() # end time
    with open(outputFile, 'r') as filetoread:
        data = [[int(num) for num in line.split()] for line in filetoread]
    with open(os.path.join(filename, 't1.txt'), 'r') as gFile:
        edgelist = [[int(num) for num in line.split()] for line in gFile]
        G = nx.from_edgelist(edgelist)
    # metric measures
    mod = metric.modularity(G,data)
    cond = metric.conductance(G,data)
    cov = metric.calculate_coverage(G,data)
    ari = metric.calculate_ari(G,data)
    cut_ratio = metric.cut_ratio(G,data)
    nmi = metric.calculate_nmi(G,data)

    print("Execution Time: ",end-start)
    plot.color_communities(G,data) # plotting
    return mod,cond,cov,ari,cut_ratio,nmi

# root function to call for executing the algorithm for a given dataset
def run_cidlpa(datasetName):
    new_path = os.path.join(cur_path, 'dataset', datasetName)
    return execFile(new_path)
