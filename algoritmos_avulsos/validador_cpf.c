#include <stdio.h>
#include <string.h>
#include <ctype.h>

int valida_cpf(char cpf_full[]);

int main() {
  char cpf_full[] = "";

  int is_valid = valida_cpf(cpf_full);
  if(is_valid) {
    printf("CPF valido \n");
    return 1;
  }
  printf("CPF invalido \n");
  return 0;
}

int valida_cpf(char cpf_full[]) {
  char cpf[11];
  int count = 0;
  int acc = 0;

  int i = 0;
  for(i = 0; i < strlen(cpf_full); i++) {
    if(isdigit(cpf_full[i])) {
      cpf[count] = cpf_full[i];
      count++;
      acc = acc + (cpf_full[i] - '0');
    }
  }

  char cpf_acc[2];
  sprintf(cpf_acc, "%d", acc);

  if(cpf_acc[0] == cpf_acc[1]) {
    return 1;
  }

  return 0;
}
