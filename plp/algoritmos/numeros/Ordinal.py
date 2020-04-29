
# -*- coding: utf-8 -*-

from Numero import Numero

class Ordinal(Numero):
    def __init__(self, numero):
        super().__init__(numero)

    def extenso(self):
        numeroExtenso = []
        
        numeroExtenso.append(self._centenaExtenso())
        numeroExtenso.append(self._dezenaExtenso())
        numeroExtenso.append(self._unidadeExtenso())

        while('' in numeroExtenso):
            numeroExtenso.remove('')

        print('\nNúmero ordinal')
        print(' '.join(numeroExtenso))


    def _unidadeExtenso(self):        
        unidade = super()._getUnidade()
        numeros = {
            0: '',
            1: 'primero',
            2: 'segundo',
            3: 'terceiro',
            4: 'quarto',
            5: 'quinto',
            6: 'sexto',
            7: 'sétimo',
            8: 'oitavo',
            9: 'nono'
        }

        return numeros[unidade]

    def _dezenaExtenso(self):
        dezena = super()._getDezena()
        numeros = {
            0: '',
            1: 'décimo',
            2: 'vigésimo',
            3: 'trigésimo',
            4: 'quadragésimo',
            5: 'quinquagésimo',
            6: 'sexagésimo',
            7: 'septuagésimo',
            8: 'octogésimo',
            9: 'nonagésimo'
        }

        return numeros[dezena]

    def _centenaExtenso(self):
        centena = super()._getCentena()
        numeros = {
            0: '',
            1: 'centésimo',
            2: 'ducentésimo',
            3: 'trecentésimo',
            4: 'quadringentésimo',
            5: 'quingentésimo',
            6: 'sexcentésimo',
            7: 'septingentésimo',
            8: 'octingentésimo',
            9: 'noningentésimo'
        }

        return numeros[centena]