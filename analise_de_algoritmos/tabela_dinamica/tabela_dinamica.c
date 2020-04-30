#include<stdio.h>
#include <stdlib.h>
#include <time.h>
#include "omp.h"

#define tam 100000000
#define execucoes 5
#define multiplicador 2
#define divisor 1/(multi*2)

typedef struct tabela_dinamica {
  long int tamanho;
  long int qtd;
  long int * vet;
} tabela_dinamica;

tabela_dinamica * aloca_tabela();

int main() {
  int i = 0;
  double tempo_inicial, tempo_final = 0.0;

  tabela_dinamica * tabela1;
  tabela1 = aloca_tabela();


  tempo_inicial =  omp_get_wtime();
  for(i = 0; i < execucoes; i++) {
    double tempo_inicial_execucao, tempo_final_execucao = 0.0;
    int j = 0;
    for(j=0; j < execucoes; j++) {

    }
  }
  tempo_final = omp_get_wtime();
  printf("%f %f", tempo_final, tempo_inicial);

  return 0;
};

tabela_dinamica * aloca_tabela() {
  tabela_dinamica * nova_tabela;

  nova_tabela = (tabela_dinamica*)malloc(sizeof(tabela_dinamica));
  nova_tabela->qtd = 0;
  nova_tabela->tamanho = 0;
  nova_tabela->vet = 0;
  return nova_tabela;
}
