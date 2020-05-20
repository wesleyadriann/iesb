load helicoide3D.mat

% X é a varial que esta a cena
cena = X;
tamanho_cena = length(cena);
projecao = ones(tamanho_cena);

% A variavel coluna representa o eixo X da cena
% A variavel linha representa o eixo Y da cena
%  variavel profundidade representa o eixo Z da cena
for eixo_z = 1:tamanho_cena
    for eixo_y = 1:tamanho_cena
        for eixo_x = 1:tamanho_cena
            if cena(eixo_x, eixo_y, eixo_z) != 0
                projecao(eixo_z, eixo_y) = 1 - (eixo_x/tamanho_cena);
                break
            end
        end
    end
end

imshow(projecao)

