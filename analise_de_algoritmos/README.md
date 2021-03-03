Analise de Algoritmos - 1/2020
===

## Rodando

#### Docker (recomendado)
```bash
docker build . -t <container_tag>
docker run -it <container_tag> sh
```
##### Python
```
python3 <file_name>.py
```
##### C
```
./build.sh <file_name>.c <file_name_out>
```

<container_tag> é o nome que o container terá.  
<file_name> é o nome do arquivo.  
<file_name_out> é o nome do arquivo após compilado.  

#### Sem Docker

##### Python
```
python3 <file_name>.py
```
##### C
```
./build.sh <file_name>.c <file_name_out>
```
<file_name> é o nome do arquivo.  
<file_name_out> é o nome do arquivo após compilado.  


## Exercicios

- **[Exercicio 01](./textos/exercicio01.md)**  | [Algoritmo](./algoritmos/python/exercicio01.py)
- **[Exercicio 02](./textos/exercicio02.md)**  | [Algoritmo](./algoritmos/python/exercicio02.py)
- **[Karatsuba Ofman](./textos/karatsuba_ofman.md)** | [Algoritmo](./algoritmos/c/karatsuba_ofman.c)

## Trabalhos

- **[Trabalho 01](./textos/trabalho1.md)**  | [Algoritmo 1](./algoritmos/python/subsetSUMBk.py) | [Algoritmo 2](./algoritmos/python/subsetSUMDynamic.py) | [Algoritmo 3](./algoritmos/python/subsetSUMRecursive.py)
