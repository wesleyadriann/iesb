
# -*- coding: utf-8 -*-

class Digraph:
    def __init__(self, V):
        self.adj = [[] for i in range(0, V)]

    def __str__(self):
        count = 1
        stringR = ""
        for v in self.adj:
            stringR += str(count) + ": "
            for i in v:
                stringR += str(i) + " "
            count += 1
            stringR += "\n"
        return stringR

    def Insert(self, v , w ):
        self.adj[v-1].append(w)
        self.adj[w-1].append(v)

V = [ 1 , 2 , 3 , 4 , 5 , 6 ]
A = [ (1,2) , (1,3) , (2,4) , (3,4) , (4,5) , (5,6) ]

digraph = Digraph(len(V))
for i in A:
    digraph.Insert(i[0], i[1])

print(digraph)
