
# -*- coding: utf-8 -*-

def main():
    numeros = []
    soma = 0
    numero = -1

    try:
        while(numero is not 0):
            try:
                numero = int(input('Numero '))

                if(numero > 100 or numero < -100):
                    raise Exception('Número invalido, deve estar entre -100 e 100.')

                numeros.append((pow(numero, 2)))
                soma = sum(numeros)

                print(f'Soma dos quadrados igual: {soma}')

            except BaseException:
                raise Exception('A entrada deve ser um numero inteiro.')

            except OverflowError:
                raise Exception('Soma dos valores é muito grande.')

        print(f'Soma dos quadrados igual: {soma}')

    except Exception as error:
        if(soma > 0):
            print(f'Soma dos quadrados igual: {soma}')

        print(f'{error}')

if __name__ == '__main__':
    main()
