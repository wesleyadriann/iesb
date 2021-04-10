#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "omp.h"

int main() {
  long int **matriz;
  long int sum_s = 0, sum_p = 0;
  int entrada, i, j;
  double t1_s, t2_s, t1_p, t2_p;
  srand(time(0));

  printf("Informe um numero inteiro positivo: ");
  scanf("%d", &entrada);


  if(entrada < 0) {
    printf("\nNumero invalido");
    return 1;
  }

  matriz = (long int**)malloc(entrada * sizeof(long int));
  for(i = 0; i <= entrada; i++) {
    matriz[i] = (long int*)malloc(entrada * sizeof(long int));
  }

  for(i = 0; i <= entrada; i++) {
    matriz[i][0] = abs(rand());
    matriz[0][i] = abs(rand());
  }

  for(i = 1; i <= entrada; i++) {
    for(j = 1; j <= entrada; j++) {
      matriz[i][j] = matriz[i - 1][j] + matriz[i][j - 1];
    }
  }


  // for(i = 0; i <= entrada; i++) {
  //   for(j = 0; j <= entrada; j++) {
  //     printf("%ld ", matriz[i][j]);
  //   }
  //   printf("\n");
  // }

  t1_s = omp_get_wtime();
  for(i = 1; i <= entrada; i++) {
    for(j = 1; j <= entrada; j++) {
      sum_s += matriz[i][j];
    }
  }
  t2_s = omp_get_wtime();


  t1_p = omp_get_wtime();
  #pragma omp parallel
  {
    long int local_sum = 0;
    #pragma omp for
    for(i = 0; i <= entrada; i++) {
      for(j = 0; j <= entrada; j++) {
        local_sum += matriz[i][j];
      }
    }

    #pragma omp critical
    {
      sum_p += local_sum;
    }
  }
  t2_p = omp_get_wtime();


  printf("\nSequencial");
  printf("\nSoma : %ld", sum_s);
  printf("\nTempo: %lf\n", t2_s - t1_s);
  printf("\nParalelo");
  printf("\nSoma : %ld", sum_p);
  printf("\nTempo: %lf\n", t2_p - t1_p);


  for(i = 0; i <= entrada; i++) {
    free(matriz[i]);
  }
  free(matriz);

  return 0;
}
