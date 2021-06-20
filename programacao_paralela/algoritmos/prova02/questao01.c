#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "mpi.h"

void print_vet(int *vet, int tamanho);
int *aloca_preenche_vetor(int tamanho);
void listener_matriculas(int *matriculas, int qtd_matriculas);
void gera_matriculas(int qtd_matriculas, int id_processo, int qtd_processos);
void gera_notas(int *notas, int id_processo, int qtd_matriculas);
void calcula_medias(int *notas, int *medias, int qtd_notas, int qtd_matriculas);
void maior_media(int *medias, int *matriculas, int qtd_medias);

int main()
{
  int qtd_processos;
  int id_processo;

  int *matriculas;
  int *notas;
  int qtd_matriculas;
  int qtd_notas;
  int *medias;

  int i;

  MPI_Init(NULL, NULL);
  MPI_Comm_size(MPI_COMM_WORLD, &qtd_processos);
  MPI_Comm_rank(MPI_COMM_WORLD, &id_processo);

  srand(time(NULL));

  if (id_processo == 0)
  {
    printf("\n\nQuantidade de alunos: ");
    fflush(stdout);
    scanf("%d", &qtd_matriculas);
    matriculas = aloca_preenche_vetor(qtd_matriculas);
    medias = aloca_preenche_vetor(qtd_matriculas);
    qtd_notas = qtd_matriculas * 4;
    notas = aloca_preenche_vetor(qtd_notas);
  }

  MPI_Bcast(&qtd_matriculas, 1, MPI_INT, 0, MPI_COMM_WORLD);

  if (id_processo != 0)
  {
    gera_matriculas(qtd_matriculas, id_processo, qtd_processos);
  }

  if (id_processo == 0)
  {
    listener_matriculas(matriculas, qtd_matriculas);
  }

  gera_notas(notas, id_processo, qtd_matriculas);

  if (id_processo == 0)
  {
    calcula_medias(notas, medias, qtd_notas, qtd_matriculas);
    maior_media(medias, matriculas, qtd_matriculas);
  }

  MPI_Finalize();
  printf("\n");
  return 0;
}

void print_vet(int *vet, int tamanho)
{
  int i;
  for (i = 0; i < tamanho; i++)
  {
    printf("%d ", vet[i]);
  }
  printf("\n");
}

int *aloca_preenche_vetor(int tamanho)
{
  int *vet;
  int i;
  vet = (int *)calloc(tamanho, sizeof(int));

  for (i = 0; i < tamanho; i++)
  {
    vet[i] = 0;
  }

  return vet;
}

void listener_matriculas(int *matriculas, int qtd_matriculas)
{
  int i;
  int tamanho_fatia = (qtd_matriculas / 3);
  for (i = 0; i < qtd_matriculas; i++)
  {
    if (i < 0 * tamanho_fatia + tamanho_fatia)
    {
      MPI_Recv(&matriculas[i], 1, MPI_INT, 1, i, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    }
    else if (i < 1 * tamanho_fatia + tamanho_fatia)
    {
      MPI_Recv(&matriculas[i], 1, MPI_INT, 2, i, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    }
    else if (i < qtd_matriculas)
    {
      MPI_Recv(&matriculas[i], 1, MPI_INT, 3, i, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    }
  }
  printf("Matriculas: ");
  print_vet(matriculas, qtd_matriculas);
}

void gera_matriculas(int qtd_matriculas, int id_processo, int qtd_processos)
{
  int start, end, tamanho_fatia, matricula, i;
  tamanho_fatia = (qtd_matriculas / 3);
  start = tamanho_fatia * (id_processo - 1);
  end = start + tamanho_fatia;
  if ((qtd_processos - 1) == id_processo && qtd_matriculas % 3 != 0)
  {
    end = qtd_matriculas;
  }
  for (i = start; i < end; i++)
  {
    matricula = i * id_processo;
    // printf("\nmatricula do aluno %d = %d", i, matricula);
    MPI_Send(&matricula, 1, MPI_INT, 0, i, MPI_COMM_WORLD);
  }
}

void gera_notas(int *notas, int id_processo, int qtd_matriculas)
{
  int i;
  for (i = 0; i < qtd_matriculas; i++)
  {
    int j, nota;
    for (j = 0; j < 4; j++)
    {
      if (id_processo == j)
      {
        nota = (rand() % 100) * (id_processo * j) % 100;
      }
    }
    MPI_Gather(&nota, 1, MPI_INT, &notas[i * 4], 1, MPI_INT, 0, MPI_COMM_WORLD);
  }
}

void calcula_medias(int *notas, int *medias, int qtd_notas, int qtd_matriculas)
{
  int i;
  printf("\nnotas: ");
  print_vet(notas, qtd_notas);
  for (i = 0; i < qtd_matriculas; i++)
  {
    medias[i] = (notas[i * 4] + notas[i * 4 + 1] + notas[i * 4 + 2] + notas[i * 4 + 3]) / 4;
  }
  printf("\nmedias: ");
  print_vet(medias, qtd_matriculas);
}

void maior_media(int *medias, int *matriculas, int qtd_medias)
{
  int maior = 0, index = 0, i;
  for (i = 0; i < qtd_medias; i++)
  {
    if (medias[i] > maior)
    {
      maior = medias[i];
      index = i;
    }
  }
  printf("\nMaior media: %d, matricula %d", maior, matriculas[index]);
}