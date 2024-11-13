from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        flipped = [row.copy() for row in grid]
        for row in flipped:
            if row[0] == 0:
                for i in range(COLS):
                    row[i] = 1 if row[i] == 0 else 0

        for col in range(COLS):
            total = sum(row[col] for row in flipped)
            res += max(total, ROWS - total) * 2 ** (COLS - col - 1)

        return res
