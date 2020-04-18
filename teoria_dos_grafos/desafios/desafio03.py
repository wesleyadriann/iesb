
# -*- coding: utf-8 -*-

class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def QUEUEput(self, x):
        self.queue.append(x)

    def QUEUEget(self):
        return self.queue.pop(0)

    def QUEUEempty(self):
        if(len(self.queue) == 0):
            return True
        return False

    def QUEUEfree(self):
        del self.queue

    def QUEUEmatrix(self, matrix):
        print("Adicionando")
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if(matrix[i][j] == 1):
                    print(self)
                    self.QUEUEput((i, j))
        print(self)

    def QUEUEclear(self):
        print("Limpando")
        while(not self.QUEUEempty()):
            print(self)
            self.QUEUEget()
        print(self)


class DiGraph:
    def __init__(self, v):
        self.matrix = [[0 for i in range(v)] for i in range(v)]

    def GraphInsert(self, v , w):
        if(self.matrix[v][w] == 0):
            self.matrix[v][w] = 1

M = [(0,1) , (1,2) , (1,3) , (2,4) , (3,4) , (4,5) , (5,6)]

digraph = DiGraph(len(M))

for i in range(len(M)):
    digraph.GraphInsert(M[i][0], M[i][1])

fila = Queue()
fila.QUEUEmatrix(digraph.matrix)
fila.QUEUEclear()
