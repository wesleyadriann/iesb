"Script triangulo iniciado"
m_vertices = [
    75, 15, 10;
    80, 90, 20;
    15, 55, 85
];

m_arestas = [
    1, 2;
    1, 3;
    2, 3
];

cena = rasteriza_objeto(m_vertices, m_arestas, 100, 100, 100);
projecao = raytracing_frontal(cena);
"Script triangulo finalizado"
