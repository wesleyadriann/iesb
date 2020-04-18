
# -*- coding: utf-8 -*-

class Digraph():
    def __init__(self, v):
        self.adj = [[] for i in range(v)]

    def DIGRAPHInsert(self, v, w):
        self.adj[v].append(w)


class Graph():
    def __init__(self, v):
        self.adj = [[] for i in range(v)]

    def GRAPHInsert(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)