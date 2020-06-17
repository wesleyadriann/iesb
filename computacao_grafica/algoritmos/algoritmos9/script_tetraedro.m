"Script tetraedro iniciado"

m_vertices = [
    70, 50, 10;
    60, 70, 40;
    40, 20, 60;
    10, 60, 35
];

m_arestas = [
    1, 2;
    1, 3;
    2, 3;
    4, 1;
    4, 2;
    4, 3;
];

cena = rasteriza_objeto(m_vertices, m_arestas, 80, 80, 80);
projecao = raytracing_frontal(cena);
"Script tetraedro finalizado"
