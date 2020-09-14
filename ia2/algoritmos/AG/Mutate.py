
# -*- coding: utf-8 -*-

# binpop - populacao binaria para cruzamento
# Lind - comprimento da sequencia binaria de cada individuo
# mp - ponto de mutação

from random import random

class Mutate():
    def __init__(binpop):
        self.binpop = binpop
        self.mutate = binpop

    def main(pmut):
        nind = len(self.binpop)
        lind = len(self.binpop[0])

        for i in range(0, nind)
            if(random() < pmut):
                mp = random()*(lind-1)+1
                if(self.binpop[i][mp] == 0):
                    self.binpop[i][mp] = 1
                else:
                    self.binpop[i][mp] = 0
        self.mutate = self.binpop[:]
