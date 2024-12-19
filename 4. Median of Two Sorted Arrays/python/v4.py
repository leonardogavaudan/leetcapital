from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        half = (len(nums1) + len(nums2) + 1) // 2
        l, r = 0, len(nums1)
        while l <= r:
            partitionX = (l + r) // 2
            partitionY = half - partitionX

            leftX = nums1[partitionX - 1] if partitionX > 0 else float("-inf")
            rightX = nums1[partitionX] if partitionX < len(nums1) else float("inf")

            leftY = nums2[partitionY - 1] if partitionY > 0 else float("-inf")
            rightY = nums2[partitionY] if partitionY < len(nums2) else float("inf")

            if leftX <= rightY and leftY <= rightX:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(leftX, leftY) + min(rightX, rightY)) / 2
                else:
                    return max(leftX, leftY)
            elif leftX > rightY:
                r = partitionX - 1
            else:
                l = partitionX + 1

        raise AssertionError("No valid partition found")
