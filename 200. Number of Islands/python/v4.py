from collections import deque
from typing import List, Set, Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        seen = set()

        def bfs(row: int, col: int, seen: Set[Tuple[int, int]]):
            nonlocal grid
            queue = deque([(row, col)])
            while queue:
                row, col = queue.popleft()
                neighbours = [
                    (row + 1, col),
                    (row - 1, col),
                    (row, col + 1),
                    (row, col - 1),
                ]
                for nr, nc in neighbours:
                    if (
                        0 <= nr < len(grid)
                        and 0 <= nc < len(grid[0])
                        and grid[nr][nc] == "1"
                        and (nr, nc) not in seen
                    ):
                        seen.add((nr, nc))
                        queue.append((nr, nc))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in seen:
                    seen.add((r, c))
                    bfs(r, c, seen)
                    res += 1

        return res
