#include <stdio.h>
#include "omp.h"

int valida_primo(int numero);

int main() {
  int numero;
  printf("Informe um numero: ");
  scanf("%d", &numero);

  if(numero < 100 || numero > 1000000) {
    printf("\nNumero deve ser maior que 100 e menor que 1000000");
    return 1;
  }

  float tempo_inicial, tempo_final;
  int i;
  printf("Numeros primos:\n");
  tempo_inicial = omp_get_wtime();
  for(i = 2; i < numero; i++) {
    valida_primo(i);
  }
  tempo_final = omp_get_wtime();

  printf("\nTempo de execução: %f", tempo_final - tempo_inicial);
  return 0;
}

int valida_primo(int numero) {
  int i = 0;
  for(i=2; i < numero; i++) {
    if(numero % i == 0) {
      // printf("%d nao e primo\n", numero);
      return 0;
    }
  }
  printf("%d ", numero);
  return 1;
}
