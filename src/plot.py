# Implmentation of the generalized plot function
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

import networkx as nx
import matplotlib.pyplot as plt
import random

def color_communities(G,communities):
    colors = {}
    # pos = nx.spring_layout(G, k=0.2, seed=4572321)
    pos = nx.spring_layout(G, k=0.2, iterations=80, threshold=0.0001, dim=2)
    for i, community in enumerate(communities):
        color = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))
        for node in community:
            G.add_node(node)
            colors[node] = color
        for j in range(i):
            intersection = set(communities[j]).intersection(set(community))
            if intersection:
                G.add_edges_from([(u, v) for u in community for v in communities[j] if u != v])
    nx.draw(G, with_labels=False, pos=pos,node_color=[colors[node] for node in G.nodes()])
    
    plt.show()