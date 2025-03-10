from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        res = 0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            res = max(res, min(citations[i], i + 1))
        return res
