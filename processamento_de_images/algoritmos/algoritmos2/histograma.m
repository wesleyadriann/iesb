function novo_hist = histograma(imagem)
    nova_imagem = rgb2gray(imagem);
    # nova_imagem = double(nova_imagem)/255;
    % nova_imagem = histeq(nova_imagem)

    hist(nova_imagem(:), 255);
    "end"

novo_hist = nova_imagem;

