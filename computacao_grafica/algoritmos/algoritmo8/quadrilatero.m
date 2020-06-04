L = 80;
C = 80;
P = 80;

cena = zeros(L,C,P);

base_p1 = [60 50 10];
base_p2 = [50 60 30];
base_p3 = [45 45 50];
base_p4 = [50 20 30];
topo_p1 = [30 50 10];
topo_p2 = [20 60 30];
topo_p3 = [15 45 50];
topo_p4 = [20 20 30];

cena = rasteriza_reta(cena, base_p1, base_p2);
cena = rasteriza_reta(cena, base_p2, base_p3);
cena = rasteriza_reta(cena, base_p3, base_p4);
cena = rasteriza_reta(cena, base_p4, base_p1);

cena = rasteriza_reta(cena, topo_p1, topo_p2);
cena = rasteriza_reta(cena, topo_p2, topo_p3);
cena = rasteriza_reta(cena, topo_p3, topo_p4);
cena = rasteriza_reta(cena, topo_p4, topo_p1);

cena = rasteriza_reta(cena, base_p1, topo_p1);
cena = rasteriza_reta(cena, base_p2, topo_p2);
cena = rasteriza_reta(cena, base_p3, topo_p3);
cena = rasteriza_reta(cena, base_p4, topo_p4);

"Quadrilatero Criado"

X = cena;
save quadrilatero.mat X;
