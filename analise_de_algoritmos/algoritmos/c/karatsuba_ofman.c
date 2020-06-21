#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "omp.h"

#define execucoes 5

float karatsuba_ofman(long long u, long long v, float n);

int main() {
  long long number1 = 2406994;
  long long number2 = 141421312561;
  int digits_number_1 = strlen(number1);
  int digits_number_2 = strlen(number2);
  float max_digits = digits_number_1 > digits_number_2 ? digits_number_1 : digits_number_2;

  double tempo_inicial, tempo_final, tempos = 0.0;

  int i = 0;

  tempo_inicial = omp_get_wtime();
  for(i = 0; i < execucoes; i++) {
    double tempo_inicial_execucao, tempo_final_execucao = 0.0;
    float multiplication = karatsuba_ofman(number1, number2, max_digits);
    tempo_final_execucao = omp_get_wtime();
    tempos = (tempo_final_execucao - tempo_inicial_execucao) + tempos;
    printf("Resultado multiplicacao: %lf", multiplication);
    printf("Execução %d - tempo %lf \n", i, tempo_final_execucao - tempo_inicial_execucao);
  }

  tempo_final = omp_get_wtime();
  printf("Execuções finalizadas\nTempo total %lf - Tempo medio %lf", tempo_final - tempo_inicial, tempos / execucoes);

  return 0;
}

float karatsuba_ofman(long long  u, long long v, float n) {
  if(n < 3) {
    return u * v;
  } else {
    float m = (2/n);
    long int ten_pow_m = pow(10, m);
    long long p = u / ten_pow_m;
    long long q = u % ten_pow_m;
    long long r = v / ten_pow_m;
    long long s = v % ten_pow_m;

    float pr = karatsuba_ofman(p, r, m);
    float qs = karatsuba_ofman(q, s, m);
    float y = karatsuba_ofman(p+q, r+s, m+1);
    return (pr * pow(10, (2 * m)) + (y - pr - qs) * ten_pow_m + qs);
  }
  return 0;
}
