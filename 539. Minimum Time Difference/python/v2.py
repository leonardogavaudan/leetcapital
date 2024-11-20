from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        points_minutes = [
            int(s.split(":")[0]) * 60 + int(s.split(":")[1]) for s in timePoints
        ]
        points_minutes.sort()

        MOD = 24 * 60
        res = min(
            points_minutes[-1] - points_minutes[0],
            (points_minutes[0] - points_minutes[-1]) % MOD,
        )
        for i in range(1, len(points_minutes)):
            res = min(res, points_minutes[i] - points_minutes[i - 1])

        return res
