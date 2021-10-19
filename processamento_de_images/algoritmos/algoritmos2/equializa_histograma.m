function novo_hist = equializa_histograma(imagem)
    nova_imagem = rgb2gray(imagem);
    # nova_imagem = double(nova_imagem)/255;
    niveis = 255

    [altura, largura, profundidade] = size(nova_imagem);
    % L = 2^profundidade
    histograma = zeros(1, niveis + 1);
    for linha = 1:altura
        for coluna = 1:largura
            pixel = nova_imagem(linha,coluna) + 1;
            pixel
            histograma(1, pixel) += 1;
        end
    end

    histograma_equalizado = zeros(1, niveis);
    tamanho = altura * largura
    for a = 1:niveis
        histograma_equalizado(1, a) = (histograma(1, a)/tamanho);
        if(a != 1)
            histograma_equalizado(1, a) += histograma_equalizado(1, a-1);
        endif
    end

    for linha = 1:altura
        for coluna = 1:largura
            pixel = nova_imagem(linha,coluna) + 1;
            nova_imagem(linha,coluna) = niveis * histograma_equalizado(1, pixel);
        end
    end

    imshow(nova_imagem);
    figure(2);
    hist(nova_imagem(:), 255);
    "end equializa_histograma"

novo_hist = nova_imagem;

