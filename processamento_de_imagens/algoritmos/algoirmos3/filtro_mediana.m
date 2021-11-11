function nova_imagem = filtro_mediana(imagem, janela)
    imagem_cinza = double(rgb2gray(imagem))/255;

    [largura_imagem, altura_imagem] = size(nova_imagem);
    imagem_mediana = zeros(largura_imagem, altura_imagem);

    for linha = 1:altura_imagem
        for coluna = 1:largura_imagem
            sub_matrix = block_set = im2col(imagem_cinza,[janela,janela],'sliding');
            mediana = median(sub_matrix(:))
            imagem_mediana[linha, coluna] = mediana;
        end
    end
    "filtro de mediana completo"

nova_imagem = imagem_mediana;
