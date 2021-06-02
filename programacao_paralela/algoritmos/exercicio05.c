#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <mpi.h>

int* aloca_preenche_vetor(int tamanho) ;
void print_vet(int * vet, int tamanho);
void sum_vet(int * vet, int tamanho);

int main() {
  int multiplicador;
  int qtd_processos;
  int id_processo;
  int * vet;
  int vet_valor = 0;

  srand(time(0));

  MPI_Init(NULL, NULL);
  MPI_Comm_size(MPI_COMM_WORLD, &qtd_processos);
  MPI_Comm_rank(MPI_COMM_WORLD, &id_processo);

  if (id_processo == 0) {
    printf("\nmultiplicador: ");
    scanf("%d", &multiplicador);
    vet = aloca_preenche_vetor(qtd_processos);
    print_vet(vet, qtd_processos);
  }

  MPI_Bcast(&multiplicador,1,MPI_INT,0,MPI_COMM_WORLD);
  MPI_Scatter(&vet[0], 1 ,MPI_INT , &vet_valor, 1, MPI_INT , 0 , MPI_COMM_WORLD);

  vet_valor = multiplicador * vet_valor;

  MPI_Gather(&vet_valor, 1 ,MPI_INT , vet , 1 , MPI_INT , 0 , MPI_COMM_WORLD);

  if(id_processo == 0) {
    print_vet(vet, qtd_processos);
    sum_vet(vet, qtd_processos);
  }

  MPI_Finalize();
  return 0;
}

int* aloca_preenche_vetor(int tamanho) {
  int *vet;
  int i;
  vet = (int *)calloc(tamanho, sizeof(int));

  for(i = 0; i < tamanho; i++) {
    vet[i] = rand() % 100;
    // vet[i] = i + 1;
  }

  return vet;
}

void print_vet(int * vet, int tamanho) {
  printf("\nvetor\n");
  int i;
  for(i = 0; i < tamanho; i++) {
    printf("%d ", vet[i]);
  }
}

void sum_vet(int * vet, int tamanho) {
  int i, acc = 0;
  for(i = 0; i < tamanho; i++) {
    acc = acc + vet[i];
  }
  printf("\nSomatorio final: %d\n", acc);
}
