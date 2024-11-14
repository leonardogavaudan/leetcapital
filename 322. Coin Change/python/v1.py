from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount + 1] * amount

        for target in range(1, amount + 1):
            for coin in coins:
                if coin <= target:
                    dp[target] = min(dp[target], dp[target - coin] + 1)

        return dp[amount] if dp[amount] <= amount else -1
