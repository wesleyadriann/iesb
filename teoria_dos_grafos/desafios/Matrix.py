
# -*- coding: utf-8 -*-

class Digraph():
    def __init__(self, v):
        self.matrix = [[-1 for i in range(v)] for i in range(v)]

    def __str__(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                print("{} ".format(matrix[i][j]), end='')
            print('')

    def DIGRAPHInsert(self, v , w):
        if(self.matrix[v][w] == 0):
            self.matrix[v][w] = 1


class Graph():
    def __init__(self, v):
        self.matrix = [[-1 for i in range(v)] for i in range(v)]

    def __str__(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                print("{} ".format(matrix[i][j]), end='')
            print('')

    def GRAPHInsert(self, v , w):
        if(self.matrix[v][w] == 0 and self.matrix[w][v] == 0):
            self.matrix[v][w] = 1
            self.matrix[w][v] = 1

