from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_y1 = 0
        max_vol = 0

        for x1, y1 in enumerate(height):
            if y1 <= max_y1:
                continue

            max_y1 = y1
            max_y2 = 0

            for x2 in range(len(height) - 1, x1, -1):
                y2 = height[x2]

                if y2 <= max_y2:
                    continue

                max_y2 = y2

                new_vol = (x2 - x1) * min(y1, y2)
                if new_vol > max_vol:
                    max_vol = new_vol

        return max_vol
