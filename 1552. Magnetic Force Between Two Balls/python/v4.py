from typing import List


class Solution:
    def can_place(self, position: List[int], ball_count: int, dist: int):
        balls_placed = 1
        last_position = position[0]
        i = 1

        while balls_placed < ball_count:
            while i < len(position) and position[i] - last_position < dist:
                i += 1
                if i >= len(position):
                    return False

            last_position = position[i]
            balls_placed += 1

        return True

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left_dist, right_dist = 1, position[-1] - position[0]

        while left_dist <= right_dist:
            dist = (left_dist + right_dist) // 2
            if self.can_place(position, m, dist):
                left_dist = dist + 1
            else:
                right_dist = dist - 1

        return left_dist - 1
