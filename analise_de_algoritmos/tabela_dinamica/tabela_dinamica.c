#include<stdio.h>
#include <stdlib.h>
#include "omp.h"

#define tam 100000000
#define execucoes 5
#define multiplicador 2
#define divisor (1/(multiplicador*2))

typedef struct tabela_dinamica {
  long int tamanho;
  long int qtd;
  long int * vet;
} tabela_dinamica;

tabela_dinamica * aloca_tabela();
long int * aloca_vetor(long int qtd) ;
void copia (long int * vetor1, long int *  vetor2, long int qtd);
void incluir(tabela_dinamica * tabela, int x);
void remover(tabela_dinamica * tabela);

int main() {
  int i = 0;
  double tempo_inicial, tempo_final, tempos = 0.0;

  tabela_dinamica * tabela1;
  tabela1 = aloca_tabela();


  tempo_inicial = omp_get_wtime();
  for(i = 0; i < execucoes; i++) {
    double tempo_inicial_execucao, tempo_final_execucao = 0.0;
    int j = 0;
    tempo_inicial_execucao =  omp_get_wtime();
    for(j=0; j < tam; j++) {
      incluir(tabela1, 1);
    }
    for(j=0; j < tam; j++) {
      remover(tabela1);
    }
    tempo_final_execucao = omp_get_wtime();
    tempos = (tempo_final_execucao - tempo_inicial_execucao) + tempos;
    printf("Execução %d , tempo %lf \n", i, tempo_final_execucao - tempo_inicial_execucao);
  }
  tempo_final = omp_get_wtime();
  printf("Execução total, tempo total %lf, tempo medio %lf", tempo_final - tempo_inicial, tempos / execucoes);

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

void incluir(tabela_dinamica * tabela, int x) {
  long int i = 0;

  if(tabela->tamanho==0) {
    tabela->vet = aloca_vetor(1);
    tabela->tamanho = 1;
  }

  if(tabela->tamanho == tabela->qtd) {
    long int * vetor_aux = NULL;

    vetor_aux = aloca_vetor(tabela->tamanho * multiplicador);
    copia(tabela->vet, vetor_aux, tabela->qtd);
    free(tabela->vet);
    tabela->vet = vetor_aux;
    tabela->tamanho = tabela->tamanho * multiplicador;
  }

  tabela->vet[tabela->qtd] = x;
  tabela->qtd++;
}

void remover(tabela_dinamica * tabela) {
  if(tabela->qtd == 0) {
    printf("\n Tabela vazia");
  }

  long int tamanho_divisor = tabela->tamanho * divisor;

  tabela->vet[tabela->qtd - 1] = 0;
  tabela->qtd--;

  if(tabela->qtd == tamanho_divisor && tabela->qtd != 1) {
    long int * vetor_aux = NULL;

    vetor_aux = aloca_vetor(tabela->tamanho / multiplicador);
    copia(tabela->vet, vetor_aux, tabela->qtd);
    free(tabela->vet);
    tabela->vet = vetor_aux;
    tabela->tamanho = tabela->tamanho / multiplicador;
  }

};

long int * aloca_vetor(long int qtd) {
  int i = 0;
  long int * novo_vetor;
  novo_vetor = (long int *)malloc(sizeof(long int) * qtd);
  for(i=0; i < qtd; i++) {
    novo_vetor[i] = 1;
  }

  return novo_vetor;
}

void copia (long int * vetor1, long int *  vetor2, long int qtd) {
  int i = 0;
  for(i=0;i<qtd;i++) {
    vetor2[i] = vetor1[i];
  };
}
