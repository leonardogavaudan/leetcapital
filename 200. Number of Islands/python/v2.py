from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        island_count = 0
        visited = set()

        def bfs(r: int, c: int):
            visited.add((r, c))
            queue = deque([(r, c)])

            while queue:
                row, col = queue.popleft()

                neighbors = [
                    [row - 1, col],
                    [row + 1, col],
                    [row, col - 1],
                    [row, col + 1],
                ]
                for neighbor_row, neighbor_col in neighbors:
                    if (
                        -1 < neighbor_row < ROWS
                        and -1 < neighbor_col < COLS
                        and grid[neighbor_row][neighbor_col] == "1"
                        and (neighbor_row, neighbor_col) not in visited
                    ):
                        queue.append((neighbor_row, neighbor_col))
                        visited.add((neighbor_row, neighbor_col))

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visited and grid[row][col] == "1":
                    bfs(row, col)
                    island_count += 1

        return island_count
