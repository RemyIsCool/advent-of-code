#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define INPUT_LENGTH 100

int main(void) {
  FILE *input_ptr = fopen("input.txt", "r");
  char input[INPUT_LENGTH];

  int hit_points, damage;

  for (int i = 0; fgets(input, INPUT_LENGTH, input_ptr); i++) {
    int num = atoi(strchr(input, ':') + 2);

    if (i == 0) {
      hit_points = num;
    } else {
      damage = num;
    }
  }

  printf("Hit Points: %d\nDamage: %d\n", hit_points, damage);

  return 0;
}
