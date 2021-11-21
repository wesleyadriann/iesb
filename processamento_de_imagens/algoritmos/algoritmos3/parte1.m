% -----
% Parte 1
% Filtro de media e mediana
% -----

pkg load image

"parte 1 iniciada"
imagem_base = imread('./imagem_base.jpg');

ruido = 0.05;

imagem_original = double(rgb2gray(imagem_base))/255;
imagem_ruidosa = imnoise(imagem_original,  'salt & pepper', ruido);

janela = 3;

"conv2"
matriz_conv2 = ones(janela, janela);
matriz_conv2 = matriz_conv2.*(1/(janela*janela));

imagem_conv2 = conv2(imagem_ruidosa, matriz_conv2, 'same');

"mediana"
imagem_mediana = filtro_mediana(imagem_ruidosa, janela);

"snr"
snr_conv2 = snr(imagem_original, imagem_conv2)
snr_mediana = snr(imagem_original, imagem_mediana)
