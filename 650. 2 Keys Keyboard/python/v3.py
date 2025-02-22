class Solution:
    def minSteps(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[1] = 0
        for i in range(2, n + 1):
            for j in range(1, int(i**0.5) + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j, dp[i // j] + j)

        return int(dp[n])
