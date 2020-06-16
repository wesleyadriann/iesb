function X = rasteriza_objeto(m_vertices, m_arestas, L, A, C)
    cena = zeros(L, A, C);
    quantidade_arestas = length(m_arestas)
    for linha = 1:quantidade_arestas
        p1 = m_arestas(linha, 1)
        p2 = m_arestas(linha, 2)
        cena = rasteriza_reta(cena, m_vertices(p1,:), m_vertices(p2,:));
    end
X = cena;
