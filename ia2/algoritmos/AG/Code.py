
# -*- coding: utf-8 -*-

# pop - populacao a ser codificada
# ncrom - numero de cromossomos (parametros) por individuo
# comlim - matrix (ncrom x 2) contendo os limites superior e inferior para os cromossomos (parametros)
# lbits - vetor ncrom contendo o numero de bits para cada cromossomo

class Code:
    def __init__(self, pop, cromlim, lbits):
        self.__pop = pop
        self.__cromlim = cromlim
        self.__lbits = lbits
        self.__binpop = [None]*len(pop)

    @property
    def binpop(self):
        return self.__binpop

    def code(self):
        nind = len(self.__pop)
        ncrom = len(self.__cromlim)
        temp = ''

        for i in range(nind):
            for j in range(ncrom):
                inf = self.__cromlim[j][0]
                sup = self.__cromlim[j][1]
                aux = int(((self.__pop[i][j]-inf)/(sup-inf))*(pow(2, self.__lbits)-1))
                aux = bin(aux)[2:]
                if(j==1):
                    temp=aux
                else:
                    temp=f'{temp}{aux}'
            self.__binpop[i] = temp
