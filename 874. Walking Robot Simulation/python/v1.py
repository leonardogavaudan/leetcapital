from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set((tuple(o) for o in obstacles))
        direction = "north"
        direction_for_right_turn = {
            "north": "west",
            "west": "south",
            "south": "east",
            "east": "north",
        }
        direction_for_left_turn = {v: k for k, v in direction_for_right_turn.items()}
        x, y = 0, 0

        def process_command(command: int):
            nonlocal direction, x, y

            if command == -2:
                direction = direction_for_left_turn[direction]
                return
            if command == -1:
                direction = direction_for_right_turn[direction]
                return

            for _ in range(command):
                if direction == "north":
                    next_position = (x, y + 1)
                elif direction == "south":
                    next_position = (x, y - 1)
                elif direction == "east":
                    next_position = (x - 1, y)
                else:
                    next_position = (x + 1, y)

                if next_position in obstacle_set:
                    break

                x, y = next_position

            return

        max_dist = 0

        for command in commands:
            process_command(command)
            max_dist = max(max_dist, x**2 + y**2)

        return max_dist
