from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        best = 0
        for v in values:
            res = max(res, v + best)
            best = max(best - 1, v - 1)

        return res
