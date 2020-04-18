
# -*- coding: utf-8 -*-

class Digraph():
    def __init__(self, v):
        self.v = v
        self.adj = [[] for i in range(len(v))]
        self.visitDFS = [-1 for i in range(len(v))]
        self.visitBFS = [-1 for i in range(len(v))]
        self.countDFS = 0

    def DIGRAPHInsert(self, v, w):
        self.adj[v].append(w)

    def DFS(self):
        for i in self.v:
            if self.visitDFS[i] is -1:
                self.DFSRecursivo(i)
        print(f"DFS visit: {self.visitDFS}")
            
    def DFSRecursivo(self, v):
        self.visitDFS[v] = self.countDFS
        self.countDFS += 1
        for i in self.adj[v]:
            if(self.visitDFS[i] is -1):
                self.DFSRecursivo(i)
        
    def BFS(self):
        count = 0
        QUEUE = [0]
        self.visitBFS[0] = count
        count += 1
        while(len(QUEUE) is not 0):
            v = QUEUE.pop(0)
            for i in self.adj[v]:
                if (self.visitBFS[i] == -1):
                    self.visitBFS[i] = count
                    count += 1
                    QUEUE.append(i)
        print(f"BFS visit: {self.visitBFS}")

        

V = (0, 1, 2, 3, 4, 5, 6 , 7)
A = [(0,2), (0,3), (0,4), (1,2), (1,4), (2,4), (3,4), (3,5), (4,5), (5,1), (6,7)]

digraph = Digraph(V)

for a in A:
    digraph.DIGRAPHInsert(a[0], a[1])

digraph.DFS()
digraph.BFS()
