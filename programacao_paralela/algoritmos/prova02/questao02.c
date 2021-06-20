#include <stdio.h>
#include <stdlib.h>
#include "mpi.h"

int main()
{
  int qtd_processos;
  int id_processo;

  int x, y, w, z, sum;

  MPI_Init(NULL, NULL);
  MPI_Comm_size(MPI_COMM_WORLD, &qtd_processos);
  MPI_Comm_rank(MPI_COMM_WORLD, &id_processo);

  switch (id_processo)
  {
  case 0:
    x = id_processo;
    printf("\nx inicial: %d", x);
    MPI_Send(&x, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
    MPI_Recv(&y, 1, MPI_INT, 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

    x = y + 1;

    MPI_Recv(&y, 1, MPI_INT, 1, 1, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    MPI_Recv(&w, 1, MPI_INT, 2, 1, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    MPI_Recv(&z, 1, MPI_INT, 3, 1, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

    sum = x + y + w + z;

    MPI_Send(&sum, 1, MPI_INT, 1, 2, MPI_COMM_WORLD);
    MPI_Send(&sum, 1, MPI_INT, 2, 2, MPI_COMM_WORLD);
    MPI_Send(&sum, 1, MPI_INT, 3, 2, MPI_COMM_WORLD);

    x = sum * 2;

    MPI_Send(&x, 1, MPI_INT, 1, 3, MPI_COMM_WORLD);
    MPI_Recv(&w, 1, MPI_INT, 3, 3, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

    x = w + 10;

    MPI_Recv(&y, 1, MPI_INT, 1, 4, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    MPI_Recv(&w, 1, MPI_INT, 2, 4, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
    MPI_Recv(&z, 1, MPI_INT, 3, 4, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

    sum = x + y + w + z;

    printf("\nSomatorio final: %d", sum);
    break;

  case 1:
    y = id_processo;
    printf("\ny inicial: %d", y);
    MPI_Send(&y, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
    MPI_Recv(&x, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

    y = x + 2;

    MPI_Send(&y, 1, MPI_INT, 0, 1, MPI_COMM_WORLD);
    MPI_Recv(&sum, 1, MPI_INT, 0, 2, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

    y = sum * 3;

    MPI_Send(&y, 1, MPI_INT, 2, 3, MPI_COMM_WORLD);
    MPI_Recv(&x, 1, MPI_INT, 0, 3, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

    y = x + 11;

    MPI_Send(&y, 1, MPI_INT, 0, 4, MPI_COMM_WORLD);
    break;

  case 2:
    w = id_processo;
    printf("\nw inicial: %d", w);
    MPI_Send(&w, 1, MPI_INT, 3, 0, MPI_COMM_WORLD);
    MPI_Recv(&z, 1, MPI_INT, 3, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

    w = z + 3;

    MPI_Send(&w, 1, MPI_INT, 0, 1, MPI_COMM_WORLD);
    MPI_Recv(&sum, 1, MPI_INT, 0, 2, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

    w = sum * 4;

    MPI_Send(&w, 1, MPI_INT, 3, 3, MPI_COMM_WORLD);
    MPI_Recv(&y, 1, MPI_INT, 1, 3, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

    w = y + 12;

    MPI_Send(&w, 1, MPI_INT, 0, 4, MPI_COMM_WORLD);
    break;
  case 3:
    z = id_processo;
    printf("\nz inicial: %d", z);
    MPI_Send(&z, 1, MPI_INT, 2, 0, MPI_COMM_WORLD);
    MPI_Recv(&w, 1, MPI_INT, 2, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

    z = w + 4;

    MPI_Send(&z, 1, MPI_INT, 0, 1, MPI_COMM_WORLD);
    MPI_Recv(&sum, 1, MPI_INT, 0, 2, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

    z = sum * 5;

    MPI_Send(&z, 1, MPI_INT, 0, 3, MPI_COMM_WORLD);
    MPI_Recv(&w, 1, MPI_INT, 2, 3, MPI_COMM_WORLD, MPI_STATUS_IGNORE);

    z = w + 13;

    MPI_Send(&z, 1, MPI_INT, 0, 4, MPI_COMM_WORLD);
    break;
  default:
    break;
  }

  MPI_Finalize();
  printf("\n");
  return 0;
}