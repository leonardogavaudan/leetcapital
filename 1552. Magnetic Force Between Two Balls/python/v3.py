from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def can_place(position: List[int], steps: int, balls: int):
            if balls > len(position):
                return False

            balls_placed = 1
            prev = position[0]
            i = 1
            while balls_placed < balls:
                while position[i] - prev < steps:
                    i += 1
                    if i >= len(position):
                        return False
                balls_placed += 1
                prev = position[i]

            return True

        position.sort()
        left, right = 1, position[-1] - position[0]

        while left <= right:
            mid = (left + right) // 2
            if can_place(position, mid, m):
                left = mid + 1
            else:
                right = mid - 1

        return right
