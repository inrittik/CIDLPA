# Demo example of how to use functions from other modules in this package
import algo

s = algo.sum(4,5)
print(s)


# import dataset and make graph
import os
import make_graph

absolute_path = os.path.dirname(__file__)
relative_path = "../dataset/demo.csv"
full_path = os.path.join(absolute_path, relative_path)

my_graph = make_graph.generate_graph(full_path)
print(my_graph)