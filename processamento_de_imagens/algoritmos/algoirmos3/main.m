image = imread('./lena_brilho_baixo.png');

% -----
% Parte 1
% Filtro de media e mediana
% -----

janela = 3

matrix_conv2 = ones(janela, janela);
matrix_conv2 = matrix_conv2.*(1/(janela*janela));
imagem_conv2 = conv2(imagem, matrix_conv2, 'same');


imagem_mediana = filtro_mediana(imagem, janela)

% imagem_ruidosa = imnoise(imagem, "salt & pepper", 0.05);

figure('conv2')
imshow(imagem_conv2);
figure('mediana');
imshow(imagem_mediana);

% -----
% Parte 2
% Formas principais
% -----



% -----
% Parte 3
% Realce de bordas
% -----
