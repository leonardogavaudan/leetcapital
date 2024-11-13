from collections import deque
import heapq
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        queue = deque([])
        seen = set()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    queue.append((0, row, col))
                    seen.add((row, col))

        safeness_grid = [row.copy() for row in grid]
        while queue:
            safeness, row, col = queue.popleft()
            safeness_grid[row][col] = safeness
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for nr, nc in neighbors:
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    queue.append((safeness + 1, nr, nc))

        nodes_seen = set()
        heap = [(-safeness_grid[0][0], 0, 0)]

        while heap:
            safeness, row, col = heapq.heappop(heap)
            safeness *= -1
            if (row, col) == (ROWS - 1, COLS - 1):
                return safeness

            if (row, col) in nodes_seen:
                continue
            nodes_seen.add((row, col))

            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for nr, nc in neighbors:
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in nodes_seen:
                    heapq.heappush(
                        heap, (-min(safeness, safeness_grid[nr][nc]), nr, nc)
                    )

        return -1
