
# -*- coding: utf-8 -*-

def main(capacidade, valores, pesos):
    pesos_valores = []
    for i in range(len(valores)):
        pesos_valores.append((pesos[i], valores[i]))

    pesos_valores_ordenanos = sorted(
        pesos_valores,
        key = lambda item: item[1]/item[0],
        reverse=True
    )

    x = [0]*len(pesos_valores_ordenanos)
    for i in range(len(pesos_valores_ordenanos)):
        if(pesos_valores_ordenanos[i][0] < capacidade):
            x[i] = pesos_valores_ordenanos[i][1]
            capacidade = capacidade - pesos_valores_ordenanos[i][0]
        else:
            x[i] = pesos_valores_ordenanos[i][1] * (capacidade/pesos_valores_ordenanos[i][0])
            capacidade = 0

    print(f'\nSolução {sum(x)}\n')

if __name__ == '__main__':

    capacidade = 50
    pesos = (40,30,20,10,20)
    valores = (840,600,400,100,300)

    if(len(valores) == len(pesos) and capacidade >= 0):
        main(capacidade, valores, pesos)


