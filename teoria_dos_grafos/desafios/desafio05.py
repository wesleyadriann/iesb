
# -*- coding: utf-8 -*-

class Digraph():
    def __init__(self, v):
        self.adj = [[] for i in range(v)]
        self.lengraph = v

    def DIGRAPHInsert(self, A):
        for v in A:
            self.adj[v[0]].append(v[1])

    def BFS(self, v):
        dist = ["INFINITO"]*self.lengraph
        pai = [None]*self.lengraph
        QUEUE = []
        dist[v] = 0
        pai[v] = v 
        QUEUE.append(v)
        while(len(QUEUE) is not 0):
            a = QUEUE.pop(0)
            for b in self.adj[v]:
                if(dist[b] is "INFINITO"):
                    dist[b] = dist[a] + 1
                    pai[b] = a
                    QUEUE.append(b)
        print(dist)

V = 7
A = [(0,2), (0,3), (0,4), (1,1), (1,2), (1,4), (1,6), (2,4), (3,4), (3,5), (4,5), (5,1), (5,6)]

digraph = Digraph(7)
digraph.DIGRAPHInsert(A)

digraph.BFS(4)