from typing import List


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        res = [[rStart, cStart]]
        dimension = 1
        next_direction = {
            "east": "south",
            "south": "west",
            "west": "north",
            "north": "east",
        }
        current_row, current_col = rStart, cStart
        current_direction = "east"

        def take_step():
            nonlocal current_row, current_col
            if current_direction == "east":
                current_col += 1
            elif current_direction == "south":
                current_row += 1
            elif current_direction == "west":
                current_col -= 1
            elif current_direction == "north":
                current_row -= 1

        while len(res) != rows * cols:
            steps_taken = 0
            while steps_taken < dimension:
                take_step()
                steps_taken += 1

                if 0 <= current_row < rows and 0 <= current_col < cols:
                    res.append([current_row, current_col])

            current_direction = next_direction[current_direction]

            if current_direction == "west" or current_direction == "east":
                dimension += 1

        return res
