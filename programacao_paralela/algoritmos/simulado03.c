#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "omp.h"

int main() {
  long long int **matriz;
  int entrada, i, j;
  srand(time(0));

  printf("Informe um numero inteiro positivo: ");
  scanf("%d", &entrada);


  if(entrada < 0) {
    printf("\nNumero invalido");
    return 1;
  }

  matriz = (long long int**)malloc(entrada * sizeof(long long int));
  for(i = 0; i <= entrada; i++) {
    matriz[i] = (long long int*)malloc(entrada * sizeof(long long int));
  }

  for(i = 0; i <= entrada; i++) {
    matriz[i][0] = abs(rand());
    matriz[0][i] = abs(rand());
  }

  for(i = 0; i <= entrada; i++) {
    for(j = 0; j <= entrada; j++) {
      printf("%lld ", matriz[i][j]);
    }
    printf("\n");
  }


  return 0;
}
