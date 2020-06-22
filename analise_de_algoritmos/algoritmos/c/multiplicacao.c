#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "omp.h"

#define execucoes 1000000

int main() {
  long long number1, number2;
        //  10000000
  number1 = 45610566449087635160404000;
  number2 = 15641564804094321664004000;

  int i = 0;
  float tempo_inicial, tempo_final, tempos = 0.0;
  tempo_inicial = omp_get_wtime();
  for(i = 0; i < execucoes; i++) {
    float tempo_inicial_execucao, tempo_final_execucao = 0.0;
    long long multiplication = number1 * number2;
    tempo_final_execucao = omp_get_wtime();
    tempos = (tempo_final_execucao - tempo_inicial_execucao) + tempos;
    printf("Resultado multiplicacao: %lld \n", multiplication);
    printf("Execução %d - tempo %lf \n", i, tempo_final_execucao - tempo_inicial_execucao);
  }

  tempo_final = omp_get_wtime();
  printf("Execuções finalizadas\nTempo total %lf - Tempo medio %lf", tempo_final - tempo_inicial, tempos / execucoes);

  return 0;
}

long long multi(long long u, long long v) {
  long long acc = 0;
  int i = 0;
  for(i = 0; i < v; i++) {
    acc = acc + u;
  }

  return acc;
}
