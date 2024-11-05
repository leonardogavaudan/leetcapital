from typing import List


class Solution:
    def can_place(self, positions: List[int], balls: int, min_dist: int):
        balls_placed = 1
        i = 1
        last_position = positions[0]

        while balls_placed < balls:
            while positions[i] - last_position < min_dist:
                i += 1
                if i == len(positions):
                    return False

            last_position = positions[i]
            balls_placed += 1

        return True

    def maxDistance(self, position: List[int], m: int) -> int:
        sorted_positions = sorted(position)

        l, r = 1, (sorted_positions[-1] - sorted_positions[0])

        while l <= r:
            mid = (l + r) // 2

            if self.can_place(sorted_positions, m, mid):
                l = mid + 1
            else:
                r = mid - 1

        return r
