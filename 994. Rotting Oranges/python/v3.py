from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        total_orange_count = 0
        queue = deque([])
        seen = set()
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    total_orange_count += 1
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                    seen.add((r, c))

        while queue:
            row, col, time = queue.popleft()
            res = max(res, time)
            neighbors = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]
            for nr, nc in neighbors:
                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and (nr, nc) not in seen
                    and grid[nr][nc] == 1
                ):
                    seen.add((nr, nc))
                    queue.append((nr, nc, time + 1))

        return res if len(seen) == total_orange_count else -1
