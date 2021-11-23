# ATIVIDADE PRÁTICA nº 03

#### Wesley Adriann - 1822130040


## FILTROS E APLICAÇÕES

### Filtro de Mediana e Ruído Sal & Pimenta

#### Ruído Sal & Pimenta
O Sal & Pimenta consiste é ruído do tipo impulsivo, onde dois níveis distintos de frequência degradam a imagem. No caso essa frequência se apresenta como pontos brancos e pretos na imagem.

#### Filtro de Mediana
O filtro de mediana, consiste em fazer a varredura pela imagem, onde é definido uma janela de pixeis a serem analisados, assim pixel a pixel e analisado ele e os vizinhos de acordo com a janela, e pegando a mediana dos valores e inserindo no local do pixel atual. Devivo a esse processo valores extremos, que é o caso do ruído sal e pimenta, tendem a ser eliminados da imagem apos a aplicação do filtro.


#### Filtro de Média
O filtro de média, segue o mesmo princípio da varredura do filtro de mediana, porem aqui, aplicamos a média da janela estabelecida. Assim, pode também solucionar o problema de imagens com ruído de sal e pimenta, porem dependo da proporção do ruído, ele pode pesar muito ao efetuar a média, e acabar fazendo alterações na cor da imagem.

#### Algoritmo

```m
% -----
% Parte 1
% Filtro de media e mediana
% -----

pkg load image

"parte 1 iniciada"
imagem_original = imread('./imagem_base.jpg');

ruido = 0.05;

imagem_base = double(rgb2gray(imagem_original))/255;
imagem_ruidosa = imnoise(imagem_base,  'salt & pepper', ruido);

ordem = 3;

"media"
mascara_media = ones(ordem, ordem);
mascara_media = mascara_media.*(1/(ordem*ordem));

imagem_media = conv2(imagem_ruidosa, mascara_media, 'same');

"mediana"
imagem_mediana = filtro_mediana(imagem_ruidosa, ordem);

"snr"
snr_conv2 = snr(imagem_base, imagem_media)
snr_mediana = snr(imagem_base, imagem_mediana)
```

Aqui temos o algoritmo principal, onde é feito o carregamento da imagem, juntamente com a conversão para escala de cinza e a aplicação do filtro sal & pimenta. É definito pela variável 'ruido', a porcentagem de ruido sal e pimenta que será aplicada na imagem, e também definito o tamanho da janela pela variável 'ordem'.  

Para o filtro de média, foi utilizada a função nativa do octave, 'conv2' passando a mascara de acordo com oque é definito na variável 'ordem'. E para o filtro de mediana foi construído um algoritmo para fazer a aplicação.

```m
function nova_imagem = filtro_mediana(imagem, ordem)

    [largura_imagem, altura_imagem] = size(imagem);
    imagem_mediana = zeros(largura_imagem, altura_imagem);

    for linha = 1:altura_imagem
        for coluna = 1:largura_imagem
            sub_matriz_ordem = sub_matriz(imagem, linha, coluna, ordem);
            mediana = median(sub_matriz_ordem(:));
            imagem_mediana(linha, coluna) = mediana;
        end
    end
    "filtro de mediana completo"

nova_imagem = imagem_mediana;
``` 

Aqui é feito a iteração pelos pixeis da imagem e calculada a mediana. Também foi desenvolvido uma função auxiliar para pegar os vizinhos do pixel atual de acordo com a variável 'ordem' definido no início


```m
function sub = sub_matriz(imagem, linha, coluna, ordem)
    matriz = zeros(ordem, ordem);
    range_vizinho = fix(ordem/2);
    i = 0;
    for linha_i = (linha-range_vizinho):(linha+range_vizinho)
        i++;
        j = 0;
        for coluna_j = (coluna-range_vizinho):(coluna+range_vizinho)
            j++;
            try
                matriz(i,j) = imagem(linha_i,coluna_j);
            catch
            end
        end
    end
sub = matriz;
```
Para evitar que o laço de repetição pare onde os vizinhos do pixel ultrapassa os limites da matriz, foi inserido um bloco de try catch, assim não tendo a necessidade de inicialmente ampliar o tamanho da imagem original para evitar o problema.  

E por fim temos a função para calcular o ganho de SNR da imagem


```m
function snr_resultado = snr(imagem_perfeita, imagem_ruidosa)
    [largura, altura] = size(imagem_perfeita);

    erro_relativo = 0;
    a = 0;
    b = 0;
    for linha = 1:altura
        for coluna = 1:largura
            a = a + power(imagem_perfeita(linha, coluna) - imagem_ruidosa(linha, coluna), 2);
            b = b + power(imagem_perfeita(linha, coluna), 2);
        end
    end
    erro_relativo = a/b;
    snr_calc = 10 * log10(1/erro_relativo);
    "snr completo"

snr_resultado = snr_calc;
```

#### Resultados

<p align="center">
  <img src="./images/doge.jpg" width="200px"><br/>
  imagem original
</p>

<p align="center">
  <img src="./images/doge_rgb2gray.jpg" width="200px"><br/>
  imagem pos escala de cinza
</p>

Imagem com ruido sal e pimenta com porcentagem de 0,05; 0,1; 0,15; e 0,2.
<p align="center">
  <img src="./images/doge_sal_005.jpg" width="200px">
  <img src="./images/doge_sal_01.jpg" width="200px"><br/>
  <img src="./images/doge_sal_015.jpg" width="200px">
  <img src="./images/doge_sal_020.jpg" width="200px">
</p>

##### Testes mediana

Imagem apos filtro de mediana com ordem 3 e ruido sal e pimenta com porcentagem de 0,05; 0,1; 0,15; e 0,2.
<p align="center">
  <img src="./images/doge_mediana3_sal_005.jpg" width="200px">
  <img src="./images/doge_mediana3_sal_01.jpg" width="200px"><br/>
  <img src="./images/doge_mediana3_sal_015.jpg" width="200px">
  <img src="./images/doge_mediana3_sal_020.jpg" width="200px">
</p>

Imagem apos filtro de mediana com ordem 5 e ruido sal e pimenta com porcentagem de 0,05; 0,1; 0,15; e 0,2.
<p align="center">
  <img src="./images/doge_mediana5_sal_005.jpg" width="200px">
  <img src="./images/doge_mediana5_sal_01.jpg" width="200px"><br/>
  <img src="./images/doge_mediana5_sal_015.jpg" width="200px">
  <img src="./images/doge_mediana5_sal_02.jpg" width="200px">
</p>

##### Testes média

Imagem apos filtro de média com ordem 3 e ruido sal e pimenta com porcentagem de 0,05; 0,1; 0,15; e 0,2.
<p align="center">
  <img src="./images/doge_media3_sal_005.jpg" width="200px">
  <img src="./images/doge_media3_sal_01.jpg" width="200px"><br />
  <img src="./images/doge_media3_sal_015.jpg" width="200px">
  <img src="./images/doge_media3_sal_020.jpg" width="200px">
</p>

Imagem apos filtro de média com ordem 7 e ruido sal e pimenta com porcentagem de 0,05; 0,1; 0,15; e 0,2.
<p align="center">
  <img src="./images/doge_media7_sal_005.jpg" width="200px">
  <img src="./images/doge_media7_sal_01.jpg" width="200px"><br />
  <img src="./images/doge_media7_sal_015.jpg" width="200px">
  <img src="./images/doge_media7_sal_020.jpg" width="200px">
</p>


Imagem apos filtro de média com ordem 15 e ruido sal e pimenta com porcentagem de 0,05; 0,1; 0,15; e 0,2.
<p align="center">
  <img src="./images/doge_media15_sal_005.jpg" width="200px">
  <img src="./images/doge_media15_sal_010.jpg" width="200px"><br />
  <img src="./images/doge_media15_sal_015.jpg" width="200px">
  <img src="./images/doge_media15_sal_020.jpg" width="200px">
</p>


Como é possível ver, o filtro de mediana se sai muito a frente do de média para resolver esse problema. Pois o pior cenário que foi da ordem 3 e sal e pimenta de 0,20; ele se sai superior ao melhor cenário da média que é a ordem 3 e sal e pimenta de 0,05.  
Também é possível visualizar o problema de alteração de cores, devido o sal e pimenta pesar muito na média, esse problema é facilmente visualizável nos cenários de ordem 3.


#### Ganho de SNR

##### Ordem 3
Sal & Pimenta   | Média  | Mediana 
------          | ------ | ------ 
0,05            | 19.941 | 29.264
0,10            | 17.372 | 27.464
0,15            | 15.630 | 25.586
0,20            | 15.691 | 25.312

##### Ordem 5
Sal & Pimenta   | Mediana  
------          | ------  
0,05            | 26.013
0,10            | 25.221
0,15            | 24.367
0,20            | 23.293

##### Ordem 7
Sal & Pimenta   | Média  
------          | ------  
0,05            | 20.204
0,10            | 19.189
0,15            | 18.084
0,20            | 17.177

##### Ordem 15
Sal & Pimenta   | Média  
------          | ------  
0,05            | 17.160
0,10            | 16.793
0,15            | 16.376
0,20            | 15.921
