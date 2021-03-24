#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "omp.h"

void ler_arquivo(char *nome_arquivo, char *texto_arquivo, int tamanho);

int main() {
  char letra;
  char *nome_arquivo;
  char *texto_arquivo;
  int tamanho = 10000;
  int num_threads = 6;
  float t1seq, t2seq, t1par, t2par;

  nome_arquivo = (char*)calloc(10, sizeof(char));
  texto_arquivo = (char*)calloc(tamanho, sizeof(char));

  printf("letra: ");
  scanf("%s", &letra);

  printf("arquivo: ");
  scanf("%s", nome_arquivo);

  ler_arquivo(nome_arquivo, texto_arquivo, tamanho);
  int tamanho_arquivo = strlen(texto_arquivo);

  int i;
  int encontrou = 0;
  t1seq = omp_get_wtime();
  for(i = 0; i < tamanho_arquivo; i++) {
    if(texto_arquivo[i] == letra) {
      encontrou = 1;
      break;
    }
  }
  t2seq = omp_get_wtime();


  omp_set_num_threads(num_threads);
  t1par = omp_get_wtime();
  #pragma omp parallel for
  for(i = 0; i < tamanho_arquivo; i++) {
    if(texto_arquivo[i] == letra) {
      encontrou = 1;
    }
  }
  t2par = omp_get_wtime();

  if(encontrou) {
    printf("letra encontrada");
  } else {
    printf("letra não encontrada");
  }
  printf("\nTempo gasto sequencial: %lf", t2seq - t1seq);
  printf("\nTempo gasto paralelo  : %lf\n", t2par - t1par);

  free(nome_arquivo);
  free(texto_arquivo);

  return 0;
}

void ler_arquivo(char *nome_arquivo, char *texto_arquivo, int tamanho) {
  FILE* file;

  file = fopen(nome_arquivo, "r");

  if (file==NULL) {
    printf("arquivo nao encontrado.");
  }

  char *linha;
  linha = (char*)calloc(tamanho, sizeof(char));
  int i;
  do {
    i = fscanf(file, "%s", linha);
    strcat(texto_arquivo, linha);
    strcpy(linha, "");
  } while (i == 1);

  free(linha);
  fclose(file);
}
