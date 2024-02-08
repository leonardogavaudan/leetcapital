#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int isPalindrome(int x) {
  if (x < 0) {
    return 0;
  }

  if (x == 0) {
    return 1;
  }

  int numberOfDigits = (int)log10(x) + 1;
  if (numberOfDigits == 1) {
    return 1;
  }

  int xCopy = x;
  int *digitsArray = malloc(sizeof(int) * numberOfDigits);
  for (int i = 0; i < numberOfDigits; i++) {
    digitsArray[i] = xCopy % 10;
    xCopy = xCopy / 10;
  }

  int startCounter = 0;
  int endCounter = numberOfDigits - 1;

  while (startCounter < endCounter) {
    if (digitsArray[startCounter] != digitsArray[endCounter]) {
      return 0;
    }

    startCounter++;
    endCounter--;
  }

  free(digitsArray);

  return 1;
}

int main() {
  int x1 = 1234321;
  int result1 = isPalindrome(x1);
  printf("Input %d - result %d\n", x1, result1);

  int x2 = 1221;
  int result2 = isPalindrome(x2);
  printf("Input %d - result %d\n", x2, result2);

  int x3 = 1234221;
  int result3 = isPalindrome(x3);
  printf("Input %d - result %d\n", x3, result3);

  int x4 = 123221;
  int result4 = isPalindrome(x4);
  printf("Input %d - result %d\n", x4, result4);

  int x5 = -123221;
  int result5 = isPalindrome(x5);
  printf("Input %d - result %d\n", x5, result5);

  int x6 = -12321;
  int result6 = isPalindrome(x6);
  printf("Input %d - result %d\n", x6, result6);
}
