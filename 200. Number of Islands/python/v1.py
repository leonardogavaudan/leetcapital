from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        seen = set()
        island_count = 0

        row_count = len(grid)
        col_count = len(grid[0])

        def bfs(row: int, col: int) -> None:
            queue = deque([(row, col)])
            seen.add((row, col))

            while queue:
                current_row, current_col = queue.popleft()

                neighbors = [
                    [current_row + 1, current_col],
                    [current_row - 1, current_col],
                    [current_row, current_col + 1],
                    [current_row, current_col - 1],
                ]

                for neighbor_row, neighbor_col in neighbors:
                    if (
                        0 <= neighbor_row < row_count
                        and 0 <= neighbor_col < col_count
                        and grid[neighbor_row][neighbor_col] == "1"
                        and (neighbor_row, neighbor_col) not in seen
                    ):
                        seen.add((neighbor_row, neighbor_col))
                        queue.append((neighbor_row, neighbor_col))

        for r in range(row_count):
            for c in range(col_count):
                if grid[r][c] == "1" and (r, c) not in seen:
                    bfs(r, c)
                    island_count += 1

        return island_count
