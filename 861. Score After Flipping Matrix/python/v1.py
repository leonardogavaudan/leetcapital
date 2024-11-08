from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        for r in range(ROWS):
            if grid[r][0] == 0:
                for c in range(COLS):
                    grid[r][c] = not grid[r][c]

        for c in range(COLS):
            count = 0
            for r in range(ROWS):
                count += grid[r][c]

            if count < ROWS / 2:
                for r in range(ROWS):
                    grid[r][c] = not grid[r][c]

        for r in range(ROWS):
            for c in range(COLS):
                res += grid[r][c] * 2 ** (COLS - c - 1)

        return res
