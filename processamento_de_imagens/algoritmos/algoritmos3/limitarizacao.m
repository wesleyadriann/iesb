
function imagem_limiarizada = limitarizacao(imagem_original)
    [largura, altura] = size(imagem_original);

    for linha = 1:altura
        for coluna = 1:largura
            pixel = 0;
            if(imagem_original(linha, coluna) >= 0.5)
                pixel = 1;
            end
            imagem_original(linha, coluna) = pixel;
        end
    end

    "limitarizacao completo"

imagem_limiarizada = imagem_original;
