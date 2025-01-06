from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        people.sort()
        l, r = 0, len(people) - 1

        while l <= r:
            if l == r:
                res += 1
                break
            if people[l] + people[r] <= limit:
                l += 1
            res += 1
            r -= 1

        return res
