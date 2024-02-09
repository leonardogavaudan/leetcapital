#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *longestCommonPrefix(char **strs, int strsSize) {
  if (strsSize == 0) {
    char *empty = malloc(1);
    empty[0] = '\0';
    return empty;
  }

  int firstStringLength = strlen(strs[0]);
  char *longest = malloc(firstStringLength + 1);
  strcpy(longest, strs[0]);

  for (int i = 1; i < strsSize; i++) {
    int j = 0;
    while (longest[j] && strs[i][j] && longest[j] == strs[i][j]) {
      j++;
    }
    longest[j] = '\0';
    if (j == 0) {
      break;
    }
  }

  return longest;
}

int main() {
  char *str[4] = {"test", "test", "tes", "te"};

  char *longestPrefix = longestCommonPrefix(str, 4);

  printf("Input: ");
  for (int i = 0; i < 4; i++) {
    printf("%s ", str[i]);
  }

  printf("\nLongest common prefix is: %s \n", longestPrefix);
  free(longestPrefix);
}
