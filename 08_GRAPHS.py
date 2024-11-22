# Graph algorithm : BFS, DFS
from typing import Any


num_nodes1 = 5
edges1 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (1, 4), (1, 3)]
num_nodes1, len(edges1)

n = 5
edges = [(0, 1), (1, 2), (1, 3), (1, 4), (2, 3),(3, 4), (4, 0)]
m = len(edges)


# Implement by adjasent list
# class Graph:
#     def __init__(self, n_vertices, edges):
#         self.data = [[] for _ in range(n_vertices)] # for n number
#         for v1, v2 in edges:
#             self.data[v1].append(v2)
#             self.data[v2].append(v1)
#     def __repr__(self):
#         result = ''
#         for i, nodes in enumerate(self.data):
#             result = result + str(i) + ':' + str(nodes) + '\n'
#         return result
#     def __str__(self):
#         self.__repr__()    

class Graph:
    def __init__(self, num_nodes, edges):
        self.data = [[] for _ in range(num_nodes)]
        for v1, v2 in edges:
            self.data[v1].append(v2)
            self.data[v2].append(v1)
            
    def __repr__(self):
        return "\n".join(["{} : {}".format(i, neighbors) for (i, neighbors) in enumerate(self.data)])

    def __str__(self):
        return repr(self)

graph1 = Graph(n, edges)



# Implement by Adjacent Matrix
class GrappMatrix:
    def __init__(self, n_vertices, edges):
        # Initialize a matrix of all zeors
        # loop over edges
            # add a 1 in the right point
        return 1
    pass

        
print(graph1)

# For Big graph : Breadth_First Search
    
# Breadth _First_ Search

def BFS(graph, soruce):
    visited = 

