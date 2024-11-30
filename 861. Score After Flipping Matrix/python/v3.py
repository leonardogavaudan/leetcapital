from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        for row in range(ROWS):
            if grid[row][0] == 0:
                for col in range(COLS):
                    grid[row][col] ^= 1

        res = 0
        for col in range(COLS):
            total = sum(grid[row][col] for row in range(ROWS))
            res += 2 ** (COLS - 1 - col) * max(total, ROWS - total)

        return res
