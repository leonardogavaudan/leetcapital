#include <stddef.h>
#include <stdio.h>

long sum_two_smallest_numbers(size_t n, const int numbers[n])
{
  int lowest;
  int second_lowest;

  if (numbers[0] < numbers[1])
  {
    lowest = numbers[0];
    second_lowest = numbers[1];
  }
  else
  {
    lowest = numbers[1];
    second_lowest = numbers[0];
  }

  for (int i = 2; i < n; i++)
  {
    if (numbers[i] < lowest)
    {
      second_lowest = lowest;
      lowest = numbers[i];
    }
    else if (numbers[i] < second_lowest)
    {
      second_lowest = numbers[i];
    }
  }

  return (long)lowest + second_lowest;
}

int main()
{
  int array1[] = {19, 5, 42, 2, 77};
  int array2[] = {10, 343445353, 3453445, 2147483647};

  long result1 = sum_two_smallest_numbers(5, array1);
  long result2 = sum_two_smallest_numbers(4, array2);

  printf("Sum of two smallest in [19, 5, 42, 2, 77]: %ld\n", result1);
  printf("Sum of two smallest in [10, 343445353, 3453445, 2147483647]: %ld\n", result2);

  return 0;
}