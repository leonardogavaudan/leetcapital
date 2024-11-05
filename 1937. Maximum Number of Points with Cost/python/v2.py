from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])
        current_row = points[0]

        for r in range(1, ROWS):
            next_row = points[r]

            left = current_row.copy()
            for i in range(1, COLS):
                left[i] = max(left[i - 1] - 1, left[i])
            right = current_row.copy()
            for i in range(COLS - 2, -1, -1):
                right[i] = max(right[i + 1] - 1, right[i])

            for i in range(COLS):
                current_row[i] = next_row[i] + max(left[i], right[i])

        return max(current_row)
