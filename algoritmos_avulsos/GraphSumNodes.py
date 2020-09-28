
# -*- coding: utf-8 -*-

class Graph:
    def __init__(self):
        self.__list_adj = []

    @property
    def list_adj(self):
        return self.__list_adj

    def insert_edge(self, v1, v2, bidirected = True):
        node_index = self.find_node(v1)
        if(node_index > -1):
            if(v2 not in self.__list_adj[node_index]['edges']):
                self.__list_adj[node_index]['edges'].append(v2)
        else:
            self.__list_adj.append({
                "node": v1,
                "edges": [v2],
                "visited": False,
                "acc": 0,
            })
        if(bidirected):
            self.insert_edge(v2, v1, False)

    def find_node(self, node_f):
        for i, node in enumerate(self.__list_adj):
            if(node['node'] == node_f):
                return i
        return -1

    def show_paths(self, root = 16):
        node_index = self.find_node(root)
        self.__list_adj[node_index]["visited"] = True
        for edge in self.__list_adj[node_index]["edges"]:
            edge_index = self.find_node(edge)
            if(not self.__list_adj[edge_index]["visited"]):
                self.__list_adj[edge_index]["acc"] += self.__list_adj[edge_index]["acc"] + self.__list_adj[node_index]["node"]
                self.__list_adj[edge_index]["visited"] = True
                self.DFS(edge_index)

    def DFS(self, node_index, rec = False):
        self.__list_adj[node_index]["visited"] = True
        for edge in self.__list_adj[node_index]["edges"]:
            edge_index = self.find_node(edge)
            if(not self.__list_adj[edge_index]["visited"]):
                self.__list_adj[edge_index]["acc"] += self.__list_adj[edge_index]["acc"] + self.__list_adj[edge_index]["node"] + self.__list_adj[node_index]["node"] + self.__list_adj[node_index]["acc"]
                self.__list_adj[edge_index]["visited"] = True
                self.DFS(edge_index)

def read_file():
    path = 'graph.txt'
    dataFile = open(path , "r")
    data = dataFile.read()
    dataFile.close()
    data = data.split('\n')
    edges = []
    for edge in data:
        if(edge):
            v1, v2 = edge.split(';')
            edges.append((int(v1),int(v2)))
    return edges

if __name__ == "__main__":
    edges = read_file()
    graph = Graph()

    for v1, v2 in edges:
        graph.insert_edge(v1, v2)

    graph.show_paths()

    print(graph.list_adj)
