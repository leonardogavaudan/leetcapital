from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        prev = nums[0]
        curr = max(nums[:2])
        i = 2
        while i < len(nums):
            new = max(prev + nums[i], curr)
            prev = curr
            curr = new
            i += 1

        return curr
