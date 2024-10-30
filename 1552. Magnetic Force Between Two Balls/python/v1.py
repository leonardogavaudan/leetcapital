from typing import List


class Solution:
    def can_place(self, position: List[int], min_dist: int, m: int) -> bool:
        count = 1
        prev_position = position[0]

        for i in range(1, len(position)):
            if position[i] - prev_position >= min_dist:
                count += 1
                prev_position = position[i]

                if count == m:
                    return True

        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        res = 0
        sorted_position = sorted(position)
        left, right = 1, sorted_position[-1] - sorted_position[0]

        while left <= right:
            mid = (left + right) // 2
            if self.can_place(sorted_position, mid, m):
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res
