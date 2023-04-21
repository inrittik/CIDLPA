# Header imports
import random
import sys
from collections import defaultdict
from typing import List, Tuple, Set

# Read input from file and write the output to a file
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

# input : 
# n - No of Nodes
# ts - No of timestamps
n, ts = map(int, input().split())
r = 0.5

# Data Structures Used :

# adj - adjacency list
# adj[t] : adjacency list at timestamp t
adj = [[set() for i in range(n+1)] for j in range(ts + 10)]

# edge - Edge list
# edge[t] : edge list at time t: {(1,2), (2,3)}
edge = [set() for i in range(ts + 10)]

# G[t] - Contains nodes at timestamp t
G = [set() for i in range(ts + 10)]

# Label : Dictionary containing details of labels of community to which a node belongs for a node x
# Access Method : Label[node] = {labels to which a node belong} with it's belonging factor
# "label" notice lowercase l denotes community no (like for community 1 : 0, community 2 : 1 etc)
# where as Label (Uppercase) denotes data structure as mentioned above

Label = defaultdict(dict)

# b - belonging factor
# Access Method : b[t] : b[t][node][label] = bf
# at timestamp t, denotes the belonging factor of the selected node to labels belonging (of community)
#  gives the value of belonging factor of node to that label

b = {}

# S[0] and S[1] tells the ability of node not to be affected or to be affected 
# by it's neighbour nodes respectively
S = [[0.0 for x in range(n+1)] for i in range(2)]

# Initialization of belonging factor
for i in range(ts + 10):
    b[i] = {}
    for j in range(n+1):
        b[i][j] = {}

def v_change(t1: int, t2: int) -> Set[int]:
    s = set()
    for x in G[t1]:
        if x not in G[t2]:
            s.add(x)
    return s

def find_belonging(i: int, strength: List[float]) -> None:
    sum_strength = sum(strength)
    S[1][i] = sum_strength / len(strength)
    S[0][i] = 1.0 - S[1][i]

def find_strength(i: int, j: int, t: int) -> float:
    set_div = 0
    for x in adj[t][j]:
        if x != i and x not in adj[t][i]:
            set_div += 1
    val = set_div / len(adj[t][j])
    return val

def cal_strength(x: int, neighb: List[int], t: int) -> List[float]:
    strength = []
    for i in neighb:
        val = find_strength(i, x, t)
        strength.append(val)
    return strength

def find_nodes(e: Set[Tuple[int, int]]) -> Set[int]:
    nodes = set()
    for it in e:
        x, y = it
        nodes.add(x)
        nodes.add(y)
    return nodes

def get_labels(neighb: List[int]) -> List[int]:
    labels = []
    for x in neighb:
        mx_bf = 0.0
        mx_label = x
        for l, bf in Label[x].items():
            if bf > mx_bf:
                mx_label = l
                mx_bf = bf
        labels.append(mx_label)
    return labels

def compute_vote(candidateLabels: List[int], neighb: List[int]) -> List[float]:
    vote = []
    for i in range(len(candidateLabels)):
        v = 0.0
        for j in neighb:
            sl = candidateLabels[i]
            if sl in Label[j]:
                v += S[0][j] * Label[j][sl] + S[1][j] * ((1 - Label[j][sl]) / 3.0)
        vote.append(v)
    return vote

def get_maximum_vote(vote: List[float], candidateLabels: List[int]) -> int:
    mx_vote = 0
    mx_vote_label = 0
    for j in range(len(vote)):
        if vote[j] > mx_vote:
            mx_vote = vote[j]
            mx_vote_label = candidateLabels[j]
    return mx_vote_label

def normalize(x: int, t: int) -> None:
    remove = []
    for c, bf in Label[x].items():
        new_bf = 0
        for y in adj[t][x]:
            if c in b[t][y]:
                new_bf += b[t][y][c]
        if len(adj[t][x]) == 0 :
            new_bf = 0
        else:
            new_bf /= len(adj[t][x])
        Label[x][c] = new_bf
        b[t+1][x][c] = new_bf
        if new_bf == 0.00:
            remove.append((x,c))
    for x,c in remove:
        Label[x].pop(c)
        b[t+1][x].pop(c)
    sum = 0
    for l, bf in b[t+1][x].items():
        sum += bf
    if sum == 0:
        Label[x][x] = 1
        b[t+1][x][x] = 1
    else:
        add_val = (1.00 - sum) / len(b[t+1][x])
        for l, bf in b[t+1][x].items():
            b[t+1][x][l] += add_val
            Label[x][l] = b[t+1][x][l]          
   
def remove_labels(t: int, r: float, set_changedNodes: Set[int]) -> None:
    global adj, edge, G, Label, b, S
    
    for x in set_changedNodes:
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
        
        for l in remove:
            b[t+1][x].pop(l, None)
        
        if not Label[x]:
            Label[x][mx_label] = 1.00
            b[t+1][x][mx_label] = 1.00
        else:
            val = (1.00 - sum_bf) / len(Label[x])
            for l in Label[x]:
                Label[x][l] += val
                b[t+1][x][l] += val


for t in range(ts) : 
    m = int(input())
    for i in range(m) : 
        x, y = map(int, input().split())
        edge[t].add((x,y))
        adj[t][x].add(y)
        adj[t][y].add(x)
        G[t].add(x)
        G[t].add(y)
        if(t == ts - 1) :
            edge[ts].add((x,y))
            adj[ts][x].add(y)
            adj[ts][y].add(x)
            G[ts].add(x)
            G[ts].add(y)
ts = ts + 1
v = set(G[0])
for t in range(ts) :
    # print(v)
    for element in v : 
        Label[element][element] = 1
        b[t][element][element] = 1
    if t != ts - 1:
        v = v_change(t + 1, t)

v = set(G[0])
for t in range(ts):
    for x in v:
        neighb = []
        for i in adj[t][x]:
            neighb.append(i)
        strength = cal_strength(x, neighb, t)
        find_belonging(x, strength)
    if t != ts-1:
        v = v_change(t+1, t)

e = edge[0]
set_changedNodes = find_nodes(e)

for t in range(ts):
    set_changedNodes = find_nodes(e)
    Vold = set()
    if t != ts-1:
        Vold = v_change(t, t+1)
    for x in Vold:
        set_changedNodes.discard(x)
    for it in range(ts):
        changedNodes = list(set_changedNodes)
        random.shuffle(changedNodes)

        for x in changedNodes:
            neighb = []
            for i in adj[t][x]:
                neighb.append(i)
            candidateLabels = get_labels(neighb)
            vote = compute_vote(candidateLabels, neighb)
            mx_vote_label = get_maximum_vote(vote, candidateLabels)
            if mx_vote_label not in Label[x]:
                Label[x][mx_vote_label] = 0
            normalize(x, t)

        remove_labels(t, r, set_changedNodes)

res = [set() for i in range(n+1)]
for i in range(n+1):
    for l, bf in Label[i].items():
        res[l].add(i)

comm_set = []
for i in range(n+1):
    if len(res[i]) == 0:
        continue
    s = set(res[i])
    comm_set.append(s)

communities = []
for i in range(len(comm_set)):
    is_subset = False
    for j in range(len(comm_set)):
        if i == j:
            continue
        if comm_set[i].issubset(comm_set[j]):
            is_subset = True
            break
    if not is_subset:
        communities.append(comm_set[i])

for s in communities:
    print(*s)
