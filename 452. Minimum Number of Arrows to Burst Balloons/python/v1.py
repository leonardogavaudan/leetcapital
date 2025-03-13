from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        res = 1
        i = 0

        for j in range(1, len(points)):
            if points[i][1] >= points[j][0]:
                points[i][1] = min(points[i][1], points[j][1])
            else:
                res += 1
                i = j

        return res
