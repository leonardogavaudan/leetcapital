from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best = 0
        left = []
        for v in values:
            best = max(best + 1, v)
            left.append(best)

        best = 0
        right = []
        for v in reversed(values):
            best = max(best + 1, v)
            right.append(best)
        right = right[::-1]

        res = 0
        for i in range(len(values)):
            res = max(
                res,
                values[i] + (right[i - 1] if i - 1 >= 0 else 0),
                values[i] + (left[i + 1] if i + 1 < len(values) else 0),
            )

        return res
