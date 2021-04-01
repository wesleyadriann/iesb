#include <stdio.h>
#include <stdlib.h>
#include "omp.h"

int valida_primo(int numero);

int main() {
  int i, inicio = 10000;
  int entrada, qtd_primos_encontrados = 0;
  long long int *numeros;
  long long int sum_s = 0, sum_p = 0;
  double t1_s, t2_s, t1_p, t2_p;

  printf("Informe um numero inteiro positivo: ");
  scanf("%d", &entrada);

  if(entrada < 0) {
    printf("\nNumero invalido");
    return 1;
  }

  numeros = (long long int *)malloc(entrada * sizeof(int));
  for(i = inicio; qtd_primos_encontrados <= entrada; i++) {
    if(valida_primo(i)) {
      numeros[qtd_primos_encontrados] = i;
      qtd_primos_encontrados++;
    }
  }

  t1_s = omp_get_wtime();
  for(i = 0; i < entrada; i++) {
    sum_p += numeros[i];
  }
  t2_s = omp_get_wtime();


  t1_p = omp_get_wtime();
  #pragma omp parallel
  {
    long long int local_sum = 0;

    #pragma omp for
    for(i = 0; i < entrada; i++) {
      local_sum = local_sum + numeros[i];
    }

    #pragma omp critical
    {
      sum_p += local_sum;
    }
  }
  t2_p = omp_get_wtime();

  printf("\nSequencial");
  printf("\nSoma : %lld", sum_s);
  printf("\nTempo: %lf\n", t2_s - t1_s);
  printf("\nParalelo");
  printf("\nSoma : %lld", sum_p);
  printf("\nTempo: %lf\n", t2_p - t1_p);

  return 0;
}

int valida_primo(int numero) {
  int i = 0;
  for(i=2; i < numero; i++) {
    if(numero % i == 0) {
      return 0;
    }
  }
  return 1;
}
