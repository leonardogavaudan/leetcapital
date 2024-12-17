from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        max_left, max_right = height[0], height[-1]
        left, right = 1, len(height) - 2

        while left <= right:
            if max_left < max_right:
                max_left = max(max_left, height[left])
                res += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right])
                res += max_right - height[right]
                right -= 1

        return res
