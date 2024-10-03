from typing import List, Set, Tuple


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        ROWS1, COLS1 = len(grid), len(grid[0])
        ROWS2, COLS2 = ROWS1 * 3, COLS1 * 3

        grid2 = [[0] * COLS2 for _ in range(ROWS2)]

        for r1 in range(ROWS1):
            r2 = 3 * r1
            for c1 in range(COLS1):
                c2 = 3 * c1

                if grid[r1][c1] == "/":
                    grid2[r2][c2 + 2] = 1
                    grid2[r2 + 1][c2 + 1] = 1
                    grid2[r2 + 2][c2] = 1
                elif grid[r1][c1] == "\\":
                    grid2[r2][c2] = 1
                    grid2[r2 + 1][c2 + 1] = 1
                    grid2[r2 + 2][c2 + 2] = 1

        def bfs(seen: Set[Tuple[int, int]], r: int, c: int):
            if (
                not 0 <= r < ROWS2
                or not 0 <= c < COLS2
                or (r, c) in seen
                or grid2[r][c] == 1
            ):
                return

            seen.add((r, c))

            neighbors = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]
            for nr, nc in neighbors:
                bfs(seen, nr, nc)

        seen = set()
        res = 0

        for r in range(ROWS2):
            for c in range(COLS2):
                if grid2[r][c] == 0 and (r, c) not in seen:
                    bfs(seen, r, c)
                    res += 1

        return res
