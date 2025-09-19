#include <stddef.h>
#include <stdio.h>
#include <string.h>

#define LINE_LENGTH 100
#define LINES_COUNT 500

int main(void) {
  char buffer[LINE_LENGTH];

  char input[LINES_COUNT][LINE_LENGTH] = {0};
  size_t len = 0;

  for (size_t i = 0; fgets(buffer, LINE_LENGTH, stdin) != NULL; i++, len++) {
    memcpy(input[i], buffer, strlen(buffer));
  }

  for (size_t i = 0; i < len; i++) {
    for (size_t oi = 0; oi < len; oi++) {
      int differences = 0;
      char common_letters[LINE_LENGTH] = {0};
      size_t last = 0;
      for (size_t c = 0; input[i][c] != '\n'; c++) {
        if (input[i][c] == input[oi][c]) {
          common_letters[last++] = input[i][c];
        } else {
          differences++;
        }
      }
      common_letters[last] = '\0';
      if (differences == 1) {
        printf("%s\n", common_letters);
        return 0;
      }
    }
  }

  return 1;
}
