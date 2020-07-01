#include <stdio.h>

int valida_primo(int numero);

int main() {

  valida_primo(6);

  return 0;
}

int valida_primo(int numero) {
  int i = 0;
  for(i=2; i < numero; i++) {
    if(numero % i == 0) {
      printf("%d nao e primo\n", numero);
      return 0;
    }
  }
  printf("%d e primo\n", numero);
  return 1;
}
