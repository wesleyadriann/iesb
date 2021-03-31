#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "omp.h"

int main() {
  long int *numeros;
  long long int sum;
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

  sum = 0;
  t1_p = omp_get_wtime();
  #pragma omp parallel
  {
    long long int mult = 0;
    #pragma omp for schedule(dynamic, 1)
    for(i = 0; i < entrada; i = i + 2) {
      mult = abs(numeros[i] * numeros[i+1]);
    }

    #pragma omp critical
    {
      sum = sum + mult;
    }
  }
  t2_p = omp_get_wtime();

  sum = 0;
  t1_s = omp_get_wtime();
  for(i = 0; i < entrada; i = i + 2) {
    sum = sum + abs(numeros[i] * numeros[i+1]);
  }
  t2_s = omp_get_wtime();


  printf("\nTempo paralelo: %lf", t2_p - t1_p);
  printf("\nTempo sequencial: %lf", t2_s - t1_s);


  free(numeros);

  return 0;
}
