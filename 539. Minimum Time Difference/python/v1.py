from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes_points = [
            int(p.split(":")[0]) * 60 + int(p.split(":")[1]) for p in timePoints
        ]
        sorted_points = sorted(minutes_points)
        min_diff = float("inf")

        if sorted_points[-1] - sorted_points[0] < 12 * 60:
            min_diff = sorted_points[-1] - sorted_points[0]
        else:
            min_diff = 24 * 60 - sorted_points[-1] + sorted_points[0]

        for i in range(1, len(timePoints)):
            min_diff = min(min_diff, sorted_points[i] - sorted_points[i - 1])

        return int(min_diff)
