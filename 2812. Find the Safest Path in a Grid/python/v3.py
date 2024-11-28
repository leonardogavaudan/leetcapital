from collections import deque
from typing import List
import heapq


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        safety_grid = [[-1] * COLS for _ in range(ROWS)]
        queue = deque([])
        safety_seen = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    queue.append((r, c, 0))
                    safety_seen.add((r, c))

        while queue:
            row, col, safety = queue.popleft()
            safety_grid[row][col] = safety
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for nr, nc in neighbors:
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in safety_seen:
                    safety_seen.add((nr, nc))
                    queue.append((nr, nc, safety + 1))

        path_finding_seen = set()
        priority_queue = [(-safety_grid[0][0], 0, 0)]
        while priority_queue:
            safety, row, col = heapq.heappop(priority_queue)
            safety = -safety
            if (row, col) in path_finding_seen:
                continue
            if (row, col) == (ROWS - 1, COLS - 1):
                return safety
            path_finding_seen.add((row, col))
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for nr, nc in neighbors:
                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and (nr, nc) not in path_finding_seen
                ):
                    heapq.heappush(
                        priority_queue, (-min(safety, safety_grid[nr][nc]), nr, nc)
                    )

        return -1
