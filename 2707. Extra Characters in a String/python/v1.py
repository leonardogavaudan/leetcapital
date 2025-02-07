from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        N = len(s)
        dp = [[N] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = 0 if s[i] in dictionary else 1

        for length in range(2, N + 1):
            for i in range(N + 1 - length):
                j = i + length - 1
                main_sub_str = s[i : j + 1]
                if main_sub_str in dictionary:
                    dp[i][j] = 0
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])

        return dp[0][N - 1]
