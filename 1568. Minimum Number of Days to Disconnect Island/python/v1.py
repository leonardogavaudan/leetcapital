from collections import deque
from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(row, col, seen):
            queue = deque([(row, col)])
            seen.add((row, col))

            while queue:
                r, c = queue.popleft()
                neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for nr, nc in neighbors:
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        if (nr, nc) not in seen:
                            seen.add((nr, nc))
                            queue.append((nr, nc))

        def count_islands():
            count = 0
            seen = set()
            for row in range(ROWS):
                for col in range(COLS):
                    if (row, col) not in seen and grid[row][col] == 1:
                        bfs(row, col, seen)
                        count += 1
            return count

        count = count_islands()
        if count != 1:
            return 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    continue

                grid[r][c] = 0
                count = count_islands()
                if count != 1:
                    return 1

                grid[r][c] = 1

        return 2
