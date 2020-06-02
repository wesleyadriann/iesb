## Exercicio 14
#### [Algoritmo 1](../algoritmos/exercicio15_1.lisp) | [Algoritmo 2](../algoritmos/exercicio15_2.pl)

1.  Desenvolva uma função ou um conjunto de funções em LISP que apresente o valor aproximado da raiz quadrada de um número A, por meio de n iterações, através da sequência de aproximação xn = (xn-1 + A/xn-1)/2, com x1 = 1 e n ∈ A.     
O número de iterações e o valor de  A  serão fornecidos pelo usuário, devendo ser um valor inteiro e positivo.     
Por exemplo, caso o valor fornecido pelo usuário para o número de iterações seja 5 e para A seja 3, oprograma deverá apresentar como resposta o valor 1.732050810, obtido pela sequência de valores
```
x1 = 1
x2 = (x1 + 3/x1) / 2 = 2
x3 = (x2 + 3/x2) / 2 = 1.75
x4 = (x3 + 3/x3) / 2 = 1.732142857
x5 = (x4 + 3/x4) / 2 = 1.732050810
```
Caso o usuário forneça um valor inválido para o número de iterações ou para  A, o programa deverá  presentar como resposta o valor nil.

2. Desenvolver um programa em Prolog que apresente o fatorial de um número, como no exemplo a seguir.
```prolog
?- fatorial(5, N), write(N), nl.
120
Yes.
```
