
# -*- coding: utf-8 -*-

# nind - numero de individuos da populacao
# cromlim - matrix (ncrom x 2) contendo os limites superior e inferior para os cromossomos (parametros)
# ncrom - numero de cromossomos (parametros) por individuo

from random import randint

class NewPop():
    def __init__(self, nind, cromlim):
        self.nind = nind
        self.cromlim = cromlim
        self.new_ṕop = [[None]*len(cromlim)]*nind

    def gerar(self):
        ncrom = len(self.cromlim)
        for i in range(self.nind):
            for j in range(ncrom):
                inf = self.cromlim[j][0]
                sup = self.cromlim[j][1]
                self.new_ṕop[i][j] = randint(0, 1000) * (sup-inf) + inf
