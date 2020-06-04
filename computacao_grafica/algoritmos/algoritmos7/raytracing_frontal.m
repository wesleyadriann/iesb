load cilindro3D.mat

% X é a varial que esta a cena
cena = X;
tamanho_cena = length(cena);
projecao = ones(tamanho_cena);


for eixo_x = 1:tamanho_cena
    for eixo_y = 1:tamanho_cena
        for eixo_z = 1:tamanho_cena
            if cena(eixo_x, eixo_y, eixo_z) != 0
                projecao(eixo_x, eixo_y) = 1 - (eixo_z/tamanho_cena);
                break
            end
        end
    end
end

imshow(projecao)

