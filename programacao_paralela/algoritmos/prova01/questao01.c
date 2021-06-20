#include <stdio.h>
#include <stdlib.h>
#include "omp.h"

int valida_primo(int numero);

int main() {
    int num_inicio = 1, num_fim = 10;

    omp_set_num_threads(3);
    #pragma omp parallel
    {
        int thread_num = omp_get_thread_num();
        int i;
        #pragma omp sections nowait
        {
            #pragma omp section
            {
                printf("\nthread: %d - ", thread_num);
                for(i=num_inicio - 1; i<=num_fim; i = i + 2) {
                    printf("%d ", i);
                }
            }
            
            #pragma omp section
            {
                printf("\nthread: %d - ", thread_num);
                for(i=num_inicio; i<=num_fim; i = i + 2) {
                    printf("%d ", i);
                }
            }

            #pragma omp section
            {
                printf("\nthread: %d - ", thread_num);
                for(i=num_inicio; i<=num_fim; i++) {
                    if(valida_primo(i)) {
                        printf("%d ", i);
                    }
                }
            }
        }
    }


    return 0;
}

int valida_primo(int numero) {
    int i;
    for(i = 2; i < numero; i++) {
        if(numero % i == 0) {
            return 0;
        }
    }
    return 1;
}