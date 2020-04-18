
# -*- coding: utf-8 -*-

class SubSet():
    def __init__(self, setNumbers, sumSubSet):
        self.__setNumbers = setNumbers[:]
        self.__matrix = [[False for i in range(sumSubSet)] for j in range(len(setNumbers))]
        self.__setNumbers.sort()

    @property
    def existSubSet(self):
        self.startSubSet()
        return self.__matrix[-1][-1] == True

    def startSubSet(self):
        for i, value in enumerate(self.__setNumbers):
            self.__matrix[i][0] = True
            for j in range(1, len(self.__matrix[i])):
                if(i > 0):
                    if(j >= value):
                        self.__matrix[i][j] = self.__matrix[i - 1][j] or self.__matrix[i - 1][j - value]
                    else:
                        self.__matrix[i][j] = self.__matrix[i-1][j]
                elif(self.__setNumbers[i] == j):
                    self.__matrix[i][j] = True        

    def printMatrix(self):
        for line in self.__matrix:
            print(line)
        print('\n')



if (__name__ == '__main__'):
    setA = [2,3,7,8,10]
    sumSubSetA = 11

    subset = SubSet(setA, sumSubSetA)
    print(subset.existSubSet == True and "Exists Subset")