from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        k = 0
        hours_used = 0

        while l <= r:
            k = (l + r) // 2
            hours_used = 0

            for p in piles:
                hours_used += p // k + (p % k != 0)

            if hours_used <= h:
                r = k - 1
            else:
                l = k + 1

        return k + (hours_used > h)
