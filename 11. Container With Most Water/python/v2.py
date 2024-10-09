from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            vol = (r - l) * min(height[l], height[r])
            if vol > res:
                res = vol

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res
