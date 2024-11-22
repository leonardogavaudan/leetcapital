from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (len(rolls) + n)
        missing = total - sum(rolls)
        if missing < n or missing > 6 * n:
            return []
        res = [1] * n
        i = 0
        missing -= n
        while missing:
            res[i] += min(missing, 5)
            missing -= min(missing, 5)
            i += 1

        return res
