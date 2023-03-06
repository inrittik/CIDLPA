# import dataset and make graph
import os
import make_graph

def take_input_file(filename):
    absolute_path = os.path.dirname(__file__)
    relative_path = filename
    full_path = os.path.join(absolute_path, relative_path)

    my_graph_t01 = make_graph.generate_graph(full_path)
    return my_graph_t01

