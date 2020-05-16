
# -*- coding: utf-8 -*-

def main(distancia, individuos):
    if(distancia == 0):
        return print("\nNumero maximo de ladroes pegos: 0\n")

    policia = []
    ladrao = []

    for i in range(len(individuos)):
        if (individuos[i] == 'P'):
            policia.append(i)
        elif (individuos[i] == 'L'):
            ladrao.append(i)
        else:
            return print("Entrada Invalida")

    l, r, pegos = 0, 0, 0
    while l < len(ladrao) and r < len(policia):
        if(abs(ladrao[l] - policia[r]) <= distancia):
            pegos += 1
            l += 1
            r += 1
        elif (ladrao[l] < policia[r]):
            l += 1
        else:
            r += 1

    print(f'\nNumero maximo de ladrões pegos: {pegos}\n')

if __name__=='__main__':
    distancia = 2
    individuos = ['P', 'L', 'L', 'P', 'L']
    main(distancia, individuos)
