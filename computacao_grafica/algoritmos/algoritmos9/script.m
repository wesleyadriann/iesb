
m_vertices = [
    20, 80, 55;
    78, 31, 44;
    79, 150, 114
];

m_arestas = [
    1, 2;
    1, 3;
    2, 3
];
"Script iniciado"
cena = rasteriza_objeto(m_vertices, m_arestas, 200, 200, 200);
projecao = raytracing_frontal(cena);
