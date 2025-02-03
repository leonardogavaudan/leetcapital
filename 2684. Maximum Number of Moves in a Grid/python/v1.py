from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        for col in range(1, COLS):
            alive = False

            for row in range(ROWS):
                if any(
                    0 <= r < ROWS
                    and grid[r][col - 1] != -1
                    and grid[r][col - 1] < grid[row][col]
                    for r in [row - 1, row, row + 1]
                ):
                    alive = True
                else:
                    grid[row][col] = -1

            if not alive:
                return col - 1

        return COLS - 1
