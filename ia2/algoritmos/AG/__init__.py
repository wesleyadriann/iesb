
# -*- coding: utf-8 -*-

from Code import Code
# import Decode
from NewPop import NewPop

if __name__ == "__main__":
    pop_size = 3
    ncrom = 10
    cromlim = [[0, 255]]*ncrom
    pop = NewPop(pop_size, cromlim)
    pop.gerar()
    print(pop.new_ṕop)
    code = Code(pop.new_pop, cromlim, 10)
    code.code()
    print(code.binpop)
