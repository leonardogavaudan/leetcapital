import heapq
from typing import List
from collections import deque


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque([])
        bfs_seen = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    queue.append((0, r, c))

        safeness_grid = [[-1] * COLS for _ in range(ROWS)]
        while queue:
            safeness, r, c = queue.popleft()
            safeness_grid[r][c] = safeness

            neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in neighbors:
                if (
                    0 <= nr < ROWS
                    and 0 <= nc < COLS
                    and grid[nr][nc] == 0
                    and (nr, nc) not in bfs_seen
                ):
                    queue.append((safeness + 1, nr, nc))
                    bfs_seen.add((nr, nc))

        node_to_safeness = {}
        heap = [(-safeness_grid[0][0], 0, 0)]

        while heap:
            safeness_score, row, col = heapq.heappop(heap)
            safeness_score = -safeness_score
            if (row, col) in node_to_safeness and safeness_score <= node_to_safeness[
                (row, col)
            ]:
                continue

            node_to_safeness[(row, col)] = safeness_score

            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for nr, nc in neighbors:
                if not (0 <= nr < ROWS) or not (0 <= nc < COLS):
                    continue

                new_safeness_score = min(safeness_score, safeness_grid[nr][nc])
                if (
                    nr,
                    nc,
                ) not in node_to_safeness or new_safeness_score > node_to_safeness[
                    (nr, nc)
                ]:
                    heapq.heappush(heap, (-new_safeness_score, nr, nc))

        return node_to_safeness[(ROWS - 1, COLS - 1)]
