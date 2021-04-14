#include <stdio.h>
#include <stdlib.h>
#include "omp.h"

int main() {
    int num_threads;

    printf("\nquantidade de threads: ");
    scanf("%d", &num_threads);

    if(num_threads < 1) {
        printf("numero invalido");
        return 1;
    }

    omp_set_num_threads(num_threads);

    #pragma omp parallel
    {
        #pragma omp single
        {
            printf("iniciando o mundo paralelo");
        }
        int thread_num = omp_get_thread_num();
        printf("\neu sou a thread %d", thread_num);

        #pragma omp barrier

        #pragma omp master
        {
            printf("\nFIM");
        }
    }

    return 0;
}