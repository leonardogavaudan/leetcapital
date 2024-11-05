from typing import List


class Solution:
    def can_eat(self, piles: List[int], k: int, hours: int):
        hours_used = 0

        for pile in piles[::-1]:
            hours_used += (pile + k - 1) // k
            if hours_used > hours:
                return False

        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            if self.can_eat(piles, mid, h):
                r = mid - 1
            else:
                l = mid + 1

        return l
