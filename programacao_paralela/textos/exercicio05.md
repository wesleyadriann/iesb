## Exercicio 05
#### [Algoritmo](../algoritmos/exercicio05.c)

Utilizando como referência as técnicas de sincronização aprendidas ( barreira e exclusão mútua) faça uma nova versão    
do programa que calcula a integral que resulta em PI sem utilizar um vetor de somatorios muito menos um a matriz de somatórios.   

Utilizando a estrutura do OpenMPI faça:
- No processo 0 leia um número n inteiro positivo do usuário e atribua a uma variável de nome multiplicador.
- No processo 0 aloque um vetor com tamanho igual a quantidade de processos e preencha-os com valores aleatórios.
- Faça com que todos processos enxerguem o valor do multiplicador recebido no processo 0.
- Distribua os valores do vetor preenchido no processo 0 entre os diversos processos.
- Em cada processo calcule o produto do multiplicador pelo valor recebido do vetor.
- Agrupe os produtos de cada processo em um vetor no processo 0.
- Calcule o somatório do vetor resultante agrupado.
