
# -*- coding: utf-8 -*-

class SubSet():
    def __init__(self, setNumbers, sumSubSet):
        self.__setNumbers = setNumbers[:]
        self.__sumSubSet = sumSubSet
        self.__setNumbers.sort()

if (__name__ == '__main__'):
    setA = [2,3,7,8,10]
    sumSubSetA = 11

    subset = SubSet(setA, sumSubSetA)
    print(subset.printAllSubsets)