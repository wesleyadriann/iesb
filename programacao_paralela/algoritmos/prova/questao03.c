#include <stdio.h>
#include <stdlib.h>
#include "omp.h"

int primo(int x);

int main() {
    int *numeros;
    int entrada, total_p = 0, total_s = 0;
    double t1_p, t2_p, t1_s, t2_s;
    int i;

    printf("numero: ");
    scanf("%d", &entrada);

    numeros = (int *)calloc(entrada, sizeof(int));
    for(i = 0; i < entrada; i++) {
        numeros[i] = i + 1;
    }

    t1_s = omp_get_wtime();
    for(i = 0; i < entrada; i++) {
        if(primo(i)) {
            total_s = total_s + 1;
        }
    }
    t2_s = omp_get_wtime();


    t1_p = omp_get_wtime();
    #pragma omp parallel
    {
        int total_local = 0;
        int i;
        #pragma omp for
        for(i = 0; i < entrada; i++) {
            if(primo(i)) {
                total_local = total_local + 1;
            }
        }
        #pragma omp critical
        {
            total_p = total_p + total_local;
        }
    }
    t2_p = omp_get_wtime();


    printf("\nSequencial");
    printf("\n  Tempo: %f", t2_s - t1_s);
    printf("\n  Soma : %d", total_s);
    printf("\nParalelo");
    printf("\n  Tempo: %f", t2_p - t1_p);
    printf("\n  Soma : %d", total_p);

    return 0;
}


int primo(int x) {
    int i,j,z;
    
    for(i=0; i<10000; i++) {
        for(j=0; i<10000; i++) {
            z = 1;
        }
    }

    if((x==0) || (x==1)) {
        return 0;
    }

    int div;
    for(div = 2; div < x ; div++){
        if (x % div == 0) {
            return 0;
        }
    }
    return 1;
}