
function snr = ganho_snr(imagem_perfeita, imagem_ruidosa)
    [largura, altura] = size(imagem_perfeita);

    snr_calc = 0
    a = 0;
    b = 0;
    for coluna = 1:largura
        for linha = 1:altura
            a = a + power(imagem_perfeita(coluna, linha) - imagem_ruidosa(coluna - linha), 2)
            b = b + power(imagem_perfeita(coluna, linha), 2)
        end
    end

    snr_calc = a/b
    "snr completo"

snr = snr_calc;
