# import dataset and make graph
import os
import csv
import networkx as nx

def generate_graph(path):
  with open(path, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    graph = nx.Graph(csvreader)
    return graph

def convert_input_to_graph(filename):
    absolute_path = os.path.dirname(__file__)
    relative_path = filename
    full_path = os.path.join(absolute_path, relative_path)
    my_graph = generate_graph(full_path)
    return my_graph

