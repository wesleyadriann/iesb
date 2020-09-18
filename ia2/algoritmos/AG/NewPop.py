
# -*- coding: utf-8 -*-

# nind - numero de individuos da populacao
# cromlim - matrix (ncrom x 2) contendo os limites superior e inferior para os cromossomos (parametros)
# ncrom - numero de cromossomos (parametros) por individuo

from random import randint

class NewPop():
    def __init__(self, nind, cromlim):
        self.__nind = nind
        self.__cromlim = cromlim
        self.__new_ṕop = [[None]*len(cromlim)]*nind

    @property
    def new_ṕop(self):
        return self.__new_ṕop

    def gerar(self):
        ncrom = len(self.__cromlim)
        for i in range(self.__nind):
            for j in range(ncrom):
                inf = self.__cromlim[j][0]
                sup = self.__cromlim[j][1]
                self.__new_ṕop[i][j] = randint(0, 1000) * (sup-inf) + inf
