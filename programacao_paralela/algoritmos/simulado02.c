#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "omp.h"

int main() {
  long int *numeros;
  long long int sum_s = 0, sum_p = 0;
  int entrada, i;
  double t1_s, t2_s, t1_p, t2_p;
  srand(time(0));

  printf("Informe um numero par positivo: ");
  scanf("%d", &entrada);

  if(entrada % 2 != 0) {
    printf("Entrada invalida");
    return 1;
  }

  numeros = (long int *)malloc(entrada * sizeof(long int));
  for(i = 0; i < entrada; i++) {
    numeros[i] = abs(rand());
  }

  t1_s = omp_get_wtime();
  for(i = 0; i < entrada; i = i + 2) {
    sum_s += abs(numeros[i] * numeros[i+1]);
  }
  t2_s = omp_get_wtime();


  t1_p = omp_get_wtime();
  #pragma omp parallel
  {
    long long int mult_local = 0;
    #pragma omp for schedule(static, 1)
    for(i = 0; i < entrada; i = i + 2) {
      mult_local = abs(numeros[i] * numeros[i+1]);
    }

    #pragma omp critical
    {
      sum_p += mult_local;
    }
  }
  t2_p = omp_get_wtime();


  printf("\nSequencial");
  printf("\nSoma : %lld", sum_s);
  printf("\nTempo: %lf\n", t2_s - t1_s);
  printf("\nParalelo");
  printf("\nSoma : %lld", sum_p);
  printf("\nTempo: %lf\n", t2_p - t1_p);


  free(numeros);

  return 0;
}
