from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        prev_solution = nums[0]
        curr_solution = max(nums[:2])

        i = 2
        next_solution = 0
        while i < len(nums):
            next_solution = max(prev_solution + nums[i], curr_solution)
            prev_solution = curr_solution
            curr_solution = next_solution
            i += 1

        return next_solution
