#include <stdio.h>
#include <stdlib.h>
#include "omp.h"

static long num_steps = 100000000;

float* cria_vet(int tamanho);

int main() {
  double pi, sum = 0.0, tempo_inicial, tempo_final, step;
  int i;

  step = 1.0 / (double)num_steps;

  int nthreads = 4;

  omp_set_num_threads(nthreads);

  float *vet = cria_vet(nthreads);

  tempo_inicial = omp_get_wtime();
  #pragma omp parallel
  {
    int id = omp_get_thread_num();
    double local_sum = 0.0, x;
    int i;
    printf("threads %d\n", id);
    for (i = id; i < num_steps; i = i + nthreads) {
      x = (i + 0.5) * step;
      local_sum = local_sum + 4.0 / (1.0 + x * x);
    }
    vet[id] = local_sum;
  }

  for(i = 0; i < nthreads; i++) {
    sum = sum + vet[i];
  }

  pi = step * sum;
  tempo_final = omp_get_wtime();

  printf("\n Pi = %lf", pi);

  printf("\n Tempo gasto: %lf", tempo_final - tempo_inicial);
  free(vet);

  return 0;
}

float* cria_vet(int tamanho) {
  int i;
  float *vet = (float *)calloc(tamanho, sizeof(float));
  for(i=0; i < tamanho; i++) {
    vet[i] = 0.0;
  }

  return vet;
}
