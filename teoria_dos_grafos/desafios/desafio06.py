
# -*- coding: utf-8 -*-

class Digraph():
    def __init__(self, v):
        self.adj = [[] for i in range(v)]
        self.vertexs = [i for i in range(v)]

    def DIGRAPHInsert(self, arcs):
        for arc in arcs:
            self.adj[arc[0]].append(arc[1])

    def TOPOLOGICList(self):
        finaltVertex = []
        initVertex = self.vertexs[:]
        middleVertex = []
        for i in range(self.vertexs[-1] + 1):
            if(not self.adj[i]):
                finaltVertex.append(i)
            for j in self.adj[i]:
                if(j in initVertex):
                    initVertex.remove(j)
        print(initVertex + finaltVertex)

        for initV in initVertex:
            middleVertex += self.BFS(initV)
        middleVertex = list(dict.fromkeys(middleVertex))
        print(middleVertex)

    def BFS(self, initV):
        count = 0
        QUEUE = [initV]
        visitBFS = [-1]*len(self.vertexs)
        lista = []
        while(QUEUE):
            v = QUEUE.pop(0)
            lista.append(v)
            for i in self.adj[v]:
                if(visitBFS[i] is -1):
                    visitBFS[i] = count
                    count += 1
                    QUEUE.append(i)
        return lista

V = 13
Arcs = [(0,1), (0,5), (0,6), (2,0), (2,3), (3,5), (5,4), (6,4), (6,9), (7,6), (8,7), (9,10), (9,11), (9,12), (11,12)]

digraph = Digraph(V)

digraph.DIGRAPHInsert(Arcs)

digraph.TOPOLOGICList()

