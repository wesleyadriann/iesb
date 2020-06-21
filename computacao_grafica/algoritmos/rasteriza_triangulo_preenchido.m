function X = rasteriza_triangulo_preenchido()
    cena = zeros(100, 100, 100);

    p_base1 = [75, 15, 10]
    p_base2 = [80, 90, 20]
    p_topo = [15, 55, 85]

    triplas_base = [];
    % Cria base do triangulo
    maxima_variacao = max(abs(p_base2 - p_base1));
    t_variacao = 1/maxima_variacao;
    for tk = 0:t_variacao:1
        tripla = round((1 - tk) * p_base1 + tk * p_base2);
        cena(tripla(1), tripla(2), tripla(3)) = 1;
        triplas_base = [triplas_base; tripla];
    end

    % Cria bordas e preenchimento
    qtd_triplas_base = length(triplas_base);
    for linha = 1:qtd_triplas_base
        p_inicial = triplas_base(linha,:);
        maxima_variacao = max(abs(p_topo - p_inicial));
        t_variacao = 1/maxima_variacao;
        for tk = 0:t_variacao:1
            tripla = round((1 - tk) * p_inicial + tk * p_topo);
            cena(tripla(1), tripla(2), tripla(3)) = 1;
        end
    end

X = cena;
