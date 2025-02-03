from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s = set(nums)
        memo = {}

        def dfs(x: int):
            if x in memo:
                return memo[x]

            next_value = x**2
            memo[x] = 1 + dfs(next_value) if next_value in s else 1
            return memo[x]

        res = 0
        for num in s:
            res = max(res, dfs(num))

        return res if res >= 2 else -1
