void merge(int *nums1, int nums1Size, int m, int *nums2, int nums2Size, int n) {
  int *endPtr = nums1 + nums1Size - 1;
  int *endPtr1 = nums1 + m - 1;
  int *endPtr2 = nums2 + n - 1;
  while (endPtr >= nums1) {
    if (endPtr1 >= nums1 && (endPtr2 < nums2 || *endPtr1 > *endPtr2)) {
      *endPtr = *endPtr1;
      endPtr1--;
    } else {
      *endPtr = *endPtr2;
      endPtr2--;
    }
    endPtr--;
  }
}
