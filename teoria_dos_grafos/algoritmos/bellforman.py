
# -*- coding: utf-8 -*-

class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def BellmanFord(self, src):
        dist = [float("Inf")] * self.vertices
        dist[src] = 0
        for i in range(self.vertices - 1):
            for u, v, w in self.graph:
                if dist[u] is not float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                
        for u, v, w in self.graph:
            if dist[u] is not float("Inf") and dist[u] + w < dist[v]:
                return False

        print(dist)
        return True

print(float("Inf"))
g = Graph(5) 
g.addEdge(0, 1, -1) 
g.addEdge(0, 2, 4) 
g.addEdge(1, 2, 3) 
g.addEdge(1, 3, 2) 
g.addEdge(1, 4, 2) 
g.addEdge(3, 2, 5) 
g.addEdge(3, 1, 1) 
g.addEdge(4, 3, -3) 
  
# Print the solution 
g.BellmanFord(0) 