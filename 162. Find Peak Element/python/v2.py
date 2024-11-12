from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[len(nums) - 1] > nums[len(nums) - 2]:
            return len(nums) - 1

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1

        return -1