#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "omp.h"

#define execucoes 1000000

long long karatsuba_ofman(long long u, long long v, int n);
int count_number(long long number);

int main() {
  long long number1, number2;

  number1 = 1000000000000000000;
  number2 = 1000000000000000000;
  return 0;
  int digits_number_1 = count_number(number1);
  int digits_number_2 = count_number(number2);

  int n = (int) digits_number_1 > digits_number_2 ? digits_number_1 : digits_number_2;

  int i = 0;
  float tempo_inicial, tempo_final, tempos = 0.0;
  tempo_inicial = omp_get_wtime();
  for(i = 0; i < execucoes; i++) {
    float tempo_inicial_execucao, tempo_final_execucao = 0.0;
    long long multiplication = karatsuba_ofman(number1, number2, n);
    tempo_final_execucao = omp_get_wtime();
    tempos = (tempo_final_execucao - tempo_inicial_execucao) + tempos;
    printf("Resultado multiplicacao: %lld \n", multiplication);
    printf("Execução %d - tempo %lf \n", i, tempo_final_execucao - tempo_inicial_execucao);
  }

  tempo_final = omp_get_wtime();
  printf("Execuções finalizadas\nTempo total %lf - Tempo medio %lf", tempo_final - tempo_inicial, tempos / execucoes);

  return 0;
}

long long karatsuba_ofman(long long u, long long v, int n) {
  if(u <= 100 || v <= 100) {
    return u * v;
  } else {

    long long p ,q ,r ,s, pr, qs, z;

    int m = floor(n / 2);
    int ten_pow_m = pow(10, m);

    p = floor(u / ten_pow_m);
    q = u % ten_pow_m;
    r = floor(v / ten_pow_m);
    s = v % ten_pow_m;

    pr = karatsuba_ofman(p, r, m);
    qs = karatsuba_ofman(q, s, m);
    z = karatsuba_ofman(p+q, r+s, m+1) - pr - qs;

    int ten_pow_2m = pow(10, (2 * m));

    return (pr * ten_pow_2m + z * ten_pow_m + qs);
  }
}

int count_number(long long number) {
	int count = 0;
	while (number >= 1) {
    number = number / 10;
    count++;
  }
  return count;

}
