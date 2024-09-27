from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        res = [sorted_intervals[0]]

        res_pnter = 0
        sorted_intervals_pnter = 1

        while sorted_intervals_pnter < len(sorted_intervals):
            if res[res_pnter][1] >= sorted_intervals[sorted_intervals_pnter][0]:
                res[res_pnter][1] = max(
                    res[res_pnter][1], sorted_intervals[sorted_intervals_pnter][1]
                )
                sorted_intervals_pnter += 1
            else:
                res.append(sorted_intervals[sorted_intervals_pnter])
                sorted_intervals_pnter += 1
                res_pnter += 1

        return res
