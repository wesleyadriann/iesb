
# -*- coding: utf-8 -*-

class DigraphDFS():
    def __init__(self, v):
        self.v = v
        self.adj = [[] for i in range(len(v) + 1)]
        self.visited_DFS = [False for i in range(len(v) + 1)]
        self.visitation_order = []
        self.with_cycle = False

    def insert_edge(self, v, w):
        self.adj[v].append(w)

    def DFS(self):
        for i in self.v:
            if self.visited_DFS[i] == False:
                self.visitation_order.append(f'{i}')
                self.recursion(i)
        print(f"DFS: {', '.join(self.visitation_order)}")

    def recursion(self, v):
        self.visited_DFS[v] = True
        for i in self.adj[v]:
            if(self.visited_DFS[i]):
                self.with_cycle = True
            else:
                self.visitation_order.append(f'{i}')
                self.recursion(i)

    def cycle(self):
        if(self.with_cycle):
            print('Há ciclos nesse grafo.')
        else:
             print('Não ciclos nesse grafo.')



def read_file():
    path = 'graph.csv'
    dataFile = open(path , "r")
    data = dataFile.read()
    dataFile.close()
    data = data.split('\n')
    edges = []
    for edge in data:
        if(edge):
            v1, v2 = edge.split(';')
            edges.append((int(v1),int(v2)))
    return edges

if __name__ == "__main__":
    edges = read_file()

    vertex = []
    for v1, v2 in edges:
        if(not v1 in vertex):
            vertex.append(v1)
        if(not v2 in vertex):
            vertex.append(v2)

    graph = DigraphDFS(vertex)

    for v1, v2 in edges:
        graph.insert_edge(v1, v2)

    graph.DFS()
    graph.cycle()

