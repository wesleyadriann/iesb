
# -*- coding: utf-8 -*-

# nind - numero de individuos da populacao
# comlim - matrix (ncrom x 2) contendo os limites superior e inferior para os cromossomos (parametros)
# ncrom - numero de cromossomos (parametros) por individuo

from random import random

class NewPop():

    def __init__(self, nind, cromlim):
        self.nind = nind
        self.cromlim = cromlim
        self.new_ṕop = [[None]*len(cromlim)]*len(nind)

    def gerar():
        ncrom = len(self.cromlim)
        for i in range(len(self.nind)):
            for j in range(ncrom):
                inf = self.cromlim[j][0]
                sup = self.cromlim[j][1]
                self.new_pop[i][j] = random() * (sup-inf) + inf
        return self.new_pop
