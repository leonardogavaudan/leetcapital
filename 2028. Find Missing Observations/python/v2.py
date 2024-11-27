from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = (len(rolls) + n) * mean
        rolled = sum(rolls)
        left = total - rolled

        if left < n or left > 6 * n:
            return []

        res = [1] * n
        left -= n
        i = 0
        while left:
            res[i] += min(left, 5)
            left -= min(left, 5)
            i += 1

        return res
