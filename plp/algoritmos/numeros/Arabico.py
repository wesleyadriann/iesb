
# -*- coding: utf-8 -*-

from Numero import Numero

class Arabico(Numero):
    def __init__(self, numero):
        super().__init__()

    def extenso(self):
        numeroExtenso = []
        
        numeroExtenso.append(self._centenaExtenso())
        numeroExtenso.append(self._dezenaExtenso())
        numeroExtenso.append(self._unidadeExtenso())

        return ' e '.join(numeroExtenso)

    def _unidadeExtenso(self):
        dezena = super()._getDezena()
            if(dezena == 1):
                return ''

        unidade = super()._getUnidade()
        numeros = {
            0: '',
            1: 'um',
            2: 'dois',
            3: 'três',
            4: 'quatro',
            5: 'cinco',
            6: 'seis',
            7: 'sete',
            8: 'oito',
            9: 'nove'
        }

        return numeros[unidade]

    def _dezenaExtenso(self):
        dezena = super()._getDezena()
        if (dezena == 1):
            unidade = super()._getUnidade()
            numeros = {
                0: 'dez',
                1: 'onze',
                2: 'doze',
                3: 'treze',
                4: 'catorze',
                5: 'quinze',
                6: 'dezesseis',
                7: 'dezessete',
                8: 'dezoito',
                9: 'dezenove'
            }
            return numeros[unidade]
            
        numeros = {
            0: '',
            1: '',
            2: 'vinte',
            3: 'trinta',
            4: 'quarenta',
            5: 'cinquenta',
            6: 'sessenta',
            7: 'setenta',
            8: 'oitenta',
            9: 'noventa'
        }

        return numeros[dezena]

    def _centenaExtenso(self):
        centena = super()._getCentena()
        if(centena == 1):
            dezena, unidade = super()._getDezena(), super()._getUnidade()
            if(dezena == 0 and unidade == 0):
                return 'cem'
                
        numeros = {
            0: '',
            1: 'cento',
            2: 'duzentos',
            3: 'trezentos',
            4: 'quatrocentos',
            5: 'quinhentos',
            6: 'seiscentos',
            7: 'setecentos',
            8: 'oitocentos',
            9: 'novecentos'
        }

        return numeros[centena]