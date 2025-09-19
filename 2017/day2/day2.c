#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
  FILE *input_stream = fopen("input.txt", "r");
  const int buf_size = 1000;
  char buf[buf_size];

  int total_checksum = 0;

  while (fgets(buf, buf_size, input_stream)) {
    char number[10];
    int number_index = 0;

    int all_numbers[25];
    int all_numbers_count = 0;

    for (char *curr = buf; *curr != '\0'; curr++) {
      if (isspace(*curr)) {
        number[number_index] = '\0';
        number_index = 0;

        all_numbers[all_numbers_count++] = atoi(number);

        continue;
      }

      number[number_index++] = *curr;
    }

    int found_result = 0;
    for (int i = 0; i < all_numbers_count; i++) {
      for (int j = 0; j < all_numbers_count; j++) {
        if (i == j)
          continue;

        if (all_numbers[i] % all_numbers[j] == 0) {
          found_result = all_numbers[i] / all_numbers[j];
        }
      }
    }
    total_checksum += found_result;
  }

  printf("%d\n", total_checksum);

  return 0;
}
