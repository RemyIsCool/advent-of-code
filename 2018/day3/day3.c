#include "stdbool.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#define FILE_SIZE 25

typedef struct {
  int x;
  int y;
  int w;
  int h;
} Claim;

int main() {
  FILE *input_file = fopen("input.txt", "r");

  char input[FILE_SIZE];

  Claim claims[1500];
  int numClaims = 0;

  while (fgets(input, FILE_SIZE, input_file)) {
    char *text = strstr(input, "@") + 2;
    text[strlen(text) - 1] = '\0';

    char *pos_str = strtok(text, ": ");
    char *dims_str = strtok(NULL, ": ");

    int x = atoi(strtok(pos_str, ","));
    int y = atoi(strtok(NULL, ","));

    int w = atoi(strtok(dims_str, "x"));
    int h = atoi(strtok(NULL, "x"));

    claims[numClaims] = (Claim){x, y, w, h};

    numClaims++;
  }

  int total = 0;

  for (int x = 0; x < 1000; x++) {
    for (int y = 0; y < 1000; y++) {
      int regions = 0;

      for (int i = 0; i < numClaims; i++) {
        Claim claim = claims[i];
        if (x >= claim.x && x < claim.x + claim.w && y > claim.y &&
            y <= claim.y + claim.h) {
          regions++;
        }
        if (regions >= 2) {
          total++;
          break;
        }
      }
    }
  }

  printf("part 1: %d\n", total);

  for (int i = 0; i < numClaims; i++) {
    Claim claim1 = claims[i];

    bool has_overlap = false;

    for (int j = 0; j < numClaims; j++) {
      if (i == j)
        continue;

      Claim claim2 = claims[j];

      if (claim1.x < claim2.x + claim2.w && claim1.x + claim1.w > claim2.x &&
          claim1.y < claim2.y + claim2.h && claim1.y + claim1.h > claim2.y) {
        has_overlap = true;
      }
    }

    if (!has_overlap) {
      printf("part 2: %d\n", i + 1);
    }
  }

  return 0;
}
