function nova_cena = rasteriza_reta(cena, p1, p2)
    cena_interna = cena;
    maxima_variacao = max(abs(p2 - p1));
    t_variacao = 1/maxima_variacao;

    for tk = 0:t_variacao:1
        tripla = round((1 - tk) * p1 + tk * p2);
        cena_interna(tripla(1), tripla(2), tripla(3)) = 1;
    end


nova_cena = cena_interna;
