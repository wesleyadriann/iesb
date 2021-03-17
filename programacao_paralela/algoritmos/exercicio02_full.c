#include <stdio.h>
#include <stdlib.h>
#include "omp.h"

static long num_steps = 100000000;

int main() {
  double pi, sum = 0.0, tempo_inicial, tempo_final, step;

  int nthreads = 4;

  step = 1.0 / (double)num_steps;
  omp_set_num_threads(nthreads);

  tempo_inicial = omp_get_wtime();
  #pragma omp parallel
  {
    int id = omp_get_thread_num();
    double local_sum = 0.0, x;
    int i;
    printf("thread id: %d\n", id);
    for (i = id; i < num_steps; i = i + nthreads) {
      x = (i + 0.5) * step;
      local_sum = local_sum + 4.0 / (1.0 + x * x);
    }

    #pragma omp critical
    {
      sum = sum + local_sum;
    }

  }

  pi = step * sum;
  tempo_final = omp_get_wtime();

  printf("\nPi = %lf", pi);
  printf("\nTempo gasto: %lf\n", tempo_final - tempo_inicial);

  return 0;
}
