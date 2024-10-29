from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        seen = set()

        def bfs(row: int, col: int):
            queue = deque([(row, col)])

            while queue:
                r, c = queue.popleft()
                neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

                for neighbor_row, neighor_col in neighbors:
                    if (
                        0 <= neighbor_row < ROWS
                        and 0 <= neighor_col < COLS
                        and grid[neighbor_row][neighor_col] == "1"
                        and (neighbor_row, neighor_col) not in seen
                    ):
                        queue.append((neighbor_row, neighor_col))
                        seen.add((neighbor_row, neighor_col))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in seen:
                    bfs(row, col)
                    res += 1

        return res
