
# -*- coding: utf-8 -*-

# binpop - populacao binaria para cruzamento
# selected - individuos selecionados da populacao
# Lind - comprimento da sequencia binaria de cada individuo
# cp - ponto de cruzamento

from random import randint

class Cross:
    def __init__(binpop, selected)
        self.binpop = binpop
        self.selected = selected
        self.lind = len(binpop)
        self.cross = [None]*self.lind

    def main():
        nind = len(self.selected)
        for i in range(nind/2):
            pai = randint(0, nind + 1)*(nind - 1) + 1
            mae = randint(0, nind + 1)*(nind - 1) + 1
            cp = randint(0, nind + 1)*(self.lind) + 1

            filho_um = pai[0:self.lind/2] + mae[0:self.lind/2]
            filho_dois = pai[self.lind/2:] + mae[self.lind/2:]

            self.cross[i] = filho_um
            self.cross[i+(nind/2)] = filho_dois

