from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        prev, current = nums[0], max(nums[0], nums[1])
        i = 2
        while i < len(nums):
            next = max(prev + nums[i], current)
            prev = current
            current = next
            i += 1
        return current
