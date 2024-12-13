from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = (len(rolls) + n) * mean
        rest = total - sum(rolls)

        if rest > 6 * n or rest < n:
            return []

        return [rest // n + (1 if i < rest % n else 0) for i in range(n)]
