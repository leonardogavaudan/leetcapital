import bisect
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        ends = [event[1] for event in events]

        dp = []
        best = 0
        for _, e, v in events:
            best = max(best, v)
            dp.append(best)

        events.sort(key=lambda x: x[0])
        res = 0
        for s, e, v in events:
            i = bisect.bisect_left(ends, s) - 1
            res = max(res, (dp[i] if i >= 0 else 0) + v)

        return res
