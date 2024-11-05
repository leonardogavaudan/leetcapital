from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        seen = set()
        total_orange_count = 0
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] in [1, 2]:
                    total_orange_count += 1
                if grid[r][c] == 2:
                    queue.append((0, r, c))

        count = 0
        while queue:
            minutes, row, col = queue.popleft()
            res = max(res, minutes)
            count += 1
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

            for nr, nc in neighbors:
                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and grid[nr][nc] == 1
                    and (nr, nc) not in seen
                ):
                    queue.append((minutes + 1, nr, nc))
                    seen.add((nr, nc))

        return res if count == total_orange_count else -1
