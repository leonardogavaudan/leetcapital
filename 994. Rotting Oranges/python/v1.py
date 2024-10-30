from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        total_oranges_to_rot_count = 0
        oranges_found_count = 0

        seen = set()
        queue = deque([])

        for row in range(ROWS):
            for col in range(COLS):
                total_oranges_to_rot_count += grid[row][col] in [1, 2]
                if grid[row][col] == 2:
                    queue.append((0, row, col))

        while queue:
            minute, row, col = queue.popleft()
            res = max(res, minute)
            oranges_found_count += 1

            neighbours = [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]
            for nr, nc in neighbours:
                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and (nr, nc) not in seen
                    and grid[nr][nc] == 1
                ):
                    seen.add((nr, nc))
                    queue.append((minute + 1, nr, nc))

        return res if oranges_found_count == total_oranges_to_rot_count else -1
