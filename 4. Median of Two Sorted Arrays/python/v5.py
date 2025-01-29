from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half = (m + n + 1) // 2

        while left <= right:
            i = (left + right) // 2
            j = half - i

            leftA = float("-inf") if i == 0 else nums1[i - 1]
            rightA = float("inf") if i == m else nums1[i]
            leftB = float("-inf") if j == 0 else nums2[j - 1]
            rightB = float("inf") if j == n else nums2[j]

            if leftA <= rightB and leftB <= rightA:
                if (m + n) % 2:
                    return max(leftA, leftB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
            elif leftA > rightB:
                right = i - 1
            else:
                left = i + 1
