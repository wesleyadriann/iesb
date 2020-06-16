L = 80;
C = 80;
P = 80;

cena = zeros(L,C,P);

base_p1 = [65 40 15];
base_p2 = [60 60 40];
base_p3 = [60 20 40];
base_p4 = [50 50 60];
base_p5 = [50 30 60];

meio_p1 = [48 40 5];
meio_p2 = [45 65 30];
meio_p3 = [45 15 30];
meio_p4 = [35 55 70];
meio_p5 = [35 25 70];
meio_p6 = [30 40 75];
meio_p7 = [30 65 35];
meio_p8 = [30 15 35];
meio_p9 = [35 55 10];
meio_p10 = [35 25 10];

topo_p1 = [10 40 65];
topo_p2 = [15 55 40];
topo_p3 = [15 25 40];
topo_p4 = [25 50 15];
topo_p5 = [25 30 15];

cena = rasteriza_reta(cena, base_p1, base_p2);
cena = rasteriza_reta(cena, base_p1, base_p3);
cena = rasteriza_reta(cena, base_p2, base_p4);
cena = rasteriza_reta(cena, base_p3, base_p5);
cena = rasteriza_reta(cena, base_p4, base_p5);

cena = rasteriza_reta(cena, topo_p1, topo_p2);
cena = rasteriza_reta(cena, topo_p1, topo_p3);
cena = rasteriza_reta(cena, topo_p2, topo_p4);
cena = rasteriza_reta(cena, topo_p3, topo_p5);
cena = rasteriza_reta(cena, topo_p4, topo_p5);

cena = rasteriza_reta(cena, base_p1, meio_p1);
cena = rasteriza_reta(cena, base_p2, meio_p2);
cena = rasteriza_reta(cena, base_p3, meio_p3);
cena = rasteriza_reta(cena, base_p4, meio_p4);
cena = rasteriza_reta(cena, base_p5, meio_p5);

cena = rasteriza_reta(cena, topo_p1, meio_p6);
cena = rasteriza_reta(cena, topo_p2, meio_p7);
cena = rasteriza_reta(cena, topo_p3, meio_p8);
cena = rasteriza_reta(cena, topo_p4, meio_p9);
cena = rasteriza_reta(cena, topo_p5, meio_p10);

cena = rasteriza_reta(cena, meio_p1, meio_p10);
cena = rasteriza_reta(cena, meio_p10, meio_p3);
cena = rasteriza_reta(cena, meio_p3, meio_p8);
cena = rasteriza_reta(cena, meio_p8, meio_p5);
cena = rasteriza_reta(cena, meio_p5, meio_p6);
cena = rasteriza_reta(cena, meio_p6, meio_p4);
cena = rasteriza_reta(cena, meio_p4, meio_p7);
cena = rasteriza_reta(cena, meio_p7, meio_p2);
cena = rasteriza_reta(cena, meio_p2, meio_p9);
cena = rasteriza_reta(cena, meio_p9, meio_p1);

"Pentagono Criado"

X = cena;
save pentagono.mat X;
