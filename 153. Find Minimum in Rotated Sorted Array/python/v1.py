from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return min(nums)

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[(mid - 1) % len(nums)] > nums[mid] < nums[(mid + 1) % len(nums)]:
                return nums[mid]
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        raise AssertionError("Problem should have solution")
