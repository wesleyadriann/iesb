L = 80;
C = 80;
P = 80;

cena = zeros(L,C,P);

base_p1 = [70 50 10];
base_p2 = [60 70 40];
base_p3 = [40 20 60];
topo_p1 = [10 60 35];

cena = rasteriza_reta(cena, base_p1, base_p2);
cena = rasteriza_reta(cena, base_p1, base_p3);
cena = rasteriza_reta(cena, base_p2, base_p3);

cena = rasteriza_reta(cena, topo_p1, base_p2);
cena = rasteriza_reta(cena, topo_p1, base_p1);
cena = rasteriza_reta(cena, topo_p1, base_p3);

"Triangulo Criado"

X = cena;
save triangulo.mat X;
