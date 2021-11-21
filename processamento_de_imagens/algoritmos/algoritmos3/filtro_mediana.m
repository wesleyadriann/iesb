function nova_imagem = filtro_mediana(imagem, ordem)

    [largura_imagem, altura_imagem] = size(imagem);
    imagem_mediana = zeros(largura_imagem, altura_imagem);

    for linha = 1:altura_imagem
        for coluna = 1:largura_imagem
            sub_matriz_ordem = sub_matriz(imagem, linha, coluna, ordem);
            mediana = median(sub_matriz_ordem(:));
            imagem_mediana(linha, coluna) = mediana;
        end
    end
    "filtro de mediana completo"

nova_imagem = imagem_mediana;
