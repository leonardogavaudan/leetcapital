from typing import List


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        heights = nums + [0]
        stack = []

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = -1 if not stack else stack[-1]
                width = i - 1 - left
                if height * width > threshold:
                    return width
            stack.append(i)

        return -1
