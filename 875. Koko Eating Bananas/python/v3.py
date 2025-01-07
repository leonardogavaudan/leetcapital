from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(piles: List[int], speed: int, h: int):
            hours = 0
            for pile in piles:
                hours += pile // speed + (1 if pile % speed != 0 else 0)
                if hours > h:
                    return False
            return True

        low, high = 1, max(piles)
        while low <= high:
            speed = (low + high) // 2
            if can_finish(piles, speed, h):
                high = speed - 1
            else:
                low = speed + 1

        return low
