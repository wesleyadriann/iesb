#include<stdio.h>
#include <stdlib.h>
#include "omp.h"

#define tam 100000000

#define multi 2

typedef struct dynamic_table {
  long int tamanho;
  long int qtd;
  long int * vet;
} tabela_dinamica;

int main() {
  printf("Tabela dinamica");

  return 0;
};

tabela_dinamica * nova_tabela() {
  tabela_dinamica * nova_tabela;

  nova_tabela = (tabela_dinamica*)malloc(sizeof(tabela_dinamica));

}
