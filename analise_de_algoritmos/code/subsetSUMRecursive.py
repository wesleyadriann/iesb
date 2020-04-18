
# -*- coding: utf-8 -*-

class SubSet():
    def __init__(self, setNumbers, sumSubSet):
        self.__setNumbers = setNumbers[:]
        self.__sumSubSet = sumSubSet
        self.__setNumbers.sort()

    @property
    def existSubSet(self):
        return self.startSubSet(self.__sumSubSet) == True

    def subSetRec(self, sumSubSet, index = 0):
        if(sumSubSet == 0):
            return False

        if(len(self.__setNumbers) - index == 1):
            if(self.__setNumbers[0] == sumSubSet):
                return True
            return False

        return self.subSetRec(sumSubSet - self.__setNumbers[index] , index + 1) or self.subSetRec(sumSubSet ,index + 1)

    def startAllSubSet(self):
        pass

    def allSubSetRec(self, setNumbers,  sets = []):
        pass
    


if (__name__ == '__main__'):
    setA = [2,3,7,8,10]
    sumSubSetA = 11

    subset = SubSet(setA, sumSubSetA)
        print(subset.existSubSet == True and "Exists Subset")