from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (max(days) + 1)
        days_set = set(days)

        costs[0] = min(costs)
        costs[1] = min(costs[1], costs[2])

        for day in range(1, max(days) + 1):
            if day not in days_set:
                dp[day] = dp[day - 1]
            else:
                dp[day] = min(
                    dp[day - 1] + costs[0],
                    dp[max(0, day - 7)] + costs[1],
                    dp[max(0, day - 30)] + costs[2],
                )

        return dp[max(days)]
