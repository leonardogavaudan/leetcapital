from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        res = []
        inserted = False

        for interval in intervals:
            if not inserted and interval[0] > newInterval[0]:
                if res and res[-1][1] >= newInterval[0]:
                    res[-1][1] = max(res[-1][1], newInterval[1])
                else:
                    res.append(newInterval)
                inserted = True

            if res and res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)

        if not inserted:
            if res[-1][1] < newInterval[0]:
                res.append(newInterval)
            else:
                res[-1][1] = max(res[-1][1], newInterval[1])

        return res
