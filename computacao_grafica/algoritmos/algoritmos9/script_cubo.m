"Script cubo iniciado"
m_vertices = [
    60, 50, 10;
    50, 60, 30;
    45, 45, 50;
    50, 20, 30;
    30, 50, 10;
    20, 60, 30;
    15, 45, 50;
    20, 20, 30;
];

m_arestas = [
    1, 2;
    2, 3;
    3, 4;
    4, 1;
    5, 6;
    6, 7;
    7, 8;
    8, 5;
    1, 5;
    2, 6;
    3, 7;
    4, 8
];
cena = rasteriza_objeto(m_vertices, m_arestas, 80, 80, 80);
projecao = raytracing_frontal(cena);
"Script cubo finalizado"
