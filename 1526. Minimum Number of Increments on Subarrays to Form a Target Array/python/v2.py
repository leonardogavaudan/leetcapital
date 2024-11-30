from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = 0
        base = 0
        for i in range(len(target)):
            res += max(0, target[i] - base)
            base = target[i]
        return res
