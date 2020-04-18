# Teoria dos grafos

Material e desafios da disciplina de teoria dos grafos.

## Rodando

#### Docker

```
docker build container_name .
docker run -it container_name sh
python3 nome_arquivo.py
```

#### Python 3

```
python3 nome_arquivo.py
```

## Desafios

#### Desafio 01

- Implementar uma matriz de adjacência;
- Criar uma função que inicializa a matriz;
- Reproduzir o seguinte grafo não direcionado:
- V = {1, 2, 3, 4, 5, 6}
- A = {(1,2), (1,3), (2,4), (3,4), (4,5), e (5,6)}
- Imprimir as arestas do grafo (utilizando a matriz de adjacência)

#### Desafio 02

- Implementar um vetor de listas de adjacência;
- Criar uma função que inicializa o vetor;
- Reproduzir o seguinte grafo não direcionado:
- V = {1, 2, 3, 4, 5, 6}
- A = {(1,2), (1,3), (2,4), (3,4), (4,5), e (5,6)}
- Imprimir as arestas do grafo (utilizando a lista de adjacência).

#### Desafio 03

- Implementar uma estrutura de fila;
- Criar uma função que percorra os vértices de uma matriz de adjacência, adicionando em uma fila;
- Após adicionar todos os vértices na fila, criar uma função que tire os vértices da lista até que ela fique vazia.
- Basicamente Implementar:
- QUEUEinit() – Inicializa a fila;
- QUEUEput() – Adiciona elemento;
- QUEUEget() – Recupera o 1º da fila;
- QUEUEempty() – Verifica se a fila está vazia;
- QUEUEfree() – Libera o espaço da fila na memória.

### Desafio 04

???

#### Desafio 05

- Dado um vértice inicial como parâmetro, implementar um algoritmo que realiza o cálculo da distância entre os vértices de um grafo;
- Usar a implementação do BFS como base da implementação
- Apresentar a distâncias entre os vértices do grafo direcionado abaixo:
  ![](https://raw.githubusercontent.com/WesleyAdriann/Teoria-dos-Grafos/master/images/grafo_desafio_05.png)
