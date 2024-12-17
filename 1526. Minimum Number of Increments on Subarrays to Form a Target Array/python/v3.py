from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = 0
        base = 0

        for num in target:
            res += max(num - base, 0)
            base = num

        return res
