from typing import List


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        difficulty_to_profit_arr = [0] * (max(difficulty) + 1)
        for i, p in enumerate(profit):
            difficulty_to_profit_arr[difficulty[i]] = max(
                difficulty_to_profit_arr[difficulty[i]], p
            )

        max_profit = 0
        for i in range(len(difficulty_to_profit_arr)):
            max_profit = max(max_profit, difficulty_to_profit_arr[i])
            difficulty_to_profit_arr[i] = max_profit

        return sum(
            (
                (
                    difficulty_to_profit_arr[d]
                    if d < len(difficulty_to_profit_arr)
                    else difficulty_to_profit_arr[-1]
                )
                for d in worker
            )
        )
