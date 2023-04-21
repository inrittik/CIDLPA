with open(os.path.join('dataset', 'demo', 't1.txt'), 'r') as gFile:
#         edgelist = [[int(num) for num in line.split()] for line in gFile]
#         G = nx.from_edgelist(edgelist)
# comm = [[1,2,3,4],[5,6,7,8,9],[10],[11,12,13,14,15],[16]]
# adj = nx.adjacency_matrix(G)
# print(comm, G)
# print(calculate_modularity(G, comm))