class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        res = 0
        dp = [[0] * N for _ in range(N)]

        for i in range(N):
            dp[i][i] = 1
            res += 1

        for length in range(2, N + 1):
            for i in range(N + 1 - length):
                j = i + length - 1

                if s[i] == s[j] and (i == j - 1 or dp[i + 1][j - 1] == 1):
                    dp[i][j] = 1
                    res += 1

        return res
