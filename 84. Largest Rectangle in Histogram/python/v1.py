from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                right = i - 1
                height = heights[stack.pop()]
                left = 0 if not stack else stack[-1] + 1
                area = height * (right - left + 1)
                max_area = max(max_area, area)
            stack.append(i)

        return max_area
