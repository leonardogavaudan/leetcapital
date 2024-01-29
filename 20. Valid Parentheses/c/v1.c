#include <stdio.h>
#include <string.h>

int isValid(char *s) {
  size_t strSize = strlen(s);
  char stack[strSize];
  size_t stackSize = 0;

  for (int i = 0; i < strSize; i++) {
    if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
      stack[stackSize] = s[i];
      stackSize++;
      continue;
    }

    if (stackSize == 0) {
      return 0;
    }

    char expectedMatchingBracket;
    switch (s[i]) {
    case ')':
      expectedMatchingBracket = '(';
      break;
    case '}':
      expectedMatchingBracket = '{';
      break;
    case ']':
      expectedMatchingBracket = '[';
      break;
    default:
      return 0;
    }

    if (stack[stackSize - 1] != expectedMatchingBracket) {
      return 0;
    }

    stackSize--;
  }

  return stackSize == 0;
}

int main() {
  char *testStrings[] = {"[{()}]", "()", "()[]{}", "(]", "", "([)]", NULL};
  for (size_t i = 0; testStrings[i] != NULL; i++) {
    int res = isValid(testStrings[i]);
    printf("%s - res: %d\n", testStrings[i], res);
  }
  return 0;
}