# File will have a function that will be called to generate a graph from any dataset(csv file)

import csv
import networkx as nx

def generate_graph(path):
  with open(path, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    graph = nx.Graph(csvreader)
    return graph