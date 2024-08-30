from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            index = (l + r + 1) // 2
            if nums[index] == target:
                return index
            elif nums[index] > target:
                r = index - 1
            elif nums[index] < target:
                l = index + 1

        if nums[index] < target:
            return index + 1
        else:
            return index
