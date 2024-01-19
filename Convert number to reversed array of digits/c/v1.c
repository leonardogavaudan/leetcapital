#include <stddef.h>
#include <inttypes.h>
#include <stdio.h>

void digitize(uint64_t n, uint8_t digits[], size_t *length_out)
{
  uint64_t nCopy = n;
  *length_out = 0;

  do
  {
    nCopy /= 10;
    (*length_out)++;
  } while (nCopy != 0);

  nCopy = n;
  for (int i = 0; i < *length_out; i++)
  {
    *(digits + i) = nCopy % 10;
    nCopy /= 10;
  }
}

int main()
{
  uint64_t number = 35231;
  uint8_t digits[20]; // Assuming the max number of digits won't exceed 20
  size_t length = 0;

  digitize(number, digits, &length);

  printf("Reversed digits: [");
  for (size_t i = 0; i < length; i++)
  {
    printf("%d", digits[i]);
    if (i < length - 1)
    {
      printf(", ");
    }
  }
  printf("]\n");

  return 0;
}