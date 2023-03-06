# Implementation of the main CIDLP algorithm
import os
import numpy as np
from collections import defaultdict
from random import shuffle

N = 10000
T = 100
adj = np.empty((T, N), dtype=object)
edge = np.empty(T, dtype=object)
G = np.empty(T, dtype=object)
Label = defaultdict(dict)
b = np.empty((T, N), dtype=object)
S = np.zeros((2, N))


def v_change(t1, t2):
    s = set()
    for x in G[t1]:
        if x not in G[t2]:
            s.add(x)
    return s

def e_change(t):
    s = set()
    for e in edge[t]:
        if e not in edge[t+1]:
            s.add(e)
    for e in edge[t+1]:
        if e not in edge[t]:
            s.add(e)
    return s

def find_strength(i, j, t):
    set_div = 0
    for x in adj[t][j]:
        if x != i and x not in adj[t][i]:
            set_div += 1
    val = set_div / len(adj[t][j])
    return val


def cal_strength(x, neighb, t):
    strength = []
    for i in neighb:
        val = find_strength(i, x, t)
        strength.append(val)
    return strength

def find_belonging(i, strength):
    sum_strength = sum(strength)
    S[1][i] = sum_strength/len(strength)
    S[0][i] = 1.00 - S[1][i]


def find_nodes(e):
    nodes = set()
    for it in e:
        x, y = it
        nodes.add(x)
        nodes.add(y)
    return nodes

def get_labels(neighb):
    labels = []
    for x in neighb:
        mx_bf = 0
        mx_label = x
        for l, bf in Label[x].items():
            if bf > mx_bf:
                mx_label = l
                mx_bf = bf
        labels.append(mx_label)
    return labels


# finds vote for each node in candidate label set
def compute_vote(candidateLabels, neighb):
    # each neighbour chooses a label and candidateLabels set and votes it

    vote = []
    for i in range(len(candidateLabels)):
        v = 0.00
        for k in range(len(neighb)):
            j = neighb[k]
            sl = candidateLabels[i]
            if sl in Label[j]:
                v += (float(S[0][j]) * Label[j][sl]) + (float(S[1][j]) * ((1 - Label[j][sl]) / 3.0))
        vote.append(v)
    return vote


def get_maximum_vote(vote, candidateLabels):
    mx_vote = 0
    mx_vote_label = 0
    for j in range(len(vote)):
        if vote[j] > mx_vote:
            mx_vote = vote[j]
            mx_vote_label = candidateLabels[j]
    return mx_vote_label


def normalize(x, t):
    remove = []
    for c, bf in Label[x].items():
        new_bf = 0
        for y in adj[t][x]:
            if c in b[t][y] and b[t][y][c] != 0:
                new_bf += b[t][y][c]
        new_bf /= len(adj[t][x])
        Label[x][c] = new_bf
        b[t+1][x][c] = new_bf
        if new_bf == 0:
            remove.append((x, c))
    for x, c in remove:
        Label[x].pop(c)
        b[t+1][x].pop(c, None)
    sum_bf = sum(bf for bf in b[t+1][x].values())
    if sum_bf == 0:
        Label[x][x] = 1
        b[t+1][x][x] = 1
    else:
        add_val = (1 - sum_bf) / len(b[t+1][x])
        for l, bf in b[t+1][x].items():
            b[t+1][x][l] += add_val
            Label[x][l] = b[t+1][x][l]


def remove_labels(t, r, set_changedNodes):
    for x in set_changedNodes:
        # Remove labels with belonging factor less than r
        remove = []
        sum_bf = 0
        mx_label = x
        mx_bf = 0
        for l, bf in Label[x].items():
            if bf < r:
                remove.append(l)
                del Label[x][l]
                del b[t+1][x][l]
                sum_bf += bf
                if bf > mx_bf:
                    mx_bf = bf
                    mx_label = l

        # If label set of node x becomes empty
        # then pick the label with max belonging factor removed, and set its bf = 1
        if not Label[x]:
            Label[x][mx_label] = 1.00
            b[t+1][x][mx_label] = 1.00
        else:
            # Add the value to belonging factor of all the labels of node x remaining
            # so that sum of bf of labels remain 1
            val = (1.00 - sum_bf) / len(Label[x])
            for l, bf in Label[x].items():
                Label[x][l] += val
                b[t+1][x][l] += val

# take input from the dataset directly

import main

g = main.take_input_file("../dataset/15node/15node_t01.csv")
print(g)
# then create a graph with that dataset by calling make_graph.generate_graph function
# try to implement all the above functions in the required format (nx.Graph)