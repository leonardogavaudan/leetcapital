from itertools import islice
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        COLS = len(matrix[0])
        prev_row = [int(x) for x in matrix[0]]
        max_area = max(prev_row)

        for row in islice(matrix, 1, None):
            curr_row = [
                int(row[i]) + prev_row[i] if row[i] != "0" else 0 for i in range(COLS)
            ]

            stack = []
            curr_row.append(0)
            for i, num in enumerate(curr_row):
                while stack and curr_row[stack[-1]] > num:
                    height = curr_row[stack.pop()]
                    length = i - 1 - (stack[-1] if stack else -1)
                    side = min(height, length)
                    max_area = max(max_area, side**2)

                stack.append(i)

            prev_row = curr_row

        return max_area
