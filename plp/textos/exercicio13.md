## Exercicio 13
#### [Algoritmo 1](../algoritmos/exercicio13_1.lisp) | [Algoritmo 2](../algoritmos/exercicio13_2.lisp)

1. Apresente a expressão em LISP, utilizando exclusivamente os operadores CAR e CDR, para retirar o elemento X da lista (A B (C (D E)(F X) G) H).

2. Desenvolva uma função ou um conjunto de funções em LISP que retorne o valor de ex utilizando a fórmula  
```
ex = x0/0! + x1/1! + x2/2! + x3/3! + ... + xn/n!
```
O valor de n será fornecido pelo usuário, devendo ser um valor inteiro e positivo.   
Por exemplo, caso o valor fornecido pelo usuário para n seja 4 e para x seja 2, o programa deverá apresentar como resposta o valor 7, ou seja, 20/0! + 21/1! + 22/2! + 23/3! + 24/4! .   
Caso o usuário forneça um valor inválido para n, o programa deverá apresentar como resposta o valor nil.   
