from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) < len(dp) and dp[i + len(w)] and s[i : i + len(w)] == w:
                    dp[i] = 1
                    break

        return dp[0] == 1
