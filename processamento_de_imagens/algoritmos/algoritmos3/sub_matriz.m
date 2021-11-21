function sub = sub_matriz(imagem, linha, coluna, ordem)
    matriz = zeros(ordem, ordem);
    range_vizinho = fix(ordem/2);
    i = 0;
    for linha_i = (linha-range_vizinho):(linha+range_vizinho)
        i++;
        j = 0;
        for coluna_j = (coluna-range_vizinho):(coluna+range_vizinho)
            j++;
            try
                matriz(i,j) = imagem(linha_i,coluna_j);
            catch
            end
        end
    end
sub = matriz;
