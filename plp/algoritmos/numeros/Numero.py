
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class Numero(ABC):
    def __init__(self, numero = 0):
        if(numero >= 1 and numero <= 999):
            self.__numero = "{0:0=3d}".format(numero)
        else:
            self.__numero = "{0:0=3d}".format(0)

    def setNumero(self, numero):
        if(numero >= 1 and numero <= 999):
            self.__numero = "{0:0=3d}".format(numero)
        else:
            print('Número inválido')

    def _getUnidade(self):
        return int(self.__numero[-1])

    def _getDezena(self):
        return int(self.__numero[1])

    def _getCentena(self):
        return int(self.__numero[0])

    @abstractmethod
    def extenso(self):
        pass

    @abstractmethod
    def _unidadeExtenso(self):
        pass

    @abstractmethod
    def _dezenaExtenso(self):
        pass

    @abstractmethod
    def _centenaExtenso(self):
        pass