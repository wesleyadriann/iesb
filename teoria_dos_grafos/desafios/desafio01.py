
# -*- coding: utf-8 -*-

def MatrixInit(v, val):
    matrix = [val for i in range(0, v)]
    for i in range(0, v):
        matrix[i] = [val for i in range(0, v)]
    return matrix

def MatrixInsert(m, v, w):
    matrix = m
    v -= 1
    w -= 1
    if (matrix[v][w] == 0 and matrix[w][v] == 0):
        matrix[v][w] = 1
        matrix[w][v] = 1
    return matrix

def MatrixShow(m):
    matrix = m
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            print("{} ".format(matrix[i][j]), end='')
        print('')


A = [[1,2] , [1,3] , [2,4] , [3,4] , [4,5] , [5,6]]

matrix_adj = MatrixInit(6, 0)

for i in range(0, len(A)):
    matrix_adj = MatrixInsert(matrix_adj, A[i][0], A[i][1])

MatrixShow(matrix_adj)