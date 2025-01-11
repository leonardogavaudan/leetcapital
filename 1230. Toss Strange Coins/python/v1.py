from typing import List


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [[0] * (len(prob) + 1) for _ in range(len(prob))]
        dp[0][0] = 1 - prob[0]
        dp[0][1] = prob[0]

        for c in range(1, len(prob)):
            for t in range(0, c + 2):
                if t > 0:
                    dp[c][t] += dp[c - 1][t - 1] * prob[c]
                dp[c][t] += dp[c - 1][t] * (1 - prob[c])

        return dp[len(prob) - 1][target]
