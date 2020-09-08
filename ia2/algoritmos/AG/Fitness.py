
# -*- coding: utf-8 -*-

class Fitness:
    def __init__(self, pop, ncrom):
        self.pop = pop
        self.ncrom = ncrom
        self.fitness = [None]*len(pop)

    def main(self):
        nind = len(self.pop)
        for i in range(nind):
            self.fitness[i] = self.obj_function(pop[i])

    def obj_function(self, x):
        ncrom = len(x)
        func = 10
        for i in range(ncrom):
            func = func - pow(x[i], 2)
        return func

