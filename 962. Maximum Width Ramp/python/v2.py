from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        res = 0
        stack = []
        for i, num in enumerate(nums):
            if not stack or num < nums[stack[-1]]:
                stack.append(i)

        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                res = max(res, i - stack.pop())

        return res
