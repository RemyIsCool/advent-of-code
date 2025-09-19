#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define LINE_LEN 100
#define GRID_SIZE 5000

int main(void) {
  int **grid = (int **)malloc(GRID_SIZE * sizeof(int));
  for (size_t i = 0; i < GRID_SIZE; i++) {
    grid[i] = (int *)malloc(GRID_SIZE * sizeof(int));
    for (size_t j = 0; j < GRID_SIZE; j++) {
      grid[i][j] = 0;
    }
  }

  char buffer[LINE_LEN];

  while (fgets(buffer, LINE_LEN, stdin)) {
    char x[10];
    char y[10];
    char w[10];
    char h[10];

    bool found_at = false;
    for (char *c = buffer; *c != '\n'; c++) {
      if (!found_at) {
        while (*c != '@') {
          c++;
        }
        found_at = true;
        c += 2;
      }
      printf("%c", *c);
    }
    printf("\n");
  }

  return 0;
}
