from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        max_local = [[0] * (len(grid) - 2) for _ in range(len(grid) - 2)]

        for row in range(len(max_local)):
            for col in range(len(max_local)):
                for i in range(0, 3):
                    for j in range(0, 3):
                        if grid[row + i][col + j] > max_local[row][col]:
                            max_local[row][col] = grid[row + i][col + j]

        return max_local
