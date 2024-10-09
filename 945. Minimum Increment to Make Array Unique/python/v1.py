from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        res = 0

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i - 1] >= sorted_nums[i]:
                diff = sorted_nums[i - 1] - sorted_nums[i]
                res += diff + 1
                sorted_nums[i] = sorted_nums[i - 1] + 1

        return res
