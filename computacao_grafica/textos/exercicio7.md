## Exercicio 7
#### [Algoritmo](../algoritmos/algoritmos7/raytracing_frontal.m)


### PROJEÇÃO PARALELA – RAY TRACING
Nesta atividade, você um algoritmo em MATLAB / Octave que realize a projeção paralela
ortográfica com o método de ray tracing. Assim, seu algoritmo receberá uma matriz 3D,
contendo um objeto tridimensional já construído (sua forma já rasterizada em 3 dimensões) e
deverá fornecer como saída a imagem 2D correspondente à projeção paralela desse objeto.  
A matriz 3D contendo objeto, recebida como entrada, estará representada numa variável na
forma X(i,j,k), em que (i,j) representa a coordenada (linha,coluna) num dos planos paralelos da
cena (ou seja, perpendiculares ao raio de projeção) localizado numa profundidade k (distância
ao plano de projeção, localizado k=1). Esta matriz conterá os pontos do objeto com sua forma
já previamente construída.  
Para isto, estão disponibilizados no Blackboard três arquivos ‘.mat’ contendo exemplos de
objetos simples tridimensionais, gerados em Matlab / Octave pelo professor, que você utilizará
para testar seu algoritmo. Cada arquivo ‘.mat’ contém uma variável, X, consistindo numa
matriz tridimensional, conforme descrito no parágrafo acima.  
Para carregar a variável contida no arquivo, baixe o arquivo ‘.mat’ disponibilizado e coloque-o
na pasta correspondente ao seu diretório do Matlab / Octave (pasta em que estão salvas as
suas funções, conforme selecionado na janela do programa – indicada acima da janela de
comando). Após salvar na pasta, utilize o comando *load* para carregar a variável. Por
exemplo, digitando *load cubo3D* na janela de comando. A variável X aparecerá para você
no campo das variáveis.  
Você aplicará a técnica de ray tracing sobre essa variável (que contém o objeto da cena). Para
isso, você escreverá o algoritmo que realiza o ray tracing.
Assim, o <ins>único parâmetro de entrada</ins> de seu algoritmo deve ser a variável X contendo o objeto
da cena (que você carregará a partir do arquivo ‘.mat’).  
O <ins>único parâmetro de saída</ins> deve ser a imagem bidimensional produzida, correspondente à
projeção paralela ortográfica do objeto no plano pela técnica de ray tracing.
Aplique seu algoritmo aos três objetos fornecidos pelo professor, inserindo as imagens
resultantes (projeções 2D) em seu relatório. Não se esqueça das recomendações para o
relatório (clareza na explicação de suas ideias etc.).  
