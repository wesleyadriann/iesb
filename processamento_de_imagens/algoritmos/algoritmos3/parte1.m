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
