#include <stdio.h>
#include <stdlib.h>
#include "omp.h"

int valida_primo(int numero);

int main() {
  int i, inicio = 10000;
  int entrada, qtd_primos_encontrados = 0;
  long long int *numeros;
  long long int sum;
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

  sum = 0;
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
      sum = sum + local_sum;
    }
  }
  t2_p = omp_get_wtime();

  sum = 0;
  t1_s = omp_get_wtime();
  for(i = 0; i < entrada; i++) {
    sum = sum + numeros[i];
  }
  t2_s = omp_get_wtime();

  printf("\nTempo paralelo: %lf", t2_p - t1_p);
  printf("\nTempo sequencial: %lf", t2_s - t1_s);

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
