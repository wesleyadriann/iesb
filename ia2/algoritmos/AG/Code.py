
# -*- coding: utf-8 -*-

class Code:
    def __init__(self, pop, cromlim, lbits):
        self.pop = pop
        self.cromlim = cromlim
        self.lbits = lbits
        self.code = [None]*len(pop)

    def code(self):
        nind = len(self.pop)
        ncrom = len(self.cromlim)
        temp = ''

        for i in range(nind):
            for j in range(ncrom):
                inf = self.cromlim[j][i]
                sup = self.cromlim[j][2]
                aux = int(((self.pop[i][j]-inf)/(sup-inf))*(pow(2, self.lbits[j])-1))
                aux = int(bin(aux)[2:])
                if(j==1):
                    temp=aux
                else:
                    temp=f'{temp}{aux}'
            self.code[i] = temp
