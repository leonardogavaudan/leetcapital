from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[0] = 0

        for i in range(1, len(nums)):
            dp[i] = 1 + min(dp[j] for j in range(i) if j + nums[j] >= i)

        return int(dp[len(nums) - 1])
