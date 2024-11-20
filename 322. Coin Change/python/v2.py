from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for sub_amount in range(1, amount + 1):
            for coin in coins:
                if coin <= sub_amount:
                    dp[sub_amount] = min(dp[sub_amount], dp[sub_amount - coin] + 1)

        return dp[amount] if dp[amount] <= amount else -1
