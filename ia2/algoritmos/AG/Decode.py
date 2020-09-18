
# -*- coding: utf-8 -*-

# pop - populacao a ser decodificada
# ncrom - numero de cromossomos (parametros) por individuo
# comlim - matrix (ncrom x 2) contendo os limites superior e inferior para os cromossomos (parametros)
# lbits - vetor ncrom contendo o numero de bits para cada cromossomo

class Decode():
    def __init__(self, binpop, cromlim, lbits):
        self.binpop = binpop
        self.cromlim = cromlim
        self.lbits = lbits
        self.__pop = [[None]*len(cromlim)]*len(binpop)

    def decode(self):
        nind = len(self.pop)
        ncrom = len(self.cromlim)
        temp = ''

        for i in range(nind):
            for j in range(ncrom):
                inf = self.cromlim[j][0]
                sup = self.cromlim[j][1]
                aux = int(self.binpop, 2)
                aux = (aux*(sup-inf))/(pow(2, self.lbits[j])-1)+inf
                self.__pop[i][j]
