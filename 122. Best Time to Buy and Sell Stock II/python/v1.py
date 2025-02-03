from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        price_bought = None
        for i, curr_price in enumerate(prices):
            if price_bought is None:
                price_bought = curr_price

            if i == len(prices) - 1 or prices[i + 1] < prices[i]:
                profit += curr_price - price_bought
                price_bought = None

        return profit
