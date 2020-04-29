
# -*- coding: utf-8 -*-

from Numero import Numero

class Romano(Numero):
    def __init__(self, numero):
        super().__init__(numero)

    def extenso(self):
        numeroExtenso = []
        
        numeroExtenso.append(self._centenaExtenso())
        numeroExtenso.append(self._dezenaExtenso())
        numeroExtenso.append(self._unidadeExtenso())

        print('\nNúmero Romano')
        print(''.join(numeroExtenso))

    def _unidadeExtenso(self):
        unidade = super()._getUnidade()

        numeros = {
            0: '',
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX'
        }

        return numeros[unidade]

    def _dezenaExtenso(self):
        dezena = super()._getDezena()

        numeros = {
            0: '',
            1: 'X',
            2: 'XX',
            3: 'XXX',
            4: 'XL',
            5: 'L',
            6: 'LX',
            7: 'LXX',
            8: 'LXXX',
            9: 'XC'
        }

        return numeros[dezena]

    def _centenaExtenso(self):
        centena = super()._getCentena()

        numeros = {
            0: '',
            1: 'C',
            2: 'CC',
            3: 'CCC',
            4: 'CD',
            5: 'D',
            6: 'DC',
            7: 'DCC',
            8: 'DCCC',
            9: 'CM'
        }

        return numeros[centena]