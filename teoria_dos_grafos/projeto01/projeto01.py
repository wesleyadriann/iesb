
# -*- coding: utf-8 -*-

class Graph():
    def __init__(self, v):
        self.__adj = [[] for i in range(v)]
        self.__pilha = []
        self.__paths = []
        self.__visit = [-1 for i in range(v)]

    def __str__(self):
        count = 0
        stringR = "LISTA DE ADJACÊNCIA\n"
        for v in self.__adj:
            stringR += str(count) + ": "
            for i in v:
                stringR += str(i) + " "
            count += 1
            stringR += "\n"
        return stringR

    def Insert(self, v, w):
        self.__adj[v].append(w)
        self.__adj[w].append(v)

    def FindPaths(self, vinit, vfinal):
        self.__visit[vinit] = 1
        self.__pilha.append(vinit)
        for v in self.__adj[vinit]:
            if(self.__visit[v] == -1):
                self.DFS(v, vfinal)
                self.__visit[v] = -1
                self.__pilha.pop()
        smaller = self.SmallerPath()
        pathSmaller = ""
        for i in self.__paths[smaller]:
            pathSmaller += str(i) + ", "
        print(f"\nQtd. de caminhos possíveis: {len(self.__paths)}")
        print(f"Melhor caminho: {pathSmaller}")
        print(f"Peso {len(self.__paths[smaller]) -1}")
        print("Outras informações\n")
        print(self)
        print(f"Todos os caminhos \n {self.__paths}")

    def DFS(self, v, vfinal):
        self.__pilha.append(v)
        self.__visit[v] = 1
        if (v == vfinal): 
            self.AddPath()
            return
        for w in self.__adj[v]:
            if(self.__visit[w] == -1):
                self.DFS(w, vfinal)
                self.__visit[w] = -1
                self.__pilha.pop()

    def AddPath(self):
        self.__paths.append(tuple(self.__pilha))

    def SmallerPath(self):
        smaller = 666
        smallerI = 666
        for i in range(len(self.__paths)):
            if(len(self.__paths[i]) < smaller):
                smaller = len(self.__paths[i])
                smallerI = i
        return smallerI

def readFile():
    path = 'labirinto.txt'
    dataFile = open(path , "r")
    data = dataFile.read()
    dataFile.close()
    data = data.split('\n')
    vertexQtd = int(data.pop(0))
    vertexInit = int(data.pop(0))
    vertexFinal = int(data.pop(0))
    a = []
    for i in data:
        a.append((int(i[0]),int(i[2])))
    return a, vertexQtd, vertexInit, vertexFinal

print("****************************")
print("******** PROJETO 01 ********")
print("****************************")

A, vertexQtd, vertexInit, vertexFinal = readFile()

graph = Graph(vertexQtd)

for a in A:
    graph.Insert(a[0], a[1])

graph.FindPaths(vertexInit, vertexFinal)