"main iniciado"
imagem_original = imread('./lena_cinza.png');

ruido = 0.05;

imagem_original = double(rgb2gray(imagem))/255;
imagem_ruidosa = imnoise(imagem, 'salt & pepper', ruido);

imagem = imagem_original

% -----
% Parte 1
% Filtro de media e mediana
% -----

janela = 3;

"conv2"
matrix_conv2 = ones(janela, janela);
matrix_conv2 = matrix_conv2.*(1/(janela*janela));
imagem_conv2 = conv2(imagem, matrix_conv2, 'same');

">>mediana"
imagem_mediana = filtro_mediana(imagem, janela);

figure(1);
imshow(imagem_conv2);
figure(2);
imshow(imagem_mediana);

% -----
% Parte 2
% Formas principais
% -----



% -----
% Parte 3
% Realce de bordas
% -----
