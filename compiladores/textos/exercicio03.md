## Exercicio 03
#### [Algoritmo](../algoritmos/exercicio03.py)

Apresente a implementação da Análise Recursiva Preditiva sobre a gramática a seguir.
```
G = ({E, T, F}, {x, &, v, ~, (, )}, P, E)
P = {E → EvT | T
     T → T&F | F
     F → (E) | ~F | x}
```


#### **Ajustes da gramatica para solução**


1. Eliminação da recursividade à esquerda: 

- Renomeação das variáveis

```
G = ({A, B, C}, {x, &, v, ~, (, )}, P, A)
P = {A → AvB | B
    B → B&C | C
    C → (A) | ~C | x}
```    
- Exclusão das recursões à esquerda direta:

```
G = ({A, B, C}, {x, &, v, ~, (, )}, P, A)
P = {A → BD
    B → CE
    C → (A) | ~C | x
    D → vBD | ε
    E → &CE | ε
    }
```

Conjunto FIRST(α):
```
FIRST(A) = {(, ~, x}
FIRST(B) = {(, ~, x}
FIRST(C) = {(, ~, x}
FIRST(D) = {v, ε}
FIRST(E) = {&, ε}
```
Conjunto FOLLOW(A):
```
FOLLOW(A) = {$, )}
FOLLOW(B) = {v, $, )}
FOLLOW(C) = {$, &, v, )}
FOLLOW(D) = {$, )}
FOLLOW(E) = {v, $, )}
```
