import sys
import networkx as nx
import random

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n, ts = map(int, input().split())

# make graph
G = nx.Graph()
G.add_nodes_from(range(n))

# data structures used
label = {}
belonging_factor = {}
each_node_strength = {}
S1 = {}
S0 = {}

# create a 3D dictionary with diagonal 1s
for i in range(ts):
    belonging_factor[i] = {}
    for j in range(n):
        belonging_factor[i][j] = {}
        for k in range(n):
            if j == k:
                belonging_factor[i][j][k] = 1
            else:
                belonging_factor[i][j][k] = 0

# print the belonging_factor dictionary
print(belonging_factor)


def strength(i, j):
    Ci = set(G.neighbors(i))
    Cj = set(G.neighbors(j))
    if(abs(len(Cj)) ==  0): return 100
    strength_ij = abs(len(Cj - Ci)) / abs(len(Cj))
    
    return strength_ij

def node_strength(x):
    strength_dict = {}
    for node in G.nodes:
        if node == x:
            strength_dict[node] = 0.0
            continue
        strength_dict[node] = strength(x, node)
    return strength_dict


for t in range(ts) : 
    
    #  no of edges in each timestamp
    m = int(input())
    
    # add each edge to the graph
    for _ in range(m) :
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        G.add_edge(x,y)
    
    # step 1 - Initialization
    # assigning a label to each node
    for i in range(n):
        label[i] = {}
        for j in range(n):
            label[i][j] = 0

    for i in range(n):
        label[i][i] = 1
                
    # print(label)

    # //////////////////////

    #step 2 - calculate s1 and s0 for each node
    for node in G.nodes :
        each_node_strength[node] = node_strength(node)
        res = 0
        for immediate_neighbors in G.neighbors(node):
            res += each_node_strength[node][immediate_neighbors]
        S1[node] = res / n
        S0[node] = 1 - S1[node]
    # print(each_node_strength)
    # print(S1)
    # print(S0)

    #step 3 - 

    # choosing a random node
    randomly_chosen_node = random.choice(list(G.nodes()))
    print(randomly_chosen_node)
    
    vote = {}

    for neighbor in G.neighbors(randomly_chosen_node):
        vote[neighbor] = S0[neighbor] * belonging_factor[t][randomly_chosen_node][neighbor] + S1[neighbor] * ((1 - belonging_factor[t][randomly_chosen_node][neighbor]) / 3)
    
    new_label = max(vote, key=lambda k: vote[k])
    print(new_label)
    
    for it in G.neighbors(randomly_chosen_node) :
        print(label[randomly_chosen_node])

    for it in G.neighbors(randomly_chosen_node) :
        label[randomly_chosen_node][it] = new_label
    
    for it in G.neighbors(randomly_chosen_node) :
        print(label[randomly_chosen_node])

    # update belonging factor of each label
    # if belonging factor is below the threshold, remove the label

    