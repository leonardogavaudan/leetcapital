#include <stdio.h>
#include <stdlib.h>

int *twoSum(int *nums, int numsSize, int target, int *returnSize) {
  for (int i = 0; i < numsSize - 1; i++) {
    for (int k = i + 1; k < numsSize; k++) {
      if (nums[i] + nums[k] == target) {
        *returnSize = 2;
        int *result = malloc(2 * sizeof(int));
        *result = i;
        *(result + 1) = k;
        return result;
      }
    }
  }

  *returnSize = 0;
  return NULL;
}

int main() {
  int nums[] = {3, 5, 1, 4, 9};
  int numSize = 5;
  int target = 10;
  int returnSize = 0;

  int *result = twoSum(nums, numSize, target, &returnSize);

  if (result == NULL) {
    printf("No match found");
    return 0;
  }

  for (int i = 0; i < returnSize; i++) {
    printf("Index %d: %d\n", result[i], nums[result[i]]);
  }

  free(result);
  return 0;
}
