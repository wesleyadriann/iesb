% -----
% Parte 3
% Realce de bordas unsharp masking
% -----

pkg load image

"parte 3 iniciada"
imagem_original = imread('./imagem_base.jpg');
imagem_base = double(rgb2gray(imagem_original))/255;

ganho = 1;

ordem = 3;

mascara_media = ones(ordem, ordem);
mascara_media = mascara_media.*(1/(ordem*ordem));

imagem_media = conv2(imagem_base, mascara_media, 'same');

filtragem_passa_baixa = imagem_base.*imagem_media;
bordas = imagem_base - filtragem_passa_baixa;
imagem_unsharp_masking = imagem_base + (ganho * bordas);
