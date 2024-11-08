from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        res = 0
        obstacles_set = set()
        for c, r in obstacles:
            obstacles_set.add((r, c))

        direction = "north"
        direction_to_right = {
            "north": "east",
            "east": "south",
            "south": "west",
            "west": "north",
        }
        direction_to_left = {value: key for key, value in direction_to_right.items()}
        row, col = 0, 0

        for command in commands:
            if command == -1:
                direction = direction_to_right[direction]
            elif command == -2:
                direction = direction_to_left[direction]
            else:
                steps_taken = 0
                while steps_taken < command:
                    direction_to_next_position = {
                        "north": (row + 1, col),
                        "west": (row, col - 1),
                        "east": (row, col + 1),
                        "south": (row - 1, col),
                    }
                    next_position = direction_to_next_position[direction]
                    if next_position in obstacles_set:
                        break

                    row, col = next_position
                    steps_taken += 1

                res = max(res, row**2 + col**2)

        return res
