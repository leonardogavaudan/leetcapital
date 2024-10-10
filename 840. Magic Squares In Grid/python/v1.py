from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        if ROWS < 3 and COLS < 3:
            return 0

        res = 0

        for row in range(ROWS - 2):
            for col in range(COLS - 2):
                numbers = set(
                    [grid[row + r][col + c] for r in range(3) for c in range(3)]
                )

                if len(numbers) != 9:
                    continue

                if numbers.intersection(set([0, 10, 11, 12, 13, 14, 15])):
                    continue

                valid = True
                expected = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]

                # rows
                for i in range(1, 3):
                    if (
                        grid[row + i][col]
                        + grid[row + i][col + 1]
                        + grid[row + i][col + 2]
                        != expected
                    ):
                        valid = False
                        break
                if not valid:
                    continue

                # columns
                for i in range(3):
                    if (
                        grid[row][col + i]
                        + grid[row + 1][col + i]
                        + grid[row + 2][col + i]
                        != expected
                    ):
                        valid = False
                        break
                if not valid:
                    continue

                # diagonals
                if sum([grid[row + i][col + i] for i in range(3)]) != expected:
                    continue
                if sum([grid[row + abs(i - 2)][col + i] for i in range(3)]) != expected:
                    continue

                res += 1

        return res
