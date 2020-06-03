## Exercicio 8
#### [Algoritmo](../algoritmos/algoritmos8/triangulo.m)

### RASTERIZAÇÃO DE SEGMENTO DE RETA EM TRÊS DIMENSÕES
Nesta atividade, você deverá escrever um algoritmo em MATLAB / Octave que realize a
rasterização de um segmento de reta – entre dois pontos cujas coordenadas são escolhidas
pelo usuário do algoritmo – no espaço tridimensional. Desta maneira, seu algoritmo deverá
receber como parâmetros de entrada as coordenadas (trios ordenados (i,j,k)) das
extremidades do segmento de reta desejado e as dimensões LxCxP (quantidade de linhas,
colunas e planos – isto é, a profundidade da cena – para rasterização do segmento) da matriz
3D contendo o segmento de reta. Esta matriz 3D deverá ser fornecida como parâmetro de
saída do algoritmo.   
Assim, os <ins>parâmetros de entrada</ins> de seu algoritmo devem ser:   
- Coordenadas (*i 0 , j 0 , k 0*) de uma extremidade do segmento;   
- Coordenadas (*i f , j f , k f*) da outra extremidade do segmento;  
- Dimensões (L, C e P) da matriz 3D em que o segmento será rasterizado.  

O <ins>único parâmetro de saída</ins> deve ser:   
- A matriz 3D (“imagem” tridimensional), de dimensões LxCxP, contendo o segmento de reta
desejado (isto é, contendo voxels – isto é, seus “pixels 3D” – iguais a 1 nas coordenadas
ocupadas pelo segmento de reta e iguais a 0 nas demais).   

Após escrever seu algoritmo, faça o seguinte procedimento:   
1. Utilize-o para a rasterização das arestas de um triângulo (escolha as coordenadas de
seus vértices de modo que suas arestas possam ser vistas em projeção paralela),
produzindo a correspondente matriz tridimensional (numa variável X);   
2. Forneça esta variável X obtida como entrada para o algoritmo de projeção paralela
(renderização por ray tracing) que você escreveu na última atividade, obtendo a
correspondente projeção numa imagem 2D, verificando a funcionalidade de seu
algoritmo de rasterização de segmento de reta e comentando os resultados.   

Repita o procedimento (itens (a) e (b) acima) para um quadrilátero e para um pentágono (não
necessariamente regulares) à sua escolha.
