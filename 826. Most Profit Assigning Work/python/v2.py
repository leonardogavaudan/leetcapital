from typing import List


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        worker.sort(reverse=True)
        diff_profit_arr = sorted(zip(difficulty, profit), key=lambda x: (-x[0], x[1]))
        max_profit = 0
        res = 0

        while worker:
            while diff_profit_arr and worker[-1] >= diff_profit_arr[-1][0]:
                max_profit = max(max_profit, diff_profit_arr.pop()[1])
            worker.pop()
            res += max_profit

        return res
