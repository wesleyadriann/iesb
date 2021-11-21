% -----
% Parte 2
% Formas principais
% -----

pkg load image

"parte 2 iniciada"
imagem_original = imread('./imagem_base.jpg');

imagem_base = double(rgb2gray(imagem_original))/255;

% -----
% Formas Principais
% -----

ordem = 3;

"formas principais"
mascara_media = ones(ordem, ordem);
mascara_media = mascara_media.*(1/(ordem*ordem));

imagem_media = conv2(imagem_base, mascara_media, 'same');
formas_principais = limitarizacao(imagem_media);


% -----
% Contornos Principais
% -----

"contornos principais"
laplaciano = [-1 -1 -1; -1 8 -1; -1 -1 -1];
passa_alta_laplaciano = conv2(formas_principais, laplaciano);
contornos_principais = abs(passa_alta_laplaciano);

