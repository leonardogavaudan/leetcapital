import math


class Solution:
    def minSteps(self, n: int) -> int:
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(1, n + 1):
            for j in range(1, math.floor(i**0.5) + 1):
                if i % j == 0:
                    solution1 = dp[j] + (i // j)
                    solution2 = dp[i // j] + j
                    dp[i] = min(dp[i], solution1, solution2)
        return dp[n]
