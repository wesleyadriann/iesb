
# -*- coding: utf-8 -*-

from random import randint

class AG():
    def __init__(self, nind, cromlim):
        self.__nind = nind
        self.__cromlim = cromlim
        self.__new_pop = []

    @property
    def new_pop(self):
        return self.__new_pop

    def gerar_pop(self):
        ncrom = len(self.__cromlim)
        for i in range(self.__nind):
            individuo = []
            for j in range(ncrom):
                inf, sup = self.__cromlim[j]
                individuo.append(randint(0, 1001) * (sup-inf) + inf)
            self.__new_pop.append(individuo)
        print('População gerada com sucesso:')
        print(self.__new_pop)

    def main(self):
        self.gerar_pop()

if __name__ == "__main__":
    pop_size = 100
    ncrom = 5
    cromlim = [[0, 255]]*ncrom
    ag = AG(pop_size, cromlim)
    ag.main()
