from collections import deque
from typing import List


class Solution:
    def getInitialCoords(self, grid: List[List[int]]) -> tuple[int, int]:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return (row, col)

        raise Exception("grid doesn't have an island")

    def getNodeHash(self, row: int, col) -> str:
        return f"{row}-{col}"

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        current_node = self.getInitialCoords(grid)
        nodes_seen = set([self.getNodeHash(current_node[0], current_node[1])])
        queue = deque([current_node])
        perimeter = 0

        while queue:
            current_node = queue.popleft()
            row, col = current_node

            left = (row, col - 1) if col - 1 >= 0 else None
            right = (row, col + 1) if col + 1 < len(grid[0]) else None
            up = (row - 1, col) if row - 1 >= 0 else None
            down = (row + 1, col) if row + 1 < len(grid) else None

            for neighbor in [left, right, up, down]:
                if (
                    neighbor is not None
                    and self.getNodeHash(neighbor[0], neighbor[1]) not in nodes_seen
                    and grid[neighbor[0]][neighbor[1]] == 1
                ):
                    queue.append(neighbor)
                    nodes_seen.add(self.getNodeHash(neighbor[0], neighbor[1]))

                if neighbor is None or grid[neighbor[0]][neighbor[1]] == 0:
                    perimeter += 1

        return perimeter
