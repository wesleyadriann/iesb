
function snr_resultado = snr(imagem_perfeita, imagem_ruidosa)
    [largura, altura] = size(imagem_perfeita);

    snr_calc = 0;
    a = 0;
    b = 0;
    for linha = 1:altura
        for coluna = 1:largura
            a = a + power(imagem_perfeita(linha, coluna) - imagem_ruidosa(coluna - linha), 2);
            b = b + power(imagem_perfeita(linha, coluna), 2);
        end
    end

    snr_calc = a/b;
    "snr completo"

snr_resultado = snr_calc;
