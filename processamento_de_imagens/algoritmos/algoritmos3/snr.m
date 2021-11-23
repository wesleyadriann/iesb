function snr_resultado = snr(imagem_perfeita, imagem_ruidosa)
    [largura, altura] = size(imagem_perfeita);

    erro_relativo = 0;
    a = 0;
    b = 0;
    for linha = 1:altura
        for coluna = 1:largura
            a = a + power(imagem_perfeita(linha, coluna) - imagem_ruidosa(linha, coluna), 2);
            b = b + power(imagem_perfeita(linha, coluna), 2);
        end
    end
    erro_relativo = a/b;
    snr_calc = 10 * log10(1/erro_relativo);
    "snr completo"

snr_resultado = snr_calc;
