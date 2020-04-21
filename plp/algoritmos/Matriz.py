
# -*- coding: utf-8 -*-

class Matriz():
    def __init__(self, linhas = 1, colunas = 1, **kwargs):
        self.matriz = []
        self.linhas = 1
        self.colunas = 1
        matrizPronta = kwargs.get('matriz')
        if(matrizPronta):
            self.matriz = matrizPronta
            self.linhas = len(matrizPronta)
            self.colunas = len(matrizPronta[0])
        else:
            self.matriz = self.criaMatrizLimpa(linhas, colunas)
            self.linhas = linhas
            self.colunas = colunas

    def criaMatrizLimpa(self, linhas, colunas):
        return [[0 for i in range(colunas)] for j in range(linhas)]

    def validaOrdem(self, matriz):
        try:
            if((len(matriz) == self.linhas) and (len(matriz[0]) == self.colunas)):
                return True
            print('Não é possível fazer a operação, a matriz fornecida possui ordem diferente.')
            return False
        except Exception as error:
            print('Ocorreu um erro ao validar a matriz fornecida')
            print(f'Erro {error}')

    def exibeMatriz(self):
        print('\n')
        for linha in self.matriz:
            print(linha)
        print('\n')

    def somar(self, matriz = [[]]):
        if(self.validaOrdem(matriz)):
            novaMatriz = self.matriz[:]
            for linha in range(self.linhas):
                for coluna in range(self.colunas):
                    novaMatriz[linha][coluna] = self.matriz[linha][coluna] + matriz[linha][coluna]

            self.matriz = novaMatriz[:]
            self.exibeMatriz()

    def subtrair(self, matriz = [[]]):
        if(self.validaOrdem(matriz)):
            novaMatriz = self.matriz[:]
            for linha in range(self.linhas):
                for coluna in range(self.colunas):
                    novaMatriz[linha][coluna] = self.matriz[linha][coluna] - matriz[linha][coluna]

            self.matriz = novaMatriz[:]
            self.exibeMatriz()

    def multiplicar(self, matriz = [[]]):
        try:
            if(self.linhas == len(matriz[0])):
                novaMatriz = self.criaMatrizLimpa(self.linhas, len(matriz[0]))
                for linha in range(len(novaMatriz)):
                    for coluna in range(len(novaMatriz)):
                        for i in range(self.colunas):
                            novaMatriz[linha][coluna]  = self.matriz[linha][i] * matriz[i][coluna] + novaMatriz[linha][coluna] 
                self.matriz = novaMatriz[:]
                self.exibeMatriz()
            else:
                print('Não é possível fazer a operação, a matriz fornecida possui uma ordem inválida.')
        except Exception as error:
            print('Ocorreu um erro ao realizar a operação.')
            print(f'Erro: {error}')


sampleMatriz = [[3,4,5], [6,7,8]]
matriz = Matriz(3, 2)
matriz.multiplicar(sampleMatriz)

sampleMatriz = [[2,3],[4,5],[6,7]]
matriz.somar(sampleMatriz)