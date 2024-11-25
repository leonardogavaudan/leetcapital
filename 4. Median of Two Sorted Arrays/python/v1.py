from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums2) < len(nums1):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            left_A = A[i] if i >= 0 else float("-inf")
            right_A = A[i + 1] if i + 1 < len(A) else float("inf")

            j = half - i - 2
            left_B = B[j] if j >= 0 else float("-inf")
            right_B = B[j + 1] if j + 1 < len(B) else float("inf")

            if left_A <= right_B and left_B <= right_A:
                if total % 2 == 1:
                    return min(right_A, right_B)
                else:
                    return (max(left_A, left_B) + min(right_A, right_B)) / 2
            elif left_A > right_B:
                r = i - 1
            else:
                l = i + 1
