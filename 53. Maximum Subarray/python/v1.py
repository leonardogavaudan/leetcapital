from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = float("-inf")
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum > max:
                max = current_sum

            if current_sum < 0:
                current_sum = 0

        return int(max)
