from bisect import bisect_left
from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]

        result = []
        for q in queries:
            idx = bisect_left(nums, q)
            left_cost = q * idx - prefix_sums[idx]
            right_cost = (prefix_sums[-1] - prefix_sums[idx]) - q * (len(nums) - idx)
            result.append(left_cost + right_cost)

        return result
