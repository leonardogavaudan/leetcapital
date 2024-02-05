#include <stddef.h>
#include <stdio.h>

void merge(int *nums1, int nums1Size, int m, int *nums2, int nums2Size, int n) {
  if (m == 0) {
    for (int i = 0; i < n; i++) {
      nums1[i] = nums2[i];
    }
    return;
  }

  int nums1Copy[m];
  for (int i = 0; i < m; i++) {
    nums1Copy[i] = nums1[i];
  }

  size_t nums1CopyCounter = 0;
  size_t nums2Counter = 0;
  size_t numsTotalCounter = 0;

  while (nums1CopyCounter < m && nums2Counter < n) {
    if (nums1Copy[nums1CopyCounter] <= nums2[nums2Counter]) {
      nums1[numsTotalCounter] = nums1Copy[nums1CopyCounter++];
    } else {
      nums1[numsTotalCounter] = nums2[nums2Counter++];
    }
    numsTotalCounter++;
  }

  while (nums1CopyCounter < m) {
    nums1[numsTotalCounter++] = nums1Copy[nums1CopyCounter++];
  }

  while (nums2Counter < n) {
    nums1[numsTotalCounter++] = nums2[nums2Counter++];
  }
}

int main() {
  int nums1[] = {1, 3, 4, 7, 0, 0, 0, 0};
  int nums2[] = {2, 5, 6, 8};
  int nums1Size = 8;
  int nums2Size = 4;

  merge(nums1, nums1Size, 4, nums2, nums2Size, nums2Size);

  printf("Merged sorted array: ");
  for (int i = 0; i < (nums1Size); i++) {
    printf("%d ", nums1[i]);
  }
}