#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PAREDE '1'
#define CAMINHO '2'
#define RECOMPENSA '3'
#define MAX_MATRIZ 10000

char **carrega_mapa(char *nome_arquivo);
char **aloca_mapa(int tamanho);
int **ler_pontos(int qtd_pontos);
void print_mapa(char **mapa);

int main() {
  char **mapa;
  int **pontos;
  char *nome_arquivo = "labirinto.txt";
  int entrada = 1;

  mapa = carrega_mapa(nome_arquivo);
  print_mapa(mapa);

  printf("quantidade de threads: ");
  scanf("%d", &entrada);

  pontos = ler_pontos(entrada);


  return 0;
}

char **carrega_mapa(char *nome_arquivo) {
  FILE* file;
  file = fopen(nome_arquivo, "r");

	if(file == 0 || file == NULL) {
    printf("arquivo nao encontrado.");
		exit(1);
	}

  char *linha;
  linha = (char*)calloc(MAX_MATRIZ, sizeof(char));
  int j, qtd_colunas;
  fscanf(file, "%s", linha);
  qtd_colunas = strlen(linha);

  char **mapa = aloca_mapa(qtd_colunas);
  strcpy(mapa[0], linha);

  free(linha);
  linha = (char*)calloc(qtd_colunas, sizeof(char));

  int i;
  for(i = 1; i < qtd_colunas; i++) {
    fscanf(file, "%s", mapa[i]);
  }

  free(linha);
  fclose(file);
  return mapa;
}

char **aloca_mapa(int tamanho) {
  char **mapa = (char**)calloc(tamanho, sizeof(char*));
  int i;
  for(i = 0; i < tamanho ; i++) {
    mapa[i] = (char *)calloc(tamanho + 1, sizeof(char));
  }
  return mapa;
}

int **ler_pontos(int qtd_pontos) {
  int **pontos = (int**)calloc(qtd_pontos, sizeof(int*));
  int i, x, y;
  for(i = 0; i < qtd_pontos; i++) {
    printf("ponto x da thread %d: ", i);
    scanf("%d", &x);
    printf("ponto y da thread %d: ", i);
    scanf("%d", &y);
    pontos[i] = calloc(2, sizeof(int));
    pontos[i][0] = x;
    pontos[i][1] = y;
  }
  return pontos;
}

void print_mapa(char **mapa) {
  int linhas = strlen(mapa[0]);
  int i;
  for(i = 0; i < linhas; i++) {
    printf("%s\n", mapa[i]);
  }
}
