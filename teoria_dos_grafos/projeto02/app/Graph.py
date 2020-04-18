
# -*- coding: utf-8 -*-

class Graph():
    def __init__(self, v):
        self.adj = [[] for i in range(v)]

    def GRAPHInsert(self, v, w):
        self.adj[v['id']].append(w)