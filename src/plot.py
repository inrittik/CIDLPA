# Implmentation of the generalized plot function
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def plot_comm( communities_list: list[list[int]], graph: nx.Graph()):

    communities={}
    for i, community in enumerate(communities_list):
        communities[i] = community


    # set of distinct colors
    node_color = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff'] 
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.tight_layout()
    pos = nx.spring_layout(graph, k=0.2, seed=4572321)
    n = graph.number_of_nodes()
    color = ['#ffffff' for i in range(n) ]
    
    # assigning each node color of it's community
    t=0
    vis = {}
    for com in range(len(communities)) :
        for nodes in communities[com]:
            if color[nodes] == '#ffffff':
                color[nodes] = node_color[t]
            elif nodes not in vis:
                color[nodes] = '#000000'
                vis[nodes] = True
        t=t+1
   
    # plotting colored graph using networkx library
    nx.draw_networkx(
        graph,
        ax = ax,
        pos = pos,
        with_labels = True,
        node_color = color,
        node_size = 500,
        edge_color = "#adadad",
        alpha = 0.5,
        font_weight = "bold",
    )
    ax.set_title("Plotting of Communities")
    plt.show()
    
    return graph
