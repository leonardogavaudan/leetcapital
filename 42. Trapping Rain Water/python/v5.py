from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 1, len(height) - 2
        left_max, right_max = height[0], height[-1]
        while left <= right:
            if left_max > right_max:
                right_max = max(right_max, height[right])
                res += right_max - height[right]
                right -= 1
            else:
                left_max = max(left_max, height[left])
                res += left_max - height[left]
                left += 1

        return res
