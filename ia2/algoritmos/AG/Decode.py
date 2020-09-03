
# -*- coding: utf-8 -*-

class Decode():
    def __init__(self, binpop, cromlim, lbits):
        self.binpop = binpop
        self.cromlim = cromlim
        self.lbits = lbits
        self.code = [[None]*len(cromlim)]*len(binpop)

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
                self.decode[i][j]
