# Projeto 02

## Finder

### BEST WAY TO FIND YOU

![](./images/finder.png)

#### O Projeto Finder

- Imagine que você está precisando, urgentemente, de um profissional que saiba configurar o certificado digital, formatar um computador, consertar a torneira da cozinha que acabara de quebrar, trocar uma telha no meio da chuva que está com goteiras...
- Seria interessante um App que pudesse buscar pessoas com expertise no assunto para lhe ajudar, não seria?!
- Estreitar e desburocratizar a relação entre quem está precisando de ajuda (cliente) e de grana (profissional)
- Claro, todo mundo tem o seu preço...
- Iremos projetar um algoritmo onde, dado alguns parâmetros pelo usuário, o algoritmo localiza pessoas que “match” com os parâmetros informados
  - Iremos usá-lo para um lado profissional... buscar desempregados que estão interessados em fazer um bico.
- O algoritmo precisa saber a localização do usuário
  - Não sabe sobre latitude e longitude? Segue os link: [[1]](https://www.youtube.com/watch?v=RxLrXbGH82A) [[2]](https://www.pilotopolicial.com.br/calculando-distancias-e-direcoes-utilizando-coordenadas-geograficas/)
  - Lat/Lon deste lab: -15.836073, -47.912019
- Cada vértice deverá ter os seguinte parâmetros:
  - Nome, latitude, longitude, profissão, disponibilidade

#### O Algoritmo

- O algoritmo deve tratar um arquivo de entrada (dados.txt) que contém dados no seguinte padrão (separados por “;”):

```
Pergentino;-15.867068,-47.761822;Programador;True
Heráclio;-7.378871,-37.189213;Programador;False
Pedrinaldino;-7.196807,-37.926007;Pistoleiro;True
Bruno Bosta;-23.571198,-46.644415;Perturbador;True
Valdemar; -26.307488,-48.841203;Dançarino;True
Zélia;-16.680895,-49.256335;Gerente;False
Harrington; 52.257689, 4.559548;Faz Tudo;True
Nigini;47.616460,-122.322166;Pintor;True
```

- OBS: Pode assumir que o usuário está no nosso laboratório
  - -15.836073, -47.912019

### Saída esperada

**Caso 1**  
_Entrada_

```

Programador, Pistoleiro, Perturbador, Faz Tudo.
```

_Saida_

```
Pedrinaldino -> Heráclio -> Bruno Bosta -> Harrington
```

**Caso 2**  
_Entrada_

```
Personal Trainer, Manicure, Advogado, Médico e Psicólogo
```

_Saida_

```
Gabi Vitoriano -> Bolinha -> Rodrigo Barros -> Yanna -> Priscila
```

### Complementando...

- Para a busca, o usuário deverá informar o raio máximo
  - Como o profissional está desempregado, o usuário vai busca-lo de carro
- E se o usuário precisar de vários profissionais?
  - Está chovendo, com goteiras no escritório, minha casa é a única da rua que está sem energia e preciso formatar meu computador pra enviar a versão do TCC ainda hoje!
- Então, nada mais inteligente do que termos um algoritmo para traçar a melhor rota para buscar os profissionais que o usuário escolher, não é!?
  - Todos os vértices estarão conectados
  - Assuma linhas retas entre os vértices
  - Grafo direcionado, rotulado e ponderado


## Rodando

#### Docker (recomendado)

```bash
docker build . -t <container_tag>
docker run -it <container_tag> sh
python3 main.py
```
<container_tag> é o nome que o container terá  

#### Python
```bash
python3 main.py
```

## Links

[Graus decimais](https://pt.wikipedia.org/wiki/Graus_decimais "Graus decimais")
