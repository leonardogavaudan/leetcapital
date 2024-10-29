from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])

        prev_row = points[0].copy()

        for r in range(1, ROWS):
            next_row = points[r].copy()

            left = [0] * COLS
            right = [0] * COLS

            left[0] = prev_row[0]
            for i in range(1, COLS):
                left[i] = max(prev_row[i], left[i - 1] - 1)

            right[-1] = prev_row[-1]
            for i in range(COLS - 2, -1, -1):
                right[i] = max(prev_row[i], right[i + 1] - 1)

            for i in range(COLS):
                next_row[i] += max(left[i], right[i])

            prev_row = next_row

        return max(prev_row)
